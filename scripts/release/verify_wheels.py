"""Zip-inspect every wheel in ``dist/`` and enforce contents rules.

Catches the two most dangerous regressions in the packaging pipeline:

  * The main wheel accidentally shipping ``pydantic_models/`` (71 MB of
    duplication; forces all users onto the fat wheel).
  * A service or shard wheel shipping a stray
    ``aws_resource_validator/__init__.py`` or
    ``aws_resource_validator/pydantic_models/__init__.py``, which
    converts the PEP 420 namespace into a regular package and breaks
    cross-wheel imports.

Exit code 0 = all wheels pass. Non-zero = one or more violations.

Usage:
    python -m scripts.release.verify_wheels dist/
"""

from __future__ import annotations

import argparse
import functools
import sys
import zipfile
from pathlib import Path

from scripts.release._manifests import PYDANTIC_MODELS_DIR
from scripts.release._naming import discover_service_dirs

MAIN_WHEEL_PREFIX = "aws_resource_validator-"
SUBPACKAGE_PREFIX = "aws_resource_validator_"

# ``aws_resource_validator/__init__.py`` must exist ONLY in the main wheel.
# ``aws_resource_validator/pydantic_models/__init__.py`` must NOT exist in
# any wheel — the directory is a PEP 420 namespace.
PACKAGE_INIT = "aws_resource_validator/__init__.py"
PYMODELS_INIT = "aws_resource_validator/pydantic_models/__init__.py"

SHARD_META_PREFIX = "_aws_resource_validator_"
SHARD_META_SUFFIX = "_meta/__init__.py"


@functools.cache
def _known_services() -> frozenset[str]:
    return frozenset(discover_service_dirs(PYDANTIC_MODELS_DIR))


def _is_main_wheel(path: Path) -> bool:
    stem = path.name.removesuffix(".whl")
    return stem.startswith(MAIN_WHEEL_PREFIX) and not stem.startswith(SUBPACKAGE_PREFIX)


def _shard_name(names: list[str]) -> str | None:
    """Return the shard name if this wheel's namelist belongs to a shard."""
    for name in names:
        if name.startswith(SHARD_META_PREFIX) and name.endswith(SHARD_META_SUFFIX):
            return name[len(SHARD_META_PREFIX) : -len(SHARD_META_SUFFIX)]
    return None


def _service_name(path: Path) -> str:
    """Derive the service directory name from a service wheel filename.

    PyPI normalizes ``aws-resource-validator-lambda`` and strips the
    trailing underscore from the on-disk directory (``lambda_``); when
    the normalized form doesn't match a real directory, retry with an
    appended underscore.
    """
    stem = path.name.removesuffix(".whl")
    rest = stem[len(SUBPACKAGE_PREFIX) :]
    candidate = rest.split("-", 1)[0]
    known = _known_services()
    if candidate in known:
        return candidate
    suffixed = f"{candidate}_"
    if suffixed in known:
        return suffixed
    return candidate  # Let verify_service produce the error.


def verify_main(names: list[str], path: Path) -> list[str]:
    errors: list[str] = []
    if PACKAGE_INIT not in names:
        errors.append(f"{path.name}: missing {PACKAGE_INIT}")
    offenders = [n for n in names if n.startswith("aws_resource_validator/pydantic_models/")]
    if offenders:
        errors.append(
            f"{path.name}: main wheel must not ship pydantic_models/; "
            f"found {len(offenders)} offending entries (first: {offenders[0]!r})"
        )
    return errors


def verify_service(names: list[str], path: Path, service: str) -> list[str]:
    errors: list[str] = []
    expected_prefix = f"aws_resource_validator/pydantic_models/{service}/"
    if PACKAGE_INIT in names:
        errors.append(f"{path.name}: must not ship {PACKAGE_INIT} (breaks PEP 420)")
    if PYMODELS_INIT in names:
        errors.append(f"{path.name}: must not ship {PYMODELS_INIT} (breaks PEP 420)")
    code_entries = [n for n in names if n.startswith("aws_resource_validator/")]
    stray = [n for n in code_entries if not n.startswith(expected_prefix)]
    if stray:
        errors.append(
            f"{path.name}: expected only files under {expected_prefix!r}; "
            f"stray entries: {stray[:5]}"
        )
    if not any(n.startswith(expected_prefix) for n in names):
        errors.append(f"{path.name}: wheel contains no files under {expected_prefix!r}")
    return errors


def verify_shard(names: list[str], path: Path, shard: str) -> list[str]:
    errors: list[str] = []
    if any(n.startswith("aws_resource_validator/") for n in names):
        errors.append(
            f"{path.name}: shard wheels must not ship any aws_resource_validator/* files"
        )
    expected_placeholder = f"{SHARD_META_PREFIX}{shard}{SHARD_META_SUFFIX}"
    py_files = [n for n in names if n.endswith(".py")]
    if py_files != [expected_placeholder]:
        errors.append(
            f"{path.name}: expected single placeholder {expected_placeholder!r}; "
            f"found {py_files}"
        )
    return errors


def verify_wheel(path: Path) -> list[str]:
    with zipfile.ZipFile(path) as zf:
        names = zf.namelist()
    if _is_main_wheel(path):
        return verify_main(names, path)
    shard = _shard_name(names)
    if shard is not None:
        return verify_shard(names, path, shard)
    if path.name.startswith(SUBPACKAGE_PREFIX):
        return verify_service(names, path, _service_name(path))
    return [f"{path.name}: unrecognised wheel filename"]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dist", type=Path, help="Directory containing wheels.")
    args = parser.parse_args(argv)

    if not args.dist.is_dir():
        sys.stderr.write(f"not a directory: {args.dist}\n")
        return 2

    wheels = sorted(args.dist.glob("*.whl"))
    if not wheels:
        sys.stderr.write(f"no wheels found in {args.dist}\n")
        return 2

    failures: list[str] = []
    for wheel in wheels:
        failures.extend(verify_wheel(wheel))

    if failures:
        print(f"verify_wheels: {len(failures)} violation(s) across {len(wheels)} wheel(s):", file=sys.stderr)
        for err in failures:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(f"verify_wheels: OK — {len(wheels)} wheel(s) passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
