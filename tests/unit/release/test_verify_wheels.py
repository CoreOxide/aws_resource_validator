"""Tests for :mod:`scripts.release.verify_wheels`.

The verifier inspects real .whl zip archives, so each test builds a
tiny synthetic zip under ``tmp_path`` and asserts on the returned
error list. We also patch the ``_known_services`` cache to isolate
tests from the real ``pydantic_models/`` tree.
"""

from __future__ import annotations

import zipfile
from collections.abc import Iterable
from pathlib import Path

import pytest

from scripts.release import verify_wheels


def _make_wheel(path: Path, entries: Iterable[str]) -> Path:
    """Write a .whl zip containing empty files at the given arcnames."""
    with zipfile.ZipFile(path, "w") as zf:
        for arcname in entries:
            zf.writestr(arcname, b"")
    return path


@pytest.fixture(autouse=True)
def _isolate_known_services(monkeypatch: pytest.MonkeyPatch) -> None:
    # ``_known_services`` is a module-level functools.cache; override it
    # so the tests don't depend on the live pydantic_models/ layout.
    verify_wheels._known_services.cache_clear()
    monkeypatch.setattr(
        verify_wheels,
        "_known_services",
        lambda: frozenset({"s3", "ec2", "lambda_", "cognito_idp"}),
    )


def test_verify_main_accepts_core_only_wheel(tmp_path: Path) -> None:
    wheel = _make_wheel(
        tmp_path / "aws_resource_validator-2.1.0-py3-none-any.whl",
        [
            "aws_resource_validator/__init__.py",
            "aws_resource_validator/core/__init__.py",
            "aws_resource_validator-2.1.0.dist-info/METADATA",
        ],
    )
    assert verify_wheels.verify_wheel(wheel) == []


def test_verify_main_rejects_pydantic_models_leakage(tmp_path: Path) -> None:
    wheel = _make_wheel(
        tmp_path / "aws_resource_validator-2.1.0-py3-none-any.whl",
        [
            "aws_resource_validator/__init__.py",
            "aws_resource_validator/pydantic_models/s3/__init__.py",
            "aws_resource_validator-2.1.0.dist-info/METADATA",
        ],
    )
    errors = verify_wheels.verify_wheel(wheel)
    assert any("must not ship pydantic_models/" in e for e in errors)


def test_verify_main_requires_package_init(tmp_path: Path) -> None:
    wheel = _make_wheel(
        tmp_path / "aws_resource_validator-2.1.0-py3-none-any.whl",
        ["aws_resource_validator-2.1.0.dist-info/METADATA"],
    )
    errors = verify_wheels.verify_wheel(wheel)
    assert any("missing aws_resource_validator/__init__.py" in e for e in errors)


def test_verify_service_accepts_scoped_subtree(tmp_path: Path) -> None:
    wheel = _make_wheel(
        tmp_path / "aws_resource_validator_s3-2.1.0-py3-none-any.whl",
        [
            "aws_resource_validator/pydantic_models/s3/__init__.py",
            "aws_resource_validator/pydantic_models/s3/s3_classes.py",
            "aws_resource_validator_s3-2.1.0.dist-info/METADATA",
        ],
    )
    assert verify_wheels.verify_wheel(wheel) == []


def test_verify_service_rejects_package_init(tmp_path: Path) -> None:
    wheel = _make_wheel(
        tmp_path / "aws_resource_validator_s3-2.1.0-py3-none-any.whl",
        [
            "aws_resource_validator/__init__.py",
            "aws_resource_validator/pydantic_models/s3/__init__.py",
            "aws_resource_validator_s3-2.1.0.dist-info/METADATA",
        ],
    )
    errors = verify_wheels.verify_wheel(wheel)
    assert any("breaks PEP 420" in e and "__init__.py" in e for e in errors)


def test_verify_service_rejects_pymodels_init(tmp_path: Path) -> None:
    wheel = _make_wheel(
        tmp_path / "aws_resource_validator_s3-2.1.0-py3-none-any.whl",
        [
            "aws_resource_validator/pydantic_models/__init__.py",
            "aws_resource_validator/pydantic_models/s3/__init__.py",
            "aws_resource_validator_s3-2.1.0.dist-info/METADATA",
        ],
    )
    errors = verify_wheels.verify_wheel(wheel)
    assert any("pydantic_models/__init__.py" in e for e in errors)


def test_verify_service_rejects_wheel_missing_content(tmp_path: Path) -> None:
    wheel = _make_wheel(
        tmp_path / "aws_resource_validator_s3-2.1.0-py3-none-any.whl",
        ["aws_resource_validator_s3-2.1.0.dist-info/METADATA"],
    )
    errors = verify_wheels.verify_wheel(wheel)
    assert any("contains no files under" in e for e in errors)


def test_verify_service_resolves_lambda_normalization(tmp_path: Path) -> None:
    # The wheel filename says ``lambda``; the on-disk directory is
    # ``lambda_``. The normalizer must still find the right service.
    wheel = _make_wheel(
        tmp_path / "aws_resource_validator_lambda-2.1.0-py3-none-any.whl",
        [
            "aws_resource_validator/pydantic_models/lambda_/__init__.py",
            "aws_resource_validator_lambda-2.1.0.dist-info/METADATA",
        ],
    )
    assert verify_wheels.verify_wheel(wheel) == []


def test_verify_service_resolves_multiword_normalization(tmp_path: Path) -> None:
    # ``aws_resource_validator_cognito_idp-...`` wheel name — underscores
    # survive because PyPI doesn't normalise ``_`` → ``-`` in the filename.
    wheel = _make_wheel(
        tmp_path / "aws_resource_validator_cognito_idp-2.1.0-py3-none-any.whl",
        [
            "aws_resource_validator/pydantic_models/cognito_idp/__init__.py",
            "aws_resource_validator_cognito_idp-2.1.0.dist-info/METADATA",
        ],
    )
    assert verify_wheels.verify_wheel(wheel) == []


def test_verify_shard_accepts_metapackage(tmp_path: Path) -> None:
    wheel = _make_wheel(
        tmp_path / "aws_resource_validator_data-2.1.0-py3-none-any.whl",
        [
            "_aws_resource_validator_data_meta/__init__.py",
            "aws_resource_validator_data-2.1.0.dist-info/METADATA",
        ],
    )
    assert verify_wheels.verify_wheel(wheel) == []


def test_verify_shard_rejects_extra_python_files(tmp_path: Path) -> None:
    wheel = _make_wheel(
        tmp_path / "aws_resource_validator_data-2.1.0-py3-none-any.whl",
        [
            "_aws_resource_validator_data_meta/__init__.py",
            "aws_resource_validator/pydantic_models/s3/s3_classes.py",
            "aws_resource_validator_data-2.1.0.dist-info/METADATA",
        ],
    )
    errors = verify_wheels.verify_wheel(wheel)
    assert any("shard wheels must not ship any aws_resource_validator/" in e for e in errors)


def test_verify_shard_rejects_wrong_placeholder(tmp_path: Path) -> None:
    wheel = _make_wheel(
        tmp_path / "aws_resource_validator_data-2.1.0-py3-none-any.whl",
        [
            "_aws_resource_validator_data_meta/__init__.py",
            "_aws_resource_validator_data_meta/extra.py",
            "aws_resource_validator_data-2.1.0.dist-info/METADATA",
        ],
    )
    errors = verify_wheels.verify_wheel(wheel)
    assert any("expected single placeholder" in e for e in errors)


def test_unrecognised_wheel_filename(tmp_path: Path) -> None:
    wheel = _make_wheel(tmp_path / "random-1.0-py3-none-any.whl", ["random.py"])
    errors = verify_wheels.verify_wheel(wheel)
    assert any("unrecognised wheel filename" in e for e in errors)
