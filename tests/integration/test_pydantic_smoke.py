"""Integration smoke tests for hand-picked pydantic services.

The full 100k+ parametrized test suite lives in :mod:`tests.generated`. The
cases here are shaped: they exercise real consumer code paths for popular
services to catch import-time or basic-instantiation regressions fast.
"""

from __future__ import annotations

import importlib

import pytest


@pytest.mark.parametrize(
    ("service", "class_name"),
    [
        ("acm", "TagTypeDef"),
        ("acm", "CertificateDetailTypeDef"),
        ("dynamodb", "AttributeValueTypeDef"),
        ("s3", "BucketTypeDef"),
        ("ec2", "InstanceTypeDef"),
        ("iam", "RoleTypeDef"),
        ("lambda_", "FunctionConfigurationTypeDef"),
    ],
)
def test_known_class_imports(service: str, class_name: str) -> None:
    module = importlib.import_module(f"aws_resource_validator.pydantic_models.{service}.{service}_classes")
    assert hasattr(module, class_name), f"{service} missing {class_name}"


def test_tag_round_trip() -> None:
    from aws_resource_validator.pydantic_models.acm.acm_classes import TagTypeDef

    tag = TagTypeDef(Key="env", Value="prod")
    dumped = tag.model_dump()
    assert dumped["Key"] == "env"
    assert dumped["Value"] == "prod"
    restored = TagTypeDef.model_validate(dumped)
    assert restored == tag


def test_optional_field_defaults_to_none() -> None:
    from aws_resource_validator.pydantic_models.acm.acm_classes import ExpiryEventsConfigurationTypeDef

    # All fields on this class are NotRequired — empty dict should validate.
    config = ExpiryEventsConfigurationTypeDef.model_validate({})
    assert config.DaysBeforeExpiry is None
