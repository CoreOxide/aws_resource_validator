"""Cached offline botocore service, operation, and tool-name resolution."""

from __future__ import annotations

import difflib
from collections.abc import Mapping
from functools import cache, lru_cache
from typing import Any

import botocore.session


@cache
def _get_botocore_session() -> Any:
    """Return a shared botocore session for offline model lookups."""
    return botocore.session.get_session()


@cache
def _get_available_services() -> tuple[str, ...]:
    """Return all botocore service names available in the installed data bundle."""
    return tuple(_get_botocore_session().get_available_services())


@cache
def _get_normalized_service_map() -> dict[str, str]:
    """Map normalized service names (no hyphens/underscores, lowercase) to canonical names."""
    return {_normalize(svc): svc for svc in _get_available_services()}


@lru_cache(maxsize=64)
def _load_service_model(canonical_service: str) -> Any:
    """Load and cache a botocore ServiceModel by canonical service name."""
    return _get_botocore_session().get_service_model(canonical_service)


def _normalize(name: str) -> str:
    """Strip whitespace, hyphens, and underscores and lowercase for matching."""
    return name.strip().lower().replace("-", "").replace("_", "")


def resolve_botocore_service(service: str) -> tuple[Any | None, str, list[str]]:
    """Resolve an AWS service name to a cached botocore ``ServiceModel``.

    Supports exact names (``"s3"``), uppercase/PascalCase (``"S3"``, ``"DynamoDB"``),
    Python-keyword suffixed names (``"lambda_"``), and underscores (``"cognito_idp"``).

    Returns ``(service_model, canonical_name, [])`` on success, or
    ``(None, service, suggestions)`` when the service cannot be found.
    """
    cleaned = service.strip()
    if not cleaned:
        return None, service, []

    available = _get_available_services()
    available_set = set(available)

    lowered = cleaned.lower()
    if lowered in available_set:
        return _load_service_model(lowered), lowered, []

    stripped_trailing = lowered.rstrip("_")
    if stripped_trailing and stripped_trailing in available_set:
        return _load_service_model(stripped_trailing), stripped_trailing, []

    norm_map = _get_normalized_service_map()
    norm = _normalize(cleaned)
    if norm in norm_map:
        canonical = norm_map[norm]
        return _load_service_model(canonical), canonical, []

    suggestions = difflib.get_close_matches(lowered, available, n=3, cutoff=0.5)
    if not suggestions and norm:
        norm_matches = difflib.get_close_matches(norm, list(norm_map.keys()), n=3, cutoff=0.5)
        suggestions = [norm_map[m] for m in norm_matches]

    return None, service, suggestions


def resolve_botocore_operation(
    service_model: Any,
    operation: str,
) -> tuple[Any | None, str, list[str]]:
    """Resolve an AWS operation name on a botocore ``ServiceModel``.

    Supports exact PascalCase (``"PutObject"``), snake_case (``"put_object"``),
    and case-insensitive matching.

    Returns ``(operation_model, canonical_name, [])`` on success, or
    ``(None, operation, suggestions)`` when the operation cannot be found.
    """
    cleaned = operation.strip()
    if not cleaned:
        return None, operation, []

    op_names: tuple[str, ...] = tuple(getattr(service_model, "operation_names", ()))
    if cleaned in op_names:
        return service_model.operation_model(cleaned), cleaned, []

    norm = _normalize(cleaned)
    norm_map = {_normalize(op): op for op in op_names}
    if norm in norm_map:
        canonical = norm_map[norm]
        return service_model.operation_model(canonical), canonical, []

    suggestions = difflib.get_close_matches(cleaned, op_names, n=3, cutoff=0.5)
    if not suggestions and norm:
        norm_matches = difflib.get_close_matches(norm, list(norm_map.keys()), n=3, cutoff=0.5)
        suggestions = [norm_map[m] for m in norm_matches]

    return None, operation, suggestions


def parse_tool_name(
    tool_name: str,
    tool_name_map: Mapping[str, tuple[str, str]] | None = None,
) -> tuple[str, str] | None:
    """Parse an LLM tool name into ``(service, operation)``.

    Checks ``tool_name_map`` first, then common delimiters (``.``, ``:``, ``/``,
    ``__``), and finally ``<service>_<operation>`` prefixes matching known
    botocore services (e.g. ``"s3_put_object"`` -> ``("s3", "put_object")``).
    """
    cleaned = tool_name.strip()
    if not cleaned:
        return None

    if tool_name_map and cleaned in tool_name_map:
        return tool_name_map[cleaned]

    for sep in (".", ":", "/", "__"):
        if sep in cleaned:
            svc, op = cleaned.split(sep, 1)
            svc_s = svc.strip()
            op_s = op.strip()
            if svc_s and op_s:
                return svc_s, op_s

    if "_" in cleaned:
        parts = cleaned.split("_")
        available = set(_get_available_services())
        # Try longest service prefix first (e.g. "cognito_idp_admin_get_user")
        for idx in range(len(parts) - 1, 0, -1):
            candidate_hyphen = "-".join(parts[:idx]).lower()
            candidate_raw = "_".join(parts[:idx]).lower()
            op_part = "_".join(parts[idx:]).strip()
            if not op_part:
                continue
            if candidate_hyphen in available:
                return candidate_hyphen, op_part
            if candidate_raw in available:
                return candidate_raw, op_part

    return None
