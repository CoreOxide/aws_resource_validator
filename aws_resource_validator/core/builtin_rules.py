"""Built-in shape constraints for AWS services where botocore models omit regex patterns.

Certain AWS services (e.g. S3 bucket naming, SQS queue names) implement validation
via custom botocore Python handlers rather than declaring patterns in service-2.json.
This module provides standard botocore-compliant rules for those shapes.
"""

from __future__ import annotations

import re
from collections.abc import Callable, Mapping
from typing import Any

from aws_resource_validator.core.api_object import APIObject

# Standard AWS naming constraints for shapes lacking regex patterns in service-2.json
BUILTIN_SHAPE_RULES: dict[tuple[str, str], APIObject] = {
    # S3 bucket naming rules: 3-63 chars, lowercase, numbers, hyphens, periods, no IP format
    ("s3", "bucketname"): APIObject(
        name="BucketName",
        type="string",
        pattern=r"^[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]$",
        min_length=3,
        max_length=63,
    ),
    ("s3", "bucket"): APIObject(
        name="BucketName",
        type="string",
        pattern=r"^[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]$",
        min_length=3,
        max_length=63,
    ),
    ("s3", "bucketprefix"): APIObject(
        name="BucketPrefix",
        type="string",
        pattern=r"^[a-z0-9][a-z0-9.-]{1,35}[a-z0-9.-]$",
        min_length=3,
        max_length=37,
    ),
    # SQS queue naming rules: 1-80 chars, alphanumeric, hyphens, underscores, optional .fifo suffix
    ("sqs", "queuename"): APIObject(
        name="QueueName",
        type="string",
        pattern=r"^[a-zA-Z0-9_-]+(\.fifo)?$",
        min_length=1,
        max_length=80,
    ),
    ("sqs", "queue"): APIObject(
        name="QueueName",
        type="string",
        pattern=r"^[a-zA-Z0-9_-]+(\.fifo)?$",
        min_length=1,
        max_length=80,
    ),
    # DynamoDB table naming rules: 3-255 chars, alphanumeric, underscores, hyphens, periods
    ("dynamodb", "tablename"): APIObject(
        name="TableName",
        type="string",
        pattern=r"^[a-zA-Z0-9_.-]+$",
        min_length=3,
        max_length=255,
    ),
    ("dynamodb", "table"): APIObject(
        name="TableName",
        type="string",
        pattern=r"^[a-zA-Z0-9_.-]+$",
        min_length=3,
        max_length=255,
    ),
    # SNS topic naming rules: 1-256 chars, alphanumeric, hyphens, underscores, optional .fifo suffix
    ("sns", "topicname"): APIObject(
        name="TopicName",
        type="string",
        pattern=r"^[a-zA-Z0-9_-]{1,256}(\.fifo)?$",
        min_length=1,
        max_length=256,
    ),
    ("sns", "topic"): APIObject(
        name="TopicName",
        type="string",
        pattern=r"^[a-zA-Z0-9_-]{1,256}(\.fifo)?$",
        min_length=1,
        max_length=256,
    ),
    # RDS database identifier naming rules: 1-63 chars, letters, digits, hyphens
    ("rds", "dbinstanceidentifier"): APIObject(
        name="DBInstanceIdentifier",
        type="string",
        pattern=r"^[a-zA-Z][a-zA-Z0-9-]*$",
        min_length=1,
        max_length=63,
    ),
    ("rds", "identifier"): APIObject(
        name="DBInstanceIdentifier",
        type="string",
        pattern=r"^[a-zA-Z][a-zA-Z0-9-]*$",
        min_length=1,
        max_length=63,
    ),
    ("rds", "dbclusteridentifier"): APIObject(
        name="DBClusterIdentifier",
        type="string",
        pattern=r"^[a-zA-Z][a-zA-Z0-9-]*$",
        min_length=1,
        max_length=63,
    ),
    ("rds", "cluster_identifier"): APIObject(
        name="DBClusterIdentifier",
        type="string",
        pattern=r"^[a-zA-Z][a-zA-Z0-9-]*$",
        min_length=1,
        max_length=63,
    ),
    # Secrets Manager secret name naming rules
    ("secretsmanager", "secretname"): APIObject(
        name="SecretName",
        type="string",
        pattern=r"^[a-zA-Z0-9/_+=.@-]+$",
        min_length=1,
        max_length=512,
    ),
    ("secretsmanager", "name"): APIObject(
        name="SecretName",
        type="string",
        pattern=r"^[a-zA-Z0-9/_+=.@-]+$",
        min_length=1,
        max_length=512,
    ),
    # SSM Parameter Store parameter name naming rules
    ("ssm", "psparametername"): APIObject(
        name="PSParameterName",
        type="string",
        pattern=r"^[a-zA-Z0-9_./-]+$",
        min_length=1,
        max_length=1011,
    ),
    ("ssm", "parametername"): APIObject(
        name="PSParameterName",
        type="string",
        pattern=r"^[a-zA-Z0-9_./-]+$",
        min_length=1,
        max_length=1011,
    ),
}

_IP_ADDRESS_RE = re.compile(r"^\d+\.\d+\.\d+\.\d+$")


def validate_s3_bucket_extra(value: str) -> list[str]:
    """Perform extra AWS S3 bucket naming checks not expressible in a single regex."""
    errors: list[str] = []
    if ".." in value:
        errors.append("S3 bucket name cannot contain consecutive periods ('..').")
    if _IP_ADDRESS_RE.match(value):
        errors.append("S3 bucket name cannot be formatted as an IP address.")
    return errors


def validate_rds_identifier_extra(value: str) -> list[str]:
    """Perform extra AWS RDS DB identifier checks."""
    errors: list[str] = []
    if value.endswith("-"):
        errors.append("RDS identifier cannot end with a hyphen ('-').")
    if "--" in value:
        errors.append("RDS identifier cannot contain two consecutive hyphens ('--').")
    return errors


_EXTRA_VALIDATORS: dict[tuple[str, str], Callable[[str], list[str]]] = {
    ("s3", "bucketname"): validate_s3_bucket_extra,
    ("s3", "bucket"): validate_s3_bucket_extra,
    ("rds", "dbinstanceidentifier"): validate_rds_identifier_extra,
    ("rds", "identifier"): validate_rds_identifier_extra,
    ("rds", "dbclusteridentifier"): validate_rds_identifier_extra,
    ("rds", "cluster_identifier"): validate_rds_identifier_extra,
}


def get_shape_rule(
    service_name: str,
    shape_name: str,
    param_name: str | None = None,
    custom_rules: Mapping[Any, Any] | None = None,
) -> APIObject | None:
    """Look up shape constraint from custom rules or built-in service rules.

    Checks:
      1. User-supplied custom rules by (service, shape) or (service, param).
      2. Built-in rules by (service, shape) or (service, param).
    """
    svc = service_name.lower()
    shape_lower = shape_name.lower()
    param_lower = param_name.lower() if param_name else ""

    if custom_rules:
        # Check custom rules
        for key in ((svc, shape_lower), (svc, param_lower), shape_lower, param_lower):
            if key in custom_rules:
                val = custom_rules[key]
                if isinstance(val, APIObject):
                    return val
                if isinstance(val, dict):
                    return APIObject(
                        name=val.get("name", shape_name),
                        type=val.get("type", "string"),
                        pattern=val["pattern"],
                        min_length=val.get("min_length"),
                        max_length=val.get("max_length"),
                    )

    # Check built-in rules
    for key in ((svc, shape_lower), (svc, param_lower)):
        if key in BUILTIN_SHAPE_RULES:
            return BUILTIN_SHAPE_RULES[key]

    return None


def get_extra_validator(
    service_name: str,
    shape_name: str,
    param_name: str | None = None,
) -> Callable[[str], list[str]] | None:
    """Return optional extra validator function for domain-specific checks."""
    svc = service_name.lower()
    shape_lower = shape_name.lower()
    param_lower = param_name.lower() if param_name else ""

    for key in ((svc, shape_lower), (svc, param_lower)):
        if key in _EXTRA_VALIDATORS:
            return _EXTRA_VALIDATORS[key]
    return None
