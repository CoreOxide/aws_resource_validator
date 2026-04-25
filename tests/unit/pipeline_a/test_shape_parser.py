"""Tests for :mod:`aws_resource_validator.generator.pipeline_a.shape_parser`."""

from __future__ import annotations

from aws_resource_validator.generator.pipeline_a.shape_parser import iter_pattern_shapes


def test_yields_only_shapes_with_pattern() -> None:
    service_json = {
        "shapes": {
            "HasPattern": {"type": "string", "pattern": r"^a.+"},
            "NoPattern": {"type": "string"},
            "NoType": {"pattern": r".+"},
            "NotADict": "oops",
        }
    }
    shapes = list(iter_pattern_shapes(service_json))
    assert [s.name for s in shapes] == ["HasPattern"]


def test_preserves_min_and_max_length() -> None:
    service_json = {
        "shapes": {
            "Arn": {"type": "string", "pattern": r"arn:.+", "min": 20, "max": 2048},
        }
    }
    (shape,) = iter_pattern_shapes(service_json)
    assert shape.min_length == 20
    assert shape.max_length == 2048


def test_handles_missing_shapes_key() -> None:
    assert list(iter_pattern_shapes({})) == []
