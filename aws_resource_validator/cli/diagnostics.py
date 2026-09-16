"""Detailed diagnostic analysis for AWS resource name validation."""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass, field
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from aws_resource_validator.core.api_object import APIObject


@dataclass(frozen=True, slots=True)
class ValidationResult:
    """Structured validation outcome containing diagnostics, bounds, and warnings."""

    is_valid: bool
    value: str
    service_name: str
    shape_name: str
    pattern: str
    length: int
    min_length: int | None = None
    max_length: int | None = None
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    strict: bool = False
    prefix_matched: bool = False
    full_matched: bool = False

    def to_dict(self) -> dict[str, Any]:
        """Serialize result to a dictionary for JSON output."""
        return asdict(self)


def diagnose_validation(
    api_object: APIObject,
    service_name: str,
    value: str,
    *,
    strict: bool = False,
) -> ValidationResult:
    """Perform detailed validation with diagnostic messages on failure.

    Checks:
      1. Minimum length constraint.
      2. Maximum length constraint.
      3. Botocore regex match (prefix-anchored via :func:`re.match`).
      4. End-to-end match (:func:`re.fullmatch`), enforced in strict mode or flagged as a warning.
    """
    length = len(value)
    errors: list[str] = []
    warnings: list[str] = []

    # 1. Length constraints
    if api_object.min_length is not None and length < api_object.min_length:
        errors.append(f"Length {length} is shorter than minimum required length ({api_object.min_length}).")

    if api_object.max_length is not None and length > api_object.max_length:
        errors.append(f"Length {length} exceeds maximum allowed length ({api_object.max_length}).")

    # 2. Regex matching
    match = re.match(api_object.pattern, value)
    prefix_matched = match is not None
    full_matched = re.fullmatch(api_object.pattern, value) is not None

    if not prefix_matched:
        errors.append(f"Value does not match required regex pattern: {api_object.pattern}")
    elif not full_matched:
        if strict:
            matched_substr = match.group(0) if match else ""
            errors.append(
                f"Value only matches prefix '{matched_substr}' under botocore re.match; "
                "strict mode requires full string match."
            )
        else:
            warnings.append(
                "Value matches prefix under botocore's re.match semantics, "
                "but does not match end-to-end (use --strict to enforce)."
            )

    is_valid = len(errors) == 0

    return ValidationResult(
        is_valid=is_valid,
        value=value,
        service_name=service_name,
        shape_name=api_object.name,
        pattern=api_object.pattern,
        min_length=api_object.min_length,
        max_length=api_object.max_length,
        length=length,
        errors=errors,
        warnings=warnings,
        strict=strict,
        prefix_matched=prefix_matched,
        full_matched=full_matched,
    )
