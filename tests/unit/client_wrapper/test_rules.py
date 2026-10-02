"""Unit tests for built-in and custom shape rules."""

from __future__ import annotations

from aws_resource_validator.client_wrapper.rules import (
    get_extra_validator,
    get_shape_rule,
    validate_s3_bucket_extra,
)
from aws_resource_validator.core.api_object import APIObject


def test_builtin_s3_bucket_rules() -> None:
    rule = get_shape_rule("s3", "BucketName")
    assert rule is not None
    assert rule.name == "BucketName"
    assert rule.min_length == 3
    assert rule.max_length == 63
    assert rule.validate("my-valid-bucket-123") is True
    assert rule.validate("INVALID_UPPERCASE") is False

    # Also looked up via parameter name 'bucket'
    rule_by_param = get_shape_rule("s3", "SomethingElse", param_name="Bucket")
    assert rule_by_param is not None
    assert rule_by_param.name == "BucketName"


def test_builtin_sqs_queue_rules() -> None:
    rule = get_shape_rule("sqs", "QueueName")
    assert rule is not None
    assert rule.validate("my-queue_123") is True
    assert rule.validate("my-queue.fifo") is True
    assert rule.validate("invalid@queue") is False


def test_custom_rule_override() -> None:
    custom = {
        ("s3", "bucketname"): APIObject(
            name="BucketName",
            type="string",
            pattern=r"^custom-[a-z0-9]+$",
            min_length=10,
            max_length=50,
        )
    }
    rule = get_shape_rule("s3", "BucketName", custom_rules=custom)
    assert rule is not None
    assert rule.pattern == r"^custom-[a-z0-9]+$"
    assert rule.min_length == 10


def test_custom_rule_from_dict() -> None:
    custom = {
        ("s3", "bucketname"): {
            "pattern": r"^prefix-[a-z]+$",
            "min_length": 5,
            "max_length": 30,
        }
    }
    rule = get_shape_rule("s3", "BucketName", custom_rules=custom)
    assert rule is not None
    assert rule.pattern == r"^prefix-[a-z]+$"
    assert rule.min_length == 5


def test_s3_bucket_extra_validation() -> None:
    assert validate_s3_bucket_extra("valid-bucket") == []
    assert validate_s3_bucket_extra("bucket..with..dots") == [
        "S3 bucket name cannot contain consecutive periods ('..')."
    ]
    assert validate_s3_bucket_extra("192.168.1.1") == ["S3 bucket name cannot be formatted as an IP address."]

    extra_val = get_extra_validator("s3", "BucketName")
    assert extra_val is not None
    assert extra_val("10.0.0.1") != []
