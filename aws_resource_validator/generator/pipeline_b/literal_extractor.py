"""Extract ``Literal[...]`` aliases from a stub's ``literals.py``."""

from __future__ import annotations

import ast

from aws_resource_validator.generator.pipeline_b.model_ir import LiteralAliasIR
from aws_resource_validator.generator.pipeline_b.type_resolver import format_literal_element


def extract_literals(tree: ast.Module) -> tuple[LiteralAliasIR, ...]:
    """Return every top-level ``Name = Literal[...]`` assignment in ``tree``."""
    aliases: list[LiteralAliasIR] = []
    for node in tree.body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if not isinstance(target, ast.Name):
            continue
        if not isinstance(node.value, ast.Subscript) or not _is_literal_subscript(node.value):
            continue
        slice_node = node.value.slice
        elements = slice_node.elts if isinstance(slice_node, ast.Tuple) else [slice_node]
        values = tuple(format_literal_element(e) for e in elements)
        if values:
            aliases.append(LiteralAliasIR(name=target.id, values=values))
    return tuple(aliases)


def _is_literal_subscript(value: ast.Subscript) -> bool:
    sub = value.value
    if isinstance(sub, ast.Name) and sub.id == "Literal":
        return True
    # typing.Literal
    if isinstance(sub, ast.Attribute) and isinstance(sub.value, ast.Name):
        return sub.value.id == "typing" and sub.attr == "Literal"
    return False
