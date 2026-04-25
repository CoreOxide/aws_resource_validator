"""Shared pytest fixtures for aws_resource_validator."""

from __future__ import annotations

import ast
from collections.abc import Callable
from pathlib import Path

import pytest

from aws_resource_validator.core.api_object import APIObject
from aws_resource_validator.core.registry import APIRegistry
from aws_resource_validator.core.service import Service


@pytest.fixture
def sample_api_object() -> APIObject:
    """A plain APIObject usable by any unit test that just needs one."""
    return APIObject(
        name="AccessPointArn",
        type="string",
        pattern=r"arn:[^:]*:s3:[^:]*:[^:]*:accesspoint/.*",
        min_length=5,
        max_length=200,
    )


@pytest.fixture
def sample_service(sample_api_object: APIObject) -> Service:
    return Service("my-service", [sample_api_object])


@pytest.fixture
def sample_registry(sample_service: Service) -> APIRegistry:
    registry = APIRegistry()
    registry.add(sample_service)
    return registry


@pytest.fixture
def parse_expr() -> Callable[[str], ast.expr]:
    """Helper: parse a Python expression and return its AST root node."""
    def _parse(source: str) -> ast.expr:
        return ast.parse(source, mode="eval").body
    return _parse


@pytest.fixture
def pydantic_models_root() -> Path:
    """Filesystem path to the generated pydantic_models tree."""
    import aws_resource_validator
    return Path(aws_resource_validator.__file__).parent / "pydantic_models"
