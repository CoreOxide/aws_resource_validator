"""Tests for :mod:`aws_resource_validator.generator.pipeline_a.code_writer`."""

from __future__ import annotations

import ast
from pathlib import Path

from aws_resource_validator.core.api_object import APIObject
from aws_resource_validator.core.registry import APIRegistry
from aws_resource_validator.core.service import Service
from aws_resource_validator.generator.pipeline_a.code_writer import (
    _to_pattern_literal,
    render_class_definitions,
    write_class_definitions,
)


def _single_service_registry() -> APIRegistry:
    registry = APIRegistry()
    registry.add(
        Service(
            "acm",
            [APIObject(name="Arn", type="string", pattern=r"arn:.+", min_length=5, max_length=10)],
        )
    )
    return registry


def test_renders_parseable_python() -> None:
    source = render_class_definitions(_single_service_registry())
    ast.parse(source)


def test_render_contains_service_class() -> None:
    source = render_class_definitions(_single_service_registry())
    assert "class Acm(Service)" in source


def test_render_is_deterministic() -> None:
    first = render_class_definitions(_single_service_registry())
    second = render_class_definitions(_single_service_registry())
    assert first == second


def test_write_creates_file(tmp_path: Path) -> None:
    destination = tmp_path / "out.py"
    write_class_definitions(_single_service_registry(), destination)
    content = destination.read_text()
    assert "class Acm(Service)" in content
    ast.parse(content)


def _parse_string_literal(rendered: str) -> str:
    """Return the Python ``str`` the source literal ``rendered`` evaluates to.

    Uses :func:`ast.parse` + :func:`ast.literal_eval` so we confirm the source
    is a *legal string literal* (raw or otherwise) without running code.
    """
    node = ast.parse(rendered, mode="eval").body
    return ast.literal_eval(node)


class TestPatternLiteral:
    """Regressions for raw-string rendering in the template."""

    def test_simple_pattern_becomes_raw_string(self) -> None:
        assert _to_pattern_literal(r"arn:aws:.+") == r"r'arn:aws:.+'"

    def test_embedded_single_quote_is_escaped(self) -> None:
        rendered = _to_pattern_literal(r"foo'bar")
        assert _parse_string_literal(rendered) == r"foo'bar"

    def test_odd_trailing_backslashes_force_repr(self) -> None:
        # Raw strings cannot end with an unpaired backslash.
        rendered = _to_pattern_literal("foo\\")
        assert not rendered.startswith("r'")
        assert _parse_string_literal(rendered) == "foo\\"

    def test_newline_in_pattern_forces_repr(self) -> None:
        rendered = _to_pattern_literal("foo\nbar")
        assert not rendered.startswith("r'")
        assert _parse_string_literal(rendered) == "foo\nbar"
