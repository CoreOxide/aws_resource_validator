import os
import importlib.util
from inspect import getmembers, isclass
import yaml
from typing import List, Tuple, Optional
from pathlib import Path

# Define the paths
class_definitions_path = Path('../aws_resource_validator/class_definitions.py')
output_dir = Path('../docs/api')
mkdocs_yml_path = Path('../mkdocs.yml')

# Load the module from the given path
spec = importlib.util.spec_from_file_location("class_definitions", class_definitions_path)
class_definitions = importlib.util.module_from_spec(spec)
spec.loader.exec_module(class_definitions)


# Ensure Service and APIObject are defined or imported here
class Service:
    def __init__(self, name: str):
        self.service_name_ = name
        self.api_objects = {}

    def add_api_object(self, name: str, api_object: 'APIObject'):
        self.api_objects[name] = api_object


class APIObject:
    def __init__(self, name: str, type: str, pattern: str, min_length: Optional[int], max_length: Optional[int]):
        self.name = name
        self.type = type
        self.pattern = pattern
        self.min_length = min_length
        self.max_length = max_length


# Function to create markdown for each class
def create_markdown_for_class(service_class: Service) -> str:
    md_content = f"# {service_class.service_name_} Service\n\n"

    if not service_class.api_objects:
        md_content += "Oops! This boto3 class is currently empty. Stay tuned!\n\n"
        md_content += '<img src="..\images\oops_loki.png" width="500" height="400" title="Oops Loki">\n'
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


# Function to find all subclasses of Service and generate markdown files
def generate_markdown_files(output_dir: Path) -> Tuple[bool, List[Tuple[str, str]]]:
    if not output_dir.exists():
        output_dir.mkdir(parents=True)

    service_classes = [cls for _, cls in getmembers(class_definitions, isclass) if
                       issubclass(cls, class_definitions.Service) and cls is not class_definitions.Service]

    print(f"Detected {len(service_classes)} service classes.")

    updates_made = False
    updated_classes: List[Tuple[str, str]] = []

    for service_class in service_classes:
        instance = service_class()
        if isinstance(instance.service_name_, str) and instance.service_name_:
            md_content = create_markdown_for_class(instance)
            file_name = f"{service_class.__name__.lower()}.md"
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
            updates_made = True
            updated_classes.append((service_class.__name__, update_type))

    return updates_made, updated_classes


# Function to update only the 'API Reference' section in mkdocs.yml
def update_mkdocs_yml(mkdocs_yml_path: Path, api_dir: Path) -> Tuple[bool, Optional[List], List]:
    with mkdocs_yml_path.open('r', encoding='utf-8') as yml_file:
        mkdocs_config = yaml.safe_load(yml_file)

    # Generate the API Reference nav entries
    api_files = sorted(api_dir.iterdir())
    api_nav = [{'{}'.format(api_file.stem.capitalize()): str(api_file.relative_to(api_dir.parent)).replace("\\", "/")} for api_file in api_files]

    # Update only the 'API Reference' section in the nav
    nav_updated = False
    original_nav = None
    for item in mkdocs_config['nav']:
        if isinstance(item, dict) and 'API Reference' in item:
            original_nav = item['API Reference']
            if item['API Reference'] != api_nav:
                item['API Reference'] = api_nav
                nav_updated = True
            break

    if not nav_updated and original_nav is None:
        mkdocs_config['nav'].append({'API Reference': api_nav})
        nav_updated = True

    if nav_updated:
        with mkdocs_yml_path.open('w', encoding='utf-8') as yml_file:
            yaml.safe_dump(mkdocs_config, yml_file, line_break='\n\n', allow_unicode=True, sort_keys=False)
        print("Updated mkdocs.yml with API reference documentation.")

    return nav_updated, original_nav, api_nav


def main() -> None:
    markdown_updates, updated_classes = generate_markdown_files(output_dir)
    mkdocs_updates, original_nav, new_nav = update_mkdocs_yml(mkdocs_yml_path, output_dir)

    if markdown_updates or mkdocs_updates:
        if updated_classes:
            print(f"Updated classes: {', '.join(f'{cls} ({utype})' for cls, utype in updated_classes)}")
        if mkdocs_updates:
            print("mkdocs.yml was updated.")
            if original_nav:
                print(f"Original 'API Reference': {original_nav}")
            print(f"New 'API Reference': {new_nav}")
    else:
        print("Nothing to update.")


if __name__ == "__main__":
    main()
