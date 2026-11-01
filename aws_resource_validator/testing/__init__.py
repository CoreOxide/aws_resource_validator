"""Testing utilities, Pytest fixtures, and Hypothesis strategies for AWS resource validation."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from aws_resource_validator.testing.helpers import (
    AWSValidatorHelper,
    assert_invalid,
    assert_valid,
    generate_valid,
    resolve_service_and_shape,
    validate_with_extras,
)

if TYPE_CHECKING:
    from aws_resource_validator.testing import strategies

__all__ = [
    "AWSValidatorHelper",
    "assert_invalid",
    "assert_valid",
    "generate_valid",
    "resolve_service_and_shape",
    "strategies",
    "validate_with_extras",
]


def __getattr__(name: str) -> Any:
    if name == "strategies":
        from aws_resource_validator.testing import strategies  # noqa: PLC0415

        return strategies
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
