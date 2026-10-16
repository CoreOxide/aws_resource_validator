"""Public API for the aws_resource_validator runtime.

Generated artifacts live under :mod:`aws_resource_validator.class_definitions`
(single-file Pipeline A output) and :mod:`aws_resource_validator.pydantic_models`
(Pipeline B output, one sub-package per AWS service). The generator itself
lives under :mod:`aws_resource_validator.generator` and is not part of the
runtime surface.
"""

__version__ = "2.6.0"

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
from aws_resource_validator.scanner import (
    ScanCandidate,
    ScanFinding,
    ScanReport,
    scan_file,
    scan_paths,
    scan_text,
)

__all__ = [
    "ARN",
    "APIObject",
    "APIRegistry",
    "ARNParseError",
    "AWSValidationError",
    "AWSValidationWarning",
    "BaseValidatorModel",
    "EventStream",
    "ScanCandidate",
    "ScanFinding",
    "ScanReport",
    "Service",
    "ValidationResult",
    "diagnose_validation",
    "scan_file",
    "scan_paths",
    "scan_text",
    "unwrap_client",
    "unwrap_session",
    "wrap_client",
    "wrap_session",
]
