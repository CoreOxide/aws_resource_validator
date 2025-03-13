"""
This module provides functionality to generate Pydantic models and constants files from TypedDict
definitions and literals found in the `mypy_boto3_*` packages within a virtual environment.

The main functions in this module include:
- `parse_type_defs`: Parses `type_defs.py` files to extract TypedDict definitions.
- `generate_pydantic_models`: Generates Pydantic models from TypedDict definitions.
- `parse_literals`: Parses `literals.py` files to extract literal definitions.
- `generate_constants_file`: Generates a constants file from literals and other definitions.
- `generate_models`: Main function to process all `mypy_boto3_*` packages and generate the corresponding
  Pydantic models and constants files.

The generated files are saved in the `aws_resource_validator/pydantic_models` directory.
"""
import os
import re
from typing import Dict, Tuple

# Define file paths
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
venv_path = os.path.join(project_root, '.venv', 'lib', 'python3.12', 'site-packages')
output_dir = os.path.join(project_root, 'aws_resource_validator', 'pydantic_models')

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)


# pylint: disable=too-many-locals
def parse_type_defs(file_path: str) -> Tuple[Dict[str, Dict[str, str]], Dict[str, str]]:
    """
    Parse the `type_defs.py` file to extract TypedDict definitions (including multi-line fields).

    Returns:
        (type_defs, other_defs):
            type_defs: { 'DomainValidationTypeDef': {
                'DomainName': 'str',
                'ValidationEmails': 'Optional[List[str]]',
                ...
            }, ... }
            other_defs: {}  # For any other definitions you might parse
    """
    type_defs, other_defs = {}, {}

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Extract each TypedDict block:
    #    This finds "class <Name>(TypedDict):" plus the subsequent indented lines.
    #    The body is captured in group(2).
    typed_dict_blocks = re.findall(
        r'class\s+(\w+)\(TypedDict\):\s*'         # class Foo(TypedDict):
        r'((?:\n[ \t]+[^\n]+)+)',                 # One or more lines of indentation and content
        content,
        flags=re.DOTALL
    )

    for type_name, body in typed_dict_blocks:
        # We'll parse each typed-dict block line by line
        fields = {}

        # Split out the block lines (indented lines)
        lines = body.splitlines()
        current_field = None
        field_lines: list[str] = []

        for raw_line in lines:
            line = raw_line.strip()
            # Skip empty or comment-only lines
            if not line or line.startswith('#'):
                continue

            # Check if this line starts a new field, like "Foo: Bar"
            field_match = re.match(r'^(\w+):\s*(.*)', line)
            if field_match:
                # If we were already accumulating a previous field, finalize it
                if current_field:
                    combined_field = ' '.join(field_lines).strip()
                    # Convert NotRequired[...] to Optional[...]
                    combined_field = combined_field.replace('NotRequired[', 'Optional[')
                    fields[current_field] = combined_field

                # Start a new field
                current_field = field_match.group(1)
                # Start collecting the field's type annotation (which might be multiline)
                field_lines = [field_match.group(2)]
            else:
                # This line continues the current field definition (multiline union, etc.)
                field_lines.append(line)

        # End of block: store the last field if it exists
        if current_field:
            combined_field = ' '.join(field_lines).strip()
            combined_field = combined_field.replace('NotRequired[', 'Optional[')
            fields[current_field] = combined_field

        # Store the parsed fields under the typed dict name
        type_defs[type_name] = fields

    return type_defs, other_defs


def generate_pydantic_models(type_defs: Dict[str, Dict[str, str]], service_name: str, file_path: str):
    generated = set()
    imports = set([
        "from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel, EventStream",
        "from datetime import datetime"
    ])
    type_imports = {
        "Optional": "from typing import Optional",
        "List": "from typing import List",
        "Union": "from typing import Union",
        "Dict": "from typing import Dict",
        "Any": "from typing import Any",
        "Literal": "from typing import Literal",
        "Sequence": "from typing import Sequence",
        "Mapping": "from typing import Mapping",
        "IO": "from typing import IO",
        "StreamingBody": "from botocore.response import StreamingBody"
    }

    def generate_model(name: str):
        if name in generated:
            return
        fields = type_defs.get(name, {})

        nested_types = set(re.findall(r'(\w+TypeDef)', ' '.join(fields.values())))
        for nested in nested_types:
            if nested != name:
                generate_model(nested)

        model_lines = [f"class {name}(BaseValidatorModel):"]
        if fields:
            for field_name, field_type in fields.items():
                if 'Optional[' in field_type:
                    model_lines.append(f"    {field_name}: {field_type} = None")
                else:
                    model_lines.append(f"    {field_name}: {field_type}")
        else:
            model_lines.append("    pass")
        model_lines.append("\n")

        with open(file_path, 'a', encoding='utf-8') as f:
            f.write('\n'.join(model_lines))
            f.write("\n")

        generated.add(name)

    with open(file_path, 'w', encoding='utf-8') as f:
        for imp in sorted(imports.union(type_imports.values())):
            f.write(f'{imp}\n')
        f.write(f'from aws_resource_validator.pydantic_models.{service_name}_constants import *\n\n')

    for model_name in type_defs:
        generate_model(model_name)


def parse_literals(file_path: str) -> Dict[str, str]:
    """
    Parse the literals.py file to identify literals.

    Args:
        file_path (str): The path to the literals.py file.

    Returns:
        Dict[str, str]: Dictionary of literals.
    """
    literals = {}
    literal_pattern = re.compile(r'(\w+)\s*=\s*Literal\[(.*?)\]', re.DOTALL)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    for match in literal_pattern.finditer(content):
        literal_name, literal_values = match.groups()
        literals[literal_name] = f'Literal[{literal_values.strip()}]'

    return literals


def generate_constants_file(literals: Dict[str, str], other_defs: Dict[str, str], file_path: str) -> None:
    """
    Generate a constants file from literals and other definitions and save them to a specified output file.

    Args:
        literals (Dict[str, str]): Dictionary of literals.
        other_defs (Dict[str, str]): Dictionary of other definitions.
        file_path (str): The path to the output file where constants will be saved.
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        # Add imports
        f.write("from typing import Literal, Union, Optional, List, Dict, Any, Sequence, Mapping, IO\n")
        f.write("from datetime import datetime\n\n")

        for literal_name, literal_values in literals.items():
            f.write(f'{literal_name} = {literal_values}\n')

        for def_name, def_value in other_defs.items():
            if 'Union' in def_value:
                def_value = re.sub(r'(\w+TypeDef)', r"'\1'", def_value)
            f.write(f'{def_name} = {def_value}\n')


def generate_models():  # pylint: disable=missing-function-docstring
    for folder in os.listdir(venv_path):
        if folder.startswith('mypy_boto3_'):
            folder_path = os.path.join(venv_path, folder)
            literals_path = os.path.join(folder_path, 'literals.py')
            type_defs_path = os.path.join(folder_path, 'type_defs.py')

            service_name = folder.replace('mypy_boto3_', '')

            literals, type_defs, other_defs = {}, {}, {}
            if os.path.exists(literals_path):
                print(f'Processing literals in {literals_path}')
                literals = parse_literals(literals_path)

            if os.path.exists(type_defs_path):
                print(f'Processing type definitions in {type_defs_path}')
                type_defs, other_defs = parse_type_defs(type_defs_path)

            if literals or other_defs:
                constants_output_path = os.path.join(output_dir, f'{service_name}_constants.py')
                generate_constants_file(literals, other_defs, constants_output_path)

            if type_defs:
                classes_output_path = os.path.join(output_dir, f'{service_name}_classes.py')
                generate_pydantic_models(type_defs, service_name, classes_output_path)
