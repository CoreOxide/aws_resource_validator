"""AI agent / LLM tool-call guardrails for pre-execution AWS argument validation."""

from __future__ import annotations

from aws_resource_validator.guardrails.adapters import guard_tool, validate_tool_call
from aws_resource_validator.guardrails.models import (
    ToolGuardrailError,
    ToolValidationResult,
    ToolViolation,
)
from aws_resource_validator.guardrails.validator import (
    AWSToolGuardrail,
    validate_tool_arguments,
)

__all__ = [
    "AWSToolGuardrail",
    "ToolGuardrailError",
    "ToolValidationResult",
    "ToolViolation",
    "guard_tool",
    "validate_tool_arguments",
    "validate_tool_call",
]
