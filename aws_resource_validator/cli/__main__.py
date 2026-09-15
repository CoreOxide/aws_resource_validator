"""Entry point for the ``arv`` CLI command."""

from __future__ import annotations

from aws_resource_validator.cli.app import app


def main() -> None:
    """Execute the arv CLI."""
    app()


if __name__ == "__main__":
    main()
