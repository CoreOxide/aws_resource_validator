"""Build per-service + shard wheels into ``dist/``.

Replaces the old ``scripts/create_subpackages.py`` (which wrote
``pyproject.toml`` files into the source tree and copied
``base_validator_model.py`` into every sub-package).

For each AWS service under ``aws_resource_validator/pydantic_models/``
this script:

  1. Stages the service subtree under ``build/<svc>/src/aws_resource_validator/pydantic_models/<svc>/``.
     The staged tree intentionally omits both
     ``aws_resource_validator/__init__.py`` and
     ``aws_resource_validator/pydantic_models/__init__.py`` so the
     wheel contributes to the PEP 420 namespace package defined by the
     main wheel.
  2. Writes a minimal ``pyproject.toml`` (hatchling backend) that
     depends on ``aws-resource-validator == <version>``.
  3. Builds the wheel via ``python -m build --wheel``.

For each shard in ``shards.toml`` this script stages a metadata-only
project whose dependency list is every service wheel in that shard.
Shard wheels contain no Python files — they're pure metapackages.

Build runs in parallel across services (``ProcessPoolExecutor``);
hatchling builds are light enough that the ~430 subprocess invocations
complete in minutes on a modern laptop.

Usage:
    python -m scripts.release.build_subpackages --outdir dist/
    python -m scripts.release.build_subpackages --outdir dist/ --only s3 ec2
    python -m scripts.release.build_subpackages --outdir dist/ --shard data
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess  # nosec B404 - used only with fixed argv lists; never shell=True
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path

from scripts.release._manifests import PYDANTIC_MODELS_DIR, REPO_ROOT, Manifest, Shard, resolve
from scripts.release._naming import extra_key, pypi_name, shard_pypi_name

BUILD_DIR = REPO_ROOT / "build"

SERVICE_PYPROJECT = """\
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "{pypi_name}"
version = "{version}"
description = "Pydantic v2 models for AWS {service}, shipped as a PEP 420 namespace extension of aws-resource-validator."
readme = "README.md"
license = {{ text = "Apache-2.0" }}
requires-python = ">=3.11"
authors = [
    {{ name = "Alexy Grabov", email = "alexy.grabov@gmail.com" }},
    {{ name = "Yafit Tupman", email = "ytupman@gmail.com" }},
]
dependencies = [
    "aws-resource-validator=={version}",
]
keywords = ["aws", "boto3", "pydantic", "{service}"]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

[project.urls]
Homepage = "https://coreoxide.github.io/aws_resource_validator/"
Repository = "https://github.com/CoreOxide/aws_resource_validator"

[tool.hatch.build.targets.wheel]
packages = ["src/aws_resource_validator"]
"""

SHARD_PYPROJECT = """\
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "{pypi_name}"
version = "{version}"
description = "{description}"
readme = "README.md"
license = {{ text = "Apache-2.0" }}
requires-python = ">=3.11"
authors = [
    {{ name = "Alexy Grabov", email = "alexy.grabov@gmail.com" }},
    {{ name = "Yafit Tupman", email = "ytupman@gmail.com" }},
]
dependencies = [
{dependencies}
]
keywords = ["aws", "boto3", "pydantic", "shard"]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python :: 3",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

[project.urls]
Homepage = "https://coreoxide.github.io/aws_resource_validator/"
Repository = "https://github.com/CoreOxide/aws_resource_validator"

[tool.hatch.build.targets.wheel]
packages = ["src/{placeholder_pkg}"]
"""

SERVICE_README = """\
# {pypi_name}

Pydantic v2 models for AWS `{service}`, shipped as a sibling namespace
wheel of [aws-resource-validator][main]. Install via the extras on the
main package:

```
pip install 'aws-resource-validator[{extra}]'
```

[main]: https://pypi.org/project/aws-resource-validator/
"""

SHARD_README = """\
# {pypi_name}

Metapackage that installs every AWS service wheel in the `{shard}`
domain ({description}). Install via the main package's extras:

```
pip install 'aws-resource-validator[{shard}]'
```
"""


@dataclass(frozen=True, slots=True)
class BuildJob:
    """A single hatchling build invocation the worker pool will execute."""

    name: str  # Reporting label (service or shard name).
    project_dir: Path  # Directory holding pyproject.toml.
    outdir: Path


def stage_service(service: str, version: str) -> Path:
    """Stage a service subtree under ``build/<service>/`` and return its root."""
    project_dir = BUILD_DIR / service
    shutil.rmtree(project_dir, ignore_errors=True)

    dest_service = project_dir / "src" / "aws_resource_validator" / "pydantic_models" / service
    dest_service.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(
        PYDANTIC_MODELS_DIR / service,
        dest_service,
        ignore=shutil.ignore_patterns("__pycache__"),
    )

    (project_dir / "pyproject.toml").write_text(
        SERVICE_PYPROJECT.format(
            pypi_name=pypi_name(service),
            version=version,
            service=service,
        ),
        encoding="utf-8",
    )
    (project_dir / "README.md").write_text(
        SERVICE_README.format(
            pypi_name=pypi_name(service),
            service=service,
            extra=extra_key(service),
        ),
        encoding="utf-8",
    )
    return project_dir


def stage_shard(shard: Shard, version: str) -> Path:
    """Stage a metapackage project for one shard and return its root."""
    project_dir = BUILD_DIR / f"shard-{shard.name}"
    shutil.rmtree(project_dir, ignore_errors=True)
    project_dir.mkdir(parents=True, exist_ok=True)

    dep_lines = ",\n".join(f'    "{pypi_name(svc)}=={version}"' for svc in sorted(shard.services))
    placeholder_pkg_name = f"_aws_resource_validator_{shard.name}_meta"
    description = shard.description or f"AWS {shard.name} domain metapackage"

    (project_dir / "pyproject.toml").write_text(
        SHARD_PYPROJECT.format(
            pypi_name=shard_pypi_name(shard.name),
            version=version,
            description=description,
            dependencies=dep_lines,
            placeholder_pkg=placeholder_pkg_name,
        ),
        encoding="utf-8",
    )
    (project_dir / "README.md").write_text(
        SHARD_README.format(
            pypi_name=shard_pypi_name(shard.name),
            shard=shard.name,
            description=description,
        ),
        encoding="utf-8",
    )
    # Hatchling refuses to produce a wheel with no source files. A single
    # placeholder package keeps the RECORD non-empty; it's never imported
    # because the wheel's reason for existing is its ``dependencies`` list.
    placeholder_pkg = project_dir / "src" / placeholder_pkg_name
    placeholder_pkg.mkdir(parents=True, exist_ok=True)
    (placeholder_pkg / "__init__.py").write_text(
        f'"""Metapackage marker for aws-resource-validator-{shard.name}."""\n',
        encoding="utf-8",
    )
    return project_dir


def run_build(job: BuildJob) -> tuple[str, int, str]:
    """Invoke ``python -m build --wheel`` inside ``job.project_dir``.

    Returns ``(name, returncode, combined_stderr)`` so the caller can
    collect failures after the pool drains.
    """
    proc = subprocess.run(  # nosec B603 - fixed argv; outdir/project_dir are Path instances resolved under BUILD_DIR
        [
            sys.executable,
            "-m",
            "build",
            "--wheel",
            "--outdir",
            str(job.outdir),
            str(job.project_dir),
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    tail = (proc.stderr or proc.stdout).splitlines()[-20:]
    return job.name, proc.returncode, "\n".join(tail)


def build_all(manifest: Manifest, outdir: Path, service_filter: set[str] | None, shard_filter: set[str] | None, workers: int) -> int:
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    outdir.mkdir(parents=True, exist_ok=True)

    jobs: list[BuildJob] = []

    services_to_build = list(manifest.services)
    if service_filter is not None:
        services_to_build = [s for s in services_to_build if s in service_filter]

    for svc in services_to_build:
        project_dir = stage_service(svc, manifest.version)
        jobs.append(BuildJob(name=svc, project_dir=project_dir, outdir=outdir))

    shards_to_build = manifest.shards
    if shard_filter is not None:
        shards_to_build = tuple(s for s in shards_to_build if s.name in shard_filter)

    for shard in shards_to_build:
        project_dir = stage_shard(shard, manifest.version)
        jobs.append(BuildJob(name=f"shard:{shard.name}", project_dir=project_dir, outdir=outdir))

    total = len(jobs)
    print(f"Building {total} wheels with {workers} workers into {outdir}", flush=True)

    failures: list[str] = []
    with ProcessPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(run_build, job) for job in jobs]
        for i, future in enumerate(as_completed(futures), start=1):
            name, code, tail = future.result()
            if code == 0:
                print(f"[{i}/{total}] ok:   {name}", flush=True)
            else:
                print(f"[{i}/{total}] FAIL: {name}\n{tail}", flush=True)
                failures.append(name)

    if failures:
        print(f"\n{len(failures)} build(s) failed:", file=sys.stderr)
        for name in failures:
            print(f"  - {name}", file=sys.stderr)
        return 1

    print(f"Built {total} wheel(s) into {outdir}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--outdir", type=Path, default=REPO_ROOT / "dist", help="Where to write wheels.")
    parser.add_argument("--only", nargs="*", metavar="SVC", help="Build only these services.")
    parser.add_argument("--shard", nargs="*", metavar="SHARD", help="Build only these shards (by name).")
    parser.add_argument("--no-services", action="store_true", help="Skip per-service builds (shards only).")
    parser.add_argument("--no-shards", action="store_true", help="Skip shard builds (services only).")
    parser.add_argument("--workers", type=int, default=min(8, (os.cpu_count() or 4)), help="Worker processes.")
    args = parser.parse_args(argv)

    manifest = resolve()
    service_filter = _resolve_filter(args.no_services, args.only)
    shard_filter = _resolve_filter(args.no_shards, args.shard)
    return build_all(manifest, args.outdir, service_filter, shard_filter, args.workers)


def _resolve_filter(skip_all: bool, only: list[str] | None) -> set[str] | None:
    if skip_all:
        return set()
    if only is not None:
        return set(only)
    return None


if __name__ == "__main__":
    raise SystemExit(main())
