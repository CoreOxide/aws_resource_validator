"""Core validation engine for AI agent / LLM AWS tool-call arguments."""

from __future__ import annotations

import difflib
import json
from collections.abc import Callable, Mapping
from datetime import date, datetime
from typing import Any, Literal

from aws_resource_validator.client_wrapper.rules import get_extra_validator
from aws_resource_validator.client_wrapper.validator import ShapeValidator
from aws_resource_validator.core.diagnostics import ValidationResult, diagnose_validation
from aws_resource_validator.guardrails.models import ToolValidationResult, ToolViolation
from aws_resource_validator.guardrails.resolver import (
    resolve_botocore_operation,
    resolve_botocore_service,
)


class AWSToolGuardrail:
    """Reusable, cached guardrail for validating LLM-generated AWS tool calls.

    Validates tool arguments offline against botocore service models,
    ``class_registry`` regex/length rules, built-in S3/RDS/SQS rules, and
    ARN structure checks before any AWS API call is executed.
    """

    def __init__(
        self,
        *,
        strict: bool = True,
        check_required: bool = True,
        check_unknown: bool = True,
        custom_rules: Mapping[Any, Any] | None = None,
        tool_name_map: Mapping[str, tuple[str, str]] | None = None,
    ) -> None:
        self.strict = strict
        self.check_required = check_required
        self.check_unknown = check_unknown
        self.custom_rules = custom_rules
        self.tool_name_map = tool_name_map
        self._shape_validator = ShapeValidator(custom_rules=custom_rules)

    def validate(
        self,
        service: str,
        operation: str,
        arguments: Mapping[str, Any] | str,
        *,
        strict: bool | None = None,
        check_required: bool | None = None,
        check_unknown: bool | None = None,
    ) -> ToolValidationResult:
        """Validate ``arguments`` for ``service.operation`` and return structured diagnostics."""
        effective_strict = self.strict if strict is None else strict
        effective_required = self.check_required if check_required is None else check_required
        effective_unknown = self.check_unknown if check_unknown is None else check_unknown

        parsed_args, parse_violation = _parse_arguments(arguments)
        if parse_violation is not None:
            return ToolValidationResult(
                is_valid=False,
                service=service,
                operation=operation,
                arguments={},
                violations=(parse_violation,),
            )

        service_model, canonical_service, svc_suggestions = resolve_botocore_service(service)
        if service_model is None:
            fix = (
                f"Did you mean: {', '.join(svc_suggestions)}?"
                if svc_suggestions
                else "Use a valid AWS service name such as 's3', 'iam', 'lambda', or 'dynamodb'."
            )
            violation = ToolViolation(
                parameter="",
                code="unknown_service",
                value=service,
                message=f"Unknown AWS service '{service}'.",
                suggested_fix=fix,
            )
            return ToolValidationResult(
                is_valid=False,
                service=service,
                operation=operation,
                arguments=parsed_args,
                violations=(violation,),
            )

        op_model, canonical_operation, op_suggestions = resolve_botocore_operation(service_model, operation)
        if op_model is None:
            fix = (
                f"Did you mean: {', '.join(op_suggestions)}?"
                if op_suggestions
                else f"Check valid operation names for AWS service '{canonical_service}'."
            )
            violation = ToolViolation(
                parameter="",
                code="unknown_operation",
                value=operation,
                message=f"Unknown operation '{operation}' for AWS service '{canonical_service}'.",
                suggested_fix=fix,
            )
            return ToolValidationResult(
                is_valid=False,
                service=canonical_service,
                operation=operation,
                arguments=parsed_args,
                violations=(violation,),
            )

        violations: list[ToolViolation] = []
        input_shape = getattr(op_model, "input_shape", None)
        if input_shape is None:
            if effective_unknown and parsed_args:
                for key, val in parsed_args.items():
                    violations.append(
                        ToolViolation(
                            parameter=key,
                            code="unknown_parameter",
                            value=val,
                            message=(
                                f"Operation '{canonical_service}.{canonical_operation}' accepts no input parameters."
                            ),
                            suggested_fix="Call this operation with an empty argument object '{}'.",
                        )
                    )
        else:
            self._validate_structure(
                service_name=canonical_service,
                value=parsed_args,
                shape=input_shape,
                path="",
                strict=effective_strict,
                check_required=effective_required,
                check_unknown=effective_unknown,
                violations=violations,
            )

        return ToolValidationResult(
            is_valid=len(violations) == 0,
            service=canonical_service,
            operation=canonical_operation,
            arguments=parsed_args,
            violations=tuple(violations),
        )

    def validate_tool_call(
        self,
        tool_call: Any,
        *,
        service: str | None = None,
        operation: str | None = None,
        tool_name_map: Mapping[str, tuple[str, str]] | None = None,
    ) -> ToolValidationResult:
        """Validate a provider-formatted tool-call object or dict using this guardrail."""
        from aws_resource_validator.guardrails.adapters import validate_tool_call  # noqa: PLC0415

        return validate_tool_call(
            tool_call,
            service=service,
            operation=operation,
            tool_name_map=tool_name_map if tool_name_map is not None else self.tool_name_map,
            strict=self.strict,
            check_required=self.check_required,
            check_unknown=self.check_unknown,
            custom_rules=self.custom_rules,
        )

    def guard(
        self,
        service: str,
        operation: str,
        *,
        on_error: Literal["return_feedback", "raise"] | Callable[[ToolValidationResult], Any] = "return_feedback",
        arg_mapping: Mapping[str, str] | None = None,
    ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        """Return a ``@guard_tool`` decorator configured with this guardrail's settings."""
        from aws_resource_validator.guardrails.adapters import guard_tool  # noqa: PLC0415

        return guard_tool(
            service,
            operation,
            on_error=on_error,
            arg_mapping=arg_mapping,
            strict=self.strict,
            check_required=self.check_required,
            check_unknown=self.check_unknown,
            custom_rules=self.custom_rules,
        )

    def _validate_structure(
        self,
        *,
        service_name: str,
        value: Mapping[str, Any],
        shape: Any,
        path: str,
        strict: bool,
        check_required: bool,
        check_unknown: bool,
        violations: list[ToolViolation],
    ) -> None:
        members: Mapping[str, Any] = getattr(shape, "members", {})
        required_members: tuple[str, ...] = tuple(getattr(shape, "required_members", ()))

        if check_required:
            for req in required_members:
                if req not in value or value[req] is None:
                    req_path = f"{path}.{req}" if path else req
                    req_shape = members.get(req)
                    violations.append(
                        ToolViolation(
                            parameter=req_path,
                            code="missing_required",
                            value=None,
                            shape_name=getattr(req_shape, "name", None),
                            message=f"Missing required parameter '{req}'.",
                            suggested_fix=f"Provide a valid value for required parameter '{req}'.",
                        )
                    )

        valid_keys = list(members.keys())
        for field_name, field_value in value.items():
            next_path = f"{path}.{field_name}" if path else field_name
            if field_name not in members:
                if check_unknown:
                    close = difflib.get_close_matches(field_name, valid_keys, n=3, cutoff=0.5)
                    fix = (
                        f"Did you mean: {', '.join(close)}?"
                        if close
                        else f"Remove '{field_name}' or use a valid parameter."
                    )
                    violations.append(
                        ToolViolation(
                            parameter=next_path,
                            code="unknown_parameter",
                            value=field_value,
                            message=f"Unknown parameter '{field_name}' for shape '{getattr(shape, 'name', '')}'.",
                            suggested_fix=fix,
                        )
                    )
                continue

            self._validate_node(
                service_name=service_name,
                value=field_value,
                shape=members[field_name],
                path=next_path,
                param_name=field_name,
                strict=strict,
                check_required=check_required,
                check_unknown=check_unknown,
                violations=violations,
            )

    def _validate_list(
        self,
        *,
        service_name: str,
        value: list[Any] | tuple[Any, ...],
        shape: Any,
        path: str,
        param_name: str | None,
        strict: bool,
        check_required: bool,
        check_unknown: bool,
        violations: list[ToolViolation],
    ) -> None:
        member_shape = getattr(shape, "member", None)
        if member_shape is None:
            return
        for idx, item in enumerate(value):
            self._validate_node(
                service_name=service_name,
                value=item,
                shape=member_shape,
                path=f"{path}[{idx}]",
                param_name=param_name,
                strict=strict,
                check_required=check_required,
                check_unknown=check_unknown,
                violations=violations,
            )

    def _validate_map(
        self,
        *,
        service_name: str,
        value: Mapping[Any, Any],
        shape: Any,
        path: str,
        param_name: str | None,
        strict: bool,
        check_required: bool,
        check_unknown: bool,
        violations: list[ToolViolation],
    ) -> None:
        key_shape = getattr(shape, "key", None)
        val_shape = getattr(shape, "value", None)
        for k, v in value.items():
            if key_shape is not None:
                self._validate_node(
                    service_name=service_name,
                    value=k,
                    shape=key_shape,
                    path=f"{path}.key({k})",
                    param_name=str(k),
                    strict=strict,
                    check_required=check_required,
                    check_unknown=check_unknown,
                    violations=violations,
                )
            if val_shape is not None:
                self._validate_node(
                    service_name=service_name,
                    value=v,
                    shape=val_shape,
                    path=f"{path}[{k}]",
                    param_name=param_name,
                    strict=strict,
                    check_required=check_required,
                    check_unknown=check_unknown,
                    violations=violations,
                )

    def _validate_string(
        self,
        *,
        service_name: str,
        value: str,
        shape: Any,
        path: str,
        param_name: str | None,
        strict: bool,
        violations: list[ToolViolation],
    ) -> None:
        shape_name: str = getattr(shape, "name", "")
        enum_values: list[str] | None = getattr(shape, "enum", None)
        if enum_values and value not in enum_values:
            close = difflib.get_close_matches(value, enum_values, n=3, cutoff=0.4)
            allowed_preview = ", ".join(repr(e) for e in enum_values[:10])
            if len(enum_values) > 10:
                allowed_preview += f", ... ({len(enum_values)} total)"
            fix = f"Did you mean: {', '.join(repr(c) for c in close)}?" if close else f"Use one of: {allowed_preview}."
            violations.append(
                ToolViolation(
                    parameter=path,
                    code="invalid_enum",
                    value=value,
                    shape_name=shape_name or None,
                    message=f"Value '{value}' is not a valid enum choice. Allowed: {allowed_preview}.",
                    suggested_fix=fix,
                )
            )
            return

        api_obj = self._shape_validator.resolve_api_object(service_name, shape, param_name)
        if api_obj is None:
            return

        res: ValidationResult = diagnose_validation(api_obj, service_name, value, strict=strict)
        extra_validator = get_extra_validator(service_name, shape_name, param_name)
        all_errors = list(res.errors)
        if extra_validator is not None:
            extra_errs = extra_validator(value)
            if extra_errs:
                all_errors.extend(extra_errs)
                res = ValidationResult(
                    is_valid=False,
                    value=res.value,
                    service_name=res.service_name,
                    shape_name=res.shape_name,
                    pattern=res.pattern,
                    length=res.length,
                    min_length=res.min_length,
                    max_length=res.max_length,
                    errors=all_errors,
                    warnings=res.warnings,
                    strict=res.strict,
                    prefix_matched=res.prefix_matched,
                    full_matched=res.full_matched,
                    failure_index=res.failure_index,
                    failure_char=res.failure_char,
                    failure_reason=res.failure_reason,
                    suggested_fix=res.suggested_fix,
                    visual_pointer=res.visual_pointer,
                )

        if not res.is_valid:
            violations.append(
                ToolViolation(
                    parameter=path,
                    code="invalid_value",
                    value=value,
                    shape_name=shape_name or res.shape_name,
                    message="; ".join(all_errors),
                    suggested_fix=res.suggested_fix,
                    pattern=res.pattern,
                    min_length=res.min_length,
                    max_length=res.max_length,
                    validation_result=res,
                )
            )

    def _validate_node(
        self,
        *,
        service_name: str,
        value: Any,
        shape: Any,
        path: str,
        param_name: str | None,
        strict: bool,
        check_required: bool,
        check_unknown: bool,
        violations: list[ToolViolation],
    ) -> None:
        if value is None:
            return

        type_name: str = getattr(shape, "type_name", "")
        shape_name: str = getattr(shape, "name", "")

        if type_name in ("structure", "list", "map", "string"):
            self._validate_complex_or_string(
                service_name=service_name,
                value=value,
                shape=shape,
                type_name=type_name,
                shape_name=shape_name,
                path=path,
                param_name=param_name,
                strict=strict,
                check_required=check_required,
                check_unknown=check_unknown,
                violations=violations,
            )
            return

        scalar_violation = _validate_scalar_type_and_bounds(path, shape, type_name, shape_name, value)
        if scalar_violation is not None:
            violations.append(scalar_violation)

    def _validate_complex_or_string(
        self,
        *,
        service_name: str,
        value: Any,
        shape: Any,
        type_name: str,
        shape_name: str,
        path: str,
        param_name: str | None,
        strict: bool,
        check_required: bool,
        check_unknown: bool,
        violations: list[ToolViolation],
    ) -> None:
        if type_name == "structure":
            if not isinstance(value, Mapping):
                violations.append(_type_mismatch(path, shape_name, "object/dict", value))
            else:
                self._validate_structure(
                    service_name=service_name,
                    value=value,
                    shape=shape,
                    path=path,
                    strict=strict,
                    check_required=check_required,
                    check_unknown=check_unknown,
                    violations=violations,
                )
        elif type_name == "list":
            if not isinstance(value, (list, tuple)):
                violations.append(_type_mismatch(path, shape_name, "list", value))
            else:
                self._validate_list(
                    service_name=service_name,
                    value=value,
                    shape=shape,
                    path=path,
                    param_name=param_name,
                    strict=strict,
                    check_required=check_required,
                    check_unknown=check_unknown,
                    violations=violations,
                )
        elif type_name == "map":
            if not isinstance(value, Mapping):
                violations.append(_type_mismatch(path, shape_name, "object/dict", value))
            else:
                self._validate_map(
                    service_name=service_name,
                    value=value,
                    shape=shape,
                    path=path,
                    param_name=param_name,
                    strict=strict,
                    check_required=check_required,
                    check_unknown=check_unknown,
                    violations=violations,
                )
        elif type_name == "string":
            if not isinstance(value, str):
                violations.append(_type_mismatch(path, shape_name, "string", value))
            else:
                self._validate_string(
                    service_name=service_name,
                    value=value,
                    shape=shape,
                    path=path,
                    param_name=param_name,
                    strict=strict,
                    violations=violations,
                )


def _parse_arguments(arguments: Mapping[str, Any] | str) -> tuple[dict[str, Any], ToolViolation | None]:
    """Parse raw tool arguments from a Mapping or JSON string."""
    if isinstance(arguments, str):
        try:
            decoded = json.loads(arguments)
        except json.JSONDecodeError as exc:
            return {}, ToolViolation(
                parameter="",
                code="invalid_json",
                value=arguments,
                message=f"Malformed JSON arguments: {exc.msg} at position {exc.pos}.",
                suggested_fix="Provide valid JSON representing an object of named parameters.",
            )
        if not isinstance(decoded, dict):
            return {}, ToolViolation(
                parameter="",
                code="invalid_json",
                value=decoded,
                message=f"Tool arguments JSON must decode to an object, got {type(decoded).__name__}.",
                suggested_fix="Wrap parameters in a JSON object (e.g. '{\"Bucket\": \"my-bucket\"}').",
            )
        return decoded, None

    if isinstance(arguments, Mapping):
        return dict(arguments), None

    return {}, ToolViolation(
        parameter="",
        code="type_mismatch",
        value=arguments,
        message=f"Expected tool arguments to be a mapping or JSON string, got {type(arguments).__name__}.",
        suggested_fix="Pass a dictionary of parameters or a JSON-encoded object string.",
    )


def _type_mismatch(path: str, shape_name: str, expected: str, value: Any) -> ToolViolation:
    """Build a standardized type_mismatch ToolViolation."""
    return ToolViolation(
        parameter=path,
        code="type_mismatch",
        value=value,
        shape_name=shape_name or None,
        message=f"Expected {expected}, got {type(value).__name__}.",
        suggested_fix=f"Provide a valid {expected} value for '{path}'.",
    )


def _validate_scalar_type_and_bounds(
    path: str,
    shape: Any,
    type_name: str,
    shape_name: str,
    value: Any,
) -> ToolViolation | None:
    """Validate non-string botocore scalar types and numeric min/max bounds."""
    violation: ToolViolation | None = None
    if type_name == "boolean":
        if not isinstance(value, bool):
            violation = _type_mismatch(path, shape_name, "boolean", value)
    elif type_name in ("integer", "long"):
        if isinstance(value, bool) or not isinstance(value, int):
            violation = _type_mismatch(path, shape_name, "integer", value)
        else:
            violation = _check_numeric_bounds(path, shape, shape_name, value)
    elif type_name in ("float", "double"):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            violation = _type_mismatch(path, shape_name, "number", value)
        else:
            violation = _check_numeric_bounds(path, shape, shape_name, value)
    elif type_name == "blob":
        if not isinstance(value, (bytes, bytearray, str)) and not hasattr(value, "read"):
            violation = _type_mismatch(path, shape_name, "bytes, string, or file-like object", value)
    elif type_name == "timestamp" and (
        isinstance(value, bool) or not isinstance(value, (datetime, date, str, int, float))
    ):
        violation = _type_mismatch(
            path,
            shape_name,
            "timestamp (ISO-8601 string, datetime, or epoch number)",
            value,
        )
    return violation


def _check_numeric_bounds(
    path: str,
    shape: Any,
    shape_name: str,
    value: int | float,
) -> ToolViolation | None:
    """Check botocore min/max metadata on numeric shapes."""
    metadata: Mapping[str, Any] = getattr(shape, "metadata", {})
    min_val = metadata.get("min")
    max_val = metadata.get("max")
    if min_val is not None and value < min_val:
        return ToolViolation(
            parameter=path,
            code="out_of_range",
            value=value,
            shape_name=shape_name or None,
            message=f"Value {value} is below minimum {min_val}.",
            suggested_fix=f"Provide a value >= {min_val}.",
        )
    if max_val is not None and value > max_val:
        return ToolViolation(
            parameter=path,
            code="out_of_range",
            value=value,
            shape_name=shape_name or None,
            message=f"Value {value} exceeds maximum {max_val}.",
            suggested_fix=f"Provide a value <= {max_val}.",
        )
    return None


_DEFAULT_GUARDRAIL = AWSToolGuardrail()


def validate_tool_arguments(
    service: str,
    operation: str,
    arguments: Mapping[str, Any] | str,
    *,
    strict: bool = True,
    check_required: bool = True,
    check_unknown: bool = True,
    custom_rules: Mapping[Any, Any] | None = None,
) -> ToolValidationResult:
    """Validate LLM-generated arguments for an AWS tool call before execution.

    Parameters:
        service: AWS service name (e.g. ``"s3"``, ``"iam"``, ``"lambda"``).
        operation: AWS operation name (e.g. ``"PutObject"``, ``"put_object"``).
        arguments: Parameter dictionary or JSON string generated by an LLM.
        strict: Enforce full-string regex matching (default ``True``).
        check_required: Verify required botocore parameters are present (default ``True``).
        check_unknown: Reject unknown/hallucinated parameter names (default ``True``).
        custom_rules: Optional custom ``APIObject`` overrides keyed by ``(service, shape)``
            or shape name.

    Returns:
        A :class:`ToolValidationResult` with ``is_valid``, ``violations``, and
        ``to_llm_feedback()`` for in-context LLM self-correction.
    """
    guardrail = AWSToolGuardrail(custom_rules=custom_rules) if custom_rules is not None else _DEFAULT_GUARDRAIL
    return guardrail.validate(
        service,
        operation,
        arguments,
        strict=strict,
        check_required=check_required,
        check_unknown=check_unknown,
    )
