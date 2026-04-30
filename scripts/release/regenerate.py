"""Regenerate committed artifacts after ``poetry update`` bumps ``boto3-stubs``.

Running ``poetry update`` can install a newer ``boto3-stubs`` whose
TypedDict shapes differ from the ones the committed ``pydantic_models/``
tree was emitted against. This script automates the recovery recipe
from ``CLAUDE.md``:

    1. Validate the environment (arv-generate + boto3-stubs present).
    2. Snapshot the current service set for a before/after diff.
    3. Wipe ``aws_resource_validator/pydantic_models/<service>/``.
    4. Run ``arv-generate pipeline-b`` against the installed stubs.
    5. [Opt-in] Run ``arv-generate pipeline-a`` (needs GITHUB_TOKEN).
    6. Re-sync ``pyproject.toml`` extras + ``docs/packaging.md``.
    7. [Unless --skip-checks] pytest + ruff + mypy gauntlet.
    8. Print a summary (services added/removed + suggested commit).

The script leaves changes unstaged so the maintainer can review before
committing.

Usage:
    python -m scripts.release.regenerate
    python -m scripts.release.regenerate --only s3
    python -m scripts.release.regenerate --pipeline-a
    python -m scripts.release.regenerate --dry-run
    python -m scripts.release.regenerate --skip-checks
"""

from __future__ import annotations

import argparse
import importlib.metadata
import os
import shutil
import subprocess
import sys

from scripts.release._manifests import PYDANTIC_MODELS_DIR, REPO_ROOT
from scripts.release._naming import discover_service_dirs


def _run(cmd: list[str], *, dry_run: bool = False) -> None:
    display = " ".join(cmd)
    if dry_run:
        print(f"  [dry-run] would run: {display}")
        return
    print(f"  $ {display}")
    result = subprocess.run(cmd, cwd=REPO_ROOT, check=False)
    if result.returncode != 0:
        raise SystemExit(f"command failed (exit {result.returncode}): {display}")


def _validate_environment() -> None:
    if shutil.which("arv-generate") is None:
        raise SystemExit(
            "arv-generate not found on PATH. Run `pip install -e '.[generator]'` first."
        )
    try:
        version = importlib.metadata.version("boto3-stubs")
    except importlib.metadata.PackageNotFoundError as exc:
        raise SystemExit(
            "boto3-stubs is not installed in the current venv. "
            "Run `poetry install` (dev deps pull it in via boto3-stubs[all])."
        ) from exc
    print(f"  boto3-stubs version: {version}")


def _snapshot_services() -> list[str]:
    return discover_service_dirs(PYDANTIC_MODELS_DIR)


def _wipe_pydantic_models(dry_run: bool) -> None:
    entries = [
        e for e in PYDANTIC_MODELS_DIR.iterdir()
        if e.is_dir() and not e.name.startswith((".", "_"))
    ]
    print(f"  {len(entries)} service directories to remove under {PYDANTIC_MODELS_DIR.relative_to(REPO_ROOT)}")
    if dry_run:
        print("  [dry-run] would remove each directory")
        return
    for entry in entries:
        shutil.rmtree(entry)


def _diff_summary(before: list[str], after: list[str]) -> tuple[list[str], list[str]]:
    before_set = set(before)
    after_set = set(after)
    added = sorted(after_set - before_set)
    removed = sorted(before_set - after_set)
    return added, removed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--only",
        action="append",
        default=[],
        metavar="SERVICE",
        help="Limit Pipeline B regen to the given service(s). Pass multiple times.",
    )
    parser.add_argument(
        "--pipeline-a",
        action="store_true",
        help="Also run Pipeline A (class_definitions.py). Requires GITHUB_TOKEN.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the steps without touching the filesystem or running subprocesses.",
    )
    parser.add_argument(
        "--skip-checks",
        action="store_true",
        help="Skip the pytest + ruff + mypy gauntlet after regenerating.",
    )
    args = parser.parse_args(argv)

    print("[1/8] validating environment...")
    _validate_environment()

    print("\n[2/8] snapshotting current service set...")
    before = _snapshot_services()
    print(f"  {len(before)} services currently committed")

    print("\n[3/8] wiping aws_resource_validator/pydantic_models/...")
    if args.only:
        print(f"  --only {args.only!r}: skipping full wipe, will regenerate in place")
    else:
        _wipe_pydantic_models(args.dry_run)

    print("\n[4/8] running Pipeline B...")
    pipeline_b_cmd = ["arv-generate", "pipeline-b"]
    for svc in args.only:
        pipeline_b_cmd.extend(["--only", svc])
    _run(pipeline_b_cmd, dry_run=args.dry_run)

    if args.pipeline_a:
        print("\n[5/8] running Pipeline A...")
        if not os.environ.get("GITHUB_TOKEN") and not args.dry_run:
            raise SystemExit(
                "GITHUB_TOKEN is not set. Pipeline A fetches botocore shapes from "
                "the GitHub API — export a token or drop --pipeline-a."
            )
        _run(["arv-generate", "pipeline-a"], dry_run=args.dry_run)
    else:
        print("\n[5/8] skipping Pipeline A (pass --pipeline-a to include it).")

    print("\n[6/8] re-syncing pyproject.toml extras and docs/packaging.md...")
    _run(
        [sys.executable, "-m", "scripts.release.sync_extras", "--write"],
        dry_run=args.dry_run,
    )
    _run(
        [sys.executable, "-m", "scripts.release.sync_packaging_docs", "--write"],
        dry_run=args.dry_run,
    )

    if args.skip_checks:
        print("\n[7/8] skipping checks (--skip-checks).")
    else:
        print("\n[7/8] running gauntlet...")
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
        _run(
            [sys.executable, "-m", "pytest", "tests/generated", "-n", "auto", "-q"],
            dry_run=args.dry_run,
        )
        _run(
            [sys.executable, "-m", "ruff", "check", "aws_resource_validator", "tests", "scripts/release"],
            dry_run=args.dry_run,
        )
        _run(
            [sys.executable, "-m", "mypy", "aws_resource_validator/core", "aws_resource_validator/generator"],
            dry_run=args.dry_run,
        )

    print("\n[8/8] summary")
    if args.dry_run:
        print("  [dry-run] nothing was changed; skipping git status summary")
    else:
        after = _snapshot_services()
        added, removed = _diff_summary(before, after)
        if added:
            print(f"  services added   ({len(added)}): {', '.join(added)}")
        if removed:
            print(f"  services removed ({len(removed)}): {', '.join(removed)}")
        if not added and not removed:
            print("  service set unchanged")

    print("\n" + "=" * 60)
    print("regenerate complete. Suggested commit:")
    print()
    paths = ["aws_resource_validator/pydantic_models", "pyproject.toml", "docs/packaging.md"]
    if args.pipeline_a:
        paths.insert(1, "aws_resource_validator/class_definitions.py")
    print(f"  git add {' '.join(paths)}")
    print('  git commit -m "Regenerate models after boto3-stubs bump"')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
