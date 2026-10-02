"""Pre-flight parameter validation for boto3 and botocore clients."""

from __future__ import annotations

from aws_resource_validator.client_wrapper.exceptions import (
    AWSValidationError,
    AWSValidationWarning,
)
from aws_resource_validator.client_wrapper.rules import BUILTIN_SHAPE_RULES
from aws_resource_validator.client_wrapper.validator import ShapeValidator
from aws_resource_validator.client_wrapper.wrapper import (
    unwrap_client,
    unwrap_session,
    wrap_client,
    wrap_session,
)

__all__ = [
    "BUILTIN_SHAPE_RULES",
    "AWSValidationError",
    "AWSValidationWarning",
    "ShapeValidator",
    "unwrap_client",
    "unwrap_session",
    "wrap_client",
    "wrap_session",
]
