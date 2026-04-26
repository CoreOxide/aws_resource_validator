"""Tests for :mod:`aws_resource_validator.generator.common.io`."""

from __future__ import annotations

from pathlib import Path

import pytest

from aws_resource_validator.generator.common import io as io_mod
from aws_resource_validator.generator.common.io import ensure_package, write_text_atomic


def test_write_creates_parent_directories(tmp_path: Path) -> None:
    destination = tmp_path / "nested" / "deep" / "file.py"
    write_text_atomic(destination, "hello")
    assert destination.read_text() == "hello"


def test_write_overwrites_existing_file(tmp_path: Path) -> None:
    destination = tmp_path / "out.txt"
    destination.write_text("old")
    write_text_atomic(destination, "new")
    assert destination.read_text() == "new"


def test_write_cleans_up_temp_on_failure(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    def explode(*_a: object, **_kw: object) -> None:
        raise RuntimeError("boom")

    monkeypatch.setattr(io_mod.os, "replace", explode)

    destination = tmp_path / "out.txt"
    with pytest.raises(RuntimeError, match="boom"):
        write_text_atomic(destination, "hello")

    leftovers = list(tmp_path.iterdir())
    # No temp file (``.out.txt.*``) should remain after a failed rename.
    assert leftovers == [], f"temp files leaked: {leftovers}"
    assert not destination.exists()


def test_ensure_package_is_idempotent(tmp_path: Path) -> None:
    target = tmp_path / "pkg"
    ensure_package(target)
    first_init = target / "__init__.py"
    assert first_init.exists()
    first_init.write_text("# custom")
    ensure_package(target)  # second call must not overwrite.
    assert first_init.read_text() == "# custom"
