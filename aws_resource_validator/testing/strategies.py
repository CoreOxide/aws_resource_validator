"""Hypothesis search strategies for AWS resource names, ARNs, and property-based testing."""

from __future__ import annotations

import re
from collections.abc import Iterable, Sequence
from typing import TYPE_CHECKING, Any, Literal

try:
    import hypothesis.strategies as st
    from hypothesis.strategies import SearchStrategy
except ImportError as exc:  # pragma: no cover
    raise ImportError(
        "Hypothesis is required for aws_resource_validator property-based testing strategies. "
        "Install it with: pip install 'aws-resource-validator[testing]' or pip install hypothesis"
    ) from exc

from aws_resource_validator.core.arn import ARN, KNOWN_PARTITIONS
from aws_resource_validator.core.builtin_rules import get_extra_validator
from aws_resource_validator.testing.helpers import resolve_service_and_shape

if TYPE_CHECKING:
    from aws_resource_validator.core.api_object import APIObject

__all__ = [
    "arn_strings",
    "arns",
    "from_api_object",
    "invalid_arns",
    "invalid_resource_names",
    "resource_names",
]

_COMMON_REGIONS: tuple[str, ...] = (
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
    "eu-west-1",
    "eu-central-1",
    "ap-northeast-1",
    "ap-southeast-1",
)

_GLOBAL_SERVICES: frozenset[str] = frozenset({"iam", "cloudfront", "route53", "waf", "shield", "s3"})

_COMMON_SERVICES: tuple[str, ...] = (
    "s3",
    "lambda",
    "iam",
    "sqs",
    "sns",
    "dynamodb",
    "kms",
    "rds",
    "secretsmanager",
    "ecs",
    "logs",
    "events",
    "stepfunctions",
)


def _to_strategy(val: Any, default_strat: SearchStrategy[str]) -> SearchStrategy[str]:
    """Convert a literal string, collection of strings, or strategy into a SearchStrategy."""
    if val is None:
        return default_strat
    if isinstance(val, SearchStrategy):
        return val
    if isinstance(val, str):
        return st.just(val)
    if isinstance(val, Sequence | Iterable):
        choices = list(val)
        if not choices:
            raise ValueError("Empty sequence provided for ARN component choices.")
        return st.sampled_from(choices)
    raise TypeError(f"Expected str, sequence of str, or SearchStrategy, got {type(val).__name__}")


def _optimize_pattern(pattern: str, eff_min: int, eff_max: int | None) -> str:
    """Rewrite unbounded regex quantifiers with explicit length bounds to avoid filter rejections."""
    pat = pattern.strip()
    anchored_start = pat.startswith("^")
    anchored_end = pat.endswith("$")
    inner = pat
    if anchored_start:
        inner = inner[1:]
    if anchored_end:
        inner = inner[:-1]

    # Case 1: single character class with + or * (e.g. [a-zA-Z0-9-_]+ or [\w+=,.@-]+)
    m1 = re.fullmatch(r"(\[[^\]]+\]|\\[wds]|\.)[\+\*]", inner)
    if m1:
        base = m1.group(1)
        max_str = str(eff_max) if eff_max is not None else ""
        return f"^{base}{{{eff_min},{max_str}}}$"

    # Case 2: single prefix atom followed by tail atom with + or * (e.g. ^[a-zA-Z][a-zA-Z0-9-]*$)
    m2 = re.fullmatch(r"(\[[^\]]+\]|\\[wds]|[a-zA-Z0-9])(\[[^\]]+\]|\\[wds]|\.)[\+\*]", inner)
    if m2:
        prefix = m2.group(1)
        tail = m2.group(2)
        tail_min = max(0, eff_min - 1)
        tail_max = max(0, eff_max - 1) if eff_max is not None else None
        max_str = str(tail_max) if tail_max is not None else ""
        return f"^{prefix}{tail}{{{tail_min},{max_str}}}$"

    return pattern


def _is_shape_valid(obj: APIObject, extra_fn: Any, s: str, strict: bool) -> bool:
    """Fast check whether string satisfies shape bounds without triggering diagnostics."""
    if not obj.validate(s):
        return False
    if strict and not re.fullmatch(obj.pattern, s):
        return False
    return not (extra_fn and extra_fn(s))


def from_api_object(
    api_object: APIObject,
    *,
    service_name: str | None = None,
    min_size: int | None = None,
    max_size: int | None = None,
    strict: bool = True,
) -> SearchStrategy[str]:
    """Build a Hypothesis strategy generating valid values for a given :class:`APIObject`."""
    shape_min = api_object.min_length or 0
    shape_max = api_object.max_length

    eff_min = shape_min if min_size is None else max(min_size, shape_min)
    if max_size is not None and shape_max is not None:
        eff_max: int | None = min(max_size, shape_max)
    elif max_size is not None:
        eff_max = max_size
    else:
        eff_max = shape_max

    if eff_max is not None and eff_min > eff_max:
        raise ValueError(
            f"Conflicting length constraints: calculated minimum size {eff_min} "
            f"exceeds maximum size {eff_max} for shape '{api_object.name}'."
        )

    # Base strategy from optimized regex
    pattern_to_use = _optimize_pattern(api_object.pattern, eff_min, eff_max)
    raw_strategy = st.from_regex(pattern_to_use, fullmatch=strict)

    # Filter by effective length bounds
    if eff_min > 0 and eff_max is not None:
        strat = raw_strategy.filter(lambda s: eff_min <= len(s) <= eff_max)
    elif eff_min > 0:
        strat = raw_strategy.filter(lambda s: len(s) >= eff_min)
    elif eff_max is not None:
        strat = raw_strategy.filter(lambda s: len(s) <= eff_max)
    else:
        strat = raw_strategy

    # Apply strict end-to-end match check if required
    if strict:
        strat = strat.filter(lambda s: re.fullmatch(api_object.pattern, s) is not None)
    else:
        strat = strat.filter(lambda s: re.match(api_object.pattern, s) is not None)

    # If domain-specific extra validator exists for this shape, apply it
    svc = service_name or api_object.service_name or ""
    extra_fn = get_extra_validator(svc, api_object.name)
    if extra_fn is not None:
        strat = strat.filter(lambda s: len(extra_fn(s)) == 0)

    return strat


def resource_names(
    service: str,
    shape: str,
    *,
    min_size: int | None = None,
    max_size: int | None = None,
    strict: bool = True,
) -> SearchStrategy[str]:
    """Generate valid AWS resource names for ``(service, shape)``.

    Supports all AWS service shapes in :mod:`aws_resource_validator.class_definitions`
    and built-in rules (e.g. S3 bucket names, SQS queue names, RDS identifiers).

    Args:
        service: AWS service identifier (e.g. ``"s3"``, ``"lambda"``, ``"iam"``).
        shape: AWS shape name (e.g. ``"BucketName"``, ``"FunctionName"``, ``"role_name_type"``).
        min_size: Optional minimum length override.
        max_size: Optional maximum length override.
        strict: When True (default), enforce full end-to-end regex match.
    """
    svc, obj = resolve_service_and_shape(service, shape)
    return from_api_object(
        obj,
        service_name=svc.service_name,
        min_size=min_size,
        max_size=max_size,
        strict=strict,
    )


def invalid_resource_names(
    service: str,
    shape: str,
    *,
    strict: bool = True,
) -> SearchStrategy[str]:
    """Generate strings guaranteed to violate naming rules for ``(service, shape)``.

    Produces values that fail length checks, forbidden character checks,
    uppercase rules, or domain constraints (such as IP addresses in S3 buckets
    or double-hyphens in RDS identifiers).
    """
    svc, obj = resolve_service_and_shape(service, shape)
    shape_name_lower = obj.name.lower()
    extra_fn = get_extra_validator(svc.service_name, obj.name, shape)

    # Pre-crafted candidates known to violate common constraints
    candidate_list: list[str] = [
        "",
        "INVALID UPPERCASE !@#",
        "has space in name",
        "has/slash",
        "has:colon",
        "-starts-with-dash",
        "ends-with-dash-",
        "double--dash",
        "double..dot",
        "192.168.1.1",
        "contains$dollar",
        "contains%percent",
        "contains?question",
    ]

    # Add length boundary violations
    if obj.min_length and obj.min_length > 1:
        candidate_list.append("a" * (obj.min_length - 1))
    if obj.max_length:
        candidate_list.append("x" * (obj.max_length + 5))

    # Add service-specific edge cases
    if "bucket" in shape_name_lower:
        candidate_list.extend(["127.0.0.1", "my..bucket", ".leadingdot", "trailingdot."])
    if "identifier" in shape_name_lower:
        candidate_list.extend(["1leadingdigit", "trailing-", "double--hyphen"])

    base_strat = st.sampled_from(candidate_list)

    # Also generate fuzzed invalid strings with illegal characters injected
    fuzzed_strat = st.text(
        alphabet=st.characters(whitelist_categories=("Po", "Zs", "Cc")),
        min_size=1,
        max_size=32,
    )

    combined = st.one_of(base_strat, fuzzed_strat)
    return combined.filter(lambda s: not _is_shape_valid(obj, extra_fn, s, strict=strict))


def arns(
    *,
    partition: str | Sequence[str] | SearchStrategy[str] | None = None,
    service: str | Sequence[str] | SearchStrategy[str] | None = None,
    region: str | Sequence[str] | SearchStrategy[str] | None = None,
    account_id: str | Sequence[str] | SearchStrategy[str] | None = None,
    resource: str | Sequence[str] | SearchStrategy[str] | None = None,
    resource_type: str | Sequence[str] | SearchStrategy[str] | None = None,
    resource_id: str | Sequence[str] | SearchStrategy[str] | None = None,
    delimiter: Literal["/", ":"] = "/",
    strict: bool = True,
) -> SearchStrategy[ARN]:
    """Generate valid :class:`~aws_resource_validator.core.ARN` instances.

    All component parameters accept a literal ``str``, a sequence of ``str``,
    a Hypothesis ``SearchStrategy[str]``, or ``None`` to automatically generate
    realistic AWS values.
    """
    partition_strat = _to_strategy(
        partition,
        st.sampled_from(sorted(KNOWN_PARTITIONS)),
    )
    service_strat = _to_strategy(
        service,
        st.sampled_from(_COMMON_SERVICES),
    )
    region_strat = _to_strategy(
        region,
        st.sampled_from((*_COMMON_REGIONS, "")),
    )
    account_strat = _to_strategy(
        account_id,
        st.from_regex(r"^\d{12}$", fullmatch=True) | st.just(""),
    )

    if resource is not None:
        resource_strat = _to_strategy(resource, st.from_regex(r"^[a-zA-Z0-9_-]{1,32}$", fullmatch=True))
    elif resource_type is not None or resource_id is not None:
        type_strat = _to_strategy(resource_type, st.sampled_from(["role", "function", "table", "alarm", "queue"]))
        id_strat = _to_strategy(resource_id, st.from_regex(r"^[a-zA-Z0-9_-]{1,32}$", fullmatch=True))
        resource_strat = st.tuples(type_strat, id_strat).map(lambda t: f"{t[0]}{delimiter}{t[1]}")
    else:
        resource_strat = st.from_regex(r"^[a-zA-Z0-9_-]{1,32}$", fullmatch=True)

    @st.composite
    def _arn_builder(draw: Any) -> ARN:
        p = draw(partition_strat)
        s = draw(service_strat)
        r = draw(region_strat)
        a = draw(account_strat)
        res = draw(resource_strat)

        # Service-aware normalizations for global or bare-resource AWS patterns
        if s in _GLOBAL_SERVICES:
            # S3 bucket ARNs omit account_id and region; IAM ARNs omit region
            if s == "s3":
                r = ""
                a = ""
            elif s == "iam":
                r = ""

        # S3, SQS, SNS typically require account_id or region if not S3
        if s in {"sqs", "sns", "lambda", "dynamodb"} and not a:
            a = "123456789012"
        if s in {"sqs", "sns", "lambda", "dynamodb"} and not r:
            r = "us-east-1"

        return ARN(partition=p, service=s, region=r, account_id=a, resource=res)

    strat = _arn_builder()
    if strict:
        strat = strat.filter(lambda a: a.is_valid)
    return strat


def arn_strings(
    *,
    partition: str | Sequence[str] | SearchStrategy[str] | None = None,
    service: str | Sequence[str] | SearchStrategy[str] | None = None,
    region: str | Sequence[str] | SearchStrategy[str] | None = None,
    account_id: str | Sequence[str] | SearchStrategy[str] | None = None,
    resource: str | Sequence[str] | SearchStrategy[str] | None = None,
    resource_type: str | Sequence[str] | SearchStrategy[str] | None = None,
    resource_id: str | Sequence[str] | SearchStrategy[str] | None = None,
    delimiter: Literal["/", ":"] = "/",
    strict: bool = True,
) -> SearchStrategy[str]:
    """Generate valid ARN formatted strings (``"arn:partition:service:..."``)."""
    return arns(
        partition=partition,
        service=service,
        region=region,
        account_id=account_id,
        resource=resource,
        resource_type=resource_type,
        resource_id=resource_id,
        delimiter=delimiter,
        strict=strict,
    ).map(str)


def invalid_arns() -> SearchStrategy[str]:
    """Generate malformed ARN strings guaranteed to fail :meth:`ARN.is_arn`."""
    malformed_templates: list[str] = [
        "not-an-arn",
        "aws:s3:::my-bucket",
        "arn:aws:s3:us-east-1",  # fewer than 5 colons
        "arn::s3:us-east-1:123456789012:bucket",  # empty partition
        "arn:INVALID!PART:s3:us-east-1:123456789012:bucket",  # malformed partition
        "arn:aws:iam::12345:role/bad",  # non-12-digit account ID
        "arn:aws:sqs:INVALID_REGION:123456789012:my-queue",  # invalid region
        "arn:aws:s3:us-east-1:123456789012:",  # empty resource
        "arn:aws:s3:us-east-1:123456789012:\x00null-byte",  # control character
        "arn:aws:s3:us-east-1:123456789012:" + "x" * 2100,  # exceeds MAX_ARN_LENGTH
    ]

    base = st.sampled_from(malformed_templates)
    fuzzed = st.text(max_size=30)
    return st.one_of(base, fuzzed).filter(lambda s: not ARN.is_arn(s))
