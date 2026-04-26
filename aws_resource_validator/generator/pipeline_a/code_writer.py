"""Render the committed ``class_definitions.py`` from an :class:`APIRegistry`.

The output is produced with Jinja2 (deterministic, easy to read) and
post-processed with :mod:`black` so diffs across generator runs are
formatting-stable.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from aws_resource_validator.core.registry import APIRegistry
from aws_resource_validator.generator.common.formatter import format_python
from aws_resource_validator.generator.common.io import write_text_atomic
from aws_resource_validator.generator.common.logging import get_logger
from aws_resource_validator.generator.common.templates import build_environment

_logger = get_logger(__name__)
_TEMPLATE_DIR = Path(__file__).parent / "templates"
_TEMPLATE_NAME = "class_definitions.py.j2"


@dataclass(frozen=True)
class _ApiObjectView:
    name: str
    type: str
    pattern_literal: str
    min_length: int | None
    max_length: int | None


@dataclass(frozen=True)
class _ServiceView:
    name: str
    instance_name: str
    api_objects: tuple[_ApiObjectView, ...]


def _to_pattern_literal(pattern: str) -> str:
    """Render a regex string as a raw-string literal when it's safe to do so.

    Raw strings cannot contain an embedded single-quote (escape sequences are
    disabled, so ``r'foo\\'bar'`` would keep the backslash in the string)
    nor end with an unpaired trailing backslash. Fall back to :func:`repr`
    in those cases, and for any string containing newlines/carriage returns.
    """
    trailing = len(pattern) - len(pattern.rstrip("\\"))
    if trailing % 2 == 1 or "\r" in pattern or "\n" in pattern or "'" in pattern:
        return repr(pattern)
    return f"r'{pattern}'"


def _build_views(registry: APIRegistry) -> list[_ServiceView]:
    services: list[_ServiceView] = []
    for service_name in sorted(registry):
        service = registry[service_name]
        api_objects = tuple(
            _ApiObjectView(
                name=obj.name,
                type=obj.type,
                pattern_literal=_to_pattern_literal(obj.pattern),
                min_length=obj.min_length,
                max_length=obj.max_length,
            )
            for obj in sorted(service.api_objects.values(), key=lambda o: o.name)
        )
        services.append(
            _ServiceView(
                name=service.service_name,
                instance_name=service.service_name.lower(),
                api_objects=api_objects,
            )
        )
    return services


def render_class_definitions(registry: APIRegistry) -> str:
    """Return the rendered, black-formatted ``class_definitions.py`` source."""
    template = build_environment(_TEMPLATE_DIR).get_template(_TEMPLATE_NAME)
    rendered = template.render(services=_build_views(registry))
    return format_python(rendered)


def write_class_definitions(registry: APIRegistry, destination: Path) -> None:
    """Render and atomically write the committed ``class_definitions.py``."""
    source = render_class_definitions(registry)
    write_text_atomic(destination, source)
    _logger.info("Wrote %s (%d services).", destination, len(registry))
