"""Tests for :mod:`aws_resource_validator.core.naming`."""

from __future__ import annotations

import pytest

from aws_resource_validator.core.naming import safe_identifier, to_pascal_case, to_snake_case


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("CamelCase", "camel_case"),
        ("HTTPHeaders", "h_t_t_p_headers"),
        ("already_snake", "already_snake"),
        ("A", "a"),
        ("HTTPSProxy", "h_t_t_p_s_proxy"),
    ],
)
def test_to_snake_case(raw: str, expected: str) -> None:
    assert to_snake_case(raw) == expected


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("access-analyzer", "AccessAnalyzer"),
        ("s3", "S3"),
        ("my_service", "MyService"),
        ("snake_case_name", "SnakeCaseName"),
    ],
)
def test_to_pascal_case(raw: str, expected: str) -> None:
    assert to_pascal_case(raw) == expected


def test_to_pascal_case_preserves_keyword_safety_for_lowercase_keywords() -> None:
    # PascalCase derivatives of Python keywords are not themselves keywords,
    # so no underscore suffix is added. This is the expected behaviour for
    # AWS service names where ``For`` or ``While`` could never collide at
    # the language level.
    assert to_pascal_case("for") == "For"


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("foo", "foo"),
        ("foo-bar", "foo_bar"),
        ("class", "class_"),
        ("from", "from_"),
    ],
)
def test_safe_identifier(raw: str, expected: str) -> None:
    assert safe_identifier(raw) == expected
