"""Tests for testing helpers, assertions, and pytest fixtures."""

from __future__ import annotations

from typing import Any

import pytest

from aws_resource_validator.client_wrapper import AWSValidationError
from aws_resource_validator.core.arn import ARN
from aws_resource_validator.testing.helpers import (
    AWSValidatorHelper,
    assert_invalid,
    assert_valid,
    generate_valid,
    resolve_service_and_shape,
)


def test_resolve_service_and_shape_success() -> None:
    svc, obj = resolve_service_and_shape("s3", "BucketName")
    assert svc.service_name.lower() == "s3"
    assert obj.name == "BucketName"


def test_resolve_service_and_shape_missing_service() -> None:
    with pytest.raises(KeyError, match="Service 'nonexistent_foo' not found"):
        resolve_service_and_shape("nonexistent_foo", "bar")


def test_resolve_service_and_shape_missing_shape() -> None:
    with pytest.raises(KeyError, match=r"(?i)Shape 'NonexistentBar' in service 's3' not found"):
        resolve_service_and_shape("s3", "NonexistentBar")


def test_assert_valid_success() -> None:
    res = assert_valid("s3", "BucketName", "my-valid-bucket-1")
    assert res.is_valid
    assert not res.errors


def test_assert_valid_failure_raises_assertion_error() -> None:
    with pytest.raises(AssertionError) as exc_info:
        assert_valid("s3", "BucketName", "INVALID_UPPERCASE")
    err_text = str(exc_info.value)
    assert "AWS resource validation failed" in err_text
    assert "INVALID_UPPERCASE" in err_text
    assert "Suggested fix" in err_text


def test_assert_invalid_success() -> None:
    res = assert_invalid("s3", "BucketName", "INVALID_NAME")
    assert not res.is_valid


def test_assert_invalid_failure_raises_assertion_error() -> None:
    with pytest.raises(AssertionError, match="Expected validation failure"):
        assert_invalid("s3", "BucketName", "valid-name-1")


def test_generate_valid() -> None:
    s3_name = generate_valid("s3", "BucketName")
    assert assert_valid("s3", "BucketName", s3_name).is_valid

    rds_name = generate_valid("rds", "DBInstanceIdentifier")
    assert assert_valid("rds", "DBInstanceIdentifier", rds_name).is_valid

    lambda_name = generate_valid("lambda", "FunctionName")
    assert assert_valid("lambda", "FunctionName", lambda_name).is_valid


def test_aws_validator_helper() -> None:
    helper = AWSValidatorHelper()
    assert repr(helper) == "<AWSValidatorHelper>"
    assert helper.validate("s3", "BucketName", "valid-test-bucket") is True
    assert helper.validate("s3", "BucketName", "BAD_NAME") is False

    detailed = helper.validate_detailed("s3", "BucketName", "valid-test-bucket")
    assert detailed.is_valid

    val = helper.generate("lambda", "FunctionName")
    assert helper.assert_valid("lambda", "FunctionName", val).is_valid
    assert helper.assert_invalid("s3", "BucketName", "UPPERCASE").is_valid is False


def test_pytest_fixture_aws_name_factory(aws_name_factory: Any) -> None:
    bucket = aws_name_factory("s3", "BucketName")
    assert isinstance(bucket, str)
    assert assert_valid("s3", "BucketName", bucket).is_valid

    queue = aws_name_factory("sqs", "QueueName")
    assert isinstance(queue, str)
    assert assert_valid("sqs", "QueueName", queue).is_valid


def test_pytest_fixture_aws_arn_factory(aws_arn_factory: Any) -> None:
    # Lambda ARN default
    fn_arn = aws_arn_factory("lambda")
    assert isinstance(fn_arn, ARN)
    assert fn_arn.service == "lambda"
    assert fn_arn.region == "us-east-1"
    assert fn_arn.account_id == "123456789012"
    assert fn_arn.is_valid

    # S3 bucket ARN (global, no region, no account)
    s3_arn = aws_arn_factory("s3", resource="my-awesome-bucket")
    assert s3_arn.service == "s3"
    assert s3_arn.region == ""
    assert s3_arn.account_id == ""
    assert s3_arn.resource == "my-awesome-bucket"
    assert s3_arn.is_valid

    # IAM role ARN
    iam_arn = aws_arn_factory("iam", resource_type="role", resource_id="CustomRole")
    assert iam_arn.service == "iam"
    assert iam_arn.resource_type == "role"
    assert iam_arn.resource_id == "CustomRole"
    assert iam_arn.is_valid


def test_pytest_fixture_aws_validator(aws_validator: AWSValidatorHelper) -> None:
    assert aws_validator.validate("s3", "BucketName", "valid-bucket-name") is True
    aws_validator.assert_valid("lambda", "FunctionName", "my-function")
    aws_validator.assert_invalid("rds", "DBInstanceIdentifier", "trailing-hyphen-")


def test_pytest_fixture_validated_boto3_session(validated_boto3_session: Any) -> None:
    s3 = validated_boto3_session.client("s3")
    # Calling with invalid Bucket parameter should fail pre-flight locally in memory
    with pytest.raises(AWSValidationError) as exc:
        s3.create_bucket(Bucket="INVALID_UPPERCASE")
    assert "INVALID_UPPERCASE" in str(exc.value)
