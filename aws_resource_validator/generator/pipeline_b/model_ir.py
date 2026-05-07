"""Intermediate representation between AST extraction and Python emission.

Extractors produce these frozen dataclasses; the emitter renders templates
from them. Keeping reading and writing split means every edge case can be
exercised against the IR directly.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

Role = Literal["input", "output", "internal"]


@dataclass(frozen=True, slots=True)
class AwsPatternTarget:
    """Where to insert the ``Annotated[str, _aws_pattern(...)]`` wrap for a field.

    ``is_list_element`` distinguishes wrapping the field's value (``str``) from
    wrapping the *element* of a list-valued field (``List[str]``). The two
    wraps are mutually exclusive in v1 — a field is either a scalar string or
    a list of strings.
    """

    service: str
    shape_name: str
    is_list_element: bool = False


@dataclass(frozen=True, slots=True)
class FieldIR:
    """A single Pydantic field.

    Attributes:
        name: The original dict key; always emitted verbatim on the wire.
        py_name: The Python identifier to use. Equal to ``name`` unless the
            name clashes with a reserved keyword, in which case the emitter
            appends an underscore and adds ``alias=name`` to :class:`Field`.
        annotation: Fully resolved type expression, e.g.
            ``"Optional[List[TagTypeDef]]"``.
        required: ``True`` if the dict key is required (no ``NotRequired``).
        default_expr: Python source for the default value. ``None`` means
            "no default"; ``"None"`` means "default of literal None".
        aws_pattern: Optional :class:`AwsPatternTarget` telling the emitter
            to wrap the field (or its list element) with an opt-in validator
            that checks the value against an AWS-documented regex / length.
    """

    name: str
    py_name: str
    annotation: str
    required: bool
    default_expr: str | None
    aws_pattern: AwsPatternTarget | None = None


@dataclass(frozen=True, slots=True)
class ClassIR:
    """A Pydantic model to emit."""

    name: str
    base: str = "BaseValidatorModel"
    fields: tuple[FieldIR, ...] = ()
    role: Role = "internal"
    role_fn: str | None = None


@dataclass(frozen=True, slots=True)
class UnionAliasIR:
    """A ``Name = Union[...]`` alias emitted as a module-level assignment."""

    name: str
    expression: str


@dataclass(frozen=True, slots=True)
class LiteralAliasIR:
    """A ``Name = Literal[...]`` alias produced from the stub's ``literals.py``."""

    name: str
    values: tuple[str, ...]
    """Pre-quoted element literals, e.g. ``("'CNAME'", "'A'")``."""


@dataclass(frozen=True, slots=True)
class ServiceModelIR:
    """Everything the emitter needs for one AWS service.

    ``items`` preserves the source order of classes and aliases so forward
    references in the generated module resolve at import time. ``classes``
    and ``union_aliases`` are views of that same content, convenient for
    manifests and cross-cutting tooling.
    """

    service: str
    items: tuple[ClassIR | UnionAliasIR, ...] = ()
    literals: tuple[LiteralAliasIR, ...] = ()

    @property
    def classes(self) -> tuple[ClassIR, ...]:
        return tuple(it for it in self.items if isinstance(it, ClassIR))

    @property
    def union_aliases(self) -> tuple[UnionAliasIR, ...]:
        return tuple(it for it in self.items if isinstance(it, UnionAliasIR))
