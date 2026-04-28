"""Tests for :mod:`scripts.release.sync_extras`."""

from __future__ import annotations

import pytest

from scripts.release._manifests import Manifest, Shard
from scripts.release.sync_extras import (
    DEPS_BEGIN,
    DEPS_END,
    EXTRAS_BEGIN,
    EXTRAS_END,
    apply_all,
    render_extras,
    render_optional_deps,
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


def test_render_optional_deps_pins_strict_version() -> None:
    block = render_optional_deps(_fixture_manifest())
    assert block.startswith(DEPS_BEGIN)
    assert block.rstrip().endswith(DEPS_END)
    assert '"aws-resource-validator-s3" = { version = "==2.1.0", optional = true }' in block
    assert '"aws-resource-validator-lambda" = { version = "==2.1.0", optional = true }' in block
    assert '"aws-resource-validator-data" = { version = "==2.1.0", optional = true }' in block


def test_render_extras_emits_expected_tables() -> None:
    block = render_extras(_fixture_manifest())
    assert block.startswith(EXTRAS_BEGIN)
    assert block.rstrip().endswith(EXTRAS_END)
    assert "[tool.poetry.extras]" in block
    assert 'generator = ["requests", "jinja2", "typer", "black"]' in block
    # Popular services keyed by normalized extras key.
    assert 's3 = ["aws-resource-validator-s3"]' in block
    assert 'lambda = ["aws-resource-validator-lambda"]' in block
    # Shards.
    assert 'data = ["aws-resource-validator-data"]' in block
    # ``all`` references every shard metapackage.
    assert '"aws-resource-validator-rest"' in block


def test_splice_replaces_region_between_markers() -> None:
    original = f"before\n{DEPS_BEGIN}\nstale\n{DEPS_END}\nafter\n"
    replacement = f"{DEPS_BEGIN}\nfresh\n{DEPS_END}\n"
    result = splice(original, DEPS_BEGIN, DEPS_END, replacement)
    assert "stale" not in result
    assert "fresh" in result
    assert result.startswith("before\n")
    assert result.endswith("after\n")


def test_splice_errors_when_markers_missing() -> None:
    with pytest.raises(SystemExit):
        splice("no markers here", DEPS_BEGIN, DEPS_END, "whatever")


def test_splice_errors_when_markers_in_wrong_order() -> None:
    reversed_text = f"{DEPS_END}\nbody\n{DEPS_BEGIN}\n"
    with pytest.raises(SystemExit):
        splice(reversed_text, DEPS_BEGIN, DEPS_END, "x")


def test_apply_all_is_idempotent() -> None:
    manifest = _fixture_manifest()
    # Minimal pyproject fixture with both marker pairs.
    text = (
        "[tool.poetry.dependencies]\n"
        "python = \"^3.11\"\n"
        f"{DEPS_BEGIN}\nold deps\n{DEPS_END}\n"
        "\n"
        f"{EXTRAS_BEGIN}\nold extras\n{EXTRAS_END}\n"
    )
    once = apply_all(text, manifest)
    twice = apply_all(once, manifest)
    assert once == twice, "apply_all should be idempotent"
    assert "old deps" not in once
    assert "old extras" not in once


def test_splice_handles_crlf_line_endings() -> None:
    original = f"head\r\n{DEPS_BEGIN}\r\nstale\r\n{DEPS_END}\r\ntail\r\n"
    replacement = f"{DEPS_BEGIN}\nfresh\n{DEPS_END}\n"
    result = splice(original, DEPS_BEGIN, DEPS_END, replacement)
    # splice finds the LF after END; CRLF collapses to LF-only in the
    # rendered region, but surrounding CRLF content is preserved.
    assert "stale" not in result
    assert "fresh" in result
    assert "tail" in result
