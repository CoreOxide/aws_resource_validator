"""Entry-point shim for the ``arv-generate`` script.

The generator pulls heavy optional dependencies (typer, jinja2, requests,
black) that we don't want to install for consumers who only use the
validator + pydantic models. Those deps live in the ``[generator]``
extra, and this module is the script target — importing the real CLI
lazily so that ``pip install aws-resource-validator`` (no extras) still
succeeds and ``arv-generate`` only fails when actually invoked.
"""

from __future__ import annotations


def main() -> None:
    try:
        from aws_resource_validator.generator.cli import app
    except ImportError as exc:
        raise SystemExit(
            "arv-generate requires the [generator] extra. Install with:\n"
            "    pip install 'aws-resource-validator[generator]'"
        ) from exc
    app()


if __name__ == "__main__":
    main()
