"""Unit tests for AWSToolGuardrail and validate_tool_arguments."""

from __future__ import annotations

import json
from datetime import UTC, datetime

import pytest

from aws_resource_validator.core.api_object import APIObject
from aws_resource_validator.guardrails import (
    AWSToolGuardrail,
    ToolValidationResult,
    validate_tool_arguments,
)


def test_valid_s3_put_object_passes() -> None:
    result = validate_tool_arguments("s3", "PutObject", {"Bucket": "my-valid-bucket-123", "Key": "data/file.csv"})
    assert isinstance(result, ToolValidationResult)
    assert result.is_valid is True
    assert result.error_count == 0
    assert result.violations == ()
    assert result.service == "s3"
    assert result.operation == "PutObject"
    assert result.to_llm_feedback() == ""


def test_invalid_s3_bucket_returns_actionable_feedback() -> None:
    result = validate_tool_arguments("s3", "PutObject", {"Bucket": "INVALID_NAME", "Key": "data.csv"})
    assert result.is_valid is False
    assert result.error_count == 1
    violation = result.violations[0]
    assert violation.parameter == "Bucket"
    assert violation.code == "invalid_value"
    assert violation.shape_name == "BucketName"
    assert violation.suggested_fix is not None

    feedback = result.to_llm_feedback()
    assert "s3.PutObject" in feedback
    assert "Bucket" in feedback
    assert "INVALID_NAME" in feedback
    assert "Fix:" in feedback


def test_json_string_arguments_and_malformed_json() -> None:
    valid = validate_tool_arguments("s3", "PutObject", '{"Bucket": "valid-bucket-name", "Key": "a.txt"}')
    assert valid.is_valid is True

    malformed = validate_tool_arguments("s3", "PutObject", '{"Bucket": "valid-bucket",')
    assert malformed.is_valid is False
    assert malformed.violations[0].code == "invalid_json"

    non_object = validate_tool_arguments("s3", "PutObject", '["not", "an", "object"]')
    assert non_object.is_valid is False
    assert non_object.violations[0].code == "invalid_json"


def test_unknown_service_and_operation() -> None:
    bad_svc = validate_tool_arguments("s3contro", "ListJobs", {})
    assert bad_svc.is_valid is False
    assert bad_svc.violations[0].code == "unknown_service"
    assert "s3control" in (bad_svc.violations[0].suggested_fix or "")

    bad_op = validate_tool_arguments("s3", "PutObjec", {})
    assert bad_op.is_valid is False
    assert bad_op.violations[0].code == "unknown_operation"
    assert "PutObject" in (bad_op.violations[0].suggested_fix or "")


def test_missing_required_parameters_and_flag_override() -> None:
    missing = validate_tool_arguments("s3", "PutObject", {"Bucket": "valid-bucket-name"})
    assert missing.is_valid is False
    assert any(v.code == "missing_required" and v.parameter == "Key" for v in missing.violations)

    ignored = validate_tool_arguments(
        "s3",
        "PutObject",
        {"Bucket": "valid-bucket-name"},
        check_required=False,
    )
    assert ignored.is_valid is True


def test_unknown_parameter_suggests_typo_and_respects_flag() -> None:
    result = validate_tool_arguments(
        "s3",
        "PutObject",
        {"Bucket": "valid-bucket-name", "Key": "a.txt", "BucketName": "oops"},
    )
    assert result.is_valid is False
    unknown = [v for v in result.violations if v.code == "unknown_parameter"]
    assert len(unknown) == 1
    assert unknown[0].parameter == "BucketName"
    assert "Bucket" in (unknown[0].suggested_fix or "")

    relaxed = validate_tool_arguments(
        "s3",
        "PutObject",
        {"Bucket": "valid-bucket-name", "Key": "a.txt", "BucketName": "oops"},
        check_unknown=False,
    )
    assert relaxed.is_valid is True


def test_enum_and_numeric_bounds_validation() -> None:
    bad_enum = validate_tool_arguments(
        "s3",
        "PutObject",
        {"Bucket": "valid-bucket-name", "Key": "a.txt", "StorageClass": "GLACIER_COLD"},
    )
    assert bad_enum.is_valid is False
    assert bad_enum.violations[0].code == "invalid_enum"
    assert "GLACIER" in (bad_enum.violations[0].suggested_fix or "")

    bad_range = validate_tool_arguments(
        "dynamodb",
        "CreateTable",
        {
            "TableName": "my-valid-table",
            "AttributeDefinitions": [{"AttributeName": "id", "AttributeType": "S"}],
            "KeySchema": [{"AttributeName": "id", "KeyType": "HASH"}],
            "ProvisionedThroughput": {"ReadCapacityUnits": 0, "WriteCapacityUnits": 5},
        },
    )
    assert bad_range.is_valid is False
    assert any(
        v.code == "out_of_range" and v.parameter == "ProvisionedThroughput.ReadCapacityUnits"
        for v in bad_range.violations
    )


def test_type_mismatch_and_bool_not_accepted_as_int() -> None:
    res_bool_int = validate_tool_arguments(
        "s3",
        "ListObjectsV2",
        {"Bucket": "valid-bucket-name", "MaxKeys": True},
    )
    assert res_bool_int.is_valid is False
    assert res_bool_int.violations[0].code == "type_mismatch"

    res_wrong_type = validate_tool_arguments(
        "s3",
        "PutObject",
        {"Bucket": 12345, "Key": "a.txt", "Expires": datetime.now(tz=UTC)},
    )
    assert res_wrong_type.is_valid is False
    assert any(v.parameter == "Bucket" and v.code == "type_mismatch" for v in res_wrong_type.violations)


def test_nested_structure_and_list_validation() -> None:
    res = validate_tool_arguments(
        "s3",
        "DeleteObjects",
        {
            "Bucket": "valid-bucket-name",
            "Delete": {
                "Objects": [{}],
            },
        },
    )
    assert res.is_valid is False
    assert any(v.parameter == "Delete.Objects[0].Key" and v.code == "missing_required" for v in res.violations)


def test_multiple_violations_collected_in_single_pass() -> None:
    res = validate_tool_arguments(
        "s3",
        "PutObject",
        {
            "Bucket": "INVALID_BUCKET",
            "StorageClass": "INVALID_TIER",
            "UnknownKey": "x",
        },
    )
    assert res.is_valid is False
    codes = {v.code for v in res.violations}
    assert {"invalid_value", "missing_required", "invalid_enum", "unknown_parameter"}.issubset(codes)

    truncated = res.to_llm_feedback(max_violations=2, include_pattern=False)
    assert "more error(s)" in truncated


def test_iam_arn_and_dynamodb_and_lambda_and_sqs() -> None:
    bad_iam = validate_tool_arguments(
        "iam",
        "CreateRole",
        {"RoleName": "bad role!", "AssumeRolePolicyDocument": "{}"},
    )
    assert bad_iam.is_valid is False
    assert bad_iam.violations[0].parameter == "RoleName"

    bad_lambda = validate_tool_arguments(
        "lambda",
        "GetFunction",
        {"FunctionName": "bad function!"},
    )
    assert bad_lambda.is_valid is False

    bad_ddb = validate_tool_arguments(
        "dynamodb",
        "DescribeTable",
        {"TableName": "a"},
    )
    assert bad_ddb.is_valid is False

    bad_sqs = validate_tool_arguments(
        "sqs",
        "CreateQueue",
        {"QueueName": "bad queue!"},
    )
    assert bad_sqs.is_valid is False


def test_custom_rules_and_strict_mode() -> None:
    custom = {
        ("s3", "bucketname"): APIObject(
            name="BucketName",
            type="string",
            pattern=r"^corp-[a-z0-9-]+$",
            min_length=5,
            max_length=40,
        )
    }
    guardrail = AWSToolGuardrail(custom_rules=custom)
    assert guardrail.validate("s3", "PutObject", {"Bucket": "my-bucket", "Key": "a"}).is_valid is False
    assert guardrail.validate("s3", "PutObject", {"Bucket": "corp-bucket", "Key": "a"}).is_valid is True


def test_serialization_and_to_tool_message_formats() -> None:
    res = validate_tool_arguments("s3", "PutObject", {"Bucket": "INVALID", "Key": "a.txt"})
    as_dict = res.to_dict()
    assert as_dict["is_valid"] is False
    assert as_dict["error_count"] == 1
    assert json.loads(res.to_json())["service"] == "s3"

    openai_msg = res.to_tool_message("call_1", format="openai")
    assert openai_msg["role"] == "tool"
    assert openai_msg["tool_call_id"] == "call_1"
    assert "INVALID" in openai_msg["content"]

    anthropic_msg = res.to_tool_message("toolu_1", format="anthropic")
    assert anthropic_msg["type"] == "tool_result"
    assert anthropic_msg["is_error"] is True

    gemini_msg = res.to_tool_message(format="gemini")
    assert gemini_msg["function_response"]["name"] == "s3.PutObject"
    assert "error" in gemini_msg["function_response"]["response"]

    generic_msg = res.to_tool_message(format="generic")
    assert generic_msg["is_valid"] is False

    with pytest.raises(ValueError, match="Unsupported tool message format"):
        res.to_tool_message(format="unknown")  # type: ignore[arg-type]
