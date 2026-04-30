"""Regenerate committed artifacts after ``poetry update`` bumps ``boto3-stubs``.

Running ``poetry update`` can install a newer ``boto3-stubs`` whose
TypedDict shapes differ from the ones the committed ``pydantic_models/``
tree was emitted against. This script automates the recovery recipe
from ``CLAUDE.md``:

    1. Validate the environment (boto3-stubs present).
    2. Snapshot the current service set for a before/after diff.
    3. Wipe ``aws_resource_validator/pydantic_models/<service>/``.
    4. Run Pipeline B against the installed stubs.
    5. [Opt-in] Run Pipeline A (needs GITHUB_TOKEN).
    6. Re-sync ``pyproject.toml`` extras + ``docs/packaging.md``.
    7. [Unless --skip-checks] pytest + mypy gauntlet.
    8. Print a summary (services added/removed + suggested commit).

Every step is implemented via direct Python imports, not subprocess, so
CI security scanners don't flag shell invocations and so a single
exception interrupts the whole run with a useful traceback. The
maintainer reviews and commits manually.

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

from scripts.release._manifests import PYDANTIC_MODELS_DIR, REPO_ROOT
from scripts.release._naming import discover_service_dirs


def _validate_environment() -> None:
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


def _run_pipeline_b(only: list[str], dry_run: bool) -> None:
    args = ["pipeline-b"]
    for svc in only:
        args.extend(["--only", svc])
    if dry_run:
        print(f"  [dry-run] would call arv-generate {' '.join(args)}")
        return

    from aws_resource_validator.generator.pipeline_b.orchestrator import emit_all
    from aws_resource_validator.generator.pipeline_b.stubs_source import (
        default_site_packages,
        discover_stubs,
    )

    stubs = discover_stubs(default_site_packages())
    if only:
        wanted = set(only)
        stubs = [s for s in stubs if s.service in wanted]
        missing = wanted - {s.service for s in stubs}
        if missing:
            raise SystemExit(
                f"no stubs found for requested service(s): {', '.join(sorted(missing))}"
            )
    print(f"  emitting Pydantic models for {len(stubs)} service(s)")
    emit_all(stubs, PYDANTIC_MODELS_DIR.parent / "pydantic_models")


def _run_pipeline_a(dry_run: bool) -> None:
    if not os.environ.get("GITHUB_TOKEN") and not dry_run:
        raise SystemExit(
            "GITHUB_TOKEN is not set. Pipeline A fetches botocore shapes from "
            "the GitHub API — export a token or drop --pipeline-a."
        )
    if dry_run:
        print("  [dry-run] would run Pipeline A (fetch botocore + emit class_definitions.py)")
        return

    from aws_resource_validator.generator.pipeline_a.code_writer import write_class_definitions
    from aws_resource_validator.generator.pipeline_a.github_source import GitHubBotocoreSource
    from aws_resource_validator.generator.pipeline_a.registry_builder import build_registry

    source = GitHubBotocoreSource(token=os.environ.get("GITHUB_TOKEN"))
    registry = build_registry(source.iter_services())
    write_class_definitions(registry, REPO_ROOT / "aws_resource_validator" / "class_definitions.py")


def _run_sync_module(module_name: str, flag: str, dry_run: bool) -> None:
    display = f"python -m scripts.release.{module_name} {flag}"
    if dry_run:
        print(f"  [dry-run] would call {display}")
        return
    print(f"  $ {display}")

    if module_name == "sync_extras":
        from scripts.release import sync_extras as mod
    elif module_name == "sync_packaging_docs":
        from scripts.release import sync_packaging_docs as mod
    else:
        raise AssertionError(f"unknown sync module: {module_name}")

    rc = mod.main([flag])
    if rc != 0:
        raise SystemExit(f"{display} exited with {rc}")


def _run_pytest(targets: list[str], dry_run: bool, extra: list[str] | None = None) -> None:
    args = [*targets, "-q"]
    if extra:
        args.extend(extra)
    display = "pytest " + " ".join(args)
    if dry_run:
        print(f"  [dry-run] would call {display}")
        return
    print(f"  $ {display}")
    import pytest

    rc = pytest.main(args)
    if rc != 0:
        raise SystemExit(f"{display} exited with {rc}")


def _run_mypy(targets: list[str], dry_run: bool) -> None:
    display = "mypy " + " ".join(targets)
    if dry_run:
        print(f"  [dry-run] would call {display}")
        return
    print(f"  $ {display}")
    from mypy import api

    stdout, stderr, rc = api.run(targets)
    if stdout:
        print(stdout, end="")
    if stderr:
        print(stderr, end="")
    if rc != 0:
        raise SystemExit(f"{display} exited with {rc}")


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
        help="Print the steps without touching the filesystem or running the pipelines.",
    )
    parser.add_argument(
        "--skip-checks",
        action="store_true",
        help="Skip the pytest + mypy gauntlet after regenerating.",
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
    _run_pipeline_b(args.only, args.dry_run)

    if args.pipeline_a:
        print("\n[5/8] running Pipeline A...")
        _run_pipeline_a(args.dry_run)
    else:
        print("\n[5/8] skipping Pipeline A (pass --pipeline-a to include it).")

    print("\n[6/8] re-syncing pyproject.toml extras and docs/packaging.md...")
    _run_sync_module("sync_extras", "--write", args.dry_run)
    _run_sync_module("sync_packaging_docs", "--write", args.dry_run)

    if args.skip_checks:
        print("\n[7/8] skipping checks (--skip-checks).")
    else:
        print("\n[7/8] running gauntlet...")
        _run_sync_module("sync_extras", "--check", args.dry_run)
        _run_sync_module("sync_packaging_docs", "--check", args.dry_run)
        _run_pytest(["tests/unit", "tests/integration"], args.dry_run)
        _run_pytest(["tests/generated"], args.dry_run, extra=["-n", "auto"])
        _run_mypy(
            ["aws_resource_validator/core", "aws_resource_validator/generator"],
            args.dry_run,
        )

    print("\n[8/8] summary")
    if args.dry_run:
        print("  [dry-run] nothing was changed; skipping summary")
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
