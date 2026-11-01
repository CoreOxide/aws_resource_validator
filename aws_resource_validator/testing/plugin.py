"""Pytest plugin providing fixtures for AWS resource validation and test data generation.

Auto-registered via the ``pytest11`` entry point under ``aws_resource_validator``.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any, Literal

import pytest

from aws_resource_validator.core.arn import ARN
from aws_resource_validator.testing.helpers import (
    AWSValidatorHelper,
    generate_valid,
)


@pytest.fixture
def aws_name_factory() -> Callable[..., str]:
    """Callable fixture that generates valid AWS resource names on demand.

    Usage:
        def test_bucket_creation(aws_name_factory):
            bucket_name = aws_name_factory("s3", "BucketName")
            fn_name = aws_name_factory("lambda", "FunctionName")
    """

    def _factory(service: str, shape: str, *, strict: bool = True) -> str:
        return generate_valid(service, shape, strict=strict)

    return _factory


@pytest.fixture
def aws_arn_factory() -> Callable[..., ARN]:
    """Callable fixture that builds valid :class:`ARN` objects with sensible defaults.

    Automatically supplies standard partition (``"aws"``), 12-digit account ID,
    and regional/global configuration appropriate for the target service.

    Usage:
        def test_iam_policy(aws_arn_factory):
            role_arn = aws_arn_factory("iam", resource_type="role", resource_id="MyRole")
            queue_arn = aws_arn_factory("sqs", resource="my-queue")
    """

    def _factory(
        service: str = "lambda",
        *,
        resource: str | None = None,
        resource_type: str | None = None,
        resource_id: str | None = None,
        region: str | None = None,
        account_id: str | None = None,
        partition: str = "aws",
        delimiter: Literal["/", ":"] = "/",
        strict: bool = True,
    ) -> ARN:
        svc_lower = service.lower()

        # Sensible defaults based on service topology
        if region is None:
            region = "" if svc_lower in {"iam", "s3", "cloudfront", "route53"} else "us-east-1"

        if account_id is None:
            account_id = "" if svc_lower == "s3" else "123456789012"

        if resource is None and resource_type is None and resource_id is None:
            if svc_lower == "iam":
                resource_type = "role"
                resource_id = "DefaultTestRole"
            elif svc_lower == "lambda":
                resource_type = "function"
                resource_id = "default-test-fn"
            elif svc_lower == "s3":
                resource = "default-test-bucket"
            else:
                resource = f"default-test-{svc_lower}"

        return ARN.build(
            service=service,
            resource=resource,
            resource_type=resource_type,
            resource_id=resource_id,
            region=region,
            account_id=account_id,
            partition=partition,
            delimiter=delimiter,
            strict=strict,
        )

    return _factory


@pytest.fixture
def aws_validator() -> AWSValidatorHelper:
    """Fixture providing helper assertions and detailed validation utilities.

    Usage:
        def test_my_service(aws_validator):
            aws_validator.assert_valid("s3", "BucketName", "valid-bucket-name")
            aws_validator.assert_invalid("s3", "BucketName", "INVALID_BUCKET")
    """
    return AWSValidatorHelper()


@pytest.fixture
def validated_boto3_session() -> Any:
    """Fixture returning a ``boto3.Session`` wrapped with :func:`~.wrap_session`.

    Any Boto3 client created from this session inherits local pre-flight
    parameter validation automatically.
    """
    try:
        import boto3  # noqa: PLC0415
    except ImportError:  # pragma: no cover
        pytest.skip("boto3 is not installed")

    from aws_resource_validator.client_wrapper import wrap_session  # noqa: PLC0415

    session = boto3.Session(region_name="us-east-1")
    return wrap_session(session)
