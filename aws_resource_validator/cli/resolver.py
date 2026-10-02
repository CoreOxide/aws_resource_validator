"""Service and shape lookup utilities with typo suggestions and fuzzy matching.

Re-exports core resolver functionality for backward compatibility with CLI callers.
"""

from __future__ import annotations

from aws_resource_validator.core.resolver import (
    get_registry,
    list_services,
    normalize_name,
    resolve_service,
    resolve_shape,
)

__all__ = [
    "get_registry",
    "list_services",
    "normalize_name",
    "resolve_service",
    "resolve_shape",
]
