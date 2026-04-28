"""Tests for :mod:`scripts.release._manifests` validation logic."""

from __future__ import annotations

from scripts.release._manifests import Shard, validate


def _shard(name: str, services: tuple[str, ...] = (), catch_all: bool = False) -> Shard:
    return Shard(name=name, description="", services=services, catch_all=catch_all)


def test_validate_accepts_well_formed_manifest() -> None:
    errors = validate(
        services=["s3", "ec2", "lambda_", "rds"],
        popular=["s3"],
        shards=[
            _shard("data", services=("s3", "rds")),
            _shard("compute", services=("ec2", "lambda_")),
            _shard("rest", catch_all=True),
        ],
    )
    assert errors == []


def test_validate_flags_unknown_popular_service() -> None:
    errors = validate(
        services=["s3"],
        popular=["s3", "ghost_service"],
        shards=[_shard("data", services=("s3",)), _shard("rest", catch_all=True)],
    )
    assert any("ghost_service" in e for e in errors)


def test_validate_flags_unknown_shard_service() -> None:
    errors = validate(
        services=["s3"],
        popular=[],
        shards=[
            _shard("data", services=("s3", "ghost")),
            _shard("rest", catch_all=True),
        ],
    )
    assert any("ghost" in e and "data" in e for e in errors)


def test_validate_flags_duplicate_shard_membership() -> None:
    errors = validate(
        services=["s3"],
        popular=[],
        shards=[
            _shard("data", services=("s3",)),
            _shard("storage", services=("s3",)),
            _shard("rest", catch_all=True),
        ],
    )
    assert any("s3" in e and "data" in e and "storage" in e for e in errors)


def test_validate_requires_exactly_one_catch_all_shard() -> None:
    no_catch_all = validate(
        services=["s3"],
        popular=[],
        shards=[_shard("data", services=("s3",))],
    )
    assert any("catch_all" in e for e in no_catch_all)

    two_catch_alls = validate(
        services=["s3"],
        popular=[],
        shards=[
            _shard("rest", catch_all=True),
            _shard("other", catch_all=True),
        ],
    )
    assert any("catch_all" in e for e in two_catch_alls)


def test_validate_popular_must_be_covered_by_a_shard() -> None:
    # Without a catch-all, a popular service not in any shard escapes the
    # metapackage graph — validate should reject it.
    errors = validate(
        services=["s3", "ec2"],
        popular=["ec2"],
        shards=[_shard("data", services=("s3",))],
    )
    # One error for no catch_all + one for ec2 uncovered.
    assert any("ec2" in e and "shard" in e for e in errors)


def test_validate_catch_all_covers_everything_not_explicitly_listed() -> None:
    errors = validate(
        services=["s3", "ec2", "orphan"],
        popular=["orphan"],
        shards=[
            _shard("data", services=("s3",)),
            _shard("compute", services=("ec2",)),
            _shard("rest", catch_all=True),
        ],
    )
    # ``orphan`` is implicitly owned by the catch-all.
    assert errors == []
