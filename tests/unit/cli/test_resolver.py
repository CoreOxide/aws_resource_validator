"""Unit tests for service and shape resolution and fuzzy suggestions."""

from __future__ import annotations

from aws_resource_validator.cli.resolver import (
    list_services,
    normalize_name,
    resolve_service,
    resolve_shape,
)
from aws_resource_validator.core.api_object import APIObject
from aws_resource_validator.core.service import Service


def test_normalize_name() -> None:
    assert normalize_name("S3-Control") == "s3control"
    assert normalize_name("Cognito_Idp") == "cognitoidp"
    assert normalize_name("lambda") == "lambda"


def test_resolve_service_exact_and_case_insensitive() -> None:
    svc, suggestions = resolve_service("Lambda")
    assert svc is not None
    assert svc.service_name == "Lambda"
    assert suggestions == []

    svc2, _ = resolve_service("lambda")
    assert svc2 is not None
    assert svc2.service_name == "Lambda"

    svc3, _ = resolve_service("LAMBDA")
    assert svc3 is not None
    assert svc3.service_name == "Lambda"


def test_resolve_service_with_hyphens_or_underscores() -> None:
    svc, _ = resolve_service("s3-control")
    assert svc is not None
    assert svc.service_name == "S3control"

    svc2, _ = resolve_service("s3_control")
    assert svc2 is not None
    assert svc2.service_name == "S3control"


def test_resolve_service_missing_returns_suggestions() -> None:
    svc, suggestions = resolve_service("lamda")
    assert svc is None
    assert "Lambda" in suggestions


def test_resolve_shape_exact_and_case_insensitive() -> None:
    sample_svc = Service(
        "Demo",
        [
            APIObject(name="ResourceName", type="string", pattern="[a-z]+"),
            APIObject(name="ClusterId", type="string", pattern="[0-9]+"),
        ],
    )

    obj, suggestions = resolve_shape(sample_svc, "ResourceName")
    assert obj is not None
    assert obj.name == "ResourceName"
    assert suggestions == []

    # snake_case alias
    obj2, _ = resolve_shape(sample_svc, "resource_name")
    assert obj2 is not None
    assert obj2.name == "ResourceName"

    # case-insensitive
    obj3, _ = resolve_shape(sample_svc, "resourcename")
    assert obj3 is not None
    assert obj3.name == "ResourceName"


def test_resolve_shape_missing_returns_suggestions() -> None:
    sample_svc = Service(
        "Demo",
        [
            APIObject(name="ResourceName", type="string", pattern="[a-z]+"),
        ],
    )
    obj, suggestions = resolve_shape(sample_svc, "ResourceNam")
    assert obj is None
    assert "ResourceName" in suggestions


def test_list_services_filtering() -> None:
    services = list_services()
    assert len(services) > 100

    filtered = list_services(query="lambda")
    assert any(s == "Lambda" for s, _ in filtered)
    assert all("lambda" in s.lower() for s, _ in filtered)
