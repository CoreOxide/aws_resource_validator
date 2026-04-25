"""Convert AST type-annotation nodes into Pydantic-friendly strings.

Each AST variant is handled by a dedicated method dispatched through the
``_dispatch`` class attribute, so every branch is independently testable.
"""

from __future__ import annotations

import ast
from collections.abc import Callable, Mapping
from typing import ClassVar

from aws_resource_validator.generator.common.logging import get_logger

_logger = get_logger(__name__)

# Types the stubs refer to that we do not emit verbatim. Sequence/Mapping
# collapse to List/Dict; PEP 585 lowercase builtins are rewritten to their
# ``typing`` counterparts so they never shadow a field name that collides
# with a builtin (regression: a stub with a field named ``list`` annotated
# ``list[dict[str, Any]]`` would otherwise fail at class-body evaluation).
_TYPING_ALIASES: Mapping[str, str] = {
    "Sequence": "List",
    "Mapping": "Dict",
    "list": "List",
    "dict": "Dict",
    "set": "Set",
    "frozenset": "FrozenSet",
    "tuple": "Tuple",
    "type": "Type",
}
# Bare identifiers that must be expanded to a concrete type when used
# outside of a subscript (e.g. ``IO`` alone is meaningless in a type hint).
_BARE_IDENTIFIER_EXPANSIONS: Mapping[str, str] = {
    "IO": "IO[Any]",
    "TypedDict": "Dict[str, Any]",
}


class TypeResolver:
    """Resolve AST annotations to Python-source type strings.

    A ``TypeResolver`` is stateless; the ``type_map`` is threaded through on
    every call so the same resolver can be shared across services if desired.
    """

    def __init__(self, *, context: str = "") -> None:
        self._context = context

    # ------------------------------------------------------------------ API

    def resolve(self, node: ast.expr | None, type_map: Mapping[str, str]) -> str:
        """Return a Python source expression for the annotation ``node``."""
        if node is None:
            return "Any"
        handler = self._dispatch.get(type(node), TypeResolver._resolve_unknown)
        return handler(self, node, type_map)

    # ---------------------------------------------------------------- helpers

    def _resolve_name(self, node: ast.Name, type_map: Mapping[str, str]) -> str:
        name = type_map.get(node.id, node.id)
        if name in _BARE_IDENTIFIER_EXPANSIONS:
            return _BARE_IDENTIFIER_EXPANSIONS[name]
        if name == "NotRequired":
            _logger.warning("%s: bare NotRequired outside Subscript; treating as Optional[Any].", self._context)
            return "Optional[Any]"
        return name

    def _resolve_constant(self, node: ast.Constant, type_map: Mapping[str, str]) -> str:
        if node.value is None:
            return "None"
        if isinstance(node.value, str):
            # Forward reference in a quoted annotation — treat as a type name.
            return type_map.get(node.value, node.value)
        return repr(node.value)

    def _resolve_attribute(self, node: ast.Attribute, type_map: Mapping[str, str]) -> str:
        if isinstance(node.value, ast.Name):
            if node.value.id in {"typing", "collections.abc"}:
                return node.attr
            if node.value.id == "datetime" and node.attr == "datetime":
                return "datetime"
        base = self.resolve(node.value, type_map)
        if base in {"Any", "None"} or base.startswith("Optional["):
            _logger.warning("%s: attribute access on %s; using Any.", self._context, base)
            return "Any"
        return f"{base}.{node.attr}"

    def _resolve_subscript(self, node: ast.Subscript, type_map: Mapping[str, str]) -> str:
        value = node.value

        if isinstance(value, ast.Name) and value.id == "NotRequired":
            inner = self.resolve(node.slice, type_map)
            return inner if inner.startswith("Optional[") else f"Optional[{inner}]"

        base = self._resolve_subscript_base(value, type_map)
        if base in {"Any", "None"} or base.startswith("Optional["):
            _logger.warning("%s: cannot subscript %s; using Any.", self._context, base)
            return "Any"

        if base == "Literal":
            return self._resolve_literal(node.slice)

        if base == "Mapping":
            return self._resolve_mapping(node.slice, type_map)
        if base in _TYPING_ALIASES:
            base = _TYPING_ALIASES[base]

        if base == "Union":
            return self._resolve_union_subscript(node.slice, type_map)

        inner = self.resolve(node.slice, type_map)
        return f"{base}[{inner}]"

    def _resolve_subscript_base(self, value: ast.expr, type_map: Mapping[str, str]) -> str:
        """Resolve the ``X`` in ``X[...]`` without auto-expanding bare names.

        When ``IO[Any]`` appears in the AST, the Name ``IO`` must not be
        expanded to ``IO[Any]`` by :meth:`_resolve_name` because the outer
        subscript is already providing the parameter.
        """
        if isinstance(value, ast.Name):
            return type_map.get(value.id, value.id)
        return self.resolve(value, type_map)

    def _resolve_literal(self, slice_node: ast.expr) -> str:
        elements = slice_node.elts if isinstance(slice_node, ast.Tuple) else [slice_node]
        values = [format_literal_element(e) for e in elements]
        if not values:
            _logger.warning("%s: Literal with no elements; falling back to Literal[Any].", self._context)
            return "Literal[Any]"
        return f"Literal[{', '.join(values)}]"

    def _resolve_mapping(self, slice_node: ast.expr, type_map: Mapping[str, str]) -> str:
        if isinstance(slice_node, ast.Tuple) and len(slice_node.elts) == 2:
            k = self.resolve(slice_node.elts[0], type_map)
            v = self.resolve(slice_node.elts[1], type_map)
            return f"Dict[{k}, {v}]"
        _logger.warning("%s: Mapping with non-tuple slice; falling back to Dict[Any, Any].", self._context)
        return "Dict[Any, Any]"

    def _resolve_union_subscript(self, slice_node: ast.expr, type_map: Mapping[str, str]) -> str:
        if isinstance(slice_node, ast.Tuple):
            parts = [self.resolve(e, type_map) for e in slice_node.elts]
        else:
            parts = [self.resolve(slice_node, type_map)]
        return _compose_union(parts)

    def _resolve_tuple(self, node: ast.Tuple, type_map: Mapping[str, str]) -> str:
        return ", ".join(self.resolve(e, type_map) for e in node.elts)

    def _resolve_binop(self, node: ast.BinOp, type_map: Mapping[str, str]) -> str:
        if not isinstance(node.op, ast.BitOr):
            return self._resolve_unknown(node, type_map)
        left = self.resolve(node.left, type_map)
        right = self.resolve(node.right, type_map)
        return _compose_union([left, right])

    def _resolve_unknown(self, node: ast.expr, type_map: Mapping[str, str]) -> str:
        _logger.warning("%s: unsupported annotation node %s; using Any.", self._context, type(node).__name__)
        return "Any"

    # Dispatch table mapping AST node type → bound handler.
    # Built as a class attribute so all instances share it.
    _dispatch: ClassVar[dict[type[ast.expr], Callable[..., str]]] = {
        ast.Name: _resolve_name,
        ast.Constant: _resolve_constant,
        ast.Attribute: _resolve_attribute,
        ast.Subscript: _resolve_subscript,
        ast.Tuple: _resolve_tuple,
        ast.BinOp: _resolve_binop,
    }


# ------------------------------------------------------------------ pure helpers


def format_literal_element(node: ast.expr) -> str:
    """Format a single element inside ``Literal[...]``.

    Bare identifiers (like ``PostgreSQL``) must be quoted because they would
    be interpreted as forward references otherwise. Constants are passed
    through :func:`repr` so strings keep their quotes.
    """
    if isinstance(node, ast.Name):
        return f"'{node.id}'"
    if isinstance(node, ast.Constant):
        return repr(node.value)
    return "'UNPARSEABLE_LITERAL'"


def _compose_union(parts: list[str]) -> str:
    """Collapse a list of type strings into one canonical Union/Optional.

    * Flattens nested ``Union[...]`` and ``Optional[...]`` members.
    * Deduplicates.
    * Returns ``Optional[X]`` when ``None`` is present with one real type,
      ``Union[X, Y]`` otherwise, and the bare type when only one remains.
    """
    collected: set[str] = set()
    for raw in parts:
        collected.update(_flatten_union_member(raw.strip()))
    has_none = "None" in collected
    non_none = sorted(t for t in collected if t != "None")
    if not non_none:
        return "None"
    inner = non_none[0] if len(non_none) == 1 else f"Union[{', '.join(non_none)}]"
    return f"Optional[{inner}]" if has_none else inner


def _flatten_union_member(part: str) -> list[str]:
    if part.startswith("Optional[") and part.endswith("]"):
        return [*_flatten_union_member(part[len("Optional["):-1]), "None"]
    if part.startswith("Union[") and part.endswith("]"):
        inner = part[len("Union["):-1]
        return [piece.strip() for piece in _split_top_level_commas(inner)]
    return [part]


def _split_top_level_commas(text: str) -> list[str]:
    """Split ``text`` on commas that are not nested inside brackets."""
    parts: list[str] = []
    depth = 0
    start = 0
    for index, char in enumerate(text):
        if char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
        elif char == "," and depth == 0:
            parts.append(text[start:index])
            start = index + 1
    parts.append(text[start:])
    return parts
