"""Read ``client.py`` to associate input/output TypedDicts with boto3 methods.

The old ``annotate_boto3_classes.py`` did this with a regex over the generated
output file. We do it with :mod:`ast` over the stub ``client.py`` before any
emission happens, so annotations become part of the IR rather than a
post-processing pass.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True, slots=True)
class MethodRole:
    fn_name: str
    role: Literal["input", "output"]


def extract_method_roles(tree: ast.Module) -> dict[str, MethodRole]:
    """Return ``{class_name: MethodRole(fn_name, role)}`` for every boto3 method.

    Matches the canonical stub shape:

    .. code-block:: python

       def foo(self, **kwargs: Unpack[FooRequestTypeDef]) -> FooResponseTypeDef:
           ...

    Works regardless of decorators, overloads, or multi-line signatures —
    :mod:`ast` handles layout for us, which is why we moved off regex.
    """
    roles: dict[str, MethodRole] = {}
    for class_def in _iter_client_classes(tree):
        for method in _iter_methods(class_def):
            pair = _extract_input_output(method)
            if pair is None:
                continue
            input_name, output_name, fn_name = pair
            # Collisions are theoretically possible (same TypedDict reused across
            # methods). Keep the first occurrence so output is stable.
            roles.setdefault(input_name, MethodRole(fn_name=fn_name, role="input"))
            roles.setdefault(output_name, MethodRole(fn_name=fn_name, role="output"))
    return roles


def _iter_client_classes(tree: ast.Module) -> list[ast.ClassDef]:
    return [node for node in tree.body if isinstance(node, ast.ClassDef)]


def _iter_methods(class_def: ast.ClassDef) -> list[ast.FunctionDef]:
    return [item for item in class_def.body if isinstance(item, ast.FunctionDef)]


def _extract_input_output(method: ast.FunctionDef) -> tuple[str, str, str] | None:
    """Return ``(input_typedef_name, output_typedef_name, method_name)`` if matched."""
    kwargs = method.args.kwarg
    if kwargs is None or kwargs.annotation is None:
        return None
    input_name = _unpack_inner_name(kwargs.annotation)
    if input_name is None:
        return None
    output_name = _simple_name(method.returns)
    if output_name is None:
        return None
    return input_name, output_name, method.name


def _unpack_inner_name(node: ast.expr) -> str | None:
    """Return ``X`` when ``node`` is ``Unpack[X]``, else ``None``."""
    if not isinstance(node, ast.Subscript):
        return None
    if not (isinstance(node.value, ast.Name) and node.value.id == "Unpack"):
        return None
    return _simple_name(node.slice)


def _simple_name(node: ast.expr | None) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    return None
