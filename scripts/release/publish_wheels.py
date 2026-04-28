"""Chunked PyPI uploader that respects the new-project rate limit.

PyPI caps *new project name* registrations at ~20 per hour per account.
``gh-action-pypi-publish`` treats that limit as a hard failure and
aborts the whole batch. When we're rolling out 430+ wheels for the
first time, ~410 of those names are new, so a single invocation would
always 429 out around wheel #20.

This uploader:

  1. Filters out wheels whose ``<name>==<version>`` is already on PyPI
     (skip-existing behaviour, but done client-side via the JSON API
     so we don't burn rate-limit budget on needless POSTs).
  2. Walks the remaining wheels in chunks of ``--chunk-size`` (default
     18 — leaves headroom under the 20/hour cap).
  3. On HTTP 429 responses, sleeps ``--backoff-seconds`` (default 3900
     = 65 min) and retries. Once all new-project creations have
     landed, subsequent releases are version-bumps on existing
     projects, which aren't subject to the same limit.
  4. Always passes ``--skip-existing`` to twine so already-uploaded
     files from a prior attempt succeed silently.

Designed to run unattended in CI — expect ~22 hours of wall-clock time
for a ~410-new-project bootstrap upload, then normal speed thereafter.
"""

from __future__ import annotations

import argparse
import os
import pathlib
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from collections.abc import Iterable

PYPI_JSON = "https://pypi.org/pypi/{name}/{version}/json"

# ``aws_resource_validator-2.0.0-py3-none-any.whl`` →
# name = "aws_resource_validator", version = "2.0.0".
WHEEL_RE = re.compile(r"^(?P<name>[^-]+(?:-[^-]+)*?)-(?P<version>\d[^-]*)-")


def parse_wheel(path: pathlib.Path) -> tuple[str, str] | None:
    match = WHEEL_RE.match(path.name)
    if not match:
        return None
    # Wheel filenames use ``_`` in place of ``-`` in the dist name; the
    # PyPI JSON endpoint accepts either, so keep the underscore form
    # the filename already has.
    return match.group("name").replace("_", "-"), match.group("version")


def version_exists(name: str, version: str, timeout: float = 15) -> bool:
    url = PYPI_JSON.format(name=name, version=version)
    request = urllib.request.Request(url, method="HEAD")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status == 200
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return False
        # 4xx/5xx we can't interpret — treat as "unknown" so the caller
        # attempts the upload anyway (twine will skip-existing on 400).
        return False
    except Exception:
        return False


def filter_fresh_wheels(wheels: Iterable[pathlib.Path]) -> list[pathlib.Path]:
    fresh: list[pathlib.Path] = []
    skipped = 0
    for wheel in wheels:
        parsed = parse_wheel(wheel)
        if parsed is None:
            print(f"[publish] skipping unparseable filename: {wheel.name}", flush=True)
            continue
        name, version = parsed
        if version_exists(name, version):
            skipped += 1
            continue
        fresh.append(wheel)
    if skipped:
        print(f"[publish] {skipped} wheel(s) already on PyPI — skipped client-side", flush=True)
    return fresh


def run_twine(chunk: list[pathlib.Path], repository_url: str | None) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    args = [
        sys.executable, "-m", "twine", "upload",
        "--skip-existing",
        "--non-interactive",
        "--verbose",
        "--username", "__token__",
    ]
    if repository_url:
        args.extend(["--repository-url", repository_url])
    args.extend(str(p) for p in chunk)
    return subprocess.run(args, env=env, capture_output=True, text=True, check=False)


def looks_like_429(output: str) -> bool:
    """Heuristic: twine doesn't set a distinct exit code for 429."""
    return "429" in output or "too many new projects" in output.lower()


def publish(
    dist: pathlib.Path,
    chunk_size: int,
    backoff_seconds: int,
    max_backoff_rounds: int,
    repository_url: str | None,
) -> int:
    if not dist.is_dir():
        sys.stderr.write(f"not a directory: {dist}\n")
        return 2

    all_wheels = sorted(dist.glob("*.whl"))
    if not all_wheels:
        sys.stderr.write(f"no wheels found in {dist}\n")
        return 2

    print(f"[publish] {len(all_wheels)} wheels in {dist}", flush=True)
    fresh = filter_fresh_wheels(all_wheels)
    if not fresh:
        print("[publish] nothing to do — every wheel is already on PyPI.")
        return 0

    print(f"[publish] {len(fresh)} wheel(s) to upload in chunks of {chunk_size}", flush=True)

    index = 0
    total = len(fresh)
    chunk_num = 0
    while index < total:
        chunk = fresh[index : index + chunk_size]
        chunk_num += 1
        print(
            f"\n[publish] === chunk {chunk_num} "
            f"(wheels {index + 1}-{index + len(chunk)} of {total}) ===",
            flush=True,
        )
        for w in chunk:
            print(f"  {w.name}", flush=True)

        backoff_round = 0
        while True:
            result = run_twine(chunk, repository_url)
            stdout = result.stdout or ""
            stderr = result.stderr or ""
            combined = stdout + "\n" + stderr
            sys.stdout.write(stdout)
            sys.stderr.write(stderr)

            if result.returncode == 0:
                break

            if looks_like_429(combined) and backoff_round < max_backoff_rounds:
                backoff_round += 1
                wait = backoff_seconds
                print(
                    f"\n[publish] chunk {chunk_num} hit 429 — sleeping "
                    f"{wait}s before retry {backoff_round}/{max_backoff_rounds}",
                    flush=True,
                )
                # The filter was run before the outer loop; any wheels in this
                # chunk that slipped through and actually uploaded during the
                # failed attempt will be handled by --skip-existing on retry.
                time.sleep(wait)
                continue

            print(
                f"\n[publish] chunk {chunk_num} failed permanently "
                f"(exit {result.returncode}).",
                file=sys.stderr,
                flush=True,
            )
            return 1

        index += len(chunk)

        if index < total:
            # Even successful chunks still consume the new-project budget.
            # Wait a full window before the next chunk so we never bunch
            # 21 new projects into a single hour and trip the limit.
            wait = backoff_seconds
            print(
                f"[publish] chunk {chunk_num} OK — sleeping {wait}s before next chunk",
                flush=True,
            )
            time.sleep(wait)

    print(f"\n[publish] all {total} wheel(s) uploaded.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dist", type=pathlib.Path, help="Directory of wheels.")
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=18,
        help="Wheels per upload chunk. Keep below PyPI's 20/hour new-project cap.",
    )
    parser.add_argument(
        "--backoff-seconds",
        type=int,
        default=3900,
        help="Seconds to sleep between chunks AND after a 429. 65 min default.",
    )
    parser.add_argument(
        "--max-backoff-rounds",
        type=int,
        default=3,
        help="Max retries after 429 before giving up on a chunk.",
    )
    parser.add_argument(
        "--repository-url",
        default=None,
        help="Override the PyPI upload URL (e.g. test.pypi.org).",
    )
    args = parser.parse_args(argv)

    return publish(
        dist=args.dist,
        chunk_size=args.chunk_size,
        backoff_seconds=args.backoff_seconds,
        max_backoff_rounds=args.max_backoff_rounds,
        repository_url=args.repository_url,
    )


if __name__ == "__main__":
    raise SystemExit(main())
