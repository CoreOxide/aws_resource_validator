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
    Parse the `type_defs.py` file to extract TypedDict definitions and other type definitions.

    Args:
        file_path (str): The path to the `type_defs.py` file.

    Returns:
        Tuple[Dict[str, Dict[str, str]], Dict[str, str]]: A tuple containing two dictionaries:
            - The first dictionary maps TypedDict names to their field definitions.
            - The second dictionary maps other type definition names to their type values.
    """
    type_defs, other_defs = {}, {}
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex pattern to capture TypedDict name and its fields, including nested types with commas
    typed_dict_pattern = re.compile(
        r'(\w+)\s*=\s*TypedDict\(\s*"\w+"\s*,\s*\{(.*?)\}', re.DOTALL
    )
    # Pattern to exclude TypedDicts and capture other definitions
    other_defs_pattern = re.compile(
        r'(\w+)\s*=\s*(?!TypedDict)(Union\[[^\]]+\]|Optional\[[^\]]+\]|Dict\[[^\]]+\]|List\[[^\]]+\]|Any|Literal\[['
        r'^\]]+\]|datetime|str|int|float|bool)',
        re.DOTALL
    )

    # Parsing TypedDict matches
    for match in typed_dict_pattern.finditer(content):
        type_name, fields = match.groups()

        # Improved regex pattern to capture fields correctly, including nested types with commas
        field_matches = re.findall(r'\s*"(\w+)"\s*:\s*([^,]+(?:\[[^\]]+\]|,|[^,\n]+)*)', fields, re.DOTALL)
        field_dict = {}
        for field_match in field_matches:
            field_name, field_type = field_match
            if 'NotRequired[' in field_type:
                field_type = field_type.replace('NotRequired[', 'Optional[')
            field_dict[field_name] = field_type.strip().replace("\n", " ").replace("  ", " ").rstrip(',')
        type_defs[type_name] = field_dict

    # Parsing other definitions
    for match in other_defs_pattern.finditer(content):
        def_name, def_value = match.groups()
        other_defs[def_name] = def_value.strip().replace("\n", " ").replace("  ", " ").rstrip(',')

    return type_defs, other_defs


def generate_pydantic_models(type_defs: Dict[str, Dict[str, str]], service_name: str, file_path: str):
    """
    Generate Pydantic models from TypedDict definitions and save them to a specified output file.

    Args:
        type_defs (Dict[str, Dict[str, str]]): Dictionary of TypedDict definitions.
        service_name (str): The service name for generating the corresponding constants file import.
        file_path (str): The path to the output file where Pydantic models will be saved.
    """
    imports = set(["from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel",
                   "from datetime import datetime"])
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

    with open(file_path, 'w', encoding='utf-8') as f:
        # Write imports
        for import_statement in sorted(imports.union(type_imports.values())):
            f.write(f'{import_statement}\n')

        # Import the corresponding constants file
        f.write(f'from aws_resource_validator.pydantic_models.{service_name}_constants import *\n\n')

        # Write Pydantic models
        for type_name, fields in type_defs.items():
            f.write(f'class {type_name}(BaseModel):\n')
            for field_name, field_type in fields.items():
                if 'Optional[' in field_type:
                    f.write(f'    {field_name}: {field_type} = None\n')
                else:
                    f.write(f'    {field_name}: {field_type}\n')
            f.write('\n')


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
