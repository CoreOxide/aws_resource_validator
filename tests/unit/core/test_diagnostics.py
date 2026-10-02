"""Unit tests for core diagnostics module."""

from __future__ import annotations

from aws_resource_validator.core.api_object import APIObject
from aws_resource_validator.core.diagnostics import ValidationResult, diagnose_validation


def test_core_diagnose_valid_value() -> None:
    obj = APIObject(name="Identifier", type="string", pattern=r"[a-z0-9-]+", min_length=3, max_length=20)
    result = diagnose_validation(obj, "TestService", "valid-123")

    assert isinstance(result, ValidationResult)
    assert result.is_valid is True
    assert result.errors == []
    assert result.warnings == []
    assert result.length == 9
    assert result.min_length == 3
    assert result.max_length == 20
    assert result.full_matched is True


def test_core_diagnose_errors_and_dict() -> None:
    obj = APIObject(name="Identifier", type="string", pattern=r"[a-z]+", min_length=5, max_length=10)
    result = diagnose_validation(obj, "TestService", "12", strict=True)

    assert result.is_valid is False
    assert len(result.errors) == 2  # length too short and regex mismatch
    d = result.to_dict()
    assert d["is_valid"] is False
    assert d["length"] == 2
