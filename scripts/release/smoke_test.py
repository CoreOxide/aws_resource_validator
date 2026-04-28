"""Install the main wheel + one service wheel in a clean venv and import across the namespace boundary.

This is the last line of defence against the PEP 420 trap: if either
wheel ships a stray ``__init__.py`` at ``aws_resource_validator/`` or
``aws_resource_validator/pydantic_models/``, the import below fails.

We also verify that invoking ``arv-generate`` without the ``[generator]``
extra raises the clean install-hint error (not a bare
``ModuleNotFoundError``).

Usage:
    python -m scripts.release.smoke_test dist/
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
import venv
from pathlib import Path

IMPORT_SCRIPT = """
from aws_resource_validator.core import BaseValidatorModel
from aws_resource_validator.pydantic_models.s3 import BucketTypeDef

assert issubclass(BucketTypeDef, BaseValidatorModel), (
    "s3 models failed to resolve BaseValidatorModel across the namespace split"
)
print("namespace import OK")
"""

ARV_WITHOUT_GENERATOR = """
import subprocess
import sys
proc = subprocess.run([sys.argv[1], "--help"], capture_output=True, text=True)
assert proc.returncode != 0, f"expected failure, got: {proc.stdout}"
assert "[generator] extra" in proc.stderr, (
    f"expected generator-extra hint in stderr, got: {proc.stderr!r}"
)
print("generator-extra gate OK")
"""


def _find_wheel(dist: Path, prefix: str) -> Path:
    matches = sorted(dist.glob(f"{prefix}*.whl"))
    if not matches:
        raise SystemExit(f"no wheel matching {prefix!r}* in {dist}")
    # Prefer the shortest stem — ``aws_resource_validator-2.0.0...`` beats
    # ``aws_resource_validator_s3-2.0.0...`` when prefix is
    # ``aws_resource_validator-``.
    return min(matches, key=lambda p: len(p.name))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dist", type=Path, help="Directory holding the built wheels.")
    parser.add_argument(
        "--service",
        default="s3",
        help="Which service wheel to install alongside main (default: s3).",
    )
    args = parser.parse_args(argv)

    main_wheel = _find_wheel(args.dist, "aws_resource_validator-")
    service_wheel = _find_wheel(args.dist, f"aws_resource_validator_{args.service}-")

    with tempfile.TemporaryDirectory(prefix="arv-smoke-") as tmp:
        tmp_path = Path(tmp)
        venv_dir = tmp_path / "venv"
        venv.create(venv_dir, with_pip=True, clear=True)
        python = venv_dir / ("Scripts" if sys.platform == "win32" else "bin") / "python"

        print(f"[smoke] venv: {venv_dir}")
        print(f"[smoke] installing {main_wheel.name} + {service_wheel.name}")
        subprocess.run(
            [str(python), "-m", "pip", "install", "--quiet", str(main_wheel), str(service_wheel)],
            check=True,
        )

        print("[smoke] cross-namespace import")
        subprocess.run([str(python), "-c", IMPORT_SCRIPT], check=True)

        print("[smoke] arv-generate without [generator] extra")
        arv_cmd = venv_dir / ("Scripts" if sys.platform == "win32" else "bin") / "arv-generate"
        subprocess.run([str(python), "-c", ARV_WITHOUT_GENERATOR, str(arv_cmd)], check=True)

    print("[smoke] all checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
