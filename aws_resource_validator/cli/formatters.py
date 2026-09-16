"""Rich terminal formatters for validation, inspection, and synthetic generation."""

from __future__ import annotations

from typing import TYPE_CHECKING

from rich import box
from rich.console import Console
from rich.markup import escape
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

if TYPE_CHECKING:
    from aws_resource_validator.cli.diagnostics import ValidationResult
    from aws_resource_validator.core.api_object import APIObject
    from aws_resource_validator.core.service import Service


def get_console() -> Console:
    """Create a default Rich console."""
    return Console()


def print_validation_result(console: Console, result: ValidationResult) -> None:
    """Render a formatted Rich panel displaying validation outcome and diagnostics."""
    if result.is_valid:
        status_badge = "[bold white on green]  PASS  [/bold white on green]"
        border_style = "green"
        summary = (
            f"[bold green]Value satisfies AWS constraints for "
            f"{escape(result.service_name)}.{escape(result.shape_name)}[/bold green]"
        )
    else:
        status_badge = "[bold white on red]  FAIL  [/bold white on red]"
        border_style = "red"
        summary = (
            f"[bold red]Value does NOT satisfy AWS constraints for "
            f"{escape(result.service_name)}.{escape(result.shape_name)}[/bold red]"
        )

    grid = Table.grid(padding=(0, 1))
    grid.add_column(style="bold cyan", justify="right", width=14)
    grid.add_column()

    grid.add_row("Status:", status_badge)
    grid.add_row("Summary:", summary)
    grid.add_row("Service:", f"[white]{escape(result.service_name)}[/white]")
    grid.add_row("Shape:", f"[white]{escape(result.shape_name)}[/white]")
    grid.add_row("Tested Value:", f"[bold white]{escape(result.value)}[/bold white]")

    # Length info
    min_l = str(result.min_length) if result.min_length is not None else "0"
    max_l = str(result.max_length) if result.max_length is not None else "unbounded"
    grid.add_row("Length:", f"{result.length} (allowed: {min_l} - {max_l})")
    grid.add_row("Regex Pattern:", f"[dim]{escape(result.pattern)}[/dim]")

    if result.errors:
        error_lines = "\n".join(f"[bold red]• {escape(err)}[/bold red]" for err in result.errors)
        grid.add_row("Errors:", error_lines)

    if result.warnings:
        warn_lines = "\n".join(f"[bold yellow]• {escape(w)}[/bold yellow]" for w in result.warnings)
        grid.add_row("Warnings:", warn_lines)

    panel = Panel(
        grid,
        title=f"[bold]Validation — {escape(result.service_name)}.{escape(result.shape_name)}[/bold]",
        border_style=border_style,
        expand=False,
    )
    console.print(panel)


def print_inspect_shape(console: Console, service_name: str, obj: APIObject) -> None:
    """Render a detailed panel showing shape metadata, constraints, and an example."""
    grid = Table.grid(padding=(0, 1))
    grid.add_column(style="bold cyan", justify="right", width=16)
    grid.add_column()

    grid.add_row("Service:", f"[bold white]{escape(service_name)}[/bold white]")
    grid.add_row("Shape:", f"[bold white]{escape(obj.name)}[/bold white]")
    grid.add_row("Botocore Type:", f"[white]{escape(obj.type)}[/white]")

    min_l = str(obj.min_length) if obj.min_length is not None else "None"
    max_l = str(obj.max_length) if obj.max_length is not None else "None"
    grid.add_row("Min Length:", min_l)
    grid.add_row("Max Length:", max_l)
    grid.add_row("Regex Pattern:", f"[yellow]{escape(obj.pattern)}[/yellow]")

    try:
        sample = obj.generate()
        grid.add_row("Sample Value:", f"[bold green]{escape(sample)}[/bold green]")
    except Exception as exc:
        grid.add_row("Sample Value:", f"[dim italic]Generation unavailable: {escape(str(exc))}[/dim italic]")

    panel = Panel(
        grid,
        title=f"[bold]Inspect: {escape(service_name)}.{escape(obj.name)}[/bold]",
        border_style="cyan",
        expand=False,
    )
    console.print(panel)


def print_inspect_service(console: Console, service: Service) -> None:
    """Render a table of all patterned shapes available in a service."""
    if not service.api_objects:
        console.print(
            f"[yellow]Service [bold]{escape(service.service_name)}[/bold] "
            "has no shapes with pattern constraints.[/yellow]"
        )
        return

    table = Table(
        title=f"Shapes in [bold cyan]{escape(service.service_name)}[/bold cyan] ({len(service.api_objects)} total)",
        box=box.ROUNDED,
        header_style="bold magenta",
    )
    table.add_column("Shape Name", style="bold cyan")
    table.add_column("Min", justify="right", style="green")
    table.add_column("Max", justify="right", style="green")
    table.add_column("Regex Pattern", style="yellow")
    table.add_column("Sample Value", style="white")

    for obj in service.api_objects.values():
        min_l = str(obj.min_length) if obj.min_length is not None else "-"
        max_l = str(obj.max_length) if obj.max_length is not None else "-"
        pattern_display = obj.pattern if len(obj.pattern) <= 40 else obj.pattern[:37] + "..."
        try:
            sample = obj.generate()
            if len(sample) > 30:
                sample = sample[:27] + "..."
        except Exception:
            sample = "-"
        table.add_row(obj.name, min_l, max_l, pattern_display, sample)

    console.print(table)


def print_generated_values(
    console: Console,
    service_name: str,
    shape_name: str,
    values: list[str],
    *,
    plain: bool = False,
) -> None:
    """Output generated synthetic values."""
    if plain:
        for val in values:
            console.print(val)
        return

    table = Table(
        title=f"Synthetic [bold cyan]{escape(service_name)}.{escape(shape_name)}[/bold cyan] ({len(values)} generated)",
        box=box.ROUNDED,
        header_style="bold magenta",
    )
    table.add_column("#", justify="right", style="dim")
    table.add_column("Generated Value", style="bold green")

    for idx, val in enumerate(values, start=1):
        table.add_row(str(idx), escape(val))

    console.print(table)


def print_services_list(
    console: Console,
    services: list[tuple[str, int]],
    total_count: int,
) -> None:
    """Render a table of registered AWS services and their shape counts."""
    table = Table(
        title=f"Registered AWS Services ({len(services)} shown of {total_count} total)",
        box=box.ROUNDED,
        header_style="bold magenta",
    )
    table.add_column("Service", style="bold cyan")
    table.add_column("Patterned Shapes", justify="right", style="green")

    for name, count in services:
        table.add_row(name, str(count))

    console.print(table)


def print_error(
    console: Console,
    message: str,
    *,
    suggestions: list[str] | None = None,
) -> None:
    """Display a formatted red error badge with optional typo suggestions."""
    badge = Text(" ERROR ", style="bold white on red")
    console.print(badge, f"[bold red]{escape(message)}[/bold red]")

    if suggestions:
        suggest_str = ", ".join(f"[bold cyan]{escape(s)}[/bold cyan]" for s in suggestions)
        console.print(f"  [dim]Did you mean:[/dim] {suggest_str}?")
