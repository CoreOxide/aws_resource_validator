"""Detailed diagnostic analysis for AWS resource name validation.

Shared across the CLI and client wrappers to provide actionable feedback
on constraint violations.
"""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass, field
from typing import TYPE_CHECKING, Any

try:
    import re._compiler as _re_compiler
    import re._parser as _re_parser
except ImportError:  # pragma: no cover
    _re_compiler = None  # type: ignore[assignment]
    _re_parser = None  # type: ignore[assignment]

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
    failure_index: int | None = None
    failure_char: str | None = None
    failure_reason: str | None = None
    suggested_fix: str | None = None
    visual_pointer: str | None = None

    @property
    def diagnostics(self) -> list[str]:
        """Actionable diagnostic error messages."""
        return list(self.errors)

    def to_dict(self) -> dict[str, Any]:
        """Serialize result to a dictionary for JSON output."""
        d = asdict(self)
        d["diagnostics"] = self.diagnostics
        return d


def _analyze_arn_mismatch(
    pattern: str,
    shape_name: str,
    service_name: str,
    value: str,
) -> tuple[int, str, str, str | None] | None:
    """Specialized failure localization for ARN shapes."""
    if not (pattern.startswith("arn:") or shape_name.endswith("Arn")):
        return None

    if not value.startswith("arn:"):
        prefix = value[:4] if len(value) >= 4 else value
        return 0, prefix, "missing required 'arn:' prefix", "Ensure the value begins with 'arn:'."

    colons = [i for i, c in enumerate(value) if c == ":"]
    if len(colons) < 5:
        last_colon = colons[-1] if colons else 3
        fail_idx = last_colon + 1
        substr = value[fail_idx:]
        svc_label = service_name.lower() or "service"
        return (
            fail_idx,
            substr,
            "does not match required ARN segments (missing account-id and resource)",
            f"Ensure ARN matches format 'arn:partition:{svc_label}:region:account-id:resource'.",
        )

    return _analyze_arn_components(pattern, service_name, value, colons)


def _analyze_arn_components(
    pattern: str,
    service_name: str,
    value: str,
    colons: list[int],
) -> tuple[int, str, str, str | None] | None:
    """Validate 6-part ARN components (partition, service, account)."""
    parts = value.split(":", 5)
    if not re.match(r"^aws(-[a-z]+)*$", parts[1]):
        return (
            4,
            parts[1],
            f"invalid partition '{parts[1]}' (expected 'aws', 'aws-cn', etc.)",
            "Use a valid AWS partition such as 'aws'.",
        )
    if service_name and parts[2].lower() != service_name.lower() and parts[2] not in pattern:
        return (
            colons[1] + 1,
            parts[2],
            f"service segment '{parts[2]}' does not match expected '{service_name.lower()}'",
            f"Use service '{service_name.lower()}' in the ARN.",
        )
    if not re.match(r"^\d{12}$", parts[4]) and parts[4] != "":
        return (
            colons[3] + 1,
            parts[4],
            f"invalid account ID '{parts[4]}' (expected 12 digits)",
            "Use a 12-digit AWS account ID.",
        )
    return None


def _walk_subpatterns_for_failure_index(pattern: str, value: str) -> int:
    """Walk compiled regex subpatterns to determine the furthest matching character index."""
    if _re_compiler is None or _re_parser is None:
        return 0
    try:
        parsed = _re_parser.parse(pattern)
        best_idx = 0
        for i in range(1, len(parsed) + 1):
            sub = _re_parser.SubPattern(parsed.state, parsed[:i])
            c = _re_compiler.compile(sub)
            m = c.match(value)
            if m:
                best_idx = max(best_idx, m.end())
            else:
                break
        return best_idx
    except Exception:
        return 0


def _diagnose_character_constraint(
    pattern: str,
    value: str,
    failure_index: int,
) -> tuple[str, str]:
    """Diagnose character-level constraint violation at failure_index."""
    char = value[failure_index] if failure_index < len(value) else ""
    if char.isupper() and not re.search(r"[A-Z]", pattern):
        reason = f"'{char}' is uppercase (pattern requires lowercase letters)"
        fix = f"Convert uppercase characters to lowercase: '{value.lower()}'."
    elif char == "_" and "_" not in pattern:
        reason = "contains forbidden character '_' (only alphanumeric and hyphens allowed)"
        fix = "Replace '_' with '-' or remove it."
    elif char.isspace():
        reason = "contains forbidden whitespace"
        fix = "Remove whitespace characters."
    elif failure_index == 0 and char == "-":
        reason = "cannot start with a hyphen '-'"
        fix = "Remove the leading hyphen."
    elif failure_index == len(value) - 1 and char == "-":
        reason = "cannot end with a hyphen '-'"
        fix = "Remove the trailing hyphen."
    elif char:
        reason = f"character '{char}' does not match pattern"
        fix = f"Ensure value satisfies pattern '{pattern}'."
    else:
        substr = value[failure_index:] or value
        reason = f"'{substr}' does not match pattern"
        fix = f"Ensure value satisfies pattern '{pattern}'."
    return reason, fix


def _analyze_prefix_mismatch(
    pattern: str,
    value: str,
    match: re.Match[str] | None,
) -> tuple[int, str, str, str]:
    """Analyze strict mode mismatch where prefix matched but full string did not."""
    failure_index = match.end() if match else len(value)
    failure_char = value[failure_index] if failure_index < len(value) else ""
    if failure_char.isupper() and not re.search(r"[A-Z]", pattern):
        reason = f"character '{failure_char}' is uppercase (pattern requires lowercase letters)"
        fix = f"Convert uppercase characters to lowercase: '{value.lower()}'."
    elif failure_char == "_" and "_" not in pattern:
        reason = "contains forbidden character '_' (only alphanumeric characters and hyphens allowed)"
        fix = "Replace '_' with '-' or remove it."
    elif failure_char.isspace():
        reason = "contains forbidden whitespace"
        fix = "Remove whitespace characters."
    elif failure_char:
        reason = f"character '{failure_char}' does not match strict pattern bounds"
        fix = f"Remove or replace '{failure_char}' at position {failure_index}."
    else:
        reason = "does not match end-to-end"
        fix = "Ensure entire value satisfies pattern bounds."
    return failure_index, failure_char, reason, fix


def _analyze_regex_mismatch(
    pattern: str,
    shape_name: str,
    service_name: str,
    value: str,
    *,
    prefix_matched: bool,
    full_matched: bool,
    match: re.Match[str] | None,
) -> tuple[int, str, str, str | None]:
    """Analyze why a value failed regex matching and locate failure position."""
    if prefix_matched and not full_matched:
        return _analyze_prefix_mismatch(pattern, value, match)

    arn_res = _analyze_arn_mismatch(pattern, shape_name, service_name, value)
    if arn_res is not None:
        return arn_res

    failure_index = _walk_subpatterns_for_failure_index(pattern, value)
    failure_char = value[failure_index] if failure_index < len(value) else ""
    reason, fix = _diagnose_character_constraint(pattern, value, failure_index)
    return failure_index, failure_char, reason, fix


def _build_suggested_fix(
    api_object: APIObject,
    length: int,
    base_fix: str | None,
) -> str | None:
    """Compose actionable remediation instructions including length and sample values."""
    fix = base_fix
    if api_object.min_length is not None and length < api_object.min_length:
        diff = api_object.min_length - length
        len_rec = f"Minimum length is {api_object.min_length} (add {diff} more characters)."
        fix = f"{fix} {len_rec}" if fix else len_rec
    elif api_object.max_length is not None and length > api_object.max_length:
        diff = length - api_object.max_length
        len_rec = f"Maximum length is {api_object.max_length} (shorten by {diff} characters)."
        fix = f"{fix} {len_rec}" if fix else len_rec

    try:
        sample = api_object.generate()
        if sample and len(sample) <= 80:
            sample_tip = f" Example valid value: '{sample}'."
            fix = (fix + sample_tip) if fix else sample_tip.strip()
    except Exception:
        pass
    return fix


def _build_visual_pointer(
    value: str,
    failure_index: int | None,
    failure_reason: str | None,
) -> str | None:
    """Build multi-line terminal visual pointer highlighting failure_index with a caret."""
    if failure_index is None or not value:
        return None
    clamped_idx = max(0, min(failure_index, len(value)))
    reason_desc = failure_reason or "constraint violation"
    return f"{value}\n{' ' * clamped_idx}^ character {clamped_idx}: {reason_desc}"


def _check_length_bounds(
    api_object: APIObject,
    length: int,
    errors: list[str],
) -> tuple[int | None, str | None, str | None]:
    """Check min/max length constraints and return failure attributes if violated."""
    if api_object.min_length is not None and length < api_object.min_length:
        errors.append(
            f"Length {length} is shorter than minimum required length ({api_object.min_length}) "
            f"(below minimum length {api_object.min_length})."
        )
        diff = api_object.min_length - length
        return (
            length,
            f"length {length} is below minimum length {api_object.min_length}",
            f"Add at least {diff} more character(s) (minimum length is {api_object.min_length}).",
        )
    if api_object.max_length is not None and length > api_object.max_length:
        errors.append(f"Length {length} exceeds maximum allowed length ({api_object.max_length}).")
        diff = length - api_object.max_length
        return (
            api_object.max_length,
            f"exceeds maximum allowed length of {api_object.max_length}",
            f"Shorten value by {diff} character(s) (maximum allowed is {api_object.max_length}).",
        )
    return None, None, None


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

    # 1. Length bounds
    len_idx, len_reason, len_fix = _check_length_bounds(api_object, length, errors)

    # 2. Regex matching
    try:
        match = re.match(api_object.pattern, value)
        prefix_matched = match is not None
        full_matched = re.fullmatch(api_object.pattern, value) is not None
    except Exception:
        match = None
        prefix_matched = False
        full_matched = False

    failure_index: int | None = len_idx
    failure_char: str | None = None
    failure_reason: str | None = len_reason
    suggested_fix: str | None = len_fix

    if not prefix_matched or (strict and not full_matched):
        fail_idx, fail_c, reason, fix = _analyze_regex_mismatch(
            api_object.pattern,
            api_object.name,
            service_name,
            value,
            prefix_matched=prefix_matched,
            full_matched=full_matched,
            match=match,
        )
        failure_index = fail_idx
        failure_char = fail_c
        failure_reason = reason
        suggested_fix = fix

        if not prefix_matched:
            errors.append(
                f"Value does not match required regex pattern: {api_object.pattern} "
                f"(failed at character {fail_idx}: '{fail_c or value[fail_idx:]}' {reason})."
            )
        elif strict and not full_matched:
            matched_substr = match.group(0) if match else ""
            errors.append(
                f"Value only matches prefix '{matched_substr}' under botocore re.match; "
                f"strict mode requires full string match (failed at character {fail_idx}: '{fail_c}' {reason})."
            )
    elif not full_matched:
        warnings.append(
            "Value matches prefix under botocore's re.match semantics, "
            "but does not match end-to-end (use --strict to enforce)."
        )

    if errors:
        suggested_fix = _build_suggested_fix(api_object, length, suggested_fix)

    visual_pointer = _build_visual_pointer(value, failure_index, failure_reason) if errors else None
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
        failure_index=failure_index,
        failure_char=failure_char,
        failure_reason=failure_reason,
        suggested_fix=suggested_fix,
        visual_pointer=visual_pointer,
    )
