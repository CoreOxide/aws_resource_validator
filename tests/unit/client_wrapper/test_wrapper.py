"""Unit tests for wrap_client, unwrap_client, wrap_session, and unwrap_session."""

from __future__ import annotations

import contextlib
import logging

import boto3
import botocore.exceptions
import botocore.session
import pytest

from aws_resource_validator import (
    AWSValidationError,
    AWSValidationWarning,
    unwrap_client,
    unwrap_session,
    wrap_client,
    wrap_session,
)


def test_wrap_client_raises_aws_validation_error() -> None:
    session = botocore.session.get_session()
    raw_s3 = session.create_client("s3", region_name="us-east-1")
    s3 = wrap_client(raw_s3)

    assert s3 is raw_s3  # Preserves identity and type

    with pytest.raises(AWSValidationError) as exc_info:
        s3.create_bucket(Bucket="INVALID_UPPERCASE")

    err = exc_info.value
    assert isinstance(err, ValueError)
    assert isinstance(err, botocore.exceptions.ParamValidationError)
    assert err.service_name == "s3"
    assert err.operation_name == "CreateBucket"
    assert err.param_name == "Bucket"
    assert err.shape_name == "BucketName"
    assert err.value == "INVALID_UPPERCASE"
    assert len(err.diagnostics) >= 1
    assert "Value does not match required regex pattern" in str(err)


def test_wrap_client_boto3_integration() -> None:
    s3 = wrap_client(boto3.client("s3", region_name="us-east-1"))

    with pytest.raises(AWSValidationError) as exc_info:
        s3.create_bucket(Bucket="my..bad..bucket")

    assert "consecutive periods" in exc_info.value.message


def test_wrap_client_mode_warn() -> None:
    session = botocore.session.get_session()
    client = session.create_client("s3", region_name="us-east-1")
    wrapped = wrap_client(client, mode="warn")

    with (
        pytest.warns(AWSValidationWarning, match="BucketName"),
        contextlib.suppress(botocore.exceptions.ClientError),
    ):
        wrapped.create_bucket(Bucket="INVALID_UPPERCASE")


def test_wrap_client_mode_log(caplog: pytest.LogCaptureFixture) -> None:
    session = botocore.session.get_session()
    client = session.create_client("s3", region_name="us-east-1")
    wrapped = wrap_client(client, mode="log")

    with caplog.at_level(logging.WARNING), contextlib.suppress(botocore.exceptions.ClientError):
        wrapped.create_bucket(Bucket="INVALID_UPPERCASE")

    assert any("failed pre-flight validation" in r.message for r in caplog.records)


def test_wrap_client_invalid_mode() -> None:
    session = botocore.session.get_session()
    client = session.create_client("s3", region_name="us-east-1")
    wrapped = wrap_client(client, mode="unknown_mode")

    with pytest.raises(ValueError, match="Invalid validation mode"):
        wrapped.create_bucket(Bucket="INVALID_UPPERCASE")


def test_unwrap_client() -> None:
    session = botocore.session.get_session()
    client = session.create_client("s3", region_name="us-east-1")
    wrap_client(client)

    # With wrapper: raises AWSValidationError
    with pytest.raises(AWSValidationError):
        client.create_bucket(Bucket="INVALID_UPPERCASE")

    # After unwrapping: no longer raises AWSValidationError (reaches AWS / ClientError)
    unwrap_client(client)
    try:
        client.create_bucket(Bucket="INVALID_UPPERCASE")
    except Exception as e:
        assert not isinstance(e, AWSValidationError)


def test_wrap_client_idempotent() -> None:
    session = botocore.session.get_session()
    client = session.create_client("s3", region_name="us-east-1")

    # Wrapping twice should not register duplicate handlers
    wrap_client(client)
    wrap_client(client)

    with pytest.raises(AWSValidationError):
        client.create_bucket(Bucket="INVALID_UPPERCASE")


def test_wrap_session() -> None:
    session = botocore.session.get_session()
    wrap_session(session)

    s3 = session.create_client("s3", region_name="us-east-1")
    with pytest.raises(AWSValidationError) as s3_err:
        s3.create_bucket(Bucket="INVALID_UPPERCASE")
    assert s3_err.value.service_name == "s3"

    lam = session.create_client("lambda", region_name="us-east-1")
    with pytest.raises(AWSValidationError) as lam_err:
        lam.get_function(FunctionName="invalid function name!")
    assert lam_err.value.service_name == "lambda"

    unwrap_session(session)


def test_wrap_boto3_session() -> None:
    boto3_session = boto3.Session()
    wrap_session(boto3_session)

    s3 = boto3_session.client("s3", region_name="us-east-1")
    with pytest.raises(AWSValidationError):
        s3.create_bucket(Bucket="INVALID_UPPERCASE")

    unwrap_session(boto3_session)


def test_wrap_boto3_resource() -> None:
    resource = boto3.resource("s3", region_name="us-east-1")
    wrapped_resource = wrap_client(resource)
    assert wrapped_resource is resource

    with pytest.raises(AWSValidationError):
        wrapped_resource.meta.client.create_bucket(Bucket="INVALID_UPPERCASE")


def test_wrap_invalid_target_type() -> None:
    with pytest.raises(TypeError, match=r"Expected a boto3/botocore client"):
        wrap_client("not-a-client")  # type: ignore[arg-type]

    with pytest.raises(TypeError, match=r"Expected a boto3\.Session"):
        wrap_session("not-a-session")  # type: ignore[arg-type]
