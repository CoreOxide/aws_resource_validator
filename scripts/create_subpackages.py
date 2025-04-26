#!/usr/bin/env python3
import toml
from pathlib import Path

def create_service_pyproject(service_dir, model_name, version):
    """Create a pyproject.toml file in the service subfolder"""
    package_name = f"boto3-pydantic-{model_name}"

    pyproject_content = {
        "build-system": {
            "requires": ["poetry-core"],
            "build-backend": "poetry.core.masonry.api"
        },
        "tool": {
            "poetry": {
                "name": package_name,
                "version": version,
                "description": f"Pydantic models for AWS {model_name.capitalize()}",
                "authors": [
                    "Original Package Author <author@example.com>"
                ],
                "dependencies": {
                    "python": "^3.9 || ^3.12 || ^3.13",
                    "pydantic": "^2.8.2",
                    "botocore": "*"
                }
            }
        }
    }

    with open(service_dir / "pyproject.toml", "w") as f:
        toml.dump(pyproject_content, f)

    print(f"Created pyproject.toml in {service_dir}")

def main():
    # Read the original project version
    main_pyproject = toml.load("../pyproject.toml")
    version = main_pyproject["tool"]["poetry"]["version"]

    # Base directory for pydantic models
    base_dir = Path("../aws_resource_validator/pydantic_models")

    # Create pyproject.toml in each service subfolder
    for model_dir in base_dir.iterdir():
        if model_dir.is_dir() and not model_dir.name.startswith("__"):
            create_service_pyproject(model_dir, model_dir.name, version)

    print(f"Created pyproject.toml files in all service subfolders")

if __name__ == "__main__":
    main()
