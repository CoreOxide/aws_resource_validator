"""Tests for :mod:`aws_resource_validator.generator.pipeline_a.github_source`."""

from __future__ import annotations

import base64
import json

import pytest
import responses

from aws_resource_validator.generator.pipeline_a.github_source import (
    GitHubBotocoreSource,
    RateLimitPolicy,
)

_BASE_URL = "https://api.github.com/repos/boto/botocore/contents/botocore/data"


@responses.activate
def test_iter_services_returns_parsed_service_json() -> None:
    service_payload = {"shapes": {"Arn": {"type": "string", "pattern": r".+"}}}
    encoded = base64.b64encode(json.dumps(service_payload).encode()).decode()

    responses.get(
        _BASE_URL,
        json=[{"type": "dir", "name": "acm", "url": f"{_BASE_URL}/acm"}],
    )
    responses.get(f"{_BASE_URL}/acm", json=[{"url": f"{_BASE_URL}/acm/2015"}])
    responses.get(
        f"{_BASE_URL}/acm/2015",
        json=[{"name": "service-2.json", "url": f"{_BASE_URL}/acm/2015/service-2.json"}],
    )
    responses.get(f"{_BASE_URL}/acm/2015/service-2.json", json={"content": encoded})

    source = GitHubBotocoreSource()
    services = list(source.iter_services())

    assert len(services) == 1
    name, payload = services[0]
    assert name == "acm"
    assert payload == service_payload


@responses.activate
def test_skips_services_without_service_2_json() -> None:
    responses.get(
        _BASE_URL,
        json=[{"type": "dir", "name": "weird", "url": f"{_BASE_URL}/weird"}],
    )
    responses.get(f"{_BASE_URL}/weird", json=[{"url": f"{_BASE_URL}/weird/v1"}])
    responses.get(f"{_BASE_URL}/weird/v1", json=[{"name": "other.json", "url": "..."}])

    source = GitHubBotocoreSource()
    assert list(source.iter_services()) == []


@responses.activate
def test_rate_limit_triggers_sleep(monkeypatch: pytest.MonkeyPatch) -> None:
    sleeps: list[float] = []
    monkeypatch.setattr(
        "aws_resource_validator.generator.pipeline_a.github_source.time.sleep",
        lambda seconds: sleeps.append(seconds),
    )
    responses.get(
        _BASE_URL,
        json=[],
        headers={"X-RateLimit-Remaining": "0", "X-RateLimit-Reset": "1"},
    )
    source = GitHubBotocoreSource(rate_limit=RateLimitPolicy(remaining_threshold=1, reset_pad_seconds=5))
    list(source.iter_services())
    assert sleeps  # at least one sleep was issued.


@responses.activate
def test_includes_bearer_token_header() -> None:
    responses.get(_BASE_URL, json=[])
    source = GitHubBotocoreSource(token="tok-123")
    list(source.iter_services())
    assert responses.calls[0].request.headers["Authorization"] == "Bearer tok-123"


@responses.activate
def test_rate_limit_reset_in_past_waits_only_the_pad(monkeypatch: pytest.MonkeyPatch) -> None:
    # Reset timestamp "1" is decades in the past; ``max(0, delta)`` clamps
    # the wait to zero so only the configured pad is slept.
    sleeps: list[float] = []
    monkeypatch.setattr(
        "aws_resource_validator.generator.pipeline_a.github_source.time.sleep",
        lambda seconds: sleeps.append(seconds),
    )
    responses.get(
        _BASE_URL,
        json=[],
        headers={"X-RateLimit-Remaining": "0", "X-RateLimit-Reset": "1"},
    )
    pad = 5.0
    source = GitHubBotocoreSource(rate_limit=RateLimitPolicy(remaining_threshold=1, reset_pad_seconds=pad))
    list(source.iter_services())
    assert sleeps == [pad]


@responses.activate
def test_malformed_remaining_header_is_tolerated() -> None:
    responses.get(
        _BASE_URL,
        json=[],
        headers={"X-RateLimit-Remaining": "oops", "X-RateLimit-Reset": "1"},
    )
    # Must not raise — the iterator simply completes without sleeping.
    assert list(GitHubBotocoreSource().iter_services()) == []
