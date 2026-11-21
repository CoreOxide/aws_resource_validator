"""Framework-agnostic adapters and decorators for LLM tool-calling loops."""

from __future__ import annotations

import functools
import inspect
from collections.abc import Callable, Mapping
from typing import Any, Literal

from aws_resource_validator.guardrails.models import ToolGuardrailError, ToolValidationResult, ToolViolation
from aws_resource_validator.guardrails.resolver import (
    _normalize,
    parse_tool_name,
    resolve_botocore_operation,
    resolve_botocore_service,
)
from aws_resource_validator.guardrails.validator import validate_tool_arguments

_MISSING = object()


def _get_field(obj: Any, key: str) -> Any:
    """Read a key from a Mapping or an attribute from an object, returning _MISSING if absent."""
    if isinstance(obj, Mapping):
        return obj.get(key, _MISSING)
    return getattr(obj, key, _MISSING)


def _extract_tool_call(tool_call: Any) -> tuple[str | None, Any]:
    """Extract ``(tool_name, raw_arguments)`` from OpenAI, Anthropic, Gemini, or generic payloads."""
    # OpenAI: {"function": {"name": ..., "arguments": ...}} or tool_call.function
    func_block = _get_field(tool_call, "function")
    if func_block is not _MISSING and func_block is not None:
        name = _get_field(func_block, "name")
        args = _get_field(func_block, "arguments")
        return (
            name if isinstance(name, str) else None,
            {} if args is _MISSING else args,
        )

    # Anthropic tool_use / Gemini function_call / generic dict or object
    name = _get_field(tool_call, "name")
    tool_name = name if isinstance(name, str) else None

    for attr in ("input", "args", "arguments"):
        val = _get_field(tool_call, attr)
        if val is not _MISSING:
            return tool_name, val

    return tool_name, {}


def validate_tool_call(
    tool_call: Any,
    *,
    service: str | None = None,
    operation: str | None = None,
    tool_name_map: Mapping[str, tuple[str, str]] | None = None,
    strict: bool = True,
    check_required: bool = True,
    check_unknown: bool = True,
    custom_rules: Mapping[Any, Any] | None = None,
) -> ToolValidationResult:
    """Validate an OpenAI, Anthropic, Gemini, or generic tool-call payload.

    If ``service`` and ``operation`` are omitted, they are inferred from the
    tool call's function name using ``tool_name_map`` or standard separators
    (``"s3.PutObject"``, ``"s3:PutObject"``, ``"s3_put_object"``, etc.).
    """
    tool_name, raw_args = _extract_tool_call(tool_call)

    resolved_service = service
    resolved_operation = operation
    if resolved_service is None or resolved_operation is None:
        parsed = parse_tool_name(tool_name, tool_name_map) if tool_name else None
        if parsed is not None:
            resolved_service = resolved_service or parsed[0]
            resolved_operation = resolved_operation or parsed[1]

    if not resolved_service or not resolved_operation:
        violation = ToolViolation(
            parameter="",
            code="unknown_operation",
            value=tool_name,
            message=(
                f"Could not resolve AWS service and operation from tool name {tool_name!r}."
                if tool_name
                else "Tool call payload is missing a tool name and no explicit service/operation was provided."
            ),
            suggested_fix=(
                "Pass explicit 'service' and 'operation' arguments, provide 'tool_name_map', "
                "or name the tool '<service>.<Operation>' (e.g. 's3.PutObject')."
            ),
        )
        return ToolValidationResult(
            is_valid=False,
            service=resolved_service or "",
            operation=resolved_operation or tool_name or "",
            arguments={},
            violations=(violation,),
        )

    return validate_tool_arguments(
        resolved_service,
        resolved_operation,
        raw_args,
        strict=strict,
        check_required=check_required,
        check_unknown=check_unknown,
        custom_rules=custom_rules,
    )


def _build_member_lookup(service: str, operation: str) -> dict[str, str]:
    """Build a normalized-name -> botocore-member-name lookup table for an operation."""
    service_model, _, _ = resolve_botocore_service(service)
    if service_model is None:
        return {}
    op_model, _, _ = resolve_botocore_operation(service_model, operation)
    if op_model is None:
        return {}
    input_shape = getattr(op_model, "input_shape", None)
    if input_shape is None:
        return {}
    members: Mapping[str, Any] = getattr(input_shape, "members", {})
    return {_normalize(member_name): member_name for member_name in members}


def _map_bound_arguments(
    sig: inspect.Signature,
    args: tuple[Any, ...],
    kwargs: dict[str, Any],
    arg_mapping: Mapping[str, str] | None,
    member_lookup: Mapping[str, str],
) -> dict[str, Any]:
    """Bind Python function arguments and map them to AWS operation parameter names."""
    bound = sig.bind_partial(*args, **kwargs)
    bound.apply_defaults()
    mapped: dict[str, Any] = {}
    for param_name, val in bound.arguments.items():
        if arg_mapping and param_name in arg_mapping:
            aws_key = arg_mapping[param_name]
        elif _normalize(param_name) in member_lookup:
            aws_key = member_lookup[_normalize(param_name)]
        else:
            aws_key = param_name
        mapped[aws_key] = val
    return mapped


def _handle_invalid_result(
    result: ToolValidationResult,
    on_error: Literal["return_feedback", "raise"] | Callable[[ToolValidationResult], Any],
) -> Any:
    """Dispatch an invalid validation result according to ``on_error``."""
    if on_error == "return_feedback":
        return result.to_llm_feedback()
    if on_error == "raise":
        raise ToolGuardrailError(result)
    return on_error(result)


def guard_tool(
    service: str,
    operation: str,
    *,
    on_error: Literal["return_feedback", "raise"] | Callable[[ToolValidationResult], Any] = "return_feedback",
    arg_mapping: Mapping[str, str] | None = None,
    strict: bool = True,
    check_required: bool = True,
    check_unknown: bool = True,
    custom_rules: Mapping[Any, Any] | None = None,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Decorate a sync or async Python tool function with pre-execution AWS validation.

    Parameters:
        service: Target AWS service name (e.g. ``"s3"``).
        operation: Target AWS operation name (e.g. ``"PutObject"``).
        on_error: Behavior when validation fails:
            - ``"return_feedback"`` (default): short-circuits and returns
              ``result.to_llm_feedback()`` so the LLM can self-correct.
            - ``"raise"``: raises :class:`ToolGuardrailError`.
            - callable: invokes ``on_error(result)`` and returns its result.
        arg_mapping: Optional mapping from Python parameter names to AWS
            parameter names (e.g. ``{"bucket_name": "Bucket"}``). When omitted,
            snake_case names are automatically matched to AWS PascalCase members.
        strict: Passed through to :func:`validate_tool_arguments`.
        check_required: Passed through to :func:`validate_tool_arguments`.
        check_unknown: Passed through to :func:`validate_tool_arguments`.
        custom_rules: Passed through to :func:`validate_tool_arguments`.
    """
    if on_error not in ("return_feedback", "raise") and not callable(on_error):
        raise ValueError(
            f"Invalid on_error handler: {on_error!r}. Must be 'return_feedback', 'raise', or a callable."
        )

    member_lookup = _build_member_lookup(service, operation)

    def _decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        sig = inspect.signature(func)

        def _validate_call(args: tuple[Any, ...], kwargs: dict[str, Any]) -> ToolValidationResult:
            mapped_args = _map_bound_arguments(sig, args, kwargs, arg_mapping, member_lookup)
            return validate_tool_arguments(
                service,
                operation,
                mapped_args,
                strict=strict,
                check_required=check_required,
                check_unknown=check_unknown,
                custom_rules=custom_rules,
            )

        if inspect.iscoroutinefunction(func):

            @functools.wraps(func)
            async def _async_wrapper(*args: Any, **kwargs: Any) -> Any:
                result = _validate_call(args, kwargs)
                if not result.is_valid:
                    return _handle_invalid_result(result, on_error)
                return await func(*args, **kwargs)

            return _async_wrapper

        @functools.wraps(func)
        def _sync_wrapper(*args: Any, **kwargs: Any) -> Any:
            result = _validate_call(args, kwargs)
            if not result.is_valid:
                return _handle_invalid_result(result, on_error)
            return func(*args, **kwargs)

        return _sync_wrapper

    return _decorator
