"""Map original type names to the sanitized names used in emitted classes.

The stubs suffix every TypedDict and Union alias with ``TypeDef``. We preserve
that in the emitted output (it is the documented import path used by
downstream consumers), but the map is still the place to normalize any name
rewrites (e.g. if we ever decide to drop the suffix, only this file changes).
"""

from __future__ import annotations

import ast
from collections.abc import Iterator


def iter_defined_names(tree: ast.Module) -> Iterator[str]:
    """Yield every TypedDict class name and Union alias name in ``tree``."""
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            if has_typeddict_base(node):
                yield node.name
        elif isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            if isinstance(target, ast.Name) and _is_type_alias_value(node.value):
                yield target.id


def has_typeddict_base(node: ast.ClassDef) -> bool:
    """Return True when ``node`` inherits directly from ``TypedDict``."""
    return any(isinstance(b, ast.Name) and b.id == "TypedDict" for b in node.bases)


def build_type_map(tree: ast.Module) -> dict[str, str]:
    """Return a mapping from original name → sanitized name.

    Identity for now; this is the single indirection point if we ever change
    the emitted name policy (e.g. stripping the ``TypeDef`` suffix).
    """
    return {name: name for name in iter_defined_names(tree)}


def _is_type_alias_value(value: ast.expr) -> bool:
    # Union[...] via typing.
    if (
        isinstance(value, ast.Subscript)
        and isinstance(value.value, ast.Name)
        and value.value.id == "Union"
    ):
        return True
    # PEP 604 pipe unions.
    if isinstance(value, ast.BinOp) and isinstance(value.op, ast.BitOr):
        return True
    # TypedDict(functional form).
    return (
        isinstance(value, ast.Call)
        and isinstance(value.func, ast.Name)
        and value.func.id == "TypedDict"
    )
