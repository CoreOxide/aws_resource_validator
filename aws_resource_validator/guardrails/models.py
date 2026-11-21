"""Data models and exceptions for AI agent / LLM tool-call guardrails."""

from __future__ import annotations

import json
from collections.abc import Mapping
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Literal

if TYPE_CHECKING:
    from aws_resource_validator.core.diagnostics import ValidationResult

ToolMessageFormat = Literal["generic", "openai", "anthropic", "gemini"]


def _json_safe(value: Any) -> Any:
    """Convert arbitrary values into JSON-serializable representations."""
    if value is None or isinstance(value, (bool, int, float, str)):
        return value
    if isinstance(value, Mapping):
        return {str(k): _json_safe(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(v) for v in value]
    return repr(value)


@dataclass(frozen=True, slots=True)
class ToolViolation:
    """A single parameter or invocation error detected before executing an AWS tool."""

    parameter: str
    code: str
    message: str
    value: Any = None
    shape_name: str | None = None
    suggested_fix: str | None = None
    pattern: str | None = None
    min_length: int | None = None
    max_length: int | None = None
    validation_result: ValidationResult | None = None

    def to_dict(self) -> dict[str, Any]:
        """Serialize the violation to a JSON-compatible dictionary."""
        return {
            "parameter": self.parameter,
            "code": self.code,
            "message": self.message,
            "value": _json_safe(self.value),
            "shape_name": self.shape_name,
            "suggested_fix": self.suggested_fix,
            "pattern": self.pattern,
            "min_length": self.min_length,
            "max_length": self.max_length,
            "validation_result": self.validation_result.to_dict() if self.validation_result is not None else None,
        }


@dataclass(frozen=True, slots=True)
class ToolValidationResult:
    """Outcome of validating an LLM-generated AWS tool call."""

    is_valid: bool
    service: str
    operation: str
    arguments: Mapping[str, Any]
    violations: tuple[ToolViolation, ...] = ()

    @property
    def error_count(self) -> int:
        """Return the number of validation violations detected."""
        return len(self.violations)

    def to_dict(self) -> dict[str, Any]:
        """Serialize the validation result to a JSON-compatible dictionary."""
        return {
            "is_valid": self.is_valid,
            "service": self.service,
            "operation": self.operation,
            "error_count": self.error_count,
            "arguments": _json_safe(dict(self.arguments)),
            "violations": [v.to_dict() for v in self.violations],
        }

    def to_json(self) -> str:
        """Serialize the validation result to a JSON string."""
        return json.dumps(self.to_dict(), default=str)

    def to_llm_feedback(
        self,
        *,
        include_pattern: bool = True,
        max_violations: int | None = None,
    ) -> str:
        """Format a concise, actionable retry prompt for LLM self-correction.

        Returns an empty string when ``is_valid`` is ``True``.
        """
        if self.is_valid:
            return ""

        total = len(self.violations)
        displayed = self.violations[:max_violations] if max_violations is not None else self.violations

        lines: list[str] = [
            f"Tool call validation failed for AWS {self.service}.{self.operation} ({total} error(s)):",
        ]

        for violation in displayed:
            lines.extend(_format_violation_lines(violation, include_pattern=include_pattern))

        if max_violations is not None and total > max_violations:
            remaining = total - max_violations
            lines.append(f"... and {remaining} more error(s).")

        lines.append("Please fix the invalid argument(s) and retry the tool call.")
        return "\n".join(lines)

    def to_tool_message(
        self,
        tool_call_id: str | None = None,
        *,
        format: ToolMessageFormat = "generic",
    ) -> dict[str, Any]:
        """Format the validation result as a provider-ready tool-result payload."""
        feedback = self.to_llm_feedback()
        if format == "openai":
            return {
                "role": "tool",
                "tool_call_id": tool_call_id or "",
                "content": feedback or "OK",
            }
        if format == "anthropic":
            return {
                "type": "tool_result",
                "tool_use_id": tool_call_id or "",
                "is_error": not self.is_valid,
                "content": feedback or "OK",
            }
        if format == "gemini":
            response_payload: dict[str, Any] = (
                {"status": "ok"}
                if self.is_valid
                else {
                    "error": feedback,
                    "violations": [v.to_dict() for v in self.violations],
                }
            )
            return {
                "function_response": {
                    "name": f"{self.service}.{self.operation}",
                    "response": response_payload,
                }
            }
        if format == "generic":
            return {
                "is_valid": self.is_valid,
                "service": self.service,
                "operation": self.operation,
                "feedback": feedback,
                "violations": [v.to_dict() for v in self.violations],
            }
        raise ValueError(
            f"Unsupported tool message format: {format!r}. Must be 'generic', 'openai', 'anthropic', or 'gemini'."
        )


def _format_violation_lines(violation: ToolViolation, *, include_pattern: bool) -> list[str]:
    """Render a single ToolViolation into readable bullet lines for an LLM."""
    label = f"Parameter '{violation.parameter}'" if violation.parameter else "Tool call"
    meta_parts: list[str] = []
    if violation.shape_name:
        meta_parts.append(f"shape {violation.shape_name}")
    if violation.value is not None:
        meta_parts.append(f"got {violation.value!r}")

    meta = f" ({', '.join(meta_parts)})" if meta_parts else ""
    lines = [f"- {label}{meta}: {violation.message}"]

    if violation.suggested_fix:
        lines.append(f"  Fix: {violation.suggested_fix}")

    constraints: list[str] = []
    if violation.min_length is not None:
        constraints.append(f"min_length={violation.min_length}")
    if violation.max_length is not None:
        constraints.append(f"max_length={violation.max_length}")
    if include_pattern and violation.pattern:
        constraints.append(f"pattern={violation.pattern!r}")
    if constraints:
        lines.append(f"  Constraints: {', '.join(constraints)}")

    return lines


class ToolGuardrailError(ValueError):
    """Raised by ``@guard_tool(..., on_error='raise')`` when validation fails."""

    def __init__(self, result: ToolValidationResult, message: str | None = None) -> None:
        self.result = result
        self.violations = result.violations
        self.feedback = result.to_llm_feedback()
        super().__init__(
            message or self.feedback or f"Tool validation failed for {result.service}.{result.operation}"
        )
