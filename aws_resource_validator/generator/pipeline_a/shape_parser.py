"""Pure functions that pull APIObjects out of a botocore service-2.json document."""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any

from aws_resource_validator.core.api_object import APIObject


def iter_pattern_shapes(service_json: dict[str, Any]) -> Iterator[APIObject]:
    """Yield an :class:`APIObject` for every shape that declares a ``pattern``.

    Shapes without a ``pattern`` are not validatable regex-wise, so they are
    skipped. Shapes without a ``type`` are ignored as malformed entries.
    """
    shapes = service_json.get("shapes", {})
    for name, data in shapes.items():
        if not isinstance(data, dict):
            continue
        if "type" not in data or "pattern" not in data:
            continue
        yield APIObject(
            name=name,
            type=data["type"],
            pattern=data["pattern"],
            min_length=data.get("min"),
            max_length=data.get("max"),
        )
