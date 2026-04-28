"""Regenerate the generated sections of ``docs/packaging.md`` from manifests.

The standalone services list, the shard section, and the "X services"
counts are all derived from ``popular_services.txt`` + ``shards.toml``.
Hand-editing them in the markdown drifts the moment a shard grows.

Run with ``--check`` in CI to fail if the doc is stale; run with
``--write`` locally to regenerate.
"""

from __future__ import annotations

import argparse
import sys

from scripts.release._manifests import REPO_ROOT, Manifest, resolve
from scripts.release._naming import extra_key, pypi_name, shard_pypi_name

DOC_PATH = REPO_ROOT / "docs" / "packaging.md"
BEGIN = "<!-- BEGIN GENERATED PACKAGING DOCS -->"
END = "<!-- END GENERATED PACKAGING DOCS -->"


def _pypi_link(name: str) -> str:
    return f"[`{name}`](https://pypi.org/project/{name}/)"


def render_body(manifest: Manifest) -> str:
    lines: list[str] = [BEGIN, ""]

    lines.append("## Standalone service packages")
    lines.append("")
    lines.append("These AWS services each get their own PyPI project and their own extras")
    lines.append("key on the main package — a curated subset chosen for typical usage")
    lines.append("(maintained in [`scripts/release/popular_services.txt`][popular]).")
    lines.append("")
    lines.append("| Extras key | PyPI project |")
    lines.append("| --- | --- |")
    for svc in sorted(manifest.popular, key=extra_key):
        lines.append(f"| `[{extra_key(svc)}]` | {_pypi_link(pypi_name(svc))} |")
    lines.append("")
    other_count = len(manifest.services) - len(manifest.popular)
    lines.append(f"Every other AWS service ({other_count} of them) is still available — just")
    lines.append("via its shard. If you need a long-tail service as a standalone extra,")
    lines.append("open an issue.")
    lines.append("")

    lines.append("## Domain shards")
    lines.append("")
    lines.append("Shards group services by domain. Installing a shard extra transitively")
    lines.append("installs every service wheel in its list. Membership is maintained in")
    lines.append("[`scripts/release/shards.toml`][shards].")
    lines.append("")
    for shard in sorted(manifest.shards, key=lambda s: s.name):
        title = shard.description or f"AWS {shard.name} services"
        lines.append(f"### `[{extra_key(shard.name)}]` — {title}")
        lines.append("")
        lines.append(f"PyPI: {_pypi_link(shard_pypi_name(shard.name))}")
        if shard.catch_all:
            lines.append("")
            lines.append("*Catch-all shard — any AWS service not explicitly assigned to another")
            lines.append("shard lives here.*")
        lines.append("")
        lines.append(f"**{len(shard.services)} services:**")
        lines.append("")
        lines.append(", ".join(f"`{svc}`" for svc in sorted(shard.services)))
        lines.append("")

    lines.append("[popular]: https://github.com/CoreOxide/aws_resource_validator/blob/main/scripts/release/popular_services.txt")
    lines.append("[shards]: https://github.com/CoreOxide/aws_resource_validator/blob/main/scripts/release/shards.toml")
    lines.append("")
    lines.append(END)
    return "\n".join(lines) + "\n"


def splice(text: str, new_body: str) -> str:
    b = text.find(BEGIN)
    e = text.find(END)
    if b == -1 or e == -1 or e < b:
        raise SystemExit(
            f"could not locate marker pair in {DOC_PATH}: expected {BEGIN!r} then {END!r}"
        )
    eol = text.find("\n", e)
    if eol == -1:
        eol = len(text)
    return text[:b] + new_body.rstrip("\n") + text[eol:]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Fail if the doc is stale.")
    mode.add_argument("--write", action="store_true", help="Regenerate the doc in-place.")
    args = parser.parse_args(argv)

    manifest = resolve()
    current = DOC_PATH.read_text(encoding="utf-8")
    rendered = splice(current, render_body(manifest))

    if args.check:
        if current != rendered:
            sys.stderr.write(
                "docs/packaging.md is out of sync with popular_services.txt / shards.toml.\n"
                "Run: python -m scripts.release.sync_packaging_docs --write\n"
            )
            return 1
        print("docs/packaging.md is in sync.")
        return 0

    if current == rendered:
        print("docs/packaging.md already in sync — no changes.")
        return 0
    DOC_PATH.write_text(rendered, encoding="utf-8")
    print(f"Rewrote generated section in {DOC_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
