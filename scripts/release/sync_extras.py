"""Sync the two generated blocks in the root ``pyproject.toml``.

Run with ``--check`` in CI to fail if either block is stale; run with
``--write`` locally to regenerate them from
``scripts/release/popular_services.txt`` + ``scripts/release/shards.toml``.

The generated blocks are:

1. **Optional dependencies** — inside ``[tool.poetry.dependencies]``,
   one ``<svc> = { version = "==X.Y.Z", optional = true }`` entry per
   popular service and per shard. Poetry requires every extras value
   to reference a key declared in this table.

2. **Extras table** — the entire ``[tool.poetry.extras]`` table, mapping
   extras keys (``s3``, ``compute``, ``all``, ``generator``) to lists
   of those optional dependency keys.

Version pinning is strict (``==`` to the current main version). Main and
all sub-packages release in lock-step.
"""

from __future__ import annotations

import argparse
import sys

from scripts.release._manifests import REPO_ROOT, Manifest, resolve
from scripts.release._naming import extra_key, pypi_name, shard_pypi_name

PYPROJECT = REPO_ROOT / "pyproject.toml"

DEPS_BEGIN = "# --- BEGIN GENERATED OPTIONAL DEPS ---"
DEPS_END = "# --- END GENERATED OPTIONAL DEPS ---"
EXTRAS_BEGIN = "# --- BEGIN GENERATED EXTRAS ---"
EXTRAS_END = "# --- END GENERATED EXTRAS ---"

GENERATOR_EXTRA = ("requests", "jinja2", "typer", "black")


def render_optional_deps(manifest: Manifest) -> str:
    """Render the ``optional = true`` deps for popular services + shards."""
    version = manifest.version
    lines: list[str] = [DEPS_BEGIN]

    lines.append("# Popular services — one optional dep per service (popular_services.txt).")
    for svc in sorted(manifest.popular, key=extra_key):
        name = pypi_name(svc)
        lines.append(f'"{name}" = {{ version = "=={version}", optional = true }}')

    lines.append("# Domain shards — metapackages (shards.toml).")
    for shard in sorted(manifest.shards, key=lambda s: s.name):
        name = shard_pypi_name(shard.name)
        lines.append(f'"{name}" = {{ version = "=={version}", optional = true }}')

    lines.append(DEPS_END)
    return "\n".join(lines) + "\n"


def render_extras(manifest: Manifest) -> str:
    """Render the entire ``[tool.poetry.extras]`` table."""
    lines: list[str] = [EXTRAS_BEGIN, "[tool.poetry.extras]"]

    gen_entries = ", ".join(f'"{d}"' for d in GENERATOR_EXTRA)
    lines.append(f"generator = [{gen_entries}]")
    lines.append("")

    lines.append("# Individual services (popular — curated in popular_services.txt).")
    for svc in sorted(manifest.popular, key=extra_key):
        key = extra_key(svc)
        lines.append(f'{key} = ["{pypi_name(svc)}"]')
    lines.append("")

    lines.append("# Domain shards (metapackages — shards.toml).")
    for shard in sorted(manifest.shards, key=lambda s: s.name):
        key = extra_key(shard.name)
        lines.append(f'{key} = ["{shard_pypi_name(shard.name)}"]')
    lines.append("")

    lines.append("# ``all`` = every shard (transitively every service).")
    all_deps = ", ".join(
        f'"{shard_pypi_name(s.name)}"' for s in sorted(manifest.shards, key=lambda s: s.name)
    )
    lines.append(f"all = [{all_deps}]")

    lines.append(EXTRAS_END)
    return "\n".join(lines) + "\n"


def splice(text: str, begin: str, end: str, new_block: str) -> str:
    """Replace the region between BEGIN/END markers with ``new_block``."""
    b = text.find(begin)
    e = text.find(end)
    if b == -1 or e == -1 or e < b:
        raise SystemExit(
            f"could not locate marker pair in {PYPROJECT}: "
            f"expected {begin!r} then {end!r}"
        )
    eol = text.find("\n", e)
    if eol == -1:
        eol = len(text)
    return text[:b] + new_block.rstrip("\n") + text[eol:]


def apply_all(text: str, manifest: Manifest) -> str:
    text = splice(text, DEPS_BEGIN, DEPS_END, render_optional_deps(manifest))
    text = splice(text, EXTRAS_BEGIN, EXTRAS_END, render_extras(manifest))
    return text


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Fail if any block is stale.")
    mode.add_argument("--write", action="store_true", help="Regenerate both blocks in-place.")
    args = parser.parse_args(argv)

    manifest = resolve()
    current = PYPROJECT.read_text(encoding="utf-8")
    rendered = apply_all(current, manifest)

    if args.check:
        if current != rendered:
            sys.stderr.write(
                "pyproject.toml generated blocks are out of sync with "
                "popular_services.txt / shards.toml. Run:\n"
                "    python -m scripts.release.sync_extras --write\n"
            )
            return 1
        print("pyproject.toml generated blocks are in sync.")
        return 0

    if args.write:
        if current == rendered:
            print("pyproject.toml generated blocks already in sync — no changes.")
            return 0
        PYPROJECT.write_text(rendered, encoding="utf-8")
        print(f"Rewrote generated blocks in {PYPROJECT}")
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
