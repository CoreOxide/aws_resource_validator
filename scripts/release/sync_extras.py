"""Sync the generated ``[project.optional-dependencies]`` block in ``pyproject.toml``.

Run with ``--check`` in CI to fail if the block is stale; run with
``--write`` locally to regenerate it from
``scripts/release/popular_services.txt`` + ``scripts/release/shards.toml``.

We write PEP 621 ``[project.optional-dependencies]`` (PEP 508
requirement strings) rather than Poetry's older
``[tool.poetry.dependencies] + [tool.poetry.extras]`` pairing. That
form is resolver-inert: ``poetry lock`` does NOT attempt to fetch
extras at lock time, which lets us ship a lockfile before any of the
per-service sub-packages have been published to PyPI. Sub-packages are
pinned strictly (``==<version>``); main and all sub-packages release
in lock-step.
"""

from __future__ import annotations

import argparse
import sys

from scripts.release._manifests import REPO_ROOT, Manifest, resolve
from scripts.release._naming import extra_key, pypi_name, shard_pypi_name

PYPROJECT = REPO_ROOT / "pyproject.toml"

EXTRAS_BEGIN = "# --- BEGIN GENERATED EXTRAS ---"
EXTRAS_END = "# --- END GENERATED EXTRAS ---"

GENERATOR_EXTRA = ("requests", "jinja2", "typer", "black")


def _extra(key: str, entries: list[str]) -> list[str]:
    """Render one PEP 621 extras entry as TOML lines."""
    if not entries:
        return [f"{key} = []"]
    lines = [f"{key} = ["]
    lines.extend(f'    "{e}",' for e in entries)
    lines.append("]")
    return lines


def render_extras(manifest: Manifest, bootstrap: bool = False) -> str:
    """Render the full ``[project.optional-dependencies]`` table.

    When ``bootstrap`` is true, omits the per-service and shard extras —
    those reference ``aws-resource-validator-<svc>`` projects that don't
    exist on PyPI yet. Used exactly once, for the very first release
    that creates those projects. After that release, switch back to the
    full extras set (the default).
    """
    version = manifest.version
    lines: list[str] = [EXTRAS_BEGIN, "[project.optional-dependencies]"]

    lines.extend(_extra("generator", list(GENERATOR_EXTRA)))

    if bootstrap:
        lines.append("")
        lines.append("# Bootstrap mode: service/shard extras omitted because the")
        lines.append("# per-service PyPI projects don't exist yet. Re-run")
        lines.append("# ``sync_extras.py --write`` (without --bootstrap) after the")
        lines.append("# first release registers those projects on PyPI.")
    else:
        lines.append("")
        lines.append("# Individual services (popular — curated in popular_services.txt).")
        for svc in sorted(manifest.popular, key=extra_key):
            key = extra_key(svc)
            lines.extend(_extra(key, [f"{pypi_name(svc)}=={version}"]))
        lines.append("")

        lines.append("# Domain shards (metapackages — shards.toml).")
        for shard in sorted(manifest.shards, key=lambda s: s.name):
            key = extra_key(shard.name)
            lines.extend(_extra(key, [f"{shard_pypi_name(shard.name)}=={version}"]))
        lines.append("")

        lines.append("# ``all`` = every shard (transitively every service).")
        all_deps = [
            f"{shard_pypi_name(s.name)}=={version}"
            for s in sorted(manifest.shards, key=lambda s: s.name)
        ]
        lines.extend(_extra("all", all_deps))

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


def apply_all(text: str, manifest: Manifest, bootstrap: bool = False) -> str:
    return splice(text, EXTRAS_BEGIN, EXTRAS_END, render_extras(manifest, bootstrap=bootstrap))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Fail if the block is stale.")
    mode.add_argument("--write", action="store_true", help="Regenerate the block in-place.")
    parser.add_argument(
        "--bootstrap",
        action="store_true",
        help=(
            "Omit the service/shard extras (only 'generator' is emitted). "
            "Use this exactly once, for the very first release that creates "
            "the per-service PyPI projects. Lets ``poetry lock`` succeed "
            "before those projects exist."
        ),
    )
    args = parser.parse_args(argv)

    manifest = resolve()
    current = PYPROJECT.read_text(encoding="utf-8")

    if args.check:
        # Accept either shape: full (default) or bootstrap. ``--bootstrap``
        # forces one specific mode; without it we're lenient so CI doesn't
        # flap between bootstrap and post-bootstrap releases.
        candidates = (
            [args.bootstrap]
            if args.bootstrap
            else [False, True]
        )
        for bootstrap in candidates:
            if current == apply_all(current, manifest, bootstrap=bootstrap):
                mode_name = "bootstrap" if bootstrap else "full"
                print(f"pyproject.toml [project.optional-dependencies] is in sync ({mode_name}).")
                return 0
        sys.stderr.write(
            "pyproject.toml [project.optional-dependencies] is out of sync with "
            "popular_services.txt / shards.toml. Run one of:\n"
            "    python -m scripts.release.sync_extras --write\n"
            "    python -m scripts.release.sync_extras --write --bootstrap\n"
        )
        return 1

    rendered = apply_all(current, manifest, bootstrap=args.bootstrap)

    if args.write:
        if current == rendered:
            print("pyproject.toml [project.optional-dependencies] already in sync — no changes.")
            return 0
        PYPROJECT.write_text(rendered, encoding="utf-8")
        print(f"Rewrote [project.optional-dependencies] block in {PYPROJECT}")
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
