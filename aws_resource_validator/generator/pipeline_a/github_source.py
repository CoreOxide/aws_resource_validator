"""Fetch ``service-2.json`` definitions from the boto/botocore GitHub repo.

Each AWS service lives under ``botocore/data/<service>/<api-version>/service-2.json``
in the repository. We walk the directory listings via the GitHub contents API,
decode the base64 blobs it returns, and yield ``(service_name, service_json)``
tuples.

The source is instantiable so its state (request counter, rate-limit policy,
HTTP session, auth token) stays local and injectable.
"""

from __future__ import annotations

import base64
import json
import time
from collections.abc import Iterator
from dataclasses import dataclass
from typing import Any

import requests
from requests import Response, Session

from aws_resource_validator.generator.common.logging import get_logger

_logger = get_logger(__name__)

_BOTOCORE_DATA_URL = "https://api.github.com/repos/boto/botocore/contents/botocore/data"
_SERVICE_FILE_NAME = "service-2.json"


@dataclass(frozen=True)
class RateLimitPolicy:
    """Sleep behaviour when GitHub signals the quota is about to run out.

    Attributes:
        remaining_threshold: Sleep when ``X-RateLimit-Remaining`` drops to
            this number or below.
        reset_pad_seconds: Extra wait added after the reset timestamp to
            guarantee the window has rolled over.
    """

    remaining_threshold: int = 1
    reset_pad_seconds: float = 10.0


class GitHubBotocoreSource:
    """Iterate over all AWS services' current ``service-2.json`` shapes."""

    def __init__(
        self,
        token: str | None = None,
        *,
        session: Session | None = None,
        rate_limit: RateLimitPolicy | None = None,
        request_timeout: float = 10.0,
    ) -> None:
        self._session = session or requests.Session()
        self._token = token
        self._rate_limit = rate_limit or RateLimitPolicy()
        self._timeout = request_timeout

    @property
    def _headers(self) -> dict[str, str]:
        headers = {"Accept": "application/vnd.github+json"}
        if self._token:
            headers["Authorization"] = f"Bearer {self._token}"
        return headers

    def _get(self, url: str) -> Response:
        """GET ``url`` and honour GitHub's rate-limit headers."""
        response = self._session.get(url, headers=self._headers, timeout=self._timeout)
        response.raise_for_status()
        self._respect_rate_limit(response)
        return response

    def _respect_rate_limit(self, response: Response) -> None:
        try:
            remaining = int(response.headers.get("X-RateLimit-Remaining", "999"))
        except ValueError:
            _logger.debug("Malformed X-RateLimit-Remaining header; skipping rate-limit check.")
            return
        if remaining > self._rate_limit.remaining_threshold:
            return
        try:
            reset_at = int(response.headers["X-RateLimit-Reset"])
        except (KeyError, ValueError):
            _logger.debug("Missing or malformed X-RateLimit-Reset header; skipping sleep.")
            return
        wait = max(0.0, reset_at - time.time()) + self._rate_limit.reset_pad_seconds
        _logger.warning("Rate limit near exhaustion; sleeping %.1fs.", wait)
        time.sleep(wait)

    # ------------------------------------------------------------------ API

    def iter_services(self) -> Iterator[tuple[str, dict[str, Any]]]:
        """Yield ``(service_name, service_json)`` for every AWS service."""
        for entry in self._list_directory(_BOTOCORE_DATA_URL):
            if entry.get("type") != "dir":
                continue
            service_name = entry["name"]
            try:
                service_json = self._fetch_service_json(entry["url"])
            except _ServiceNotFound as err:
                _logger.warning("Skipping %s: %s", service_name, err)
                continue
            yield service_name, service_json

    # ---------------------------------------------------------------- internal

    def _list_directory(self, url: str) -> list[dict[str, Any]]:
        payload = self._get(url).json()
        if not isinstance(payload, list):
            raise RuntimeError(f"Expected directory listing at {url}, got: {type(payload).__name__}")
        return payload

    def _fetch_service_json(self, service_dir_url: str) -> dict[str, Any]:
        versions = self._list_directory(service_dir_url)
        if not versions:
            raise _ServiceNotFound("no API versions published")
        latest_url = versions[0]["url"]
        files = self._list_directory(latest_url)
        service_file = next((f for f in files if f["name"] == _SERVICE_FILE_NAME), None)
        if service_file is None:
            raise _ServiceNotFound(f"{_SERVICE_FILE_NAME} missing under {latest_url}")
        file_payload = self._get(service_file["url"]).json()
        content = file_payload.get("content")
        if not content:
            raise _ServiceNotFound("service-2.json has no content blob")
        decoded = base64.b64decode(content).decode("utf-8")
        return json.loads(decoded)


class _ServiceNotFound(RuntimeError):
    """Signals a service directory listing was shaped unexpectedly."""
