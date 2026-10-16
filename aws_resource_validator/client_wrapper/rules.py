"""Built-in shape constraints for AWS services where botocore models omit regex patterns.

Re-exports from :mod:`aws_resource_validator.core.builtin_rules` for backward compatibility.
"""

from __future__ import annotations

from aws_resource_validator.core.builtin_rules import (
    BUILTIN_SHAPE_RULES,
    get_extra_validator,
    get_shape_rule,
    validate_rds_identifier_extra,
    validate_s3_bucket_extra,
)

__all__ = [
    "BUILTIN_SHAPE_RULES",
    "get_extra_validator",
    "get_shape_rule",
    "validate_rds_identifier_extra",
    "validate_s3_bucket_extra",
]
