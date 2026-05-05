"""Tests for :mod:`aws_resource_validator.core.pattern_validation`."""

from __future__ import annotations

from typing import Annotated

import pytest
from pydantic import Field, ValidationError

from aws_resource_validator.class_definitions import class_registry
from aws_resource_validator.core.base_validator_model import BaseValidatorModel
from aws_resource_validator.core.pattern_validation import aws_field_pattern

_OPT_IN = {"aws_validate_patterns": True}


def _token_obj():
    # ACM 'IdempotencyToken' shape: pattern r'\w+', min=1, max=32 — convenient
    # for length-bound checks because re.match on \w+ only fails on a leading
    # non-word character, so length violations exercise the min/max path.
    return class_registry["Acm"]["IdempotencyToken"]


def _good_token() -> str:
    return _token_obj().generate()


class TokenModel(BaseValidatorModel):
    value: Annotated[str, aws_field_pattern("Acm", "IdempotencyToken")]


class OptionalTokenModel(BaseValidatorModel):
    value: Annotated[str, aws_field_pattern("Acm", "IdempotencyToken")] | None = None


class TokenListModel(BaseValidatorModel):
    values: list[Annotated[str, aws_field_pattern("Acm", "IdempotencyToken")]]


class MultiFieldModel(BaseValidatorModel):
    a: Annotated[str, aws_field_pattern("Acm", "IdempotencyToken")]
    b: Annotated[str, aws_field_pattern("Acm", "IdempotencyToken")]


class UnknownShapeModel(BaseValidatorModel):
    value: Annotated[str, aws_field_pattern("NoSuchService", "NoSuchShape")]


class AliasedModel(BaseValidatorModel):
    token_: Annotated[str, aws_field_pattern("Acm", "IdempotencyToken")] = Field(
        ..., alias="detail-type"
    )


def test_default_no_validation_constructor() -> None:
    # Bad value (empty string violates min_length=1) is silently accepted when
    # the caller never activates pattern validation.
    TokenModel(value="")


def test_default_no_validation_model_validate() -> None:
    TokenModel.model_validate({"value": ""})


def test_opt_in_rejects_bad_value() -> None:
    with pytest.raises(ValidationError) as exc_info:
        TokenModel.model_validate({"value": ""}, context=_OPT_IN)
    errors = exc_info.value.errors()
    assert len(errors) == 1
    assert errors[0]["type"] == "aws_pattern"


def test_opt_in_accepts_good_value() -> None:
    good = _good_token()
    TokenModel.model_validate({"value": good}, context=_OPT_IN)


def test_optional_none_short_circuits_even_with_opt_in() -> None:
    OptionalTokenModel.model_validate({"value": None}, context=_OPT_IN)
    OptionalTokenModel.model_validate({}, context=_OPT_IN)


def test_list_wrapping_validates_each_element() -> None:
    good = _good_token()
    with pytest.raises(ValidationError) as exc_info:
        TokenListModel.model_validate(
            {"values": [good, "", good, ""]}, context=_OPT_IN
        )
    aws_errors = [e for e in exc_info.value.errors() if e["type"] == "aws_pattern"]
    assert len(aws_errors) == 2
    # List-path locs look like ('values', 1) etc.
    bad_indexes = sorted(err["loc"][-1] for err in aws_errors)
    assert bad_indexes == [1, 3]


def test_unknown_service_or_shape_is_permissive() -> None:
    # Even with validation active, an unresolvable (service, shape) resolves to
    # a no-op so a stale emitter never breaks a caller.
    UnknownShapeModel.model_validate({"value": "anything"}, context=_OPT_IN)


def test_wire_alias_round_trip() -> None:
    good = _good_token()
    m = AliasedModel.model_validate({"detail-type": good}, context=_OPT_IN)
    dumped = m.model_dump(by_alias=True)
    assert dumped == {"detail-type": good}


def test_multiple_errors_aggregate() -> None:
    with pytest.raises(ValidationError) as exc_info:
        MultiFieldModel.model_validate({"a": "", "b": ""}, context=_OPT_IN)
    errors = exc_info.value.errors()
    assert len(errors) == 2
    assert {e["type"] for e in errors} == {"aws_pattern"}
    assert {e["loc"][-1] for e in errors} == {"a", "b"}


def test_context_without_flag_does_not_validate() -> None:
    # A dict without the magic key does not activate validation.
    TokenModel.model_validate({"value": ""}, context={"other": True})


def test_falsy_flag_does_not_validate() -> None:
    TokenModel.model_validate(
        {"value": ""}, context={"aws_validate_patterns": False}
    )
