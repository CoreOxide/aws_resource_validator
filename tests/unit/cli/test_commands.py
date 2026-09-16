"""Integration / smoke tests for CLI subcommands via Typer CliRunner."""

from __future__ import annotations

import json

from typer.testing import CliRunner

from aws_resource_validator import __version__
from aws_resource_validator.cli.app import app

runner = CliRunner()


def test_version_command() -> None:
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert __version__ in result.stdout
    assert "Python:" in result.stdout


def test_validate_success() -> None:
    result = runner.invoke(app, ["validate", "lambda", "FunctionName", "my-function-name"])
    assert result.exit_code == 0
    assert "PASS" in result.stdout
    assert "Lambda.FunctionName" in result.stdout


def test_validate_success_json() -> None:
    result = runner.invoke(app, ["validate", "lambda", "FunctionName", "my-function-name", "--json"])
    assert result.exit_code == 0
    data = json.loads(result.stdout)
    assert data["is_valid"] is True
    assert data["service_name"] == "Lambda"
    assert data["shape_name"] == "FunctionName"


def test_validate_failure() -> None:
    result = runner.invoke(app, ["validate", "lambda", "FunctionName", "invalid func! name", "--strict"])
    assert result.exit_code == 1
    assert "FAIL" in result.stdout


def test_validate_failure_json() -> None:
    result = runner.invoke(
        app,
        ["validate", "lambda", "FunctionName", "invalid func! name", "--strict", "--json"],
    )
    assert result.exit_code == 1
    data = json.loads(result.stdout)
    assert data["is_valid"] is False
    assert len(data["errors"]) > 0


def test_validate_unknown_service() -> None:
    result = runner.invoke(app, ["validate", "nonexistentservice", "SomeShape", "val"])
    assert result.exit_code == 2
    assert "not found" in result.stdout


def test_validate_unknown_shape() -> None:
    result = runner.invoke(app, ["validate", "lambda", "NonExistentShape", "val"])
    assert result.exit_code == 2
    assert "not found" in result.stdout


def test_inspect_shape() -> None:
    result = runner.invoke(app, ["inspect", "lambda", "FunctionName"])
    assert result.exit_code == 0
    assert "Inspect: Lambda.FunctionName" in result.stdout
    assert "Regex Pattern:" in result.stdout


def test_inspect_shape_json() -> None:
    result = runner.invoke(app, ["inspect", "lambda", "FunctionName", "--json"])
    assert result.exit_code == 0
    data = json.loads(result.stdout)
    assert data["service"] == "Lambda"
    assert data["shape"] == "FunctionName"
    assert "pattern" in data


def test_inspect_service_all_shapes() -> None:
    result = runner.invoke(app, ["inspect", "lambda"])
    assert result.exit_code == 0
    assert "Shapes in Lambda" in result.stdout
    assert "FunctionName" in result.stdout


def test_inspect_service_json() -> None:
    result = runner.invoke(app, ["inspect", "lambda", "--json"])
    assert result.exit_code == 0
    data = json.loads(result.stdout)
    assert data["service"] == "Lambda"
    assert len(data["shapes"]) > 0


def test_generate_default() -> None:
    result = runner.invoke(app, ["generate", "lambda", "FunctionName"])
    assert result.exit_code == 0
    assert "Synthetic" in result.stdout
    assert "Lambda.FunctionName" in result.stdout
    assert "Generated Value" in result.stdout


def test_generate_plain() -> None:
    result = runner.invoke(app, ["generate", "lambda", "FunctionName", "--count", "3", "--plain"])
    assert result.exit_code == 0
    lines = [line.strip() for line in result.stdout.strip().splitlines() if line.strip()]
    assert len(lines) == 3


def test_generate_json() -> None:
    result = runner.invoke(app, ["generate", "lambda", "FunctionName", "--count", "2", "--json"])
    assert result.exit_code == 0
    data = json.loads(result.stdout)
    assert data["service"] == "Lambda"
    assert data["shape"] == "FunctionName"
    assert len(data["values"]) == 2


def test_list_services() -> None:
    result = runner.invoke(app, ["list"])
    assert result.exit_code == 0
    assert "Registered AWS Services" in result.stdout


def test_list_services_search() -> None:
    result = runner.invoke(app, ["list", "--search", "dynamodb"])
    assert result.exit_code == 0
    assert "Dynamodb" in result.stdout


def test_list_delegates_to_inspect_when_service_provided() -> None:
    result = runner.invoke(app, ["list", "lambda"])
    assert result.exit_code == 0
    assert "Shapes in Lambda" in result.stdout
