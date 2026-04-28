"""Loaders and validators for popular_services.txt and shards.toml."""

from __future__ import annotations

import sys
import tomllib
from dataclasses import dataclass
from pathlib import Path

from scripts.release._naming import discover_service_dirs

REPO_ROOT = Path(__file__).resolve().parents[2]
PYDANTIC_MODELS_DIR = REPO_ROOT / "aws_resource_validator" / "pydantic_models"
POPULAR_FILE = REPO_ROOT / "scripts" / "release" / "popular_services.txt"
SHARDS_FILE = REPO_ROOT / "scripts" / "release" / "shards.toml"


@dataclass(frozen=True, slots=True)
class Shard:
    name: str
    description: str
    services: tuple[str, ...]
    catch_all: bool


@dataclass(frozen=True, slots=True)
class Manifest:
    """Resolved view of the release manifests.

    ``services`` is the full set discovered on disk. ``popular`` is a
    subset — those that get a per-service PyPI project *and* extras
    key. ``shards`` is the grouping used for metapackages.
    """

    services: tuple[str, ...]
    popular: tuple[str, ...]
    shards: tuple[Shard, ...]
    version: str


def read_version() -> str:
    """Read ``__version__`` from the main package."""
    # Main package imports are cheap and available in every release-venv
    # (CI runs ``poetry install``); no need to parse ``__init__.py`` by
    # hand.
    from aws_resource_validator import __version__

    return __version__


def _read_nonblank_lines(path: Path) -> list[str]:
    lines = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        lines.append(line)
    return lines


def load_popular() -> list[str]:
    return _read_nonblank_lines(POPULAR_FILE)


def load_shards() -> list[Shard]:
    data = tomllib.loads(SHARDS_FILE.read_text(encoding="utf-8"))
    shards: list[Shard] = []
    for name, body in data.items():
        shards.append(
            Shard(
                name=name,
                description=body.get("description", ""),
                services=tuple(body.get("services", [])),
                catch_all=bool(body.get("catch_all", False)),
            )
        )
    return shards


def validate(services: list[str], popular: list[str], shards: list[Shard]) -> list[str]:
    """Return a list of human-readable validation errors (empty means OK)."""
    errors: list[str] = []
    service_set = set(services)

    # Every popular service must be a real directory.
    for svc in popular:
        if svc not in service_set:
            errors.append(f"popular_services.txt lists unknown service: {svc!r}")

    # Exactly one shard has catch_all.
    catch_alls = [s.name for s in shards if s.catch_all]
    if len(catch_alls) != 1:
        errors.append(
            f"exactly one shard must have catch_all=true (got {catch_alls or 'none'})"
        )

    # No service appears in two shards (ignoring the catch_all).
    seen: dict[str, str] = {}
    for shard in shards:
        if shard.catch_all:
            continue
        for svc in shard.services:
            if svc in seen:
                errors.append(
                    f"service {svc!r} appears in both shards {seen[svc]!r} and {shard.name!r}"
                )
            seen[svc] = shard.name

    # Every listed service in a non-catch-all shard must be a real directory.
    for shard in shards:
        if shard.catch_all:
            continue
        for svc in shard.services:
            if svc not in service_set:
                errors.append(f"shard {shard.name!r} lists unknown service: {svc!r}")

    # Every popular service must appear in some shard (otherwise it escapes the
    # shard metapackage dependency graph).
    populated = set(seen.keys())
    catch_all_shard = next((s for s in shards if s.catch_all), None)
    if catch_all_shard:
        # The catch-all implicitly owns everything not in ``populated``.
        populated |= service_set - populated
    for svc in popular:
        if svc not in populated:
            errors.append(f"popular service {svc!r} is not covered by any shard")

    return errors


def resolve() -> Manifest:
    """Load all manifests, expand the catch-all shard, and validate."""
    services = discover_service_dirs(PYDANTIC_MODELS_DIR)
    popular = load_popular()
    shards = load_shards()

    errors = validate(services, popular, shards)
    if errors:
        msg = "manifest validation failed:\n" + "\n".join(f"  - {e}" for e in errors)
        raise SystemExit(msg)

    # Expand the catch-all shard to include everything not in another shard.
    explicit: set[str] = set()
    for shard in shards:
        if not shard.catch_all:
            explicit.update(shard.services)
    missing = sorted(set(services) - explicit)

    resolved_shards: list[Shard] = []
    for shard in shards:
        if shard.catch_all:
            resolved_shards.append(
                Shard(
                    name=shard.name,
                    description=shard.description,
                    services=tuple(sorted(set(shard.services) | set(missing))),
                    catch_all=True,
                )
            )
        else:
            resolved_shards.append(shard)

    return Manifest(
        services=tuple(services),
        popular=tuple(popular),
        shards=tuple(resolved_shards),
        version=read_version(),
    )


if __name__ == "__main__":
    manifest = resolve()
    print(f"services: {len(manifest.services)}")
    print(f"popular:  {len(manifest.popular)}")
    for shard in manifest.shards:
        print(f"  shard {shard.name!r}: {len(shard.services)} services (catch_all={shard.catch_all})")
    sys.exit(0)
