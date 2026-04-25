"""Command-line entry point for both generation pipelines.

Run with ``arv-generate --help`` after installing the package in editable
mode. The CLI is intentionally thin: argument parsing, logging setup, and
delegation to the pipeline modules.
"""

from __future__ import annotations

import logging
from pathlib import Path

import typer

from aws_resource_validator.core.registry import APIRegistry
from aws_resource_validator.generator.common.logging import get_logger
from aws_resource_validator.generator.pipeline_a.code_writer import write_class_definitions
from aws_resource_validator.generator.pipeline_a.github_source import GitHubBotocoreSource
from aws_resource_validator.generator.pipeline_a.registry_builder import build_registry
from aws_resource_validator.generator.pipeline_b.orchestrator import emit_all as emit_pipeline_b
from aws_resource_validator.generator.pipeline_b.stubs_source import default_site_packages, discover_stubs

app = typer.Typer(help="Generate aws_resource_validator artifacts.", no_args_is_help=True)
_logger = get_logger(__name__)

# Repository layout is stable; computing paths relative to this file is less
# error-prone than making the user pass them in every time.
_PACKAGE_ROOT = Path(__file__).resolve().parents[1]
_DEFAULT_PIPELINE_A_OUTPUT = _PACKAGE_ROOT / "class_definitions.py"
_DEFAULT_PIPELINE_B_OUTPUT = _PACKAGE_ROOT / "pydantic_models"


def _configure_verbosity(verbose: bool) -> None:
    logging.getLogger().setLevel(logging.DEBUG if verbose else logging.INFO)


@app.command("pipeline-a")
def pipeline_a(
    token: str | None = typer.Option(None, "--token", envvar="GITHUB_TOKEN", help="GitHub API token."),
    output: Path = typer.Option(_DEFAULT_PIPELINE_A_OUTPUT, "--output", help="Destination class_definitions.py."),
    verbose: bool = typer.Option(False, "--verbose"),
) -> None:
    """Fetch botocore shapes and regenerate ``class_definitions.py``."""
    _configure_verbosity(verbose)
    source = GitHubBotocoreSource(token=token)
    registry: APIRegistry = build_registry(source.iter_services())
    write_class_definitions(registry, output)


@app.command("pipeline-b")
def pipeline_b(
    only: list[str] = typer.Option([], "--only", help="Limit to the given service names."),
    site_packages: Path | None = typer.Option(None, "--site-packages"),
    output: Path = typer.Option(_DEFAULT_PIPELINE_B_OUTPUT, "--output"),
    verbose: bool = typer.Option(False, "--verbose"),
) -> None:
    """Regenerate Pydantic models for every (or selected) AWS service."""
    _configure_verbosity(verbose)
    site = site_packages or default_site_packages()
    stubs = discover_stubs(site)
    if only:
        wanted = set(only)
        stubs = [s for s in stubs if s.service in wanted]
        missing = wanted - {s.service for s in stubs}
        if missing:
            _logger.warning("No stubs found for services: %s", ", ".join(sorted(missing)))
    _logger.info("Emitting Pydantic models for %d services to %s", len(stubs), output)
    emit_pipeline_b(stubs, output)


@app.command("all")
def run_all(
    token: str | None = typer.Option(None, "--token", envvar="GITHUB_TOKEN"),
    site_packages: Path | None = typer.Option(None, "--site-packages"),
    verbose: bool = typer.Option(False, "--verbose"),
) -> None:
    """Run both pipelines sequentially with their default destinations."""
    pipeline_a(token=token, output=_DEFAULT_PIPELINE_A_OUTPUT, verbose=verbose)
    pipeline_b(only=[], site_packages=site_packages, output=_DEFAULT_PIPELINE_B_OUTPUT, verbose=verbose)


if __name__ == "__main__":
    app()
