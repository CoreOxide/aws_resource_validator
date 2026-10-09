"""Universal Amazon Resource Name (ARN) parser, validator, and builder.

An ARN has the form ``arn:partition:service:region:account-id:resource``.
The resource segment may itself contain ``:`` and ``/`` characters (IAM paths,
S3 object keys, CloudWatch alarm names, Lambda aliases, ...), so naive
``value.split(":")`` code silently breaks. :class:`ARN` splits on at most five
colons and keeps the resource segment intact.

Validation happens in two layers:

1. **Generic ARN grammar** (always on, zero I/O): each component is checked
   against the structural rules every AWS ARN follows. This covers services
   such as IAM, SQS, SNS, and KMS whose botocore models declare no ARN regex.
2. **Botocore shape rules** (opt-in): :meth:`ARN.validate_against` and
   :meth:`ARN.matching_shapes` check the ARN against the ``*Arn`` shapes in
   :mod:`aws_resource_validator.class_definitions`. The registry is loaded
   lazily, so plain parsing never pays its import cost.
"""

from __future__ import annotations

import dataclasses
import re
from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Literal

from aws_resource_validator.core.diagnostics import ValidationResult, diagnose_validation
from aws_resource_validator.core.resolver import get_registry, resolve_service, resolve_shape

if TYPE_CHECKING:
    from pydantic import GetCoreSchemaHandler
    from pydantic_core import CoreSchema

    from aws_resource_validator.core.service import Service

__all__ = ["ARN", "KNOWN_PARTITIONS", "MAX_ARN_LENGTH", "ARNParseError"]

#: Partitions documented by AWS. Unknown but well-formed partitions only warn,
#: so newly launched partitions keep working without a library release.
KNOWN_PARTITIONS: frozenset[str] = frozenset(
    {"aws", "aws-cn", "aws-us-gov", "aws-iso", "aws-iso-b", "aws-iso-e", "aws-iso-f", "aws-eusc"}
)

#: Largest ``max_length`` declared by any botocore ARN shape.
MAX_ARN_LENGTH = 2048

_PARTITION_RE = re.compile(r"aws(-[a-z]+)*")
_SERVICE_RE = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")
_REGION_RE = re.compile(r"[a-z]{2,4}(-[a-z]+)+-\d{1,2}")
_ACCOUNT_RE = re.compile(r"\d{12}")
_RESOURCE_TYPE_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]*")
_CONTROL_CHARS_RE = re.compile(r"[\x00-\x1f\x7f]")
_WHITESPACE_RE = re.compile(r"\s")

# Services whose resource segment is a bare name (no ``type/`` or ``type:`` prefix).
_TYPELESS_SERVICES = frozenset({"sns", "sqs"})


class ARNParseError(ValueError):
    """Raised when a string cannot be decomposed into an ARN, or fails strict validation.

    Attributes:
        value: The offending input string.
        errors: Individual validation failures (empty for structural parse failures).
    """

    def __init__(self, message: str, *, value: str, errors: tuple[str, ...] = ()) -> None:
        super().__init__(message)
        self.value = value
        self.errors = errors


@dataclass(frozen=True, slots=True)
class ARN:
    """An immutable, validated Amazon Resource Name.

    Construct instances with :meth:`parse` or :meth:`build`. Direct
    construction is allowed too; validation runs in ``__post_init__`` and its
    outcome is exposed via :attr:`is_valid`, :attr:`errors`, and :attr:`warnings`.

    Equality and hashing consider only the five ARN components.
    """

    partition: str
    service: str
    region: str
    account_id: str
    resource: str
    errors: tuple[str, ...] = field(init=False, compare=False, repr=False)
    warnings: tuple[str, ...] = field(init=False, compare=False, repr=False)

    def __post_init__(self) -> None:
        errors, warnings = _check_components(self)
        object.__setattr__(self, "errors", errors)
        object.__setattr__(self, "warnings", warnings)

    def __str__(self) -> str:
        return f"arn:{self.partition}:{self.service}:{self.region}:{self.account_id}:{self.resource}"

    # ------------------------------------------------------------------ #
    # Construction
    # ------------------------------------------------------------------ #
    @classmethod
    def parse(cls, value: str, *, strict: bool = False) -> ARN:
        """Decompose ``value`` into an :class:`ARN`.

        Raises :class:`ARNParseError` only when ``value`` cannot be split into
        the six ARN segments. Component-level problems are reported via
        :attr:`errors` / :attr:`is_valid` instead, unless ``strict=True``, in
        which case any validation error raises.
        """
        if not isinstance(value, str):
            raise ARNParseError(f"Expected a string, got {type(value).__name__}.", value=repr(value))
        parts = value.split(":", 5)
        if len(parts) < 6 or parts[0] != "arn":
            raise ARNParseError(
                f"Not an ARN: {value!r} (expected 'arn:partition:service:region:account-id:resource').",
                value=value,
            )
        arn = cls(partition=parts[1], service=parts[2], region=parts[3], account_id=parts[4], resource=parts[5])
        if strict:
            arn._raise_if_invalid()
        return arn

    @classmethod
    def try_parse(cls, value: str) -> ARN | None:
        """Like :meth:`parse`, but return ``None`` instead of raising on structural failures."""
        try:
            return cls.parse(value)
        except ARNParseError:
            return None

    @classmethod
    def is_arn(cls, value: str) -> bool:
        """Return ``True`` iff ``value`` parses and passes generic ARN validation. Never raises."""
        arn = cls.try_parse(value) if isinstance(value, str) else None
        return arn is not None and arn.is_valid

    @classmethod
    def build(
        cls,
        *,
        service: str,
        resource: str | None = None,
        resource_type: str | None = None,
        resource_id: str | None = None,
        region: str = "",
        account_id: str = "",
        partition: str = "aws",
        delimiter: Literal["/", ":"] = "/",
        strict: bool = True,
    ) -> ARN:
        """Assemble an ARN from its components.

        Supply either ``resource`` (the full resource segment) or both
        ``resource_type`` and ``resource_id``, which are joined with
        ``delimiter``. With ``strict=True`` (the default) an invalid result
        raises :class:`ARNParseError`.
        """
        if resource is not None and (resource_type is not None or resource_id is not None):
            raise ValueError("Pass either 'resource' or 'resource_type'/'resource_id', not both.")
        if resource is None:
            if resource_type is None or resource_id is None:
                raise ValueError("Pass 'resource', or both 'resource_type' and 'resource_id'.")
            if delimiter not in ("/", ":"):
                raise ValueError(f"delimiter must be '/' or ':', got {delimiter!r}.")
            resource = f"{resource_type}{delimiter}{resource_id}"

        arn = cls(partition=partition, service=service, region=region, account_id=account_id, resource=resource)
        if strict:
            arn._raise_if_invalid()
        return arn

    def replace(self, **changes: str) -> ARN:
        """Return a copy with the given components replaced, re-validated."""
        return dataclasses.replace(self, **changes)

    # ------------------------------------------------------------------ #
    # Derived views
    # ------------------------------------------------------------------ #
    @property
    def is_valid(self) -> bool:
        """``True`` when the ARN satisfies the generic ARN grammar."""
        return not self.errors

    @property
    def resource_type(self) -> str | None:
        """Resource type prefix (``role``, ``function``, ``alarm``, ...) or ``None`` for bare names."""
        return _split_resource(self.service, self.account_id, self.resource)[0]

    @property
    def resource_id(self) -> str:
        """Resource identifier after the type prefix; the whole resource for bare names."""
        return _split_resource(self.service, self.account_id, self.resource)[1]

    @property
    def resource_delimiter(self) -> str | None:
        """The ``/`` or ``:`` separating :attr:`resource_type` from :attr:`resource_id`."""
        return _split_resource(self.service, self.account_id, self.resource)[2]

    def to_dict(self) -> dict[str, Any]:
        """Serialize components, derived views, and validation outcome for JSON output."""
        return {
            "arn": str(self),
            "partition": self.partition,
            "service": self.service,
            "region": self.region,
            "account_id": self.account_id,
            "resource": self.resource,
            "resource_type": self.resource_type,
            "resource_id": self.resource_id,
            "resource_delimiter": self.resource_delimiter,
            "is_valid": self.is_valid,
            "errors": list(self.errors),
            "warnings": list(self.warnings),
        }

    # ------------------------------------------------------------------ #
    # Botocore shape layer (lazy registry)
    # ------------------------------------------------------------------ #
    def validate_against(self, service: str, shape: str, *, strict: bool = False) -> ValidationResult:
        """Validate this ARN against a specific botocore shape, e.g. ``("S3Control", "JobArn")``.

        Raises :class:`KeyError` (with suggestions) for unknown services or shapes.
        """
        svc = _resolve_service_or_raise(service)
        obj, suggestions = resolve_shape(svc, shape)
        if obj is None:
            raise KeyError(_not_found_message(f"Shape '{shape}' in service '{svc.service_name}'", suggestions))
        return diagnose_validation(obj, svc.service_name, str(self), strict=strict)

    def matching_shapes(self, *, services: Iterable[str] | None = None) -> list[tuple[str, str]]:
        """Return ``(service, shape)`` pairs of botocore ``*Arn`` shapes this ARN satisfies.

        By default every registered service is searched, but only shapes whose
        pattern pins this ARN's service literally (e.g. ``:s3:``) are
        considered; generic catch-all ARN patterns would match everything and
        add noise. Pass ``services`` to restrict the search to specific
        services, in which case all of their ``*Arn`` shapes are checked.
        """
        if services is None:
            candidates: Iterable[Service] = get_registry().services.values()
            pins = (f":{self.service}:", ":" + self.service.replace("-", "\\-") + ":")
        else:
            candidates = [_resolve_service_or_raise(name) for name in services]
            pins = ()

        value = str(self)
        matches: list[tuple[str, str]] = []
        for svc in candidates:
            for name, obj in svc.api_objects.items():
                if not name.lower().endswith("arn"):
                    continue
                if pins and not any(pin in obj.pattern for pin in pins):
                    continue
                try:
                    ok = obj.validate(value)
                except re.error:
                    continue
                if ok:
                    matches.append((svc.service_name, name))
        return matches

    # ------------------------------------------------------------------ #
    # Pydantic v2 integration
    # ------------------------------------------------------------------ #
    @classmethod
    def __get_pydantic_core_schema__(cls, source: Any, handler: GetCoreSchemaHandler) -> CoreSchema:
        """Allow ``ARN`` as a Pydantic field type: accepts ``str`` or ``ARN``, serializes to ``str``."""
        from pydantic_core import core_schema  # noqa: PLC0415

        def _from_str(value: str) -> ARN:
            return cls.parse(value, strict=True)

        def _check_instance(value: ARN) -> ARN:
            value._raise_if_invalid()
            return value

        from_str = core_schema.chain_schema(
            [core_schema.str_schema(), core_schema.no_info_plain_validator_function(_from_str)]
        )
        return core_schema.json_or_python_schema(
            json_schema=from_str,
            python_schema=core_schema.union_schema(
                [
                    core_schema.chain_schema(
                        [
                            core_schema.is_instance_schema(cls),
                            core_schema.no_info_plain_validator_function(_check_instance),
                        ]
                    ),
                    from_str,
                ]
            ),
            serialization=core_schema.plain_serializer_function_ser_schema(str),
        )

    # ------------------------------------------------------------------ #
    # Internals
    # ------------------------------------------------------------------ #
    def _raise_if_invalid(self) -> None:
        if self.errors:
            raise ARNParseError(
                f"Invalid ARN {str(self)!r}: " + " ".join(self.errors),
                value=str(self),
                errors=self.errors,
            )


def _check_components(arn: ARN) -> tuple[tuple[str, ...], tuple[str, ...]]:
    """Apply the generic ARN grammar; return ``(errors, warnings)``."""
    errors: list[str] = []
    warnings: list[str] = []

    if not arn.partition:
        errors.append("Partition is empty.")
    elif not _PARTITION_RE.fullmatch(arn.partition):
        errors.append(f"Partition {arn.partition!r} is malformed (expected e.g. 'aws', 'aws-cn', 'aws-us-gov').")
    elif arn.partition not in KNOWN_PARTITIONS:
        warnings.append(f"Partition {arn.partition!r} is not a known AWS partition.")

    if not arn.service:
        errors.append("Service is empty.")
    elif not _SERVICE_RE.fullmatch(arn.service):
        errors.append(f"Service {arn.service!r} is malformed (expected lowercase letters, digits, and single hyphens).")

    if arn.region and not _REGION_RE.fullmatch(arn.region):
        errors.append(f"Region {arn.region!r} is malformed (expected e.g. 'us-east-1', or empty for global).")

    if arn.account_id and arn.account_id != "aws" and not _ACCOUNT_RE.fullmatch(arn.account_id):
        errors.append(
            f"Account ID {arn.account_id!r} must be exactly 12 digits "
            f"(got {len(arn.account_id)} characters), 'aws', or empty."
        )

    if not arn.resource:
        errors.append("Resource is empty.")
    elif _CONTROL_CHARS_RE.search(arn.resource):
        errors.append("Resource contains control characters.")
    elif _WHITESPACE_RE.search(arn.resource):
        warnings.append("Resource contains whitespace; most AWS services reject it.")

    length = len(str(arn))
    if length > MAX_ARN_LENGTH:
        errors.append(f"ARN length {length} exceeds the maximum of {MAX_ARN_LENGTH} characters.")

    return tuple(errors), tuple(warnings)


def _split_resource(service: str, account_id: str, resource: str) -> tuple[str | None, str, str | None]:
    """Split a resource segment into ``(resource_type, resource_id, delimiter)``."""
    # SNS/SQS resources are bare names; S3 bucket/object ARNs have no account and no type.
    if service in _TYPELESS_SERVICES or (service == "s3" and not account_id):
        return None, resource, None
    for index, char in enumerate(resource):
        if char in "/:":
            prefix = resource[:index]
            if prefix and index < len(resource) - 1 and _RESOURCE_TYPE_RE.fullmatch(prefix):
                return prefix, resource[index + 1 :], char
            break
    return None, resource, None


def _resolve_service_or_raise(name: str) -> Service:
    svc, suggestions = resolve_service(name)
    if svc is None:
        raise KeyError(_not_found_message(f"Service '{name}'", suggestions))
    return svc


def _not_found_message(subject: str, suggestions: list[str]) -> str:
    hint = f" Did you mean: {', '.join(suggestions)}?" if suggestions else ""
    return f"{subject} not found.{hint}"
