"""Service and shape lookup utilities with typo suggestions and fuzzy matching."""

from __future__ import annotations

import difflib
from functools import cache
from typing import TYPE_CHECKING

from aws_resource_validator.core.naming import to_pascal_case

if TYPE_CHECKING:
    from aws_resource_validator.core.api_object import APIObject
    from aws_resource_validator.core.registry import APIRegistry
    from aws_resource_validator.core.service import Service


@cache
def get_registry() -> APIRegistry:
    """Lazily load and cache the class registry from class_definitions.

    Deferring import preserves sub-50ms startup time for commands like ``--help``.
    """
    from aws_resource_validator.class_definitions import class_registry

    return class_registry


def normalize_name(name: str) -> str:
    """Strip hyphens, underscores, and lowercase for fault-tolerant comparison."""
    return name.lower().replace("-", "").replace("_", "")


def resolve_service(query: str) -> tuple[Service | None, list[str]]:
    """Look up an AWS service in the registry by name.

    Supports exact PascalCase, snake_case, kebab-case, and case-insensitive queries.
    Returns ``(service, [])`` on success, or ``(None, suggestions)`` on failure.
    """
    registry = get_registry()

    # 1. Exact match
    if query in registry:
        return registry[query], []

    # 2. PascalCase conversion (e.g. "s3-control" -> "S3Control", "lambda" -> "Lambda")
    pascal = to_pascal_case(query)
    if pascal in registry:
        return registry[pascal], []

    # 3. Normalized match across all registered services
    query_norm = normalize_name(query)
    for name, svc in registry.services.items():
        if normalize_name(name) == query_norm:
            return svc, []

    # 4. Fuzzy suggestions for typos
    all_names = list(registry.services.keys())
    suggestions = difflib.get_close_matches(query, all_names, n=3, cutoff=0.5)
    if not suggestions:
        suggestions = difflib.get_close_matches(pascal, all_names, n=3, cutoff=0.5)

    return None, suggestions


def resolve_shape(service: Service, query: str) -> tuple[APIObject | None, list[str]]:
    """Look up an API shape within a service.

    Supports exact PascalCase, snake_case aliases, and case-insensitive queries.
    Returns ``(api_object, [])`` on success, or ``(None, suggestions)`` on failure.
    """
    # 1. Exact index or alias (Service.__getitem__ handles PascalCase and snake_case)
    try:
        return service[query], []
    except KeyError:
        pass

    # 2. Normalized match across available shapes
    query_norm = normalize_name(query)
    for name, obj in service.api_objects.items():
        if normalize_name(name) == query_norm:
            return obj, []

    # 3. Fuzzy suggestions
    all_shapes = list(service.api_objects.keys())
    suggestions = difflib.get_close_matches(query, all_shapes, n=3, cutoff=0.5)

    return None, suggestions


def list_services(query: str | None = None) -> list[tuple[str, int]]:
    """Return a sorted list of ``(service_name, shape_count)``, optionally filtered."""
    registry = get_registry()
    items: list[tuple[str, int]] = []
    norm_query = query.lower() if query else None

    for name in sorted(registry.services.keys()):
        if norm_query and norm_query not in name.lower():
            continue
        items.append((name, len(registry[name])))

    return items
