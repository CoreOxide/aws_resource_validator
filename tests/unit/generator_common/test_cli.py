"""Smoke tests for the ``arv-generate`` CLI entry point."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import patch

import pytest
from typer.testing import CliRunner

from aws_resource_validator.generator.cli import app

runner = CliRunner()


def test_help_lists_all_commands() -> None:
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    for command in ("pipeline-a", "pipeline-b", "all"):
        assert command in result.stdout


def test_pipeline_b_delegates_to_orchestrator(tmp_path: Path) -> None:
    with (
        patch("aws_resource_validator.generator.cli.discover_stubs", return_value=[]) as discover,
        patch("aws_resource_validator.generator.cli.emit_pipeline_b") as emit,
    ):
        result = runner.invoke(app, ["pipeline-b", "--output", str(tmp_path), "--site-packages", str(tmp_path)])

    assert result.exit_code == 0
    discover.assert_called_once()
    emit.assert_called_once()


def test_pipeline_b_only_flag_filters_stubs(tmp_path: Path) -> None:
    fake_stub = type("Stub", (), {"service": "acm"})()
    with (
        patch("aws_resource_validator.generator.cli.discover_stubs", return_value=[fake_stub]),
        patch("aws_resource_validator.generator.cli.emit_pipeline_b") as emit,
    ):
        result = runner.invoke(
            app,
            ["pipeline-b", "--only", "acm", "--output", str(tmp_path), "--site-packages", str(tmp_path)],
        )

    assert result.exit_code == 0
    args, _kwargs = emit.call_args
    passed_stubs = list(args[0])
    assert [s.service for s in passed_stubs] == ["acm"]


@pytest.mark.parametrize("command", ["pipeline-a", "pipeline-b", "all"])
def test_command_has_help(command: str) -> None:
    result = runner.invoke(app, [command, "--help"])
    assert result.exit_code == 0
