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

    for model_file in models_dir.glob("*_classes.py"):  # Only process _classes.py files
        module_name = model_file.stem
        try:
            module = importlib.import_module(f"aws_resource_validator.pydantic_models.{module_name}")
            classes = [cls for _, cls in getmembers(module, isclass) if
                       issubclass(cls, BaseModel) and cls is not BaseModel]

            # Collect markdown content for all classes in the file
            md_content = f"# Pydantic Models in {module_name}\n\n"
            for cls in classes:
                md_content += create_markdown_for_pydantic_model(cls) + "\n"

            # Create markdown file for the module (file-based)
            file_name = f"{module_name.lower()}.md"
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
            updated_files.append((module_name, update_type))

        except ModuleNotFoundError as e:
            print(f"Module {module_name} not found: {e}")
            continue

    return updated_files


# Function to update mkdocs.yml with separate sections for API Reference and Pydantic Models
def update_mkdocs_yml(mkdocs_yml_path: Path, api_dir: Path, pydantic_dir: Path) -> Tuple[
    bool, Optional[Dict[str, List]], Dict[str, List]]:
    yaml = YAML()
    with open(mkdocs_yml_path, 'r', encoding='utf-8') as yml_file:
        mkdocs_config = yaml.load(yml_file)

    # Generate the API Reference nav entries
    api_files = sorted(api_dir.iterdir())
    api_nav: List[Dict[str, str]] = [
        {api_file.stem.capitalize(): str(api_file.relative_to(api_dir.parent)).replace("\\", "/")} for api_file in
        api_files]

    # Generate the Pydantic Models nav entries
    pydantic_files = sorted(pydantic_dir.iterdir())
    pydantic_nav: List[Dict[str, str]] = [
        {pydantic_file.stem.capitalize(): str(pydantic_file.relative_to(pydantic_dir.parent)).replace("\\", "/")} for
        pydantic_file in
        pydantic_files]

    nav_updated = False
    original_nav = {'API Reference': None, 'Pydantic Models': None}

    # Update the 'API Reference' section in the nav
    for item in mkdocs_config['nav']:
        if isinstance(item, dict) and 'API Reference' in item:
            original_nav['API Reference'] = item['API Reference']
            if item['API Reference'] != api_nav:
                item['API Reference'] = api_nav
                nav_updated = True
            break
    else:
        mkdocs_config['nav'].append({'API Reference': api_nav})
        nav_updated = True

    # Update the 'Pydantic Models' section in the nav
    for item in mkdocs_config['nav']:
        if isinstance(item, dict) and 'Pydantic Models' in item:
            original_nav['Pydantic Models'] = item['Pydantic Models']
            if item['Pydantic Models'] != pydantic_nav:
                item['Pydantic Models'] = pydantic_nav
                nav_updated = True
            break
    else:
        mkdocs_config['nav'].append({'Pydantic Models': pydantic_nav})
        nav_updated = True

    if nav_updated:
        yaml.indent(mapping=2, sequence=4, offset=2)
        with mkdocs_yml_path.open('w', encoding='utf-8') as yml_file:
            yaml.dump(mkdocs_config, yml_file)
        print("Updated mkdocs.yml with API reference and Pydantic models documentation.")

    return nav_updated, original_nav, {'API Reference': api_nav, 'Pydantic Models': pydantic_nav}


def main() -> None:
    updated_classes_api = generate_markdown_files(API_DIR, Service, class_definitions)
    updated_classes_pydantic = generate_pydantic_markdown_files(PYDANTIC_DIR, Path(
        __file__).resolve().parent.parent / 'aws_resource_validator' / 'pydantic_models')
    mkdocs_updates, original_nav, new_nav = update_mkdocs_yml(MKDOCS_YAML_PATH, API_DIR, PYDANTIC_DIR)

    if updated_classes_api or updated_classes_pydantic or mkdocs_updates:
        if updated_classes_api:
            print(f"Updated classes in api: {', '.join(f'{cls} ({utype})' for cls, utype in updated_classes_api)}")
        if updated_classes_pydantic:
            print(
                f"Updated classes in pydantic: {', '.join(f'{cls} ({utype})' for cls, utype in updated_classes_pydantic)}")
        if mkdocs_updates:
            print("mkdocs.yml was updated.")
            if original_nav:
                print(f"Original 'API Reference': {original_nav['API Reference']}")
                print(f"Original 'Pydantic Models': {original_nav['Pydantic Models']}")
            print(f"New 'API Reference': {new_nav['API Reference']}")
            print(f"New 'Pydantic Models': {new_nav['Pydantic Models']}")
    else:
        print("Nothing to update.")


if __name__ == "__main__":
    main()
