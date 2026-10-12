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
    assert "diagnostics" in d
    assert d["failure_index"] == 0
    assert d["visual_pointer"] is not None
    assert d["suggested_fix"] is not None


def test_api_object_validate_detailed_method() -> None:
    obj = APIObject(name="Identifier", type="string", pattern=r"[a-z0-9-]+", min_length=3, max_length=20)
    res_valid = obj.validate_detailed("valid-name")
    assert res_valid.is_valid is True
    assert res_valid.diagnostics == []

    res_invalid = obj.validate_detailed("AB")
    assert res_invalid.is_valid is False
    assert len(res_invalid.diagnostics) >= 1
    assert res_invalid.failure_index is not None


def test_linkedin_acm_arn_diagnostics_example() -> None:
    from aws_resource_validator.class_definitions import class_registry

    acm = class_registry["Acm"]
    result = acm.Arn.validate_detailed("arn:aws:acm:bad_arn")

    assert result.is_valid is False
    assert len(result.diagnostics) >= 2
    # Diagnostic 1: length below minimum
    assert any(
        "below minimum length 20" in d or "shorter than minimum required length (20)" in d for d in result.diagnostics
    )
    # Diagnostic 2: regex failure at character 12
    assert any("character 12" in d and "bad_arn" in d for d in result.diagnostics)
    assert result.failure_index == 12
    assert result.failure_char == "bad_arn"
    assert result.visual_pointer is not None
    assert "^ character 12:" in result.visual_pointer
    assert result.suggested_fix is not None
    assert "arn:partition:acm:region:account-id:resource" in result.suggested_fix


def test_character_offset_casing_and_illegal_chars() -> None:
    obj = APIObject(name="BucketName", type="string", pattern=r"^[a-z0-9][a-z0-9-]+$", min_length=3, max_length=63)

    # Uppercase character detection
    res_upper = obj.validate_detailed("myBucket")
    assert res_upper.is_valid is False
    assert res_upper.failure_index == 2
    assert res_upper.failure_char == "B"
    assert "uppercase" in (res_upper.failure_reason or "")
    assert "lowercase" in (res_upper.suggested_fix or "")

    # Illegal character '_'
    res_underscore = obj.validate_detailed("my_bucket")
    assert res_underscore.is_valid is False
    assert res_underscore.failure_index == 2
    assert res_underscore.failure_char == "_"
    assert "_" in (res_underscore.failure_reason or "")

    # Leading hyphen
    res_leading_hyphen = obj.validate_detailed("-bucket")
    assert res_leading_hyphen.is_valid is False
    assert res_leading_hyphen.failure_index == 0
    assert "cannot start with a hyphen" in (res_leading_hyphen.failure_reason or "")


def test_length_bounds_diagnostics() -> None:
    obj = APIObject(name="FixedCode", type="string", pattern=r"[0-9]+", min_length=4, max_length=6)

    # Too short
    short_res = obj.validate_detailed("12")
    assert short_res.is_valid is False
    assert short_res.failure_index == 2
    assert "below minimum length" in (short_res.failure_reason or "")
    assert "Add at least 2 more character(s)" in (short_res.suggested_fix or "")

    # Too long
    long_res = obj.validate_detailed("12345678")
    assert long_res.is_valid is False
    assert long_res.failure_index == 6
    assert "exceeds maximum allowed length" in (long_res.failure_reason or "")
    assert "Shorten value by 2 character(s)" in (long_res.suggested_fix or "")


def test_service_and_registry_validate_detailed() -> None:
    from aws_resource_validator.class_definitions import class_registry

    # Service convenience method
    acm = class_registry["Acm"]
    svc_res = acm.validate_detailed("Arn", "arn:aws:acm:bad_arn")
    assert svc_res.is_valid is False
    assert svc_res.shape_name == "Arn"

    # Registry convenience method
    reg_res = class_registry.validate_detailed("Acm", "Arn", "arn:aws:acm:bad_arn")
    assert reg_res.is_valid is False
    assert reg_res.service_name == "Acm"


def test_visual_pointer_formatting() -> None:
    obj = APIObject(name="Id", type="string", pattern=r"^[a-z]+$", min_length=1, max_length=10)
    res = obj.validate_detailed("ab9cd")
    assert res.is_valid is False
    assert res.visual_pointer is not None
    lines = res.visual_pointer.split("\n")
    assert len(lines) == 2
    assert lines[0] == "ab9cd"
    assert lines[1].startswith("  ^ character 2:")


def test_robustness_on_unusual_patterns() -> None:
    # Pattern that cannot be parsed by standard re parser (e.g. invalid syntax)
    obj = APIObject(name="Special", type="string", pattern=r"(?i:invalid_escape_\p{L})", min_length=1, max_length=10)
    # Should not raise exception
    res = obj.validate_detailed("test")
    assert res.is_valid is False
    assert res.failure_index == 0
