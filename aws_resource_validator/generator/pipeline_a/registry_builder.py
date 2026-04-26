"""Glue: turn a :class:`GitHubBotocoreSource` into an :class:`APIRegistry`."""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any

from aws_resource_validator.core.registry import APIRegistry
from aws_resource_validator.core.service import Service
from aws_resource_validator.generator.common.logging import get_logger
from aws_resource_validator.generator.pipeline_a.shape_parser import iter_pattern_shapes

_logger = get_logger(__name__)


def build_registry(services: Iterator[tuple[str, dict[str, Any]]]) -> APIRegistry:
    """Assemble an :class:`APIRegistry` from ``(service_name, service_json)`` pairs.

    Services with no pattern-carrying shapes are skipped (they contribute no
    validation surface and would be empty classes).
    """
    registry = APIRegistry()
    for name, service_json in services:
        api_objects = list(iter_pattern_shapes(service_json))
        if not api_objects:
            _logger.debug("Skipping %s: no pattern shapes.", name)
            continue
        registry.add(Service(name, api_objects))
        _logger.info("Registered %s with %d API objects.", name, len(api_objects))
    return registry
