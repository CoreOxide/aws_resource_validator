"""Extract Pydantic-model IR from a stub's ``type_defs.py``.

Produces a tuple of :class:`~.ClassIR` plus a tuple of
:class:`~.UnionAliasIR` in the same order they were defined in the source.
Preserving order keeps generator output diff-stable and avoids forward-ref
issues (the stubs are carefully ordered so each type is defined before use).
"""

from __future__ import annotations

import ast
import keyword
from collections.abc import Mapping

from aws_resource_validator.generator.common.logging import get_logger
from aws_resource_validator.generator.pipeline_b.model_ir import ClassIR, FieldIR, UnionAliasIR
from aws_resource_validator.generator.pipeline_b.type_map import has_typeddict_base
from aws_resource_validator.generator.pipeline_b.type_resolver import TypeResolver

_logger = get_logger(__name__)

_EVENT_STREAM_MARKER = "EventStream"
_TYPEDDICT_BASE = "TypedDict"
_PY_KEYWORDS = frozenset(keyword.kwlist) | frozenset(keyword.softkwlist)


def extract_items(
    tree: ast.Module,
    type_map: Mapping[str, str],
    resolver: TypeResolver | None = None,
) -> tuple[ClassIR | UnionAliasIR, ...]:
    """Walk ``tree`` once; return classes and aliases in source order.

    Preserving source order is what prevents ``NameError`` at import time:
    the upstream stubs are deliberately topologically sorted so each type is
    defined before use, and we must faithfully reproduce that ordering.
    """
    resolver = resolver or TypeResolver()
    items: list[ClassIR | UnionAliasIR] = []

    for node in tree.body:
        if isinstance(node, ast.ClassDef) and has_typeddict_base(node):
            items.append(_extract_class(node, type_map, resolver))
        elif isinstance(node, ast.Assign) and len(node.targets) == 1:
            alias = _try_extract_alias(node, type_map, resolver)
            if alias is not None:
                items.append(alias)
                continue
            typeddict_cls = _try_extract_functional_typeddict(node, type_map, resolver)
            if typeddict_cls is not None:
                items.append(typeddict_cls)
    return tuple(items)


# ------------------------------------------------------------------ class form


def _extract_class(
    node: ast.ClassDef,
    type_map: Mapping[str, str],
    resolver: TypeResolver,
) -> ClassIR:
    sanitized = type_map.get(node.name, node.name)
    fields: list[FieldIR] = []
    for item in node.body:
        if not isinstance(item, ast.AnnAssign) or not isinstance(item.target, ast.Name):
            continue
        event_inner = _event_stream_inner(item.annotation, type_map, resolver)
        if event_inner is not None:
            return ClassIR(name=sanitized, base=f"EventStream[{event_inner}]")
        fields.append(_build_field(item.target.id, item.annotation, type_map, resolver))
    return ClassIR(name=sanitized, fields=tuple(fields))


def _event_stream_inner(
    annotation: ast.expr,
    type_map: Mapping[str, str],
    resolver: TypeResolver,
) -> str | None:
    if (
        isinstance(annotation, ast.Subscript)
        and isinstance(annotation.value, ast.Name)
        and annotation.value.id == _EVENT_STREAM_MARKER
    ):
        return resolver.resolve(annotation.slice, type_map)
    return None


# ---------------------------------------------------------------- functional form


def _try_extract_functional_typeddict(
    node: ast.Assign,
    type_map: Mapping[str, str],
    resolver: TypeResolver,
) -> ClassIR | None:
    """Handle ``Name = TypedDict('Name', {'field': Type, ...})``."""
    target = node.targets[0]
    if not isinstance(target, ast.Name):
        return None
    call = node.value
    if (
        not isinstance(call, ast.Call)
        or not isinstance(call.func, ast.Name)
        or call.func.id != _TYPEDDICT_BASE
    ):
        return None
    if len(call.args) < 2 or not isinstance(call.args[1], ast.Dict):
        return None
    sanitized = type_map.get(target.id, target.id)
    fields: list[FieldIR] = []
    for key, value in zip(call.args[1].keys, call.args[1].values, strict=False):
        if isinstance(key, ast.Constant) and isinstance(key.value, str):
            fields.append(_build_field(key.value, value, type_map, resolver))
    return ClassIR(name=sanitized, fields=tuple(fields))


# ------------------------------------------------------------------ aliases


def _try_extract_alias(
    node: ast.Assign,
    type_map: Mapping[str, str],
    resolver: TypeResolver,
) -> UnionAliasIR | None:
    target = node.targets[0]
    if not isinstance(target, ast.Name):
        return None
    # Only Union[...] / pipe unions count as aliases; Literal aliases belong
    # to literal_extractor and TypedDict calls to the functional-form path.
    if not _is_union_alias(node.value):
        return None
    sanitized = type_map.get(target.id, target.id)
    expression = resolver.resolve(node.value, type_map)
    return UnionAliasIR(name=sanitized, expression=expression)


def _is_union_alias(value: ast.expr) -> bool:
    if isinstance(value, ast.Subscript) and isinstance(value.value, ast.Name):
        return value.value.id == "Union"
    return isinstance(value, ast.BinOp) and isinstance(value.op, ast.BitOr)


# ------------------------------------------------------------------ fields


def _build_field(
    field_name: str,
    annotation_node: ast.expr,
    type_map: Mapping[str, str],
    resolver: TypeResolver,
) -> FieldIR:
    annotation = resolver.resolve(annotation_node, type_map)
    required = not annotation.startswith("Optional[")
    # Required fields get no default; optional get ``None``.
    default_expr = None if required else "None"
    py_name = _safe_field_name(field_name)
    return FieldIR(
        name=field_name,
        py_name=py_name,
        annotation=annotation,
        required=required,
        default_expr=default_expr,
    )


def _safe_field_name(name: str) -> str:
    """Return a Python-identifier-safe version of a wire field name.

    * Keywords and soft keywords (``or``, ``lambda``, ``match``, ``case``)
      get a trailing underscore.
    * Names with characters invalid in identifiers (e.g. hyphenated keys
      like ``detail-type``) have those characters replaced with underscores
      and are additionally suffixed to avoid colliding with real fields.
    * The emitter detects that ``py_name != name`` and adds
      ``Field(alias=name)`` so the wire format is unchanged.
    """
    if name in _PY_KEYWORDS:
        return f"{name}_"
    if name.isidentifier():
        return name
    sanitized = "".join(ch if ch.isalnum() or ch == "_" else "_" for ch in name)
    if not sanitized or not sanitized[0].isalpha():
        sanitized = f"field_{sanitized.lstrip('_')}"
    return f"{sanitized}_"
