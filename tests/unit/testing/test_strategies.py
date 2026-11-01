"""Property-based tests for Hypothesis strategies in aws_resource_validator.testing."""

from __future__ import annotations

import re

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from aws_resource_validator.core.api_object import APIObject
from aws_resource_validator.core.arn import ARN
from aws_resource_validator.testing.helpers import validate_with_extras
from aws_resource_validator.testing.strategies import (
    arn_strings,
    arns,
    from_api_object,
    invalid_arns,
    invalid_resource_names,
    resource_names,
)


@settings(max_examples=30)
@given(name=resource_names("s3", "BucketName"))
def test_resource_names_s3_bucket(name: str) -> None:
    assert validate_with_extras("s3", "BucketName", name, strict=True).is_valid
    assert 3 <= len(name) <= 63
    assert not name.startswith("-") and not name.endswith("-")
    assert ".." not in name
    assert not re.match(r"^\d+\.\d+\.\d+\.\d+$", name)


@settings(max_examples=30)
@given(name=resource_names("sqs", "QueueName"))
def test_resource_names_sqs_queue(name: str) -> None:
    assert validate_with_extras("sqs", "QueueName", name, strict=True).is_valid
    assert 1 <= len(name) <= 80


@settings(max_examples=30)
@given(name=resource_names("rds", "DBInstanceIdentifier"))
def test_resource_names_rds_identifier(name: str) -> None:
    assert validate_with_extras("rds", "DBInstanceIdentifier", name, strict=True).is_valid
    assert 1 <= len(name) <= 63
    assert not name.endswith("-")
    assert "--" not in name


@settings(max_examples=30)
@given(name=resource_names("dynamodb", "TableName"))
def test_resource_names_dynamodb_table(name: str) -> None:
    assert validate_with_extras("dynamodb", "TableName", name, strict=True).is_valid
    assert 3 <= len(name) <= 255


@settings(max_examples=30)
@given(name=resource_names("lambda", "FunctionName"))
def test_resource_names_lambda_function(name: str) -> None:
    assert validate_with_extras("lambda", "FunctionName", name, strict=True).is_valid


@settings(max_examples=30)
@given(name=resource_names("iam", "role_name_type"))
def test_resource_names_iam_role(name: str) -> None:
    assert validate_with_extras("iam", "role_name_type", name, strict=True).is_valid


@settings(max_examples=25)
@given(name=resource_names("lambda", "FunctionName", min_size=20, max_size=40))
def test_resource_names_custom_size_bounds(name: str) -> None:
    assert 20 <= len(name) <= 40
    assert validate_with_extras("lambda", "FunctionName", name, strict=True).is_valid


def test_resource_names_conflicting_bounds_raises() -> None:
    with pytest.raises(ValueError, match="Conflicting length constraints"):
        resource_names("s3", "BucketName", min_size=50, max_size=10)


def test_resource_names_unknown_service_raises_key_error() -> None:
    with pytest.raises(KeyError, match="Service 'nonexistent_service' not found"):
        resource_names("nonexistent_service", "BucketName")


def test_resource_names_unknown_shape_raises_key_error() -> None:
    with pytest.raises(KeyError, match=r"(?i)Shape 'NonexistentShape' in service 's3' not found"):
        resource_names("s3", "NonexistentShape")


@settings(max_examples=25)
@given(
    val=from_api_object(
        APIObject(
            name="CustomIdentifier",
            type="string",
            pattern=r"^[a-z]{3}-[0-9]{3}$",
            min_length=7,
            max_length=7,
        )
    )
)
def test_from_api_object(val: str) -> None:
    assert len(val) == 7
    assert re.fullmatch(r"^[a-z]{3}-[0-9]{3}$", val) is not None


@settings(max_examples=30)
@given(name=invalid_resource_names("s3", "BucketName"))
def test_invalid_resource_names_s3(name: str) -> None:
    res = validate_with_extras("s3", "BucketName", name, strict=True)
    assert not res.is_valid


@settings(max_examples=30)
@given(name=invalid_resource_names("rds", "DBInstanceIdentifier"))
def test_invalid_resource_names_rds(name: str) -> None:
    res = validate_with_extras("rds", "DBInstanceIdentifier", name, strict=True)
    assert not res.is_valid


@settings(max_examples=30)
@given(arn=arns())
def test_arns_default(arn: ARN) -> None:
    assert isinstance(arn, ARN)
    assert arn.is_valid
    assert not arn.errors
    assert arn.partition in {
        "aws",
        "aws-cn",
        "aws-us-gov",
        "aws-iso",
        "aws-iso-b",
        "aws-iso-e",
        "aws-iso-f",
        "aws-eusc",
    }


@settings(max_examples=25)
@given(
    arn=arns(
        partition="aws",
        service="sqs",
        region="us-east-1",
        account_id="123456789012",
        resource="my-custom-queue",
    )
)
def test_arns_pinned_components(arn: ARN) -> None:
    assert arn.partition == "aws"
    assert arn.service == "sqs"
    assert arn.region == "us-east-1"
    assert arn.account_id == "123456789012"
    assert arn.resource == "my-custom-queue"
    assert arn.is_valid


@settings(max_examples=25)
@given(
    arn=arns(
        service="lambda",
        resource_type="function",
        resource_id=st.sampled_from(["handler", "processor", "worker"]),
        delimiter=":",
    )
)
def test_arns_with_type_and_id(arn: ARN) -> None:
    assert arn.service == "lambda"
    assert arn.resource_type == "function"
    assert arn.resource_delimiter == ":"
    assert arn.resource_id in {"handler", "processor", "worker"}
    assert arn.is_valid


@settings(max_examples=25)
@given(arn_str=arn_strings(service="iam", resource_type="role", resource_id="MyRole"))
def test_arn_strings(arn_str: str) -> None:
    assert isinstance(arn_str, str)
    assert arn_str.startswith("arn:")
    parsed = ARN.parse(arn_str, strict=True)
    assert parsed.is_valid
    assert parsed.service == "iam"
    assert parsed.resource_type == "role"


@settings(max_examples=30)
@given(bad_arn=invalid_arns())
def test_invalid_arns(bad_arn: str) -> None:
    assert not ARN.is_arn(bad_arn)


def test_to_strategy_type_and_value_errors() -> None:
    from aws_resource_validator.testing.strategies import _to_strategy

    with pytest.raises(ValueError, match="Empty sequence provided"):
        _to_strategy([], st.just("default"))

    with pytest.raises(TypeError, match="Expected str, sequence of str"):
        _to_strategy(12345, st.just("default"))
