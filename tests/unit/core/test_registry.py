"""Tests for :mod:`aws_resource_validator.core.registry`."""

from __future__ import annotations

import pytest

from aws_resource_validator.core.api_object import APIObject
from aws_resource_validator.core.registry import APIRegistry
from aws_resource_validator.core.service import Service


def _make_service(name: str) -> Service:
    return Service(name, [APIObject(name="Arn", type="string", pattern=r".+")])


class TestAdd:
    def test_registers_under_canonical_service_name(self) -> None:
        registry = APIRegistry()
        registry.add(_make_service("acm"))
        assert registry["Acm"].service_name == "Acm"

    def test_attribute_access(self) -> None:
        registry = APIRegistry()
        acm = _make_service("acm")
        registry.add(acm)
        assert registry.Acm is acm

    def test_add_service_alias_matches_add(self) -> None:
        registry = APIRegistry()
        registry.add_service(_make_service("acm"))
        assert "Acm" in registry


class TestMappingBehavior:
    def test_len_and_iter(self) -> None:
        registry = APIRegistry()
        for name in ("acm", "ec2", "s3"):
            registry.add(_make_service(name))
        assert len(registry) == 3
        assert sorted(registry) == ["Acm", "Ec2", "S3"]

    def test_services_property_returns_read_only_view(self, sample_registry: APIRegistry) -> None:
        view = sample_registry.services
        with pytest.raises(TypeError):
            view["X"] = None  # type: ignore[index]

    def test_missing_service_raises(self) -> None:
        registry = APIRegistry()
        with pytest.raises(AttributeError):
            registry.Nope
