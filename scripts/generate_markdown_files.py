from inspect import getmembers, isclass
from ruamel.yaml import YAML

from aws_resource_validator import class_definitions
from aws_resource_validator.class_definitions import Service
from typing import List, Tuple, Optional, Dict
from pathlib import Path

# Define the paths
OUTER_DIR: Path = Path('../docs/api')
MKDOCS_YAML_PATH: Path = Path('../mkdocs.yml')


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


# Function to find all subclasses of Service and generate markdown files
def generate_markdown_files(output_dir: Path) -> List[Tuple[str, str]]:
    output_dir.mkdir(parents=True, exist_ok=True)

    service_classes: List[Service.__class__] = [cls for _, cls in getmembers(class_definitions, isclass) if
                                                issubclass(cls, Service) and cls is not Service]

    print(f"Detected {len(service_classes)} service classes.")

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
            updated_classes.append((service_class.__name__, update_type))

    return updated_classes


# Function to update only the 'API Reference' section in mkdocs.yml
def update_mkdocs_yml(mkdocs_yml_path: Path, api_dir: Path) -> Tuple[bool, Optional[List], List]:
    yaml = YAML()
    with open(mkdocs_yml_path, 'r', encoding='utf-8') as yml_file:
        mkdocs_config = yaml.load(yml_file)

    # Generate the API Reference nav entries
    api_files = sorted(api_dir.iterdir())
    api_nav: List[Dict[str, str]] = [
        {api_file.stem.capitalize(): str(api_file.relative_to(api_dir.parent)).replace("\\", "/")} for api_file in
        api_files]

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
        yaml.indent(mapping=2, sequence=4, offset=2)
        with mkdocs_yml_path.open('w', encoding='utf-8') as yml_file:
            yaml.dump(mkdocs_config, yml_file, )
        print("Updated mkdocs.yml with API reference documentation.")

    return nav_updated, original_nav, api_nav


def main() -> None:
    updated_classes = generate_markdown_files(OUTER_DIR)
    mkdocs_updates, original_nav, new_nav = update_mkdocs_yml(MKDOCS_YAML_PATH, OUTER_DIR)

    if updated_classes or mkdocs_updates:
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
