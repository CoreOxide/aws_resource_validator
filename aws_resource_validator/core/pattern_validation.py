"""Opt-in regex/length validation for generated Pydantic fields.

The Pipeline B emitter wraps pattern-backed string fields with
``Annotated[str, aws_field_pattern(service, shape_name)]``. At runtime the
returned :class:`~pydantic.AfterValidator` is a no-op unless the caller
explicitly opts in by passing ``context={"aws_validate_patterns": True}`` to
:meth:`~pydantic.BaseModel.model_validate` (or :meth:`model_validate_json`).
This keeps default ``Cls(**data)`` construction zero-overhead and backward
compatible with every existing consumer of the generated models.

v1 coverage is deliberately narrow: only fields whose annotation is exactly
``str``, ``Optional[str]``, ``List[str]``, or ``Optional[List[str]]`` are
wrapped. Map values (``Dict[str, PatternedShape]``), ``Union[str, ...]``, and
nested container types are not decorated even when their target shape carries
a regex. Expanding the whitelist requires AST-aware rewriting in the
extractor.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import AfterValidator
from pydantic_core import PydanticCustomError

if TYPE_CHECKING:
    from pydantic import ValidationInfo

    from aws_resource_validator.core.api_object import APIObject

_CTX_KEY = "aws_validate_patterns"

# Shared across every generated module so that a shape referenced by N fields
# (common in large services) reuses a single ``AfterValidator`` instance.
_VALIDATOR_CACHE: dict[tuple[str, str], AfterValidator] = {}


def aws_field_pattern(service: str, shape_name: str) -> AfterValidator:
    """Return an :class:`~pydantic.AfterValidator` keyed on ``(service, shape_name)``.

    The validator is a no-op unless the caller passes
    ``context={"aws_validate_patterns": True}`` to
    :meth:`~pydantic.BaseModel.model_validate`. When active, the value is
    checked against :class:`~aws_resource_validator.core.api_object.APIObject`
    — which covers the regex pattern as well as any declared length bounds —
    and a :class:`~pydantic_core.PydanticCustomError` is raised on mismatch.

    Unknown service or shape names resolve to a permissive no-op so that a
    stale generator output never breaks a consumer's validation call.

    Note: :class:`~aws_resource_validator.core.base_validator_model.BaseValidatorModel`
    is configured with ``extra="allow"``, so keys that are not declared fields
    (e.g. from a typo or a newer boto3 release) bypass this validator
    entirely — they are silently preserved rather than rejected.
    """
    key = (service, shape_name)
    cached = _VALIDATOR_CACHE.get(key)
    if cached is not None:
        return cached

    # Resolved on the first opt-in call and reused thereafter. ``None`` before
    # resolution is ambiguous, so track the looked-up state with a separate
    # flag rather than a sentinel; ``nonlocal`` mutates the closure in place.
    api_object: APIObject | None = None
    resolved = False

    def _check(value: str, info: ValidationInfo) -> str:
        nonlocal api_object, resolved
        ctx = info.context
        if ctx is None or not (isinstance(ctx, dict) and ctx.get(_CTX_KEY)):
            return value
        if not resolved:
            # Deferred: ``class_definitions`` is a ~15k-line module that every
            # generated ``*_classes.py`` transitively imports; loading it here
            # (rather than at module scope) preserves zero-overhead-by-default.
            from aws_resource_validator.class_definitions import class_registry  # noqa: PLC0415

            try:
                api_object = class_registry[service][shape_name]
            except KeyError:
                api_object = None
            resolved = True
        if api_object is None or api_object.validate(value):
            return value
        raise PydanticCustomError(
            "aws_pattern",
            "value does not match AWS shape {shape} in service {service}",
            {"service": service, "shape": shape_name, "value": value},
        )

    validator = AfterValidator(_check)
    _VALIDATOR_CACHE[key] = validator
    return validator
