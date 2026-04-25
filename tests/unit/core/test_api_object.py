"""Tests for :mod:`aws_resource_validator.core.api_object`."""

from __future__ import annotations

import pytest

from aws_resource_validator.core.api_object import APIObject


class TestValidate:
    def test_accepts_value_matching_pattern(self) -> None:
        obj = APIObject(name="Arn", type="string", pattern=r"arn:aws:\w+:.+")
        assert obj.validate("arn:aws:s3:example") is True

    def test_rejects_value_not_matching_pattern(self) -> None:
        obj = APIObject(name="Arn", type="string", pattern=r"arn:aws:.+")
        assert obj.validate("not-an-arn") is False

    def test_rejects_value_below_min_length(self) -> None:
        obj = APIObject(name="Arn", type="string", pattern=r".+", min_length=10)
        assert obj.validate("short") is False

    def test_rejects_value_above_max_length(self) -> None:
        obj = APIObject(name="Arn", type="string", pattern=r".+", max_length=3)
        assert obj.validate("too-long") is False

    def test_accepts_value_at_length_boundaries(self) -> None:
        obj = APIObject(name="Arn", type="string", pattern=r".+", min_length=3, max_length=5)
        assert obj.validate("abc") is True
        assert obj.validate("abcde") is True


class TestGenerate:
    def test_produces_value_matching_pattern(self) -> None:
        # ``generate`` is exrex-backed; its output may exceed max_length, since
        # exrex's ``limit`` bounds the quantifier expansion, not the total
        # length. The pattern-match check is what we actually care about.
        import re
        obj = APIObject(name="Arn", type="string", pattern=r"arn:aws:s3:[a-z]+", max_length=30)
        assert re.match(obj.pattern, obj.generate()) is not None

    def test_limit_is_passed_to_exrex(self) -> None:
        # Bounded pattern + small max: exrex keeps output roughly in range.
        obj = APIObject(name="Code", type="string", pattern=r"[a-z]{1,5}", max_length=5)
        assert len(obj.generate()) <= 5


class TestDataclass:
    def test_is_frozen(self, sample_api_object: APIObject) -> None:
        # ``frozen=True`` dataclasses raise ``FrozenInstanceError`` on write.
        with pytest.raises((AttributeError, TypeError)):
            sample_api_object.name = "other"  # type: ignore[misc]

    def test_equality_by_value(self) -> None:
        a = APIObject(name="X", type="string", pattern=r".")
        b = APIObject(name="X", type="string", pattern=r".")
        assert a == b
