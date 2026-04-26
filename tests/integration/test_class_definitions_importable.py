"""Integration: the committed Pipeline A artifact must import and be usable."""

from __future__ import annotations

import pytest

from aws_resource_validator import class_definitions
from aws_resource_validator.core.registry import APIRegistry


def test_class_registry_is_populated() -> None:
    assert isinstance(class_definitions.class_registry, APIRegistry)
    assert len(class_definitions.class_registry) > 100


@pytest.mark.parametrize("service_name", ["Acm", "Dynamodb", "Accessanalyzer"])
def test_popular_services_are_registered(service_name: str) -> None:
    registry = class_definitions.class_registry
    assert service_name in registry
    assert len(registry[service_name]) > 0


def test_acm_arn_pattern_validates_real_arn() -> None:
    acm = class_definitions.class_registry["Acm"]
    real_arn = "arn:aws:acm:us-east-1:123456789012:certificate/abcd1234-1234-1234-1234-123456789012"
    assert acm.Arn.validate(real_arn)
