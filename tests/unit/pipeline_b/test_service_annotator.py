"""Tests for :mod:`aws_resource_validator.generator.pipeline_b.service_annotator`."""

from __future__ import annotations

import ast
import textwrap

from aws_resource_validator.generator.pipeline_b.service_annotator import extract_method_roles


def _parse(source: str) -> ast.Module:
    return ast.parse(textwrap.dedent(source))


def test_extracts_input_and_output_typedefs() -> None:
    tree = _parse(
        """
        class Client:
            def get_certificate(self, **kwargs: Unpack[GetCertificateRequestTypeDef]) -> GetCertificateResponseTypeDef:
                ...
        """
    )
    roles = extract_method_roles(tree)
    assert roles["GetCertificateRequestTypeDef"].role == "input"
    assert roles["GetCertificateRequestTypeDef"].fn_name == "get_certificate"
    assert roles["GetCertificateResponseTypeDef"].role == "output"


def test_ignores_methods_without_unpack() -> None:
    tree = _parse(
        """
        class Client:
            def close(self) -> None:
                ...
        """
    )
    assert extract_method_roles(tree) == {}


def test_handles_multiple_methods() -> None:
    tree = _parse(
        """
        class Client:
            def a(self, **kwargs: Unpack[ARequestTypeDef]) -> AResponseTypeDef: ...
            def b(self, **kwargs: Unpack[BRequestTypeDef]) -> BResponseTypeDef: ...
        """
    )
    roles = extract_method_roles(tree)
    assert roles["ARequestTypeDef"].fn_name == "a"
    assert roles["BRequestTypeDef"].fn_name == "b"


def test_handles_decorated_methods() -> None:
    # Regression: the old regex-based annotator missed decorated methods.
    tree = _parse(
        """
        class Client:
            @overload
            def x(self, **kwargs: Unpack[XRequestTypeDef]) -> XResponseTypeDef:
                ...
        """
    )
    roles = extract_method_roles(tree)
    assert "XRequestTypeDef" in roles
