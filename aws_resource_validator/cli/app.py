"""Typer application for the ``arv`` command-line interface."""

from __future__ import annotations

import json
import platform
import sys
from typing import Any

import rich
import typer

from aws_resource_validator import __version__
from aws_resource_validator.cli.diagnostics import diagnose_validation
from aws_resource_validator.cli.formatters import (
    get_console,
    print_error,
    print_generated_values,
    print_inspect_service,
    print_inspect_shape,
    print_services_list,
    print_validation_result,
)
from aws_resource_validator.cli.resolver import (
    get_registry,
    list_services,
    resolve_service,
    resolve_shape,
)

app = typer.Typer(
    name="arv",
    help="AWS Resource Validator: inspect AWS constraints, validate resource names, and generate test data.",
    no_args_is_help=True,
    add_completion=True,
)


def _output_json(data: Any) -> None:
    """Print machine-readable JSON directly to standard output without terminal markup."""
    print(json.dumps(data, indent=2))


@app.command("validate")
def validate(
    service: str = typer.Argument(..., help="AWS service name (e.g. lambda, dynamodb, s3control)."),
    shape: str = typer.Argument(..., help="AWS shape or resource name (e.g. FunctionName, TableName)."),
    value: str = typer.Argument(..., help="Candidate value to test against AWS naming constraints."),
    strict: bool = typer.Option(
        False,
        "--strict",
        "-s",
        help="Enforce end-to-end regex matching instead of botocore prefix matching.",
    ),
    json_output: bool = typer.Option(False, "--json", help="Output result as JSON."),
) -> None:
    """Validate an AWS resource name against botocore patterns and length limits."""
    console = get_console()
    svc, svc_suggestions = resolve_service(service)

    if svc is None:
        if json_output:
            _output_json({"error": f"Service '{service}' not found", "suggestions": svc_suggestions})
        else:
            print_error(console, f"Service '{service}' not found.", suggestions=svc_suggestions)
        raise typer.Exit(code=2)

    obj, shape_suggestions = resolve_shape(svc, shape)
    if obj is None:
        if json_output:
            _output_json(
                {"error": f"Shape '{shape}' not found in {svc.service_name}", "suggestions": shape_suggestions}
            )
        else:
            print_error(
                console,
                f"Shape '{shape}' not found in service '{svc.service_name}'.",
                suggestions=shape_suggestions,
            )
        raise typer.Exit(code=2)

    result = diagnose_validation(obj, svc.service_name, value, strict=strict)

    if json_output:
        _output_json(result.to_dict())
    else:
        print_validation_result(console, result)

    if not result.is_valid:
        raise typer.Exit(code=1)


@app.command("inspect")
def inspect(
    service: str = typer.Argument(..., help="AWS service name (e.g. lambda, dynamodb, s3control)."),
    shape: str | None = typer.Argument(None, help="Optional shape name to inspect specifically."),
    json_output: bool = typer.Option(False, "--json", help="Output details as JSON."),
) -> None:
    """Inspect regex pattern constraints, length limits, and sample values."""
    console = get_console()
    svc, svc_suggestions = resolve_service(service)

    if svc is None:
        if json_output:
            _output_json({"error": f"Service '{service}' not found", "suggestions": svc_suggestions})
        else:
            print_error(console, f"Service '{service}' not found.", suggestions=svc_suggestions)
        raise typer.Exit(code=2)

    if shape is not None:
        obj, shape_suggestions = resolve_shape(svc, shape)
        if obj is None:
            if json_output:
                _output_json(
                    {"error": f"Shape '{shape}' not found in {svc.service_name}", "suggestions": shape_suggestions}
                )
            else:
                print_error(
                    console,
                    f"Shape '{shape}' not found in service '{svc.service_name}'.",
                    suggestions=shape_suggestions,
                )
            raise typer.Exit(code=2)

        if json_output:
            data = {
                "service": svc.service_name,
                "shape": obj.name,
                "type": obj.type,
                "pattern": obj.pattern,
                "min_length": obj.min_length,
                "max_length": obj.max_length,
            }
            _output_json(data)
        else:
            print_inspect_shape(console, svc.service_name, obj)
        return

    # Inspect all shapes in service
    if json_output:
        shapes_data = [
            {
                "shape": obj.name,
                "type": obj.type,
                "pattern": obj.pattern,
                "min_length": obj.min_length,
                "max_length": obj.max_length,
            }
            for obj in svc.api_objects.values()
        ]
        _output_json({"service": svc.service_name, "shapes": shapes_data})
    else:
        print_inspect_service(console, svc)


@app.command("generate")
def generate(
    service: str = typer.Argument(..., help="AWS service name (e.g. lambda, dynamodb)."),
    shape: str = typer.Argument(..., help="Shape name (e.g. FunctionName)."),
    count: int = typer.Option(1, "--count", "-c", min=1, max=100, help="Number of synthetic values to generate."),
    plain: bool = typer.Option(
        False,
        "--plain",
        "-p",
        help="Print raw values one per line (ideal for shell scripts and pipelines).",
    ),
    json_output: bool = typer.Option(False, "--json", help="Output values as a JSON list."),
) -> None:
    """Generate compliant synthetic test values satisfying AWS constraints."""
    console = get_console()
    svc, svc_suggestions = resolve_service(service)

    if svc is None:
        if json_output:
            _output_json({"error": f"Service '{service}' not found", "suggestions": svc_suggestions})
        else:
            print_error(console, f"Service '{service}' not found.", suggestions=svc_suggestions)
        raise typer.Exit(code=2)

    obj, shape_suggestions = resolve_shape(svc, shape)
    if obj is None:
        if json_output:
            _output_json(
                {"error": f"Shape '{shape}' not found in {svc.service_name}", "suggestions": shape_suggestions}
            )
        else:
            print_error(
                console,
                f"Shape '{shape}' not found in service '{svc.service_name}'.",
                suggestions=shape_suggestions,
            )
        raise typer.Exit(code=2)

    values = [obj.generate() for _ in range(count)]

    if json_output:
        _output_json({"service": svc.service_name, "shape": obj.name, "values": values})
    else:
        print_generated_values(console, svc.service_name, obj.name, values, plain=plain)


@app.command("list")
def list_cmd(
    service: str | None = typer.Argument(None, help="Optional service name to list shapes for."),
    search: str | None = typer.Option(None, "--search", "-s", help="Filter services by name substring."),
    json_output: bool = typer.Option(False, "--json", help="Output as JSON."),
) -> None:
    """List supported AWS services and their validated shape counts."""
    console = get_console()

    if service is not None:
        # Delegate to inspect
        inspect(service=service, shape=None, json_output=json_output)
        return

    services = list_services(query=search)
    total_registry_count = len(get_registry())

    if json_output:
        data = [{"service": s, "shape_count": c} for s, c in services]
        _output_json(data)
    else:
        print_services_list(console, services, total_count=total_registry_count)


@app.command("version")
def version() -> None:
    """Display version information for arv and its runtime environment."""
    console = get_console()
    console.print(f"[bold cyan]aws-resource-validator (arv)[/bold cyan] version [bold green]{__version__}[/bold green]")
    console.print(f"  Python:  {platform.python_version()} ({sys.executable})")
    console.print(f"  Rich:    {rich.__file__}")
    console.print(f"  Typer:   {typer.__version__}")
