"""Unit tests for ShapeValidator pre-flight inspection."""

from __future__ import annotations

import botocore.session
import pytest

from aws_resource_validator.client_wrapper.validator import ShapeValidator
from aws_resource_validator.core.api_object import APIObject


@pytest.fixture
def session() -> botocore.session.Session:
    return botocore.session.get_session()


def test_validator_s3_bucket(session: botocore.session.Session) -> None:
    client = session.create_client("s3", region_name="us-east-1")
    op = client.meta.service_model.operation_model("CreateBucket")
    validator = ShapeValidator()

    # Valid bucket name
    v_ok = validator.validate_operation_parameters("s3", op, {"Bucket": "my-cool-bucket-2026"})
    assert v_ok == []

    # Invalid uppercase bucket
    v_bad = validator.validate_operation_parameters("s3", op, {"Bucket": "INVALID_BUCKET"})
    assert len(v_bad) == 1
    path, shape, res = v_bad[0]
    assert path == "Bucket"
    assert shape == "BucketName"
    assert res.is_valid is False
    assert any("does not match required regex pattern" in e for e in res.errors)

    # Double dots in bucket
    v_dots = validator.validate_operation_parameters("s3", op, {"Bucket": "my..bucket"})
    assert len(v_dots) == 1
    assert any("consecutive periods" in e for e in v_dots[0][2].errors)


def test_validator_lambda_function_name(session: botocore.session.Session) -> None:
    client = session.create_client("lambda", region_name="us-east-1")
    op = client.meta.service_model.operation_model("GetFunction")
    validator = ShapeValidator()

    # Valid function name
    v_ok = validator.validate_operation_parameters("lambda", op, {"FunctionName": "valid-function_123"}, strict=True)
    assert v_ok == []

    # Invalid function name with illegal symbols
    v_bad = validator.validate_operation_parameters(
        "lambda", op, {"FunctionName": "bad function with spaces!"}, strict=True
    )
    assert len(v_bad) == 1
    path, _shape, res = v_bad[0]
    assert path == "FunctionName"
    assert res.is_valid is False


def test_validator_nested_structures_and_maps(session: botocore.session.Session) -> None:
    client = session.create_client("lambda", region_name="us-east-1")
    op = client.meta.service_model.operation_model("CreateFunction")
    validator = ShapeValidator()

    # CreateFunction has Environment.Variables (map of EnvironmentVariableName -> string)
    # Variable names must match [a-zA-Z]([a-zA-Z0-9_])+
    params = {
        "FunctionName": "my-func",
        "Role": "arn:aws:iam::123456789012:role/my-role",
        "Handler": "index.handler",
        "Code": {"ZipFile": b"bytes"},
        "Environment": {
            "Variables": {
                "123_INVALID_START": "foo",  # Starts with digits!
            }
        },
    }

    violations = validator.validate_operation_parameters("lambda", op, params, strict=True)
    assert len(violations) >= 1
    paths = [v[0] for v in violations]
    assert any("Environment.Variables.key(123_INVALID_START)" in p for p in paths)


def test_validator_custom_rules(session: botocore.session.Session) -> None:
    client = session.create_client("s3", region_name="us-east-1")
    op = client.meta.service_model.operation_model("CreateBucket")

    custom = {
        ("s3", "bucketname"): APIObject(
            name="BucketName",
            type="string",
            pattern=r"^prod-[a-z0-9]+$",
            min_length=6,
            max_length=30,
        )
    }
    validator = ShapeValidator(custom_rules=custom)

    # Violates custom prefix requirement
    v_dev = validator.validate_operation_parameters("s3", op, {"Bucket": "dev-bucket-1"})
    assert len(v_dev) == 1

    # Matches custom prefix requirement
    v_prod = validator.validate_operation_parameters("s3", op, {"Bucket": "prod-bucket1"})
    assert v_prod == []


def test_validator_empty_and_none_params(session: botocore.session.Session) -> None:
    client = session.create_client("s3", region_name="us-east-1")
    op = client.meta.service_model.operation_model("ListBuckets")
    validator = ShapeValidator()

    assert validator.validate_operation_parameters("s3", op, {}) == []
