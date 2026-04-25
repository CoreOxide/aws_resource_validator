"""Tests for :mod:`aws_resource_validator.core.service`."""

from __future__ import annotations

import pytest

from aws_resource_validator.core.api_object import APIObject
from aws_resource_validator.core.service import Service


class TestServiceName:
    @pytest.mark.parametrize(
        ("raw", "expected"),
        [
            ("acm", "Acm"),
            ("access-analyzer", "AccessAnalyzer"),
            ("application_autoscaling", "ApplicationAutoscaling"),
            ("s3", "S3"),
        ],
    )
    def test_normalizes_to_pascal_case(self, raw: str, expected: str) -> None:
        assert Service(raw).service_name == expected


class TestAddApiObject:
    def test_stores_object_under_canonical_name(self) -> None:
        obj = APIObject(name="AccessPointArn", type="string", pattern=r".+")
        svc = Service("acm")
        svc.add_api_object(obj)
        assert svc.AccessPointArn is obj
        assert svc["AccessPointArn"] is obj

    def test_registers_snake_case_alias(self) -> None:
        obj = APIObject(name="AccessPointArn", type="string", pattern=r".+")
        svc = Service("acm")
        svc.add_api_object(obj)
        assert svc.access_point_arn is obj
        assert svc["access_point_arn"] is obj

    def test_single_word_names_have_no_distinct_snake_alias(self) -> None:
        obj = APIObject(name="Arn", type="string", pattern=r".+")
        svc = Service("acm")
        svc.add_api_object(obj)
        assert svc.Arn is obj
        # No KeyError — single-word name reuses the same alias.
        assert svc["Arn"] is obj

    def test_supports_legacy_two_argument_form(self) -> None:
        obj = APIObject(name="Arn", type="string", pattern=r".+")
        svc = Service("acm")
        # Legacy call site: ``add_api_object("Arn", obj)`` — the name is ignored.
        svc.add_api_object("ignored", obj)
        assert svc.Arn is obj

    def test_rejects_non_api_object(self) -> None:
        svc = Service("acm")
        with pytest.raises(TypeError, match="expected APIObject"):
            svc.add_api_object("just a string")  # type: ignore[arg-type]


class TestMappingBehavior:
    def test_len_matches_object_count(self, sample_service: Service) -> None:
        assert len(sample_service) == 1

    def test_iteration_yields_canonical_names(self, sample_service: Service) -> None:
        assert list(sample_service) == ["AccessPointArn"]

    def test_missing_attribute_raises(self) -> None:
        svc = Service("acm")
        with pytest.raises(AttributeError):
            svc.Nope

    def test_missing_key_raises(self) -> None:
        svc = Service("acm")
        with pytest.raises(KeyError):
            svc["Nope"]
