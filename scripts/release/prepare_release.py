"""Prepare a release bump commit.

Bumps the package version, re-pins the generated extras block to match,
regenerates the packaging docs, and runs the CI gauntlet. Leaves the
changes unstaged so you can review and commit yourself.

Usage:
    python -m scripts.release.prepare_release 2.1.0
    python -m scripts.release.prepare_release 2.0.1 --dry-run

Steps performed (in order):

  1. Validate the new version is a valid PEP 440 string and not already
     on PyPI for the main package.
  2. Rewrite ``version`` in ``pyproject.toml``'s ``[project]`` table and
     ``__version__`` in ``aws_resource_validator/__init__.py``.
  3. Run ``scripts.release.sync_extras --write`` to re-pin every extra
     to the new version.
  4. Run ``scripts.release.sync_packaging_docs --write`` so the service
     list in ``docs/packaging.md`` reflects the new version.
  5. Run the static gauntlet: ``sync_extras --check``,
     ``sync_packaging_docs --check``, ``pytest tests/unit
     tests/integration``, ``ruff``, ``mypy``.

No ``poetry lock`` step — the repo doesn't commit ``poetry.lock``
because the circular constraint between main and the per-service
sub-packages can't be resolved across a version bump until the new
sub-packages exist on PyPI.

The script prints a summary of files it changed and the suggested
``git add`` + ``git commit`` commands. It does NOT commit or push.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

from scripts.release._manifests import REPO_ROOT

INIT_PATH = REPO_ROOT / "aws_resource_validator" / "__init__.py"
PYPROJECT = REPO_ROOT / "pyproject.toml"

# PEP 440 version regex (relaxed — we accept the common release shapes).
_VERSION_RE = re.compile(
    r"^\d+(\.\d+)*((a|b|rc)\d+)?(\.post\d+)?(\.dev\d+)?$"
)


def _current_version() -> str:
    for line in INIT_PATH.read_text(encoding="utf-8").splitlines():
        if line.startswith("__version__"):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit(f"could not find __version__ in {INIT_PATH}")


def _validate_new_version(new: str, current: str) -> None:
    if not _VERSION_RE.match(new):
        raise SystemExit(f"{new!r} is not a valid PEP 440 version")
    if new == current:
        raise SystemExit(
            f"{new!r} is the current version; nothing to do"
        )


def _version_on_pypi(version: str) -> bool:
    url = f"https://pypi.org/pypi/aws-resource-validator/{version}/json"
    try:
        with urllib.request.urlopen(
            urllib.request.Request(url, method="HEAD"), timeout=15
        ) as response:
            return response.status == 200
    except urllib.error.HTTPError as exc:
        return exc.code != 404
    except Exception:
        return False


def _bump_init(new: str) -> bool:
    text = INIT_PATH.read_text(encoding="utf-8")
    updated = re.sub(
        r'^(__version__\s*=\s*["\'])[^"\']+(["\'])',
        rf"\g<1>{new}\g<2>",
        text,
        count=1,
        flags=re.MULTILINE,
    )
    if updated == text:
        raise SystemExit(f"failed to rewrite __version__ in {INIT_PATH}")
    INIT_PATH.write_text(updated, encoding="utf-8")
    return True


def _bump_pyproject(new: str) -> bool:
    text = PYPROJECT.read_text(encoding="utf-8")
    # Only the [project] table's version line — leave any [tool.*] version
    # references alone. We anchor to the preceding "[project]" header.
    updated, count = re.subn(
        r'(\[project\][^\[]*?\n\s*version\s*=\s*["\'])[^"\']+(["\'])',
        rf"\g<1>{new}\g<2>",
        text,
        count=1,
        flags=re.DOTALL,
    )
    if count != 1:
        raise SystemExit(
            f"failed to find [project] version in {PYPROJECT}; "
            "was the file restructured?"
        )
    PYPROJECT.write_text(updated, encoding="utf-8")
    return True


def _run(cmd: list[str], *, cwd: Path | None = None, dry_run: bool = False) -> None:
    display = " ".join(cmd)
    if dry_run:
        print(f"  [dry-run] would run: {display}")
        return
    print(f"  $ {display}")
    result = subprocess.run(cmd, cwd=cwd or REPO_ROOT, check=False)
    if result.returncode != 0:
        raise SystemExit(
            f"command failed (exit {result.returncode}): {display}"
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("version", help="New version string, e.g. 2.1.0 or 2.0.1")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the steps without touching the filesystem or running subprocesses.",
    )
    parser.add_argument(
        "--skip-checks",
        action="store_true",
        help="Skip the pytest + ruff + mypy gauntlet after bumping.",
    )
    parser.add_argument(
        "--allow-published-version",
        action="store_true",
        help=(
            "Proceed even if the target version is already on PyPI. Only useful "
            "if you're intentionally re-running the script for documentation."
        ),
    )
    args = parser.parse_args(argv)

    current = _current_version()
    new = args.version

    print(f"current version: {current}")
    print(f"target  version: {new}")
    _validate_new_version(new, current)

    if not args.allow_published_version and _version_on_pypi(new):
        raise SystemExit(
            f"aws-resource-validator=={new} is already on PyPI. "
            "Pick a higher version, or pass --allow-published-version if "
            "you're deliberately re-running this script without a new release."
        )

    print("\n[1/5] rewriting __version__ and [project].version...")
    if args.dry_run:
        print(f"  [dry-run] would set version = {new!r} in:")
        print(f"    {INIT_PATH.relative_to(REPO_ROOT)}")
        print(f"    {PYPROJECT.relative_to(REPO_ROOT)}")
    else:
        _bump_init(new)
        _bump_pyproject(new)

    print("\n[2/5] regenerating pyproject.toml extras block...")
    _run(
        [sys.executable, "-m", "scripts.release.sync_extras", "--write"],
        dry_run=args.dry_run,
    )

    print("\n[3/5] regenerating docs/packaging.md...")
    _run(
        [sys.executable, "-m", "scripts.release.sync_packaging_docs", "--write"],
        dry_run=args.dry_run,
    )

    if args.skip_checks:
        print("\n[4-5/5] skipping checks (--skip-checks).")
    else:
        print("\n[4/5] running sync --check and tests...")
        _run(
            [sys.executable, "-m", "scripts.release.sync_extras", "--check"],
            dry_run=args.dry_run,
        )
        _run(
            [sys.executable, "-m", "scripts.release.sync_packaging_docs", "--check"],
            dry_run=args.dry_run,
        )
        _run(
            [sys.executable, "-m", "pytest", "tests/unit", "tests/integration", "-q"],
            dry_run=args.dry_run,
        )

        print("\n[5/5] running ruff + mypy...")
        _run(
            [sys.executable, "-m", "ruff", "check", "scripts/release", "aws_resource_validator", "tests"],
            dry_run=args.dry_run,
        )
        _run(
            [sys.executable, "-m", "mypy", "aws_resource_validator/core", "aws_resource_validator/generator"],
            dry_run=args.dry_run,
        )

    print("\n" + "=" * 60)
    print(f"release {new} is prepared. Suggested commit:")
    print()
    print("  git add aws_resource_validator/__init__.py pyproject.toml docs/packaging.md")
    print(f'  git commit -m "Bump version to {new}"')
    print()
    print("Then cut the GitHub release on the committed tag:")
    print(f"  git tag v{new} && git push origin v{new}")
    print()
    print("Publish on GitHub via Releases UI to trigger the pipeline.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
