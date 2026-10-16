"""Service and shape lookup utilities with typo suggestions and fuzzy matching."""

from __future__ import annotations

import difflib
from functools import cache
from typing import TYPE_CHECKING

from aws_resource_validator.core.builtin_rules import BUILTIN_SHAPE_RULES
from aws_resource_validator.core.naming import to_pascal_case
from aws_resource_validator.core.service import Service

if TYPE_CHECKING:
    from aws_resource_validator.core.api_object import APIObject
    from aws_resource_validator.core.registry import APIRegistry


@cache
def get_registry() -> APIRegistry:
    """Lazily load and cache the class registry from class_definitions.

    Deferring import preserves sub-50ms startup time for commands like ``--help``.
    """
    from aws_resource_validator.class_definitions import class_registry  # noqa: PLC0415

    return class_registry


def normalize_name(name: str) -> str:
    """Strip hyphens, underscores, and lowercase for fault-tolerant comparison."""
    return name.lower().replace("-", "").replace("_", "")


def _get_builtin_service(query_norm: str) -> Service | None:
    """Create a virtual Service populated from BUILTIN_SHAPE_RULES if matching shapes exist."""
    shapes_by_name: dict[str, APIObject] = {}
    for (svc_name, _), obj in BUILTIN_SHAPE_RULES.items():
        if normalize_name(svc_name) == query_norm:
            shapes_by_name[obj.name] = obj

    if not shapes_by_name:
        return None

    return Service(to_pascal_case(query_norm), shapes_by_name.values())


def resolve_service(query: str) -> tuple[Service | None, list[str]]:
    """Look up an AWS service in the registry by name.

    Supports exact PascalCase, snake_case, kebab-case, and case-insensitive queries.
    Falls back to built-in service rules when missing from class_registry.
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

    # 4. Check built-in services (e.g. s3, sqs, rds)
    builtin_svc = _get_builtin_service(query_norm)
    if builtin_svc is not None:
        return builtin_svc, []

    # 5. Fuzzy suggestions for typos
    all_names = list(registry.services.keys())
    for svc_key, _ in BUILTIN_SHAPE_RULES:
        p_name = to_pascal_case(svc_key)
        if p_name not in all_names:
            all_names.append(p_name)

    suggestions = difflib.get_close_matches(query, all_names, n=3, cutoff=0.5)
    if not suggestions:
        suggestions = difflib.get_close_matches(pascal, all_names, n=3, cutoff=0.5)

    return None, suggestions


def resolve_shape(service: Service, query: str) -> tuple[APIObject | None, list[str]]:
    """Look up an API shape within a service.

    Supports exact PascalCase, snake_case aliases, and case-insensitive queries.
    Falls back to built-in shape rules when missing from the service definition.
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

    # 3. Check built-in rules for this service
    svc_norm = normalize_name(service.service_name)
    for (svc_key, shape_key), obj in BUILTIN_SHAPE_RULES.items():
        if normalize_name(svc_key) == svc_norm and (
            normalize_name(shape_key) == query_norm or normalize_name(obj.name) == query_norm
        ):
            return obj, []

    # 4. Fuzzy suggestions
    all_shapes = list(service.api_objects.keys())
    for (svc_key, _), obj in BUILTIN_SHAPE_RULES.items():
        if normalize_name(svc_key) == svc_norm and obj.name not in all_shapes:
            all_shapes.append(obj.name)

    suggestions = difflib.get_close_matches(query, all_shapes, n=3, cutoff=0.5)

    return None, suggestions


def list_services(query: str | None = None) -> list[tuple[str, int]]:
    """Return a sorted list of ``(service_name, shape_count)``, optionally filtered."""
    registry = get_registry()
    counts: dict[str, int] = {}
    norm_query = query.lower() if query else None

    for name in registry.services:
        counts[name] = len(registry[name])

    # Include built-in services if not already present
    for (svc_key, _), _ in BUILTIN_SHAPE_RULES.items():
        p_name = to_pascal_case(svc_key)
        if p_name not in counts:
            builtin = _get_builtin_service(normalize_name(svc_key))
            counts[p_name] = len(builtin.api_objects) if builtin else 0

    items: list[tuple[str, int]] = []
    for name in sorted(counts.keys()):
        if norm_query and norm_query not in name.lower():
            continue
        items.append((name, counts[name]))

    return items
