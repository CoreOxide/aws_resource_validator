"""Unit tests for validate_tool_call and @guard_tool adapters."""

from __future__ import annotations

import asyncio
from types import SimpleNamespace

import pytest

from aws_resource_validator.guardrails import (
    AWSToolGuardrail,
    ToolGuardrailError,
    guard_tool,
    validate_tool_call,
)


def test_validate_tool_call_openai_dict_and_object() -> None:
    openai_dict = {
        "id": "call_123",
        "type": "function",
        "function": {
            "name": "s3.PutObject",
            "arguments": '{"Bucket": "INVALID_BUCKET", "Key": "data.csv"}',
        },
    }
    res_dict = validate_tool_call(openai_dict)
    assert res_dict.is_valid is False
    assert res_dict.violations[0].parameter == "Bucket"

    openai_obj = SimpleNamespace(
        function=SimpleNamespace(
            name="s3.PutObject",
            arguments='{"Bucket": "valid-bucket-name", "Key": "data.csv"}',
        )
    )
    res_obj = validate_tool_call(openai_obj)
    assert res_obj.is_valid is True


def test_validate_tool_call_anthropic_and_gemini() -> None:
    anthropic_payload = {
        "type": "tool_use",
        "id": "toolu_01",
        "name": "s3_put_object",
        "input": {"Bucket": "INVALID_BUCKET", "Key": "data.csv"},
    }
    res_anthropic = validate_tool_call(anthropic_payload)
    assert res_anthropic.is_valid is False
    assert res_anthropic.service == "s3"
    assert res_anthropic.operation == "PutObject"

    gemini_payload = SimpleNamespace(
        name="upload_file",
        args={"Bucket": "valid-bucket-name", "Key": "data.csv"},
    )
    res_gemini = validate_tool_call(
        gemini_payload,
        tool_name_map={"upload_file": ("s3", "PutObject")},
    )
    assert res_gemini.is_valid is True


def test_validate_tool_call_unresolvable_name() -> None:
    res = validate_tool_call({"name": "mystery_tool", "arguments": {}})
    assert res.is_valid is False
    assert res.violations[0].code == "unknown_operation"


def test_guard_tool_sync_return_feedback_and_pass_through() -> None:
    executed: list[tuple[str, str]] = []

    @guard_tool("s3", "PutObject")
    def put_object(bucket: str, key: str) -> str:
        executed.append((bucket, key))
        return f"ok:{bucket}/{key}"

    feedback = put_object("INVALID_NAME", "data.csv")
    assert isinstance(feedback, str)
    assert "Tool call validation failed" in feedback
    assert executed == []

    ok = put_object("valid-bucket-name", "data.csv")
    assert ok == "ok:valid-bucket-name/data.csv"
    assert executed == [("valid-bucket-name", "data.csv")]


def test_guard_tool_raise_and_custom_handler_and_arg_mapping() -> None:
    @guard_tool("s3", "PutObject", on_error="raise", arg_mapping={"b": "Bucket", "k": "Key"})
    def upload(b: str, k: str) -> str:
        return f"{b}/{k}"

    with pytest.raises(ToolGuardrailError) as exc_info:
        upload("INVALID_NAME", "data.csv")
    assert exc_info.value.result.is_valid is False
    assert len(exc_info.value.violations) == 1
    assert "INVALID_NAME" in exc_info.value.feedback

    @guard_tool("s3", "PutObject", on_error=lambda res: {"error_count": res.error_count})
    def upload_custom(bucket: str, key: str) -> dict[str, int]:
        return {"error_count": 0}

    assert upload_custom("INVALID", "a.txt") == {"error_count": 1}

    with pytest.raises(ValueError, match="Invalid on_error handler"):
        guard_tool("s3", "PutObject", on_error="invalid_mode")  # type: ignore[arg-type]


def test_guard_tool_async_function() -> None:
    @guard_tool("s3", "PutObject")
    async def async_put(bucket: str, key: str) -> str:
        return f"async:{bucket}/{key}"

    bad = asyncio.run(async_put("INVALID_NAME", "data.csv"))
    assert isinstance(bad, str)
    assert "Tool call validation failed" in bad

    good = asyncio.run(async_put("valid-bucket-name", "data.csv"))
    assert good == "async:valid-bucket-name/data.csv"


def test_guardrail_instance_convenience_methods() -> None:
    guardrail = AWSToolGuardrail(tool_name_map={"s3_put": ("s3", "PutObject")})
    res = guardrail.validate_tool_call({"name": "s3_put", "arguments": {"Bucket": "valid-bucket", "Key": "x"}})
    assert res.is_valid is True

    @guardrail.guard("s3", "PutObject")
    def fn(bucket: str, key: str) -> str:
        return f"{bucket}/{key}"

    assert "Tool call validation failed" in fn("BAD_BUCKET", "x")
