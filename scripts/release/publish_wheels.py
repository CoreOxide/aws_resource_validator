"""PyPI uploader that chunks only when the new-project rate limit is relevant.

PyPI caps *new project name* registrations at ~20 per hour per account.
The bootstrap release of this project created ~410 names; subsequent
releases are version bumps on projects that already exist and aren't
subject to any comparable limit.

This uploader:

  1. Filters out wheels whose ``<name>==<version>`` is already on PyPI
     (skip-existing behaviour, but done client-side via the JSON API
     so we don't burn rate-limit budget on needless POSTs).
  2. Counts how many of the remaining wheels belong to project names
     that don't exist on PyPI yet ("new projects").
  3. If zero new projects: uploads everything in a single ``twine``
     call and returns. This is the steady-state path, seconds per
     release.
  4. Otherwise: uploads in chunks of ``--chunk-size`` (default 18),
     sleeping ``--backoff-seconds`` (default 3900 s / 65 min) between
     chunks AND on 429 retries. Only the first bootstrap release
     exercises this path.
  5. Always passes ``--skip-existing`` to twine so already-uploaded
     files from a prior attempt succeed silently.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import os
import pathlib
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from collections.abc import Iterable

PYPI_VERSION_JSON = "https://pypi.org/pypi/{name}/{version}/json"
PYPI_PROJECT_JSON = "https://pypi.org/pypi/{name}/json"

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


def _pypi_head(url: str, timeout: float = 15) -> bool:
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


def version_exists(name: str, version: str, timeout: float = 15) -> bool:
    return _pypi_head(PYPI_VERSION_JSON.format(name=name, version=version), timeout)


def project_exists(name: str, timeout: float = 15) -> bool:
    return _pypi_head(PYPI_PROJECT_JSON.format(name=name), timeout)


def filter_fresh_wheels(wheels: Iterable[pathlib.Path]) -> list[pathlib.Path]:
    candidates: list[tuple[pathlib.Path, str, str]] = []
    for wheel in wheels:
        parsed = parse_wheel(wheel)
        if parsed is None:
            print(f"[publish] skipping unparseable filename: {wheel.name}", flush=True)
            continue
        candidates.append((wheel, parsed[0], parsed[1]))

    with concurrent.futures.ThreadPoolExecutor(max_workers=24) as pool:
        exists = list(pool.map(lambda c: version_exists(c[1], c[2]), candidates))

    fresh = [c[0] for c, ok in zip(candidates, exists, strict=True) if not ok]
    skipped = len(candidates) - len(fresh)
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


def is_new_project_limit(output: str) -> bool:
    """Distinguish the 20/hour new-project cap from any other 429."""
    return "too many new projects" in output.lower()


def upload_with_retry(
    wheels: list[pathlib.Path],
    repository_url: str | None,
    *,
    short_retries: int = 4,
    short_backoff_base: int = 30,
) -> subprocess.CompletedProcess[str]:
    """Upload ``wheels`` once, retrying short 429s with exponential backoff.

    Handles the generic "PyPI is busy right now" case that can hit a
    single large upload batch on a shared CI IP. Returns the final
    ``CompletedProcess``. Does NOT wait for the 65-min new-project cap
    — that's a different beast and the caller should fall back to the
    chunked path if ``is_new_project_limit`` is true on the final
    attempt.
    """
    for attempt in range(short_retries + 1):
        result = run_twine(wheels, repository_url)
        stdout = result.stdout or ""
        stderr = result.stderr or ""
        sys.stdout.write(stdout)
        sys.stderr.write(stderr)
        if result.returncode == 0:
            return result
        combined = stdout + "\n" + stderr
        if not looks_like_429(combined) or attempt == short_retries:
            return result
        if is_new_project_limit(combined):
            return result  # Caller will switch to chunked path.
        wait = short_backoff_base * (2 ** attempt)
        print(
            f"\n[publish] hit a generic 429 — sleeping {wait}s before retry "
            f"{attempt + 1}/{short_retries}",
            flush=True,
        )
        time.sleep(wait)
    return result


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

    # Decide between the fast path (single upload) and the chunked path.
    # New-project names are the only thing PyPI rate-limits here; if
    # every project already exists, pipe the whole batch to twine at
    # once — takes seconds, not hours.
    fresh_project_names = {
        parse_wheel(w)[0]  # type: ignore[index]  # filtered above
        for w in fresh
    }
    names = sorted(fresh_project_names)
    with concurrent.futures.ThreadPoolExecutor(max_workers=24) as pool:
        exists = list(pool.map(project_exists, names))
    new_project_names = [name for name, ok in zip(names, exists, strict=True) if not ok]
    if not new_project_names:
        print(
            f"[publish] every project already exists on PyPI — "
            f"uploading {len(fresh)} wheel(s) in one shot",
            flush=True,
        )
        result = upload_with_retry(fresh, repository_url)
        if result.returncode == 0:
            print(f"\n[publish] all {len(fresh)} wheel(s) uploaded.")
            return 0
        # If we bounced off the new-project cap despite thinking every
        # project existed, fall through to the chunked path — it's more
        # defensive anyway. Otherwise we're out of options.
        combined = (result.stdout or "") + "\n" + (result.stderr or "")
        if not is_new_project_limit(combined):
            print(
                "\n[publish] single-shot upload failed; aborting.",
                file=sys.stderr,
                flush=True,
            )
            return 1
        print(
            "\n[publish] single-shot upload hit the new-project cap — "
            "falling back to chunked uploads",
            flush=True,
        )

    print(
        f"[publish] {len(new_project_names)} new project name(s) — "
        f"chunking uploads to respect PyPI's 20/hour new-project cap",
        flush=True,
    )
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

        # Each chunk gets the generic-429 retry loop inside upload_with_retry;
        # only the new-project cap escalates to the longer backoff_seconds
        # sleep (which then loops back to retry the same chunk).
        new_project_round = 0
        while True:
            result = upload_with_retry(chunk, repository_url)
            if result.returncode == 0:
                break
            combined = (result.stdout or "") + "\n" + (result.stderr or "")
            if is_new_project_limit(combined) and new_project_round < max_backoff_rounds:
                new_project_round += 1
                print(
                    f"\n[publish] chunk {chunk_num} hit new-project 429 — "
                    f"sleeping {backoff_seconds}s before retry "
                    f"{new_project_round}/{max_backoff_rounds}",
                    flush=True,
                )
                time.sleep(backoff_seconds)
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
