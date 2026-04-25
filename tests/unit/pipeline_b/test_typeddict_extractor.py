"""Tests for :mod:`aws_resource_validator.generator.pipeline_b.typeddict_extractor`."""

from __future__ import annotations

import ast
import textwrap

from aws_resource_validator.generator.pipeline_b.model_ir import ClassIR, UnionAliasIR
from aws_resource_validator.generator.pipeline_b.type_map import build_type_map
from aws_resource_validator.generator.pipeline_b.typeddict_extractor import (
    _safe_field_name,
    extract_items,
)


def _parse(source: str) -> ast.Module:
    return ast.parse(textwrap.dedent(source))


def _classes_and_aliases(tree: ast.Module) -> tuple[list[ClassIR], list[UnionAliasIR]]:
    items = extract_items(tree, build_type_map(tree))
    return (
        [it for it in items if isinstance(it, ClassIR)],
        [it for it in items if isinstance(it, UnionAliasIR)],
    )


class TestClassExtraction:
    def test_simple_typeddict(self) -> None:
        tree = _parse(
            """
            class TagTypeDef(TypedDict):
                Key: str
                Value: NotRequired[str]
            """
        )
        classes, _ = _classes_and_aliases(tree)
        assert len(classes) == 1
        cls = classes[0]
        assert cls.name == "TagTypeDef"
        assert cls.base == "BaseValidatorModel"
        assert [f.name for f in cls.fields] == ["Key", "Value"]
        assert cls.fields[0].required is True
        assert cls.fields[1].required is False
        assert cls.fields[1].default_expr == "None"

    def test_functional_typeddict_form(self) -> None:
        tree = _parse(
            """
            EventTypeDef = TypedDict(
                "EventTypeDef",
                {"source": str, "detail-type": str},
            )
            """
        )
        classes, _ = _classes_and_aliases(tree)
        assert len(classes) == 1
        cls = classes[0]
        # "detail-type" has no valid Python identifier — py_name must differ.
        field_names = [(f.name, f.py_name) for f in cls.fields]
        assert ("detail-type", "detail_type_") in field_names

    def test_event_stream_class_has_no_fields(self) -> None:
        tree = _parse(
            """
            class EventResponseTypeDef(TypedDict):
                stream: EventStream[FooEvent]
            """
        )
        classes, _ = _classes_and_aliases(tree)
        assert classes[0].base == "EventStream[FooEvent]"
        assert classes[0].fields == ()


class TestAliasExtraction:
    def test_subscript_union_alias(self) -> None:
        tree = _parse(
            """
            class DummyTypeDef(TypedDict):
                pass

            BlobTypeDef = Union[str, bytes, IO[Any]]
            """
        )
        _, aliases = _classes_and_aliases(tree)
        assert len(aliases) == 1
        assert aliases[0].name == "BlobTypeDef"
        assert "IO[Any]" in aliases[0].expression
        # Brackets must be balanced — the old generator sometimes lost the final ].
        assert aliases[0].expression.count("[") == aliases[0].expression.count("]")


class TestSourceOrdering:
    def test_items_preserve_source_order(self) -> None:
        tree = _parse(
            """
            BlobTypeDef = Union[str, bytes]

            class UsesBlobTypeDef(TypedDict):
                payload: BlobTypeDef
            """
        )
        items = extract_items(tree, build_type_map(tree))
        # The alias must come first so the class that references it resolves.
        assert items[0].name == "BlobTypeDef"
        assert items[1].name == "UsesBlobTypeDef"


class TestSafeFieldName:
    def test_keyword_gets_trailing_underscore(self) -> None:
        assert _safe_field_name("or") == "or_"
        assert _safe_field_name("lambda") == "lambda_"

    def test_hyphenated_name_is_sanitized(self) -> None:
        assert _safe_field_name("detail-type") == "detail_type_"

    def test_leading_digit_is_prefixed(self) -> None:
        assert _safe_field_name("1abc") == "field_1abc_"

    def test_plain_identifier_unchanged(self) -> None:
        assert _safe_field_name("Key") == "Key"
