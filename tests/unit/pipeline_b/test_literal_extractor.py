"""Tests for :mod:`aws_resource_validator.generator.pipeline_b.literal_extractor`."""

from __future__ import annotations

import ast
import textwrap

from aws_resource_validator.generator.pipeline_b.literal_extractor import extract_literals


def _parse(source: str) -> ast.Module:
    return ast.parse(textwrap.dedent(source))


def test_extracts_single_literal_alias() -> None:
    tree = _parse("StatusType = Literal['active', 'inactive']")
    literals = extract_literals(tree)
    assert len(literals) == 1
    assert literals[0].name == "StatusType"
    assert literals[0].values == ("'active'", "'inactive'")


def test_handles_single_element_literal() -> None:
    tree = _parse("OnlyType = Literal['x']")
    (literal,) = extract_literals(tree)
    assert literal.values == ("'x'",)


def test_quotes_bare_identifiers() -> None:
    tree = _parse("DbEngine = Literal[PostgreSQL, MySQL]")
    (literal,) = extract_literals(tree)
    assert literal.values == ("'PostgreSQL'", "'MySQL'")


def test_ignores_non_literal_assignments() -> None:
    tree = _parse(
        """
        StatusType = Literal['a']
        NotALiteral = int
        X = 1
        """
    )
    literals = extract_literals(tree)
    assert [lit.name for lit in literals] == ["StatusType"]


def test_handles_typing_literal_prefix() -> None:
    tree = _parse("StatusType = typing.Literal['a', 'b']")
    (literal,) = extract_literals(tree)
    assert literal.values == ("'a'", "'b'")
