"""Botocore-backed lookup from ``(struct_shape, member)`` to pattern-bearing target shape.

The ``mypy_boto3_*`` stubs that feed Pipeline B do not preserve the original
botocore shape name of each field — a member is just annotated as ``str``.
To decorate string fields with an AWS regex we need the mapping from a
TypedDict's member name to its target string shape. That mapping is trivially
derivable from the installed ``botocore`` package's service model, which is
already a transitive dependency via ``boto3``.

Loading is best-effort and lazily cached per stub service. Any failure
(missing service, malformed shape) yields an empty lookup and a single
warning log line; the extractor then simply emits today's output for that
service. This keeps rollout per-service — if botocore is stale, Pipeline B
does not break.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import cache
from typing import TYPE_CHECKING

from aws_resource_validator.generator.common.logging import get_logger

if TYPE_CHECKING:
    from botocore.model import ServiceModel

_logger = get_logger(__name__)

_TYPEDEF_SUFFIX = "TypeDef"


@dataclass(frozen=True, slots=True)
class FieldPatternLookup:
    """Map ``(struct_shape, member_name)`` to scalar / list-member pattern shapes.

    Values are ``(scalar_target, list_member_target)`` pairs. Either entry is
    ``None`` when the target doesn't carry a regex; the all-``None`` pair
    means the field is not decorated.
    """

    _entries: dict[tuple[str, str], tuple[str | None, str | None]]

    def for_field(
        self, typeddict_class_name: str, field_wire_name: str
    ) -> tuple[str | None, str | None]:
        struct_name = _strip_typedef_suffix(typeddict_class_name)
        return self._entries.get((struct_name, field_wire_name), (None, None))

    def is_empty(self) -> bool:
        return not self._entries


_EMPTY_LOOKUP = FieldPatternLookup({})


def _strip_typedef_suffix(name: str) -> str:
    if name.endswith(_TYPEDEF_SUFFIX):
        return name[: -len(_TYPEDEF_SUFFIX)]
    return name


def _botocore_service_name(stub_service: str) -> str:
    """Translate the ``stubs_source`` service id to the botocore service id.

    - ``lambda_`` → ``lambda`` (the trailing ``_`` escapes the Python keyword)
    - ``acm_pca`` → ``acm-pca`` (botocore uses hyphens for multi-word ids)
    """
    return stub_service.removesuffix("_").replace("_", "-")


def _shape_has_pattern(shape: object) -> bool:
    metadata = getattr(shape, "metadata", None)
    if not isinstance(metadata, dict):
        return False
    return bool(metadata.get("pattern"))


def _build_entries(
    model: ServiceModel,
) -> dict[tuple[str, str], tuple[str | None, str | None]]:
    # Deferred import keeps the module itself importable in environments that
    # have no botocore — matches the behaviour of ``get_pattern_map`` below.
    from botocore.model import ListShape, StringShape, StructureShape  # noqa: PLC0415

    entries: dict[tuple[str, str], tuple[str | None, str | None]] = {}
    for shape_name in model.shape_names:
        shape = model.shape_for(shape_name)
        if not isinstance(shape, StructureShape):
            continue
        for member_name, member in shape.members.items():
            scalar_target: str | None = None
            list_target: str | None = None
            if isinstance(member, StringShape) and _shape_has_pattern(member):
                scalar_target = member.name
            elif isinstance(member, ListShape):
                inner = member.member
                if isinstance(inner, StringShape) and _shape_has_pattern(inner):
                    list_target = inner.name
            if scalar_target is not None or list_target is not None:
                entries[(shape.name, member_name)] = (scalar_target, list_target)
    return entries


@cache
def get_pattern_map(stub_service: str) -> FieldPatternLookup:
    """Return a :class:`FieldPatternLookup` for ``stub_service`` (cached).

    A missing botocore service (``UnknownServiceError``) or an absent
    ``botocore`` package logs a single warning and returns an empty lookup —
    callers treat that as "no pattern info for this service" and emit today's
    output unchanged. Any other botocore error is allowed to propagate.
    """
    botocore_name = _botocore_service_name(stub_service)
    try:
        # Deferred: botocore is only needed at pattern-map build time, and
        # importing it conditionally keeps the generator usable without boto3.
        from botocore.exceptions import UnknownServiceError  # noqa: PLC0415
        from botocore.session import Session  # noqa: PLC0415
    except ImportError:
        _logger.warning("botocore not importable; skipping pattern map for %s", stub_service)
        return _EMPTY_LOOKUP

    session = Session()
    try:
        model = session.get_service_model(botocore_name)
    except UnknownServiceError:
        _logger.warning(
            "botocore has no service %r (for stub %r); skipping pattern map",
            botocore_name,
            stub_service,
        )
        return _EMPTY_LOOKUP

    entries = _build_entries(model)
    return FieldPatternLookup(entries)
