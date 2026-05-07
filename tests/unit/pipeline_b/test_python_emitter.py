"""Tests for :mod:`aws_resource_validator.generator.pipeline_b.python_emitter`."""

from __future__ import annotations

import ast
from pathlib import Path

from aws_resource_validator.generator.pipeline_b.model_ir import (
    AwsPatternTarget,
    ClassIR,
    FieldIR,
    LiteralAliasIR,
    ServiceModelIR,
    UnionAliasIR,
)
from aws_resource_validator.generator.pipeline_b.python_emitter import (
    build_init_content,
    build_manifest,
    emit_service,
    render_classes,
    render_constants,
)


def _ir() -> ServiceModelIR:
    return ServiceModelIR(
        service="dummy",
        items=(
            ClassIR(
                name="TagTypeDef",
                fields=(
                    FieldIR(name="Key", py_name="Key", annotation="str", required=True, default_expr=None),
                    FieldIR(
                        name="Value",
                        py_name="Value",
                        annotation="Optional[str]",
                        required=False,
                        default_expr="None",
                    ),
                ),
            ),
            UnionAliasIR(name="BlobTypeDef", expression="Union[str, bytes]"),
        ),
        literals=(LiteralAliasIR(name="StatusType", values=("'a'", "'b'")),),
    )


def test_classes_output_is_parseable_python() -> None:
    source = render_classes(_ir())
    ast.parse(source)
    assert "class TagTypeDef(BaseValidatorModel):" in source
    assert "BlobTypeDef = Union[str, bytes]" in source


def test_alias_preserved_in_source_order() -> None:
    ir = ServiceModelIR(
        service="dummy",
        items=(
            UnionAliasIR(name="AliasTypeDef", expression="Union[str, int]"),
            ClassIR(
                name="UsesAliasTypeDef",
                fields=(
                    FieldIR(
                        name="payload",
                        py_name="payload",
                        annotation="AliasTypeDef",
                        required=True,
                        default_expr=None,
                    ),
                ),
            ),
        ),
    )
    source = render_classes(ir)
    alias_pos = source.find("AliasTypeDef = ")
    class_pos = source.find("class UsesAliasTypeDef")
    assert 0 < alias_pos < class_pos


def test_constants_output_contains_literal_aliases() -> None:
    source = render_constants(_ir())
    ast.parse(source)
    # Don't pin the quote style — ``black`` normalizes ' to ".
    assert "StatusType = Literal[" in source
    assert "a" in source and "b" in source


def test_manifest_structure() -> None:
    manifest = build_manifest(_ir(), module="path.to.module")
    assert manifest == {
        "service": "dummy",
        "module": "path.to.module",
        "classes": ["TagTypeDef"],
        "union_aliases": ["BlobTypeDef"],
    }


def test_init_content_reexports_public_names() -> None:
    source = build_init_content(_ir())
    assert "TagTypeDef" in source
    assert "BlobTypeDef" in source
    assert "__all__" in source


def test_emit_service_writes_four_files(tmp_path: Path) -> None:
    artifacts = emit_service(_ir(), tmp_path)
    assert artifacts.classes_file.exists()
    assert artifacts.constants_file.exists()
    assert artifacts.init_file.exists()
    assert artifacts.manifest_file.exists()


def _ir_with_patterns() -> ServiceModelIR:
    return ServiceModelIR(
        service="acm_pca",
        items=(
            ClassIR(
                name="SampleTypeDef",
                fields=(
                    FieldIR(
                        name="Arn",
                        py_name="Arn",
                        annotation="Optional[str]",
                        required=False,
                        default_expr="None",
                        aws_pattern=AwsPatternTarget("AcmPca", "Arn"),
                    ),
                    FieldIR(
                        name="Arns",
                        py_name="Arns",
                        annotation="List[str]",
                        required=True,
                        default_expr=None,
                        aws_pattern=AwsPatternTarget("AcmPca", "Arn", is_list_element=True),
                    ),
                    FieldIR(
                        name="Count",
                        py_name="Count",
                        annotation="Optional[int]",
                        required=False,
                        default_expr="None",
                    ),
                ),
            ),
        ),
    )


def test_classes_output_includes_pattern_imports_and_wraps() -> None:
    source = render_classes(_ir_with_patterns())
    ast.parse(source)
    # Black may wrap the long ``from typing import ...`` onto multiple lines;
    # assert on the symbol presence, not on line layout.
    assert "Annotated," in source or "import Annotated" in source
    assert (
        "from aws_resource_validator.core.pattern_validation import aws_field_pattern as _aws_pattern"
        in source
    )
    # Scalar wrap on Optional[str] — the inner ``str`` becomes Annotated[str, ...].
    assert 'Optional[Annotated[str, _aws_pattern("AcmPca", "Arn")]]' in source
    # List wrap: the whole ``List[str]`` token is rewritten.
    assert 'List[Annotated[str, _aws_pattern("AcmPca", "Arn")]]' in source
    # Untouched field keeps the raw annotation.
    assert "Count: Optional[int] = None" in source


def test_pattern_metadata_does_not_affect_untagged_fields() -> None:
    # Sanity: a field without ``aws_pattern`` must emit exactly the old
    # annotation — no phantom ``Annotated`` wrap.
    source = render_classes(_ir())
    assert "Annotated[str" not in source
