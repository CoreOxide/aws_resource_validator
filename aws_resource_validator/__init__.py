"""Public API for the aws_resource_validator runtime.

Generated artifacts live under :mod:`aws_resource_validator.class_definitions`
(single-file Pipeline A output) and :mod:`aws_resource_validator.pydantic_models`
(Pipeline B output, one sub-package per AWS service). The generator itself
lives under :mod:`aws_resource_validator.generator` and is not part of the
runtime surface.
"""

__version__ = "2.7.1"

from aws_resource_validator.client_wrapper import (
    AWSValidationError,
    AWSValidationWarning,
    unwrap_client,
    unwrap_session,
    wrap_client,
    wrap_session,
)
from aws_resource_validator.core import (
    ARN,
    APIObject,
    APIRegistry,
    ARNParseError,
    BaseValidatorModel,
    EventStream,
    Service,
    ValidationResult,
    diagnose_validation,
)
from aws_resource_validator.guardrails import (
    AWSToolGuardrail,
    ToolGuardrailError,
    ToolValidationResult,
    ToolViolation,
    guard_tool,
    validate_tool_arguments,
    validate_tool_call,
)
from aws_resource_validator.scanner import (
    ScanCandidate,
    ScanFinding,
    ScanReport,
    scan_file,
    scan_paths,
    scan_text,
)
from aws_resource_validator.testing import (
    assert_invalid,
    assert_valid,
)

__all__ = [
    "ARN",
    "APIObject",
    "APIRegistry",
    "ARNParseError",
    "AWSToolGuardrail",
    "AWSValidationError",
    "AWSValidationWarning",
    "BaseValidatorModel",
    "EventStream",
    "ScanCandidate",
    "ScanFinding",
    "ScanReport",
    "Service",
    "ToolGuardrailError",
    "ToolValidationResult",
    "ToolViolation",
    "ValidationResult",
    "assert_invalid",
    "assert_valid",
    "diagnose_validation",
    "guard_tool",
    "scan_file",
    "scan_paths",
    "scan_text",
    "unwrap_client",
    "unwrap_session",
    "validate_tool_arguments",
    "validate_tool_call",
    "wrap_client",
    "wrap_session",
]
