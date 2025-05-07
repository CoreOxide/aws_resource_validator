from inspect import getmembers, isclass

from pydantic_core import PydanticUndefined
from ruamel.yaml import YAML
from aws_resource_validator import class_definitions
from aws_resource_validator.class_definitions import Service
from pydantic import BaseModel
from typing import List, Tuple, Optional, Dict
from pathlib import Path
import importlib
import sys
import warnings

# Suppress all warnings related to field shadowing in Pydantic
warnings.filterwarnings("ignore", message='Field name .* shadows an attribute in parent "BaseValidatorModel"')

# Define the paths
API_DIR: Path = Path('../docs/api')
PYDANTIC_DIR: Path = Path('../docs/pydantic_models')
MKDOCS_YAML_PATH: Path = Path('../mkdocs.yml')

# Add the pydantic_models folder to the system path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'aws_resource_validator' / 'pydantic_models'))


# Function to create markdown for each class
def create_markdown_for_class(service_class: Service) -> str:
    md_content = f"# {service_class.service_name_} Service\n\n"

    if not service_class.api_objects:
        md_content += "Oops! This boto3 class is currently empty. Stay tuned!\n\n"
        md_content += '<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">\n'
    else:
        for api_object_name, api_object in service_class.api_objects.items():
            md_content += f"### {api_object.name}\n"
            md_content += f"- **Type**: {api_object.type}\n"
            md_content += f"- **Pattern**: `{api_object.pattern}`\n"
            if api_object.min_length is not None:
                md_content += f"- **Min Length**: {api_object.min_length}\n"
            if api_object.max_length is not None:
                md_content += f"- **Max Length**: {api_object.max_length}\n"
            md_content += "\n"

    return md_content


def create_markdown_for_pydantic_model(pydantic_model_class: BaseModel) -> str:
    md_content = f"# {pydantic_model_class.__name__}\n\n"

    fields = pydantic_model_class.model_fields
    if not fields:
        md_content += "Oops! This Pydantic model is currently empty. Stay tuned!\n\n"
        md_content += '<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">\n'
    else:
        for field_name, field_info in fields.items():
            md_content += f"### {field_name}\n"
            md_content += f"- **Type**: {field_info.annotation}\n"
            if field_info.default is not None and field_info.default is not PydanticUndefined:
                md_content += f"- **Default**: {field_info.default}\n"
            if field_info.is_required():
                md_content += f"- **Required**: Yes\n"
            md_content += "\n"

    return md_content


# Function to find all subclasses and generate markdown files
def generate_markdown_files(output_dir: Path, base_class: type, module) -> List[Tuple[str, str]]:
    output_dir.mkdir(parents=True, exist_ok=True)

    classes: List[base_class.__class__] = [cls for _, cls in getmembers(module, isclass) if
                                           issubclass(cls, base_class) and cls is not base_class]

    print(f"Detected {len(classes)} classes in {module.__name__}.")

    updated_classes: List[Tuple[str, str]] = []

    for cls in classes:
        instance = cls()
        if base_class is Service:
            md_content = create_markdown_for_class(instance)
        else:
            md_content = create_markdown_for_pydantic_model(instance)

        file_name = f"{cls.__name__.lower()}.md"
        file_path = output_dir / file_name
        if file_path.exists():
            with file_path.open('r', encoding='utf-8') as md_file:
                current_content = md_file.read()
            if current_content == md_content:
                continue
            else:
                update_type = 'updated'
        else:
            update_type = 'created'
        with file_path.open('w', encoding='utf-8') as md_file:
            md_file.write(md_content)
        updated_classes.append((cls.__name__, update_type))

    return updated_classes


# Function to generate markdown files for all Pydantic models in a directory (one file per module)
def generate_pydantic_markdown_files(output_dir: Path, models_dir: Path) -> List[Tuple[str, str]]:
    output_dir.mkdir(parents=True, exist_ok=True)

    updated_files: List[Tuple[str, str]] = []

    for model_file in models_dir.glob("**/*_classes.py"):  # Only process _classes.py files, recursively
        # Get the relative path from the models_dir
        rel_path = model_file.relative_to(models_dir)
        # Extract the parent directory (service name)
        service_name = rel_path.parts[0] if len(rel_path.parts) > 1 else ""
        # Get the module name without extension
        module_name = model_file.stem

        # Build the full module path
        if service_name:
            import_path = f"aws_resource_validator.pydantic_models.{service_name}.{module_name}"
            display_name = module_name
            file_name = f"{module_name.lower()}.md"
        else:
            import_path = f"aws_resource_validator.pydantic_models.{module_name}"
            display_name = module_name
            file_name = f"{module_name.lower()}.md"

        try:
            module = importlib.import_module(import_path)
            classes = [cls for _, cls in getmembers(module, isclass) if
                       issubclass(cls, BaseModel) and cls is not BaseModel]

            # Collect markdown content for all classes in the file
            md_content = f"# {display_name}\n\n".replace("_", ' ').title()
            for cls in classes:
                md_content += create_markdown_for_pydantic_model(cls) + "\n"

            # Create markdown file for the module (file-based)
            file_path = output_dir / file_name
            if file_path.exists():
                with file_path.open('r', encoding='utf-8') as md_file:
                    current_content = md_file.read()
                if current_content == md_content:
                    continue
                else:
                    update_type = 'updated'
            else:
                update_type = 'created'
            with file_path.open('w', encoding='utf-8') as md_file:
                md_file.write(md_content)
            updated_files.append((display_name, update_type))

        except ModuleNotFoundError as e:
            print(f"Module {import_path} not found: {e}")
            continue

    return updated_files


def main() -> None:
    updated_classes_api = generate_markdown_files(API_DIR, Service, class_definitions)
    updated_classes_pydantic = generate_pydantic_markdown_files(PYDANTIC_DIR, Path(
        __file__).resolve().parent.parent / 'aws_resource_validator' / 'pydantic_models')

    if updated_classes_api or updated_classes_pydantic:
        if updated_classes_api:
            print(f"Updated classes in api: {', '.join(f'{cls} ({utype})' for cls, utype in updated_classes_api)}")
        if updated_classes_pydantic:
            print(
                f"Updated classes in pydantic: {', '.join(f'{cls} ({utype})' for cls, utype in updated_classes_pydantic)}")
    else:
        print("Nothing to update.")


if __name__ == "__main__":
    main()