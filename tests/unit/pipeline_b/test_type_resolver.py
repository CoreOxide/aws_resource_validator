"""Tests for :mod:`aws_resource_validator.generator.pipeline_b.type_resolver`.

The TypeResolver is the part of Pipeline B where 90% of the previous
generator's bugs lived (missing brackets, stray ``IO[Any][Any]`` expansions,
unquoted Literal identifiers). Every edge case from the old ``replace.zsh``
hack script has a regression test here.
"""

from __future__ import annotations

import ast
from collections.abc import Mapping

import pytest

from aws_resource_validator.generator.pipeline_b.type_resolver import TypeResolver


def _resolve(source: str, type_map: Mapping[str, str] | None = None) -> str:
    node = ast.parse(source, mode="eval").body
    return TypeResolver().resolve(node, type_map or {})


class TestBasicTypes:
    @pytest.mark.parametrize(
        ("source", "expected"),
        [
            ("str", "str"),
            ("int", "int"),
            ("bool", "bool"),
            ("datetime", "datetime"),
            ("None", "None"),
        ],
    )
    def test_names_pass_through(self, source: str, expected: str) -> None:
        assert _resolve(source) == expected


class TestOptionalNormalization:
    """All four ways of spelling "maybe this" must collapse to Optional[T]."""

    @pytest.mark.parametrize(
        "source",
        [
            "Optional[str]",
            "NotRequired[str]",
            "Union[str, None]",
            "str | None",
        ],
    )
    def test_all_optional_sources_normalize(self, source: str) -> None:
        assert _resolve(source) == "Optional[str]"

    def test_nested_not_required_optional_flattens(self) -> None:
        assert _resolve("NotRequired[Optional[str]]") == "Optional[str]"


class TestGenerics:
    def test_list(self) -> None:
        assert _resolve("List[Tag]") == "List[Tag]"

    def test_sequence_is_rewritten_to_list(self) -> None:
        assert _resolve("Sequence[Tag]") == "List[Tag]"

    def test_mapping_is_rewritten_to_dict(self) -> None:
        assert _resolve("Mapping[str, int]") == "Dict[str, int]"

    def test_dict(self) -> None:
        assert _resolve("Dict[str, List[int]]") == "Dict[str, List[int]]"


class TestLiteral:
    def test_single_string_element(self) -> None:
        assert _resolve("Literal['CNAME']") == "Literal['CNAME']"

    def test_multiple_string_elements(self) -> None:
        assert _resolve("Literal['A', 'B']") == "Literal['A', 'B']"

    def test_bare_identifier_gets_quoted(self) -> None:
        # Regression: PostgreSQL appeared bare in mypy_boto3; must be quoted
        # or Python treats it as an undefined name at import time.
        assert _resolve("Literal[PostgreSQL]") == "Literal['PostgreSQL']"


class TestUnion:
    def test_union_with_three_types_preserves_all_three(self) -> None:
        # Regression: the old generator produced "Union[str, bytes, IO[Any]"
        # (missing ]). Must never happen again.
        result = _resolve("Union[str, bytes, IO[Any]]")
        assert result.count("[") == result.count("]")
        assert "str" in result
        assert "bytes" in result
        assert "IO[Any]" in result

    def test_single_member_union_unwraps(self) -> None:
        assert _resolve("Union[str]") == "str"

    def test_pipe_union_with_none_becomes_optional(self) -> None:
        assert _resolve("str | None") == "Optional[str]"

    def test_pipe_union_of_three(self) -> None:
        assert _resolve("str | bytes | None") == "Optional[Union[bytes, str]]"


class TestIOHandling:
    """Regression tests for IO[Any][Any] expansion bug."""

    def test_bare_io_expands_to_io_any(self) -> None:
        assert _resolve("IO") == "IO[Any]"

    def test_subscripted_io_is_not_double_expanded(self) -> None:
        # Previous generator turned IO[Any] into IO[Any][Any].
        assert _resolve("IO[Any]") == "IO[Any]"

    def test_io_inside_union(self) -> None:
        result = _resolve("Union[str, IO[Any]]")
        assert result == "Union[IO[Any], str]"


class TestTypeMap:
    def test_name_rewriting(self) -> None:
        assert _resolve("FooTypeDef", {"FooTypeDef": "Foo"}) == "Foo"

    def test_rewriting_propagates_through_generics(self) -> None:
        assert _resolve("List[FooTypeDef]", {"FooTypeDef": "Foo"}) == "List[Foo]"


class TestFallbacks:
    def test_unknown_node_returns_any(self) -> None:
        # Constructing a synthetic ast.Lambda, which the resolver doesn't handle.
        node = ast.Lambda(
            args=ast.arguments(
                posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]
            ),
            body=ast.Constant(value=None),
        )
        assert TypeResolver().resolve(node, {}) == "Any"

    def test_none_node_returns_any(self) -> None:
        assert TypeResolver().resolve(None, {}) == "Any"
