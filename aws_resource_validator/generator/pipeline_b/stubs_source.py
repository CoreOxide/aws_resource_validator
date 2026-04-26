"""Locate and iterate the ``mypy_boto3_*`` stub packages installed in a venv."""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

from aws_resource_validator.core.naming import safe_identifier

_STUB_PREFIX = "mypy_boto3_"


@dataclass(frozen=True, slots=True)
class StubPackage:
    """One installed ``mypy_boto3_<service>`` package on disk."""

    service: str
    path: Path

    @property
    def literals_file(self) -> Path:
        return self.path / "literals.py"

    @property
    def type_defs_file(self) -> Path:
        return self.path / "type_defs.py"

    @property
    def client_file(self) -> Path:
        return self.path / "client.py"


def default_site_packages() -> Path:
    """Best-effort guess of the active virtualenv's site-packages directory.

    Falls back to scanning :data:`sys.path` for a ``site-packages`` entry.
    Raises :class:`FileNotFoundError` if none is found.
    """
    for path_str in sys.path:
        if path_str.endswith("site-packages") and Path(path_str).is_dir():
            return Path(path_str)
    raise FileNotFoundError("No site-packages directory found on sys.path")


def discover_stubs(site_packages: Path | None = None) -> list[StubPackage]:
    """Return all installed ``mypy_boto3_*`` stub packages sorted by service name."""
    root = site_packages or default_site_packages()
    packages: list[StubPackage] = []
    for entry in root.iterdir():
        if not entry.is_dir() or not entry.name.startswith(_STUB_PREFIX):
            continue
        if entry.name.endswith(".dist-info"):
            continue
        raw_service = entry.name[len(_STUB_PREFIX):]
        # ``lambda`` is an AWS service name and a Python keyword — safe_identifier
        # appends ``_`` so the emitted sub-package is importable.
        packages.append(StubPackage(service=safe_identifier(raw_service), path=entry))
    packages.sort(key=lambda p: p.service)
    return packages
