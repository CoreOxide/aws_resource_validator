"""Shared naming helpers for the release tooling.

Service directories live under ``aws_resource_validator/pydantic_models/``
and use Python-safe identifiers (e.g. ``lambda_`` because ``lambda`` is
a keyword). PyPI project names and extras keys use the canonical
hyphenated form without the trailing underscore.
"""

from __future__ import annotations

from pathlib import Path

PACKAGE_PREFIX = "aws-resource-validator-"


def pypi_name(service: str) -> str:
    """Return the PyPI project name for a service directory.

    >>> pypi_name("s3")
    'aws-resource-validator-s3'
    >>> pypi_name("lambda_")
    'aws-resource-validator-lambda'
    >>> pypi_name("cognito_idp")
    'aws-resource-validator-cognito-idp'
    """
    return f"{PACKAGE_PREFIX}{extra_key(service)}"


def shard_pypi_name(shard: str) -> str:
    """Return the PyPI project name for a shard (metapackage)."""
    return pypi_name(shard)


def extra_key(service: str) -> str:
    """Return the canonical ``[...]`` extra key for a service or shard.

    Lowercase, ``_`` → ``-``, trailing ``-`` stripped, so ``lambda_`` →
    ``lambda`` and ``cognito_idp`` → ``cognito-idp``. Matches how PyPI
    normalizes project names for the wheel family.
    """
    key = service.lower().replace("_", "-").rstrip("-")
    if not key:
        raise ValueError(f"empty extra key for input {service!r}")
    return key


def discover_service_dirs(pydantic_models_dir: Path) -> list[str]:
    """Return every real service directory under ``pydantic_models/``.

    Skips ``__pycache__`` and any dotfile/dunder-named entries. The
    generator produces one directory per AWS service; no other
    directories live here.
    """
    names = []
    for entry in pydantic_models_dir.iterdir():
        if not entry.is_dir():
            continue
        if entry.name.startswith((".", "_")):
            continue
        names.append(entry.name)
    return sorted(names)
