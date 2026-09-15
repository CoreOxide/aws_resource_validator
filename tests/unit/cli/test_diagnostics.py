"""Unit tests for validation diagnostics and strict mode enforcement."""

from __future__ import annotations

from aws_resource_validator.cli.diagnostics import diagnose_validation
from aws_resource_validator.core.api_object import APIObject


def test_diagnose_valid_value() -> None:
    obj = APIObject(name="Identifier", type="string", pattern=r"[a-z0-9-]+", min_length=3, max_length=20)
    result = diagnose_validation(obj, "TestService", "valid-123")

    assert result.is_valid is True
    assert result.errors == []
    assert result.warnings == []
    assert result.length == 9
    assert result.min_length == 3
    assert result.max_length == 20
    assert result.full_matched is True


def test_diagnose_too_short() -> None:
    obj = APIObject(name="Identifier", type="string", pattern=r"[a-z0-9-]+", min_length=5, max_length=20)
    result = diagnose_validation(obj, "TestService", "ab")

    assert result.is_valid is False
    assert any("shorter than minimum" in err for err in result.errors)


def test_diagnose_too_long() -> None:
    obj = APIObject(name="Identifier", type="string", pattern=r"[a-z0-9-]+", min_length=1, max_length=5)
    result = diagnose_validation(obj, "TestService", "toolongvalue")

    assert result.is_valid is False
    assert any("exceeds maximum" in err for err in result.errors)


def test_diagnose_regex_mismatch() -> None:
    obj = APIObject(name="Identifier", type="string", pattern=r"[0-9]+", min_length=1, max_length=10)
    result = diagnose_validation(obj, "TestService", "letters_only")

    assert result.is_valid is False
    assert any("does not match required regex pattern" in err for err in result.errors)


def test_diagnose_prefix_vs_strict_mode() -> None:
    # Pattern without $ / \Z: matches prefix under re.match
    obj = APIObject(name="Identifier", type="string", pattern=r"[a-z]+", min_length=1, max_length=50)

    # In non-strict mode: valid under botocore semantics, with a warning
    loose_res = diagnose_validation(obj, "TestService", "prefix_with_invalid_!@#", strict=False)
    assert loose_res.is_valid is True
    assert len(loose_res.warnings) == 1
    assert "matches prefix" in loose_res.warnings[0]

    # In strict mode: rejected
    strict_res = diagnose_validation(obj, "TestService", "prefix_with_invalid_!@#", strict=True)
    assert strict_res.is_valid is False
    assert any("strict mode requires full string match" in err for err in strict_res.errors)


def test_validation_result_to_dict() -> None:
    obj = APIObject(name="Id", type="string", pattern=r".+", min_length=1, max_length=10)
    result = diagnose_validation(obj, "Svc", "val")
    d = result.to_dict()

    assert d["is_valid"] is True
    assert d["service_name"] == "Svc"
    assert d["shape_name"] == "Id"
    assert d["pattern"] == ".+"
    assert d["value"] == "val"
    assert d["length"] == 3
