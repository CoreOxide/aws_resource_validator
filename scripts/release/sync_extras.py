"""Sync the generated ``[project.optional-dependencies]`` block in ``pyproject.toml``.

Run with ``--check`` in CI to fail if the block is stale; run with
``--write`` locally to regenerate it from
``scripts/release/popular_services.txt`` + ``scripts/release/shards.toml``.

Extras pin sub-packages strictly (``==<version>``). Main + every
sub-package release in lock-step, so a pinned install guarantees
consumers get a coherent version set. The repo does not commit a
``poetry.lock`` — circular constraints between main and the
per-service wheels would break lockfile resolution across version
bumps. See ``.gitignore`` for the why.
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


def render_extras(manifest: Manifest) -> str:
    """Render the full ``[project.optional-dependencies]`` table."""
    version = manifest.version
    lines: list[str] = [EXTRAS_BEGIN, "[project.optional-dependencies]"]

    lines.extend(_extra("generator", list(GENERATOR_EXTRA)))
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


def apply_all(text: str, manifest: Manifest) -> str:
    return splice(text, EXTRAS_BEGIN, EXTRAS_END, render_extras(manifest))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Fail if the block is stale.")
    mode.add_argument("--write", action="store_true", help="Regenerate the block in-place.")
    args = parser.parse_args(argv)

    manifest = resolve()
    current = PYPROJECT.read_text(encoding="utf-8")
    rendered = apply_all(current, manifest)

    if args.check:
        if current != rendered:
            sys.stderr.write(
                "pyproject.toml [project.optional-dependencies] is out of sync with "
                "popular_services.txt / shards.toml. Run:\n"
                "    python -m scripts.release.sync_extras --write\n"
            )
            return 1
        print("pyproject.toml [project.optional-dependencies] is in sync.")
        return 0

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
