"""Unit tests for guardrails service, operation, and tool-name resolution."""

from __future__ import annotations

from aws_resource_validator.guardrails.resolver import (
    parse_tool_name,
    resolve_botocore_operation,
    resolve_botocore_service,
)


def test_resolve_botocore_service_variants() -> None:
    for query, expected in [
        ("s3", "s3"),
        ("S3", "s3"),
        ("lambda_", "lambda"),
        ("DynamoDB", "dynamodb"),
        ("cognito_idp", "cognito-idp"),
    ]:
        model, canonical, suggestions = resolve_botocore_service(query)
        assert model is not None
        assert canonical == expected
        assert suggestions == []


def test_resolve_botocore_service_unknown_suggests_close_matches() -> None:
    model, canonical, suggestions = resolve_botocore_service("s3contro")
    assert model is None
    assert canonical == "s3contro"
    assert "s3control" in suggestions

    model_empty, _, suggestions_empty = resolve_botocore_service("   ")
    assert model_empty is None
    assert suggestions_empty == []


def test_resolve_botocore_operation_variants() -> None:
    s3_model, _, _ = resolve_botocore_service("s3")
    assert s3_model is not None

    op_exact, name_exact, _ = resolve_botocore_operation(s3_model, "PutObject")
    assert op_exact is not None
    assert name_exact == "PutObject"

    op_snake, name_snake, _ = resolve_botocore_operation(s3_model, "put_object")
    assert op_snake is not None
    assert name_snake == "PutObject"

    op_missing, _, suggestions = resolve_botocore_operation(s3_model, "PutObjec")
    assert op_missing is None
    assert "PutObject" in suggestions


def test_parse_tool_name_formats() -> None:
    assert parse_tool_name("s3.PutObject") == ("s3", "PutObject")
    assert parse_tool_name("iam:CreateRole") == ("iam", "CreateRole")
    assert parse_tool_name("lambda/CreateFunction") == ("lambda", "CreateFunction")
    assert parse_tool_name("dynamodb__create_table") == ("dynamodb", "create_table")
    assert parse_tool_name("s3_put_object") == ("s3", "put_object")
    assert parse_tool_name("cognito_idp_admin_get_user") == ("cognito-idp", "admin_get_user")

    custom_map = {"upload_file_to_s3": ("s3", "PutObject")}
    assert parse_tool_name("upload_file_to_s3", custom_map) == ("s3", "PutObject")

    assert parse_tool_name("unrecognized_tool_name") is None
    assert parse_tool_name("   ") is None
