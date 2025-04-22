#!/usr/bin/env python3
import os
import shutil
import toml
from pathlib import Path

def create_subpackage(model_name, base_dir, version):
    """Create a sub-package for a specific model directory"""
    # Create package directories
    package_name = f"boto3-pydantic-{model_name}"
    package_dir = Path(f"packages/{package_name}")
    src_dir = package_dir / "src" / "boto3_pydantic"
    model_dir = src_dir / model_name
    
    os.makedirs(model_dir, exist_ok=True)
    
    # Copy the base validator model
    base_validator_path = base_dir.parent / "base_validator_model.py"
    shutil.copy2(base_validator_path, src_dir / "base_validator_model.py")
    
    # Copy all model files
    source_model_dir = base_dir / model_name
    for file in source_model_dir.glob("**/*.py"):
        # Create corresponding directories in the target if needed
        relative_path = file.relative_to(source_model_dir)
        target_file = model_dir / relative_path
        os.makedirs(target_file.parent, exist_ok=True)
        shutil.copy2(file, target_file)
    
    # Create package __init__ files
    with open(src_dir / "__init__.py", "w") as f:
        f.write(f"from . import {model_name}\n")
    
    with open(model_dir / "__init__.py", "w") as f:
        f.write(f"# boto3-pydantic-{model_name} package\n")
        f.write("from .__about__ import __version__\n")
    
    # Create __about__.py with version info
    with open(model_dir / "__about__.py", "w") as f:
        f.write(f'__version__ = "{version}"\n')
    
    # Create pyproject.toml
    create_pyproject(package_dir, package_name, model_name, version)
    
    # Create README
    create_readme(package_dir, package_name, model_name)
    
    print(f"Created sub-package: {package_name}")
    
def create_pyproject(package_dir, package_name, model_name, version):
    """Create the pyproject.toml file for the sub-package"""
    pyproject_content = {
        "build-system": {
            "requires": ["hatchling"],
            "build-backend": "hatchling.build"
        },
        "project": {
            "name": package_name,
            "version": version,
            "description": f"Pydantic models for AWS {model_name.capitalize()}",
            "readme": "README.md",
            "requires-python": ">=3.8",
            "authors": [
                {"name": "Original Package Author", "email": "author@example.com"}
            ],
            "classifiers": [
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
            ],
            "dependencies": [
                "pydantic>=2.0.0",
                "boto3",
            ]
        },
        "project.urls": {
            "Homepage": "https://github.com/yourusername/aws_resource_validator",
            "Documentation": "https://github.com/yourusername/aws_resource_validator#readme",
            "Bug Tracker": "https://github.com/yourusername/aws_resource_validator/issues"
        }
    }
    
    with open(package_dir / "pyproject.toml", "w") as f:
        toml.dump(pyproject_content, f)

def create_readme(package_dir, package_name, model_name):
    """Create a README.md file for the sub-package"""
    with open(package_dir / "README.md", "w") as f:
        f.write(f"# {package_name}\n\n")
        f.write(f"Pydantic models for AWS {model_name.capitalize()} service.\n\n")
        f.write("This package contains type-annotated classes for AWS resources validation.\n")

def main():
    # Read the original project version
    main_pyproject = toml.load("pyproject.toml")
    version = main_pyproject["project"]["version"]
    
    # Base directory for pydantic models
    base_dir = Path("aws_resource_validator/pydantic_models")
    
    # Create 'packages' directory if it doesn't exist
    os.makedirs("packages", exist_ok=True)

    # For demonstration, create the accessanalyzer package
    create_subpackage("accessanalyzer", base_dir, version)
    
    # Uncomment to create packages for all model directories
    # for model_dir in base_dir.iterdir():
    #     if model_dir.is_dir() and not model_dir.name.startswith("__"):
    #         create_subpackage(model_dir.name, base_dir, version)

if __name__ == "__main__":
    main()
