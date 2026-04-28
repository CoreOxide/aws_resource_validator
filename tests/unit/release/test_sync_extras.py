"""Tests for :mod:`scripts.release.sync_extras`."""

from __future__ import annotations

import pytest

from scripts.release._manifests import Manifest, Shard
from scripts.release.sync_extras import (
    EXTRAS_BEGIN,
    EXTRAS_END,
    apply_all,
    render_extras,
    splice,
)


def _fixture_manifest() -> Manifest:
    return Manifest(
        services=("s3", "ec2", "lambda_"),
        popular=("s3", "lambda_"),
        shards=(
            Shard(name="data", description="Data services", services=("s3",), catch_all=False),
            Shard(name="compute", description="Compute services", services=("ec2", "lambda_"), catch_all=False),
            Shard(name="rest", description="Everything else", services=(), catch_all=True),
        ),
        version="2.1.0",
    )


def test_render_extras_emits_pep621_table() -> None:
    block = render_extras(_fixture_manifest())
    assert block.startswith(EXTRAS_BEGIN)
    assert block.rstrip().endswith(EXTRAS_END)
    assert "[project.optional-dependencies]" in block
    # Generator extra is hand-curated and always present.
    assert '"requests"' in block
    assert '"black"' in block
    # Service extras emit PEP 508 strings with strict pins.
    assert '"aws-resource-validator-s3==2.1.0"' in block
    assert '"aws-resource-validator-lambda==2.1.0"' in block
    assert '"aws-resource-validator-data==2.1.0"' in block
    assert '"aws-resource-validator-rest==2.1.0"' in block


def test_render_extras_bootstrap_omits_service_and_shard_extras() -> None:
    block = render_extras(_fixture_manifest(), bootstrap=True)
    # Generator still present.
    assert '"requests"' in block
    # Service + shard + all extras must NOT be present — the whole point
    # of bootstrap is that those projects don't exist on PyPI yet.
    assert "aws-resource-validator-s3" not in block
    assert "aws-resource-validator-data" not in block
    assert "aws-resource-validator-rest" not in block
    assert "\nall = [" not in block


def test_splice_replaces_region_between_markers() -> None:
    original = f"before\n{EXTRAS_BEGIN}\nstale\n{EXTRAS_END}\nafter\n"
    replacement = f"{EXTRAS_BEGIN}\nfresh\n{EXTRAS_END}\n"
    result = splice(original, EXTRAS_BEGIN, EXTRAS_END, replacement)
    assert "stale" not in result
    assert "fresh" in result
    assert result.startswith("before\n")
    assert result.endswith("after\n")


def test_splice_errors_when_markers_missing() -> None:
    with pytest.raises(SystemExit):
        splice("no markers here", EXTRAS_BEGIN, EXTRAS_END, "whatever")


def test_splice_errors_when_markers_in_wrong_order() -> None:
    reversed_text = f"{EXTRAS_END}\nbody\n{EXTRAS_BEGIN}\n"
    with pytest.raises(SystemExit):
        splice(reversed_text, EXTRAS_BEGIN, EXTRAS_END, "x")


def test_apply_all_is_idempotent() -> None:
    manifest = _fixture_manifest()
    text = (
        "[project]\n"
        'name = "test"\n'
        f"{EXTRAS_BEGIN}\nold extras\n{EXTRAS_END}\n"
    )
    once = apply_all(text, manifest)
    twice = apply_all(once, manifest)
    assert once == twice, "apply_all should be idempotent"
    assert "old extras" not in once
    assert "[project.optional-dependencies]" in once


def test_splice_handles_crlf_line_endings() -> None:
    original = f"head\r\n{EXTRAS_BEGIN}\r\nstale\r\n{EXTRAS_END}\r\ntail\r\n"
    replacement = f"{EXTRAS_BEGIN}\nfresh\n{EXTRAS_END}\n"
    result = splice(original, EXTRAS_BEGIN, EXTRAS_END, replacement)
    assert "stale" not in result
    assert "fresh" in result
    assert "tail" in result
