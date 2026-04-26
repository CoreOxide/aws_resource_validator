"""Legacy entrypoint delegating to the ``arv-generate`` CLI."""

from aws_resource_validator.generator.cli import app

if __name__ == "__main__":
    app()
