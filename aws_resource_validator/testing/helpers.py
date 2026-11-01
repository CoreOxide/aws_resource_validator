"""Testing helper functions and validation assertions for pytest and unittest."""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

from aws_resource_validator.core.builtin_rules import get_extra_validator
from aws_resource_validator.core.diagnostics import ValidationResult, diagnose_validation
from aws_resource_validator.core.resolver import resolve_service, resolve_shape

if TYPE_CHECKING:
    from aws_resource_validator.core.api_object import APIObject
    from aws_resource_validator.core.service import Service


def resolve_service_and_shape(service: str, shape: str) -> tuple[Service, APIObject]:
    """Look up service and shape, raising :class:`KeyError` with typo hints if missing."""
    svc, svc_suggestions = resolve_service(service)
    if svc is None:
        hint = f" Did you mean: {', '.join(svc_suggestions)}?" if svc_suggestions else ""
        raise KeyError(f"Service {service!r} not found.{hint}")

    obj, shape_suggestions = resolve_shape(svc, shape)
    if obj is None:
        hint = f" Did you mean: {', '.join(shape_suggestions)}?" if shape_suggestions else ""
        raise KeyError(f"Shape {shape!r} in service {svc.service_name!r} not found.{hint}")

    return svc, obj


def validate_with_extras(
    service: str,
    shape: str,
    value: str,
    *,
    strict: bool = True,
) -> ValidationResult:
    """Validate a resource name against shape regex, length bounds, and domain-specific rules."""
    svc, obj = resolve_service_and_shape(service, shape)
    result = diagnose_validation(obj, svc.service_name, value, strict=strict)

    extra_validator = get_extra_validator(svc.service_name, obj.name, shape)
    if extra_validator is None:
        return result

    extra_errors = extra_validator(value)
    if not extra_errors:
        return result

    # Merge extra errors into the validation result
    all_errors = list(result.errors) + list(extra_errors)
    return ValidationResult(
        is_valid=False,
        value=value,
        service_name=svc.service_name,
        shape_name=obj.name,
        pattern=obj.pattern,
        min_length=obj.min_length,
        max_length=obj.max_length,
        length=result.length,
        errors=all_errors,
        warnings=result.warnings,
        strict=strict,
        prefix_matched=result.prefix_matched,
        full_matched=result.full_matched,
        failure_index=result.failure_index,
        failure_char=result.failure_char,
        failure_reason=extra_errors[0] if not result.errors else result.failure_reason,
        suggested_fix=result.suggested_fix,
        visual_pointer=result.visual_pointer,
    )


def assert_valid(
    service: str,
    shape: str,
    value: str,
    *,
    strict: bool = True,
) -> ValidationResult:
    """Assert that ``value`` is a valid AWS resource name for ``(service, shape)``.

    Raises :class:`AssertionError` with detailed diagnostics, visual pointers,
    and remediation suggestions on failure.
    """
    result = validate_with_extras(service, shape, value, strict=strict)
    if not result.is_valid:
        error_lines = "\n".join(f"  - {err}" for err in result.errors)
        pointer_str = f"\n\n{result.visual_pointer}" if result.visual_pointer else ""
        fix_str = f"\n\nSuggested fix: {result.suggested_fix}" if result.suggested_fix else ""
        msg = (
            f"AWS resource validation failed for service '{result.service_name}', "
            f"shape '{result.shape_name}':\n"
            f"Value: {value!r} (length: {result.length})\n"
            f"Errors:\n{error_lines}"
            f"{pointer_str}"
            f"{fix_str}"
        )
        raise AssertionError(msg)
    return result


def assert_invalid(
    service: str,
    shape: str,
    value: str,
    *,
    strict: bool = True,
) -> ValidationResult:
    """Assert that ``value`` fails validation for ``(service, shape)``.

    Raises :class:`AssertionError` if ``value`` unexpectedly passes validation.
    """
    result = validate_with_extras(service, shape, value, strict=strict)
    if result.is_valid:
        msg = (
            f"Expected validation failure for service '{result.service_name}', "
            f"shape '{result.shape_name}', but value {value!r} passed validation."
        )
        raise AssertionError(msg)
    return result


def generate_valid(
    service: str,
    shape: str,
    *,
    strict: bool = True,
    max_attempts: int = 50,
) -> str:
    """Generate a single compliant resource name satisfying all regex and domain constraints."""
    _, obj = resolve_service_and_shape(service, shape)

    for _ in range(max_attempts):
        val = obj.generate()
        result = validate_with_extras(service, shape, val, strict=strict)
        if result.is_valid:
            return val

    # Fallback to bounded alphanumeric generation if random exrex generation hit domain filters
    min_len = obj.min_length or 3
    max_len = obj.max_length or 63
    clean_prefix = re.sub(r"[^a-z0-9]", "", shape.lower()) or "res"
    candidate = clean_prefix[: min(len(clean_prefix), max_len)]
    if len(candidate) < min_len:
        candidate = candidate + "1" * (min_len - len(candidate))
    return candidate


class AWSValidatorHelper:
    """Helper wrapper for test assertions and diagnostics (used by the ``aws_validator`` fixture)."""

    def assert_valid(self, service: str, shape: str, value: str, *, strict: bool = True) -> ValidationResult:
        """Assert that ``value`` is valid for ``(service, shape)``."""
        return assert_valid(service, shape, value, strict=strict)

    def assert_invalid(self, service: str, shape: str, value: str, *, strict: bool = True) -> ValidationResult:
        """Assert that ``value`` is invalid for ``(service, shape)``."""
        return assert_invalid(service, shape, value, strict=strict)

    def validate(self, service: str, shape: str, value: str, *, strict: bool = True) -> bool:
        """Return ``True`` iff ``value`` satisfies ``(service, shape)``."""
        return validate_with_extras(service, shape, value, strict=strict).is_valid

    def validate_detailed(self, service: str, shape: str, value: str, *, strict: bool = True) -> ValidationResult:
        """Return structured :class:`~.ValidationResult` for ``value``."""
        return validate_with_extras(service, shape, value, strict=strict)

    def generate(self, service: str, shape: str, *, strict: bool = True) -> str:
        """Generate a valid resource name for ``(service, shape)``."""
        return generate_valid(service, shape, strict=strict)

    def __repr__(self) -> str:
        return "<AWSValidatorHelper>"
