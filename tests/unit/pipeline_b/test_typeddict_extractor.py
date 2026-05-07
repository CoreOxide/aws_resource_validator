"""Tests for :mod:`aws_resource_validator.generator.pipeline_b.typeddict_extractor`."""

from __future__ import annotations

import ast
import textwrap

from aws_resource_validator.generator.pipeline_b.model_ir import AwsPatternTarget, ClassIR, UnionAliasIR
from aws_resource_validator.generator.pipeline_b.shape_pattern_map import FieldPatternLookup
from aws_resource_validator.generator.pipeline_b.type_map import build_type_map
from aws_resource_validator.generator.pipeline_b.typeddict_extractor import (
    PatternContext,
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


class TestPatternTagging:
    """Exercise ``_resolve_aws_pattern`` through ``extract_items``.

    Uses a hand-constructed :class:`FieldPatternLookup` so the test is isolated
    from whatever botocore happens to ship — we only care that the extractor
    correctly threads ``(scalar_target, list_target)`` tuples into
    ``FieldIR.aws_pattern`` based on the annotation shape.
    """

    _SOURCE = """
    class SampleTypeDef(TypedDict):
        Scalar: str
        OptScalar: NotRequired[str]
        Listed: List[str]
        OptListed: NotRequired[List[str]]
        NotAString: int
        StrayDict: Dict[str, str]
    """

    def _tagged(
        self,
        lookup_entries: dict[tuple[str, str], tuple[str | None, str | None]],
    ) -> dict[str, AwsPatternTarget | None]:
        tree = _parse(self._SOURCE)
        ctx = PatternContext(lookup=FieldPatternLookup(lookup_entries), service="Fake")
        items = extract_items(tree, build_type_map(tree), pattern_context=ctx)
        cls = items[0]
        assert isinstance(cls, ClassIR)
        return {f.name: f.aws_pattern for f in cls.fields}

    def test_scalar_string_tagged(self) -> None:
        tags = self._tagged({("Sample", "Scalar"): ("Arn", None)})
        assert tags["Scalar"] == AwsPatternTarget("Fake", "Arn")

    def test_optional_scalar_tagged(self) -> None:
        tags = self._tagged({("Sample", "OptScalar"): ("Arn", None)})
        assert tags["OptScalar"] == AwsPatternTarget("Fake", "Arn")

    def test_list_of_string_tagged(self) -> None:
        tags = self._tagged({("Sample", "Listed"): (None, "Arn")})
        assert tags["Listed"] == AwsPatternTarget("Fake", "Arn", is_list_element=True)

    def test_optional_list_of_string_tagged(self) -> None:
        tags = self._tagged({("Sample", "OptListed"): (None, "Arn")})
        assert tags["OptListed"] == AwsPatternTarget("Fake", "Arn", is_list_element=True)

    def test_scalar_lookup_with_non_string_annotation_is_skipped(self) -> None:
        # ``NotAString: int`` must never be decorated even if the lookup pairs
        # its wire name with a scalar target — the whitelist is annotation-driven.
        tags = self._tagged({("Sample", "NotAString"): ("Arn", None)})
        assert tags["NotAString"] is None

    def test_list_lookup_on_scalar_annotation_is_skipped(self) -> None:
        # A list-target tag on a scalar-string field is a mismatch — skip it
        # rather than produce a nonsense wrap.
        tags = self._tagged({("Sample", "Scalar"): (None, "Arn")})
        assert tags["Scalar"] is None

    def test_scalar_lookup_on_list_annotation_is_skipped(self) -> None:
        tags = self._tagged({("Sample", "Listed"): ("Arn", None)})
        assert tags["Listed"] is None

    def test_complex_annotation_never_tagged(self) -> None:
        # ``Dict[str, str]`` is outside the v1 whitelist even though it contains
        # ``str`` tokens — an extractor that tagged this would produce a wrap
        # that corrupts the dict's value type.
        tags = self._tagged({("Sample", "StrayDict"): ("Arn", None)})
        assert tags["StrayDict"] is None

    def test_absent_lookup_leaves_fields_untagged(self) -> None:
        tags = self._tagged({})
        assert all(tag is None for tag in tags.values())

    def test_none_pattern_context_leaves_fields_untagged(self) -> None:
        tree = _parse(self._SOURCE)
        items = extract_items(tree, build_type_map(tree), pattern_context=None)
        cls = items[0]
        assert isinstance(cls, ClassIR)
        assert all(f.aws_pattern is None for f in cls.fields)


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
