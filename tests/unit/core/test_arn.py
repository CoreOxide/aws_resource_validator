"""Unit tests for the universal ARN parser, validator, and builder."""

from __future__ import annotations

import pytest
from pydantic import BaseModel, ValidationError

from aws_resource_validator import ARN, ARNParseError
from aws_resource_validator.core.arn import MAX_ARN_LENGTH
from aws_resource_validator.core.diagnostics import ValidationResult

# (arn, partition, service, region, account, resource_type, resource_id, delimiter)
DECOMPOSITION_CASES = [
    (
        "arn:aws:s3:::my-bucket/logs/2026:10:09.gz",
        "aws",
        "s3",
        "",
        "",
        None,
        "my-bucket/logs/2026:10:09.gz",
        None,
    ),
    (
        "arn:aws:s3:::my-bucket",
        "aws",
        "s3",
        "",
        "",
        None,
        "my-bucket",
        None,
    ),
    (
        "arn:aws:iam::123456789012:role/service-role/MyRole",
        "aws",
        "iam",
        "",
        "123456789012",
        "role",
        "service-role/MyRole",
        "/",
    ),
    (
        "arn:aws:cloudwatch:us-east-1:123456789012:alarm:CPU:High",
        "aws",
        "cloudwatch",
        "us-east-1",
        "123456789012",
        "alarm",
        "CPU:High",
        ":",
    ),
    (
        "arn:aws:lambda:us-east-1:123456789012:function:fn:prod",
        "aws",
        "lambda",
        "us-east-1",
        "123456789012",
        "function",
        "fn:prod",
        ":",
    ),
    (
        "arn:aws:sns:us-east-1:123456789012:my-topic",
        "aws",
        "sns",
        "us-east-1",
        "123456789012",
        None,
        "my-topic",
        None,
    ),
    (
        "arn:aws:sns:us-east-1:123456789012:my-topic:6b0e71bd-7e97-4d97-80ce-4a0994e55286",
        "aws",
        "sns",
        "us-east-1",
        "123456789012",
        None,
        "my-topic:6b0e71bd-7e97-4d97-80ce-4a0994e55286",
        None,
    ),
    (
        "arn:aws:sqs:us-east-1:123456789012:my-queue.fifo",
        "aws",
        "sqs",
        "us-east-1",
        "123456789012",
        None,
        "my-queue.fifo",
        None,
    ),
    (
        "arn:aws:s3:us-east-1:123456789012:accesspoint/ap",
        "aws",
        "s3",
        "us-east-1",
        "123456789012",
        "accesspoint",
        "ap",
        "/",
    ),
    (
        "arn:aws:iam::aws:policy/AdministratorAccess",
        "aws",
        "iam",
        "",
        "aws",
        "policy",
        "AdministratorAccess",
        "/",
    ),
    (
        "arn:aws-cn:ec2:cn-north-1:123456789012:instance/i-0abc",
        "aws-cn",
        "ec2",
        "cn-north-1",
        "123456789012",
        "instance",
        "i-0abc",
        "/",
    ),
    (
        "arn:aws-us-gov:kms:us-gov-west-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab",
        "aws-us-gov",
        "kms",
        "us-gov-west-1",
        "123456789012",
        "key",
        "1234abcd-12ab-34cd-56ef-1234567890ab",
        "/",
    ),
    (
        "arn:aws-iso-b:ec2:us-isob-east-1:123456789012:vpc/vpc-1",
        "aws-iso-b",
        "ec2",
        "us-isob-east-1",
        "123456789012",
        "vpc",
        "vpc-1",
        "/",
    ),
    (
        "arn:aws:execute-api:us-east-1:123456789012:abc123/prod/GET/pets",
        "aws",
        "execute-api",
        "us-east-1",
        "123456789012",
        "abc123",
        "prod/GET/pets",
        "/",
    ),
    (
        "arn:aws:dynamodb:us-east-1:123456789012:table",
        "aws",
        "dynamodb",
        "us-east-1",
        "123456789012",
        None,
        "table",
        None,
    ),
]


@pytest.mark.parametrize(
    ("value", "partition", "service", "region", "account", "rtype", "rid", "delim"),
    DECOMPOSITION_CASES,
)
def test_parse_decomposes_and_round_trips(
    value: str,
    partition: str,
    service: str,
    region: str,
    account: str,
    rtype: str | None,
    rid: str,
    delim: str | None,
) -> None:
    arn = ARN.parse(value)

    assert arn.is_valid, arn.errors
    assert (arn.partition, arn.service, arn.region, arn.account_id) == (partition, service, region, account)
    assert arn.resource_type == rtype
    assert arn.resource_id == rid
    assert arn.resource_delimiter == delim
    assert str(arn) == value


def test_naive_split_would_break_but_arn_does_not() -> None:
    value = "arn:aws:s3:::my-bucket/logs/2026:10:09.gz"
    assert len(value.split(":")) == 8  # the bug users hit
    assert ARN.parse(value).resource == "my-bucket/logs/2026:10:09.gz"


@pytest.mark.parametrize(
    ("value", "fragment"),
    [
        ("arn:AWS:s3:::bucket", "Partition 'AWS' is malformed"),
        ("arn::s3:::bucket", "Partition is empty"),
        ("arn:aws::us-east-1:123456789012:x", "Service is empty"),
        ("arn:aws:S3:::bucket", "Service 'S3' is malformed"),
        ("arn:aws:sqs:useast1:123456789012:q", "Region 'useast1' is malformed"),
        ("arn:aws:sqs:us-east-1:12345678901:q", "must be exactly 12 digits"),
        ("arn:aws:sqs:us-east-1:1234567890123:q", "must be exactly 12 digits"),
        ("arn:aws:sqs:us-east-1:12345678901a:q", "must be exactly 12 digits"),
        ("arn:aws:sqs:us-east-1:123456789012:", "Resource is empty"),
        ("arn:aws:sqs:us-east-1:123456789012:bad\x00queue", "control characters"),
    ],
)
def test_component_errors(value: str, fragment: str) -> None:
    arn = ARN.parse(value)
    assert arn.is_valid is False
    assert any(fragment in err for err in arn.errors), arn.errors


def test_length_limit() -> None:
    prefix = "arn:aws:s3:::"
    arn = ARN.parse(prefix + "b" * (MAX_ARN_LENGTH - len(prefix) + 1))
    assert arn.is_valid is False
    assert any("exceeds the maximum" in e for e in arn.errors)
    assert ARN.parse(prefix + "b" * (MAX_ARN_LENGTH - len(prefix))).is_valid


def test_unknown_partition_and_whitespace_are_warnings_only() -> None:
    arn = ARN.parse("arn:aws-future:s3:::bucket")
    assert arn.is_valid
    assert any("not a known AWS partition" in w for w in arn.warnings)

    alarm = ARN.parse("arn:aws:cloudwatch:us-east-1:123456789012:alarm:My Alarm")
    assert alarm.is_valid
    assert any("whitespace" in w for w in alarm.warnings)


@pytest.mark.parametrize("value", ["", "not-an-arn", "arn:aws:s3", "arn:aws:s3::", "urn:aws:s3:::bucket"])
def test_unparseable_values_raise(value: str) -> None:
    with pytest.raises(ARNParseError) as exc_info:
        ARN.parse(value)
    assert exc_info.value.value == value
    assert isinstance(exc_info.value, ValueError)


def test_parse_non_string_raises() -> None:
    with pytest.raises(ARNParseError):
        ARN.parse(123)  # type: ignore[arg-type]


def test_strict_parse_raises_with_errors() -> None:
    with pytest.raises(ARNParseError) as exc_info:
        ARN.parse("arn:aws:iam::12345:role/x", strict=True)
    assert exc_info.value.errors
    assert "12 digits" in str(exc_info.value)


def test_try_parse_and_is_arn_never_raise() -> None:
    assert ARN.try_parse("garbage") is None
    assert ARN.try_parse("arn:aws:sqs:us-east-1:123456789012:q") is not None
    assert ARN.is_arn("arn:aws:sqs:us-east-1:123456789012:q") is True
    assert ARN.is_arn("arn:aws:sqs:us-east-1:1:q") is False
    assert ARN.is_arn("garbage") is False
    assert ARN.is_arn(None) is False  # type: ignore[arg-type]


def test_build_from_resource() -> None:
    arn = ARN.build(service="sqs", region="us-east-1", account_id="123456789012", resource="my-queue")
    assert str(arn) == "arn:aws:sqs:us-east-1:123456789012:my-queue"


@pytest.mark.parametrize(
    ("delimiter", "expected"),
    [
        ("/", "arn:aws:iam::123456789012:role/path/MyRole"),
        (":", "arn:aws:iam::123456789012:role:path/MyRole"),
    ],
)
def test_build_from_type_and_id(delimiter: str, expected: str) -> None:
    arn = ARN.build(
        service="iam",
        account_id="123456789012",
        resource_type="role",
        resource_id="path/MyRole",
        delimiter=delimiter,  # type: ignore[arg-type]
    )
    assert str(arn) == expected
    assert arn.resource_type == "role"
    assert arn.resource_id == "path/MyRole"


def test_build_validates_by_default() -> None:
    with pytest.raises(ARNParseError):
        ARN.build(service="sqs", region="us-east-1", account_id="123", resource="q")
    lenient = ARN.build(service="sqs", region="us-east-1", account_id="123", resource="q", strict=False)
    assert lenient.is_valid is False


@pytest.mark.parametrize(
    "kwargs",
    [
        {"resource": "q", "resource_type": "x"},
        {"resource": "q", "resource_id": "x"},
        {},
        {"resource_type": "role"},
        {"resource_type": "role", "resource_id": "r", "delimiter": "|"},
    ],
)
def test_build_argument_conflicts(kwargs: dict[str, str]) -> None:
    with pytest.raises(ValueError):
        ARN.build(service="iam", **kwargs)  # type: ignore[arg-type]


def test_replace_revalidates() -> None:
    arn = ARN.parse("arn:aws:sqs:us-east-1:123456789012:q")
    moved = arn.replace(region="eu-west-1")
    assert str(moved) == "arn:aws:sqs:eu-west-1:123456789012:q"
    broken = arn.replace(account_id="nope")
    assert broken.is_valid is False


def test_equality_hash_and_immutability() -> None:
    a = ARN.parse("arn:aws:sqs:us-east-1:123456789012:q")
    b = ARN.build(service="sqs", region="us-east-1", account_id="123456789012", resource="q")
    assert a == b
    assert hash(a) == hash(b)
    assert len({a, b}) == 1
    with pytest.raises(AttributeError):
        a.region = "eu-west-1"  # type: ignore[misc]


def test_to_dict() -> None:
    data = ARN.parse("arn:aws:iam::123456789012:role/MyRole").to_dict()
    assert data["arn"] == "arn:aws:iam::123456789012:role/MyRole"
    assert data["resource_type"] == "role"
    assert data["resource_id"] == "MyRole"
    assert data["is_valid"] is True
    assert data["errors"] == []


def test_validate_against_real_shape() -> None:
    arn = ARN.parse("arn:aws:s3:us-east-1:123456789012:job/abc")
    result = arn.validate_against("s3control", "JobArn")
    assert isinstance(result, ValidationResult)
    assert result.is_valid is True

    other = ARN.parse("arn:aws:sqs:us-east-1:123456789012:q").validate_against("s3control", "JobArn")
    assert other.is_valid is False


def test_validate_against_unknown_raises_key_error() -> None:
    arn = ARN.parse("arn:aws:s3:us-east-1:123456789012:job/abc")
    with pytest.raises(KeyError, match="not found"):
        arn.validate_against("nonexistentservice", "JobArn")
    with pytest.raises(KeyError, match="not found"):
        arn.validate_against("s3control", "NoSuchShapeXyz")


def test_matching_shapes_default_is_service_pinned() -> None:
    matches = ARN.parse("arn:aws:s3:us-east-1:123456789012:job/abc").matching_shapes()
    assert ("S3control", "JobArn") in matches
    assert all(name.lower().endswith("arn") for _, name in matches)


def test_matching_shapes_restricted_services() -> None:
    arn = ARN.parse("arn:aws:s3:us-east-1:123456789012:job/abc")
    matches = arn.matching_shapes(services=["s3control"])
    assert matches
    assert {svc for svc, _ in matches} == {"S3control"}
    with pytest.raises(KeyError):
        arn.matching_shapes(services=["nonexistentservice"])


class _Model(BaseModel):
    role_arn: ARN


def test_pydantic_accepts_str_and_instance() -> None:
    m = _Model(role_arn="arn:aws:iam::123456789012:role/MyRole")  # type: ignore[arg-type]
    assert isinstance(m.role_arn, ARN)
    assert m.role_arn.resource_type == "role"
    assert m.model_dump() == {"role_arn": "arn:aws:iam::123456789012:role/MyRole"}
    assert m.model_dump_json() == '{"role_arn":"arn:aws:iam::123456789012:role/MyRole"}'

    m2 = _Model(role_arn=ARN.parse("arn:aws:iam::123456789012:role/MyRole"))
    assert m2.role_arn == m.role_arn

    m3 = _Model.model_validate_json('{"role_arn": "arn:aws:iam::123456789012:role/MyRole"}')
    assert m3.role_arn == m.role_arn


@pytest.mark.parametrize(
    "bad",
    ["not-an-arn", "arn:aws:iam::12345:role/x", 42],
)
def test_pydantic_rejects_invalid(bad: object) -> None:
    with pytest.raises(ValidationError):
        _Model(role_arn=bad)  # type: ignore[arg-type]


def test_pydantic_rejects_invalid_instance() -> None:
    with pytest.raises(ValidationError):
        _Model(role_arn=ARN.parse("arn:aws:iam::12345:role/x"))


def test_pydantic_json_schema_is_string() -> None:
    schema = _Model.model_json_schema()
    assert schema["properties"]["role_arn"]["type"] == "string"


def test_parse_does_not_load_registry() -> None:
    import subprocess
    import sys

    code = (
        "import sys; from aws_resource_validator import ARN; "
        "ARN.parse('arn:aws:sqs:us-east-1:123456789012:q'); "
        "print('aws_resource_validator.class_definitions' in sys.modules)"
    )
    out = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, check=True)
    assert out.stdout.strip() == "False"
