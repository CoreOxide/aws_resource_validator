#pylint: disable=logging-fstring-interpolation

import ast
import logging
import os
import sys
from pathlib import Path
from typing import Dict, Optional

# --- Configuration ---
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

try:
    SCRIPT_DIR = Path(__file__).parent.resolve()
except NameError:
    SCRIPT_DIR = Path(os.getcwd()).resolve()

PROJECT_ROOT = SCRIPT_DIR.parent.resolve()
PYTHON_VERSION_SUBDIR = f"python{sys.version_info.major}.{sys.version_info.minor}"
VENV_PATHS_TO_CHECK = [
    PROJECT_ROOT / '.venv' / 'lib' / PYTHON_VERSION_SUBDIR / 'site-packages',
    PROJECT_ROOT / 'venv' / 'lib' / PYTHON_VERSION_SUBDIR / 'site-packages',
]
VENV_PATH = None
for path_check in VENV_PATHS_TO_CHECK:
    if path_check.is_dir():
        VENV_PATH = path_check
        break

if VENV_PATH is None:
    for path_str in sys.path:
        if 'site-packages' in path_str and ('.venv' in path_str or 'venv' in path_str):
            path_check = Path(path_str)
            if path_check.is_dir():
                VENV_PATH = path_check
                logging.warning(f"Using venv path found in sys.path: {VENV_PATH}")
                break

if VENV_PATH is None:
    logging.error("Could not automatically determine virtual environment site-packages path.")
    VENV_PATH = Path("./.venv/lib/pythonX.Y/site-packages")  # Placeholder

OUTPUT_DIR = PROJECT_ROOT / 'aws_resource_validator' / 'pydantic_models'


# --- Helper Functions ---

def create_init_file(directory: Path):
    """Create an empty __init__.py file in the specified directory if it doesn't exist."""
    init_file = directory / "__init__.py"
    if not init_file.exists():
        init_file.write_text("")
        logging.info(f"Created empty __init__.py file in {directory}")
    else:
        logging.debug(f"__init__.py file already exists in {directory}")


def sanitize_name(name: str) -> str:
    """Removes 'TypeDef' suffix."""
    return name.replace('TypeDef', '')


def format_literal_element(elt_node: ast.expr) -> str:
    """Formats an element within a Literal[...] based on its type."""
    if isinstance(elt_node, ast.Name):
        # Identifier like PostgreSQL - needs quoting
        return f"'{elt_node.id}'"
    elif isinstance(elt_node, ast.Constant):
        # String needs repr() to keep quotes, others repr() is fine
        return repr(elt_node.value)
    else:
        logging.warning(f"Unsupported element type in Literal: {type(elt_node)}")
        # Attempt repr as fallback
        try:
            # Avoid ast.literal_eval here as it might execute code
            return repr(elt_node)  # Basic repr
        except:
            return "'UNPARSEABLE_LITERAL'"


def parse_ast_node_to_type_str(
        node: Optional[ast.expr],
        constants_module: str,
        type_map: Dict[str, str]
) -> str:
    """
    Recursively converts an AST node representing a type hint into a string.
    Assumes types are defined in order. Correctly handles NotRequired -> Optional
    and quotes identifiers in Literals.
    """
    if node is None:
        return "Any"

    if isinstance(node, ast.Name):
        type_name = node.id
        sanitized_name = type_map.get(type_name, type_name)
        if sanitized_name == 'IO': return 'IO[Any]'
        if sanitized_name == 'StreamingBody': return 'StreamingBody'
        if sanitized_name == 'TypedDict': return 'Dict[str, Any]'
        # NotRequired should only appear in Subscript, handle bare occurrence as fallback
        if sanitized_name == 'NotRequired':
            logging.warning("Bare 'NotRequired' found, interpreting as Optional[Any]")
            return 'Optional[Any]'
        return sanitized_name

    elif isinstance(node, ast.Constant):
        if node.value is None:
            return 'None'
        # String constants in annotations might be forward refs
        if isinstance(node.value, str):
            type_name = node.value
            sanitized_name = type_map.get(type_name, type_name)
            return sanitized_name  # Assume it's a type name
        return repr(node.value)  # Other constants (int, bool, etc.)

    elif isinstance(node, ast.Attribute):
        # Handles typing.List, datetime.datetime etc.
        if isinstance(node.value, ast.Name) and node.value.id in ('typing', 'collections.abc'):
            return node.attr  # e.g., List, Dict, Optional, Union, Literal
        if isinstance(node.value, ast.Name) and node.value.id == 'datetime' and node.attr == 'datetime':
            return 'datetime'
        # Recursively parse the base
        value_str = parse_ast_node_to_type_str(node.value, constants_module, type_map)
        # Prevent invalid attribute access like Any.Something or Optional.Something
        if value_str == "Any" or value_str.startswith("Optional["):
            logging.warning(f"Attempting attribute access on {value_str}, returning Any.")
            return "Any"
        return f"{value_str}.{node.attr}"

    elif isinstance(node, ast.Subscript):
        value_node = node.value
        slice_node = node.slice

        # *** Prioritize NotRequired check ***
        if isinstance(value_node, ast.Name) and value_node.id == 'NotRequired':
            inner_type_str = parse_ast_node_to_type_str(slice_node, constants_module, type_map)
            # Ensure inner type isn't Optional itself to avoid Optional[Optional[X]]
            if inner_type_str.startswith("Optional["):
                return inner_type_str
            else:
                return f"Optional[{inner_type_str}]"

        # If not NotRequired, parse value and slice separately
        value_type = parse_ast_node_to_type_str(value_node, constants_module, type_map)
        # Prevent invalid subscripting early
        if value_type in ("Any", "None") or value_type.startswith("Optional["):
            logging.warning(f"Attempting subscript on invalid type '{value_type}', returning Any.")
            return "Any"

        # *** Handle Literal quoting ***
        if value_type == 'Literal':
            literal_values = []
            elements_to_process = []
            if isinstance(slice_node, ast.Tuple):
                elements_to_process = slice_node.elts
            else:  # Handle single value Literal[X]
                elements_to_process = [slice_node]

            for elt in elements_to_process:
                literal_values.append(format_literal_element(elt))

            if literal_values:
                return f'Literal[{", ".join(literal_values)}]'
            else:
                logging.warning(f"Could not parse elements for Literal: {ast.dump(node)}")
                return "Literal[Any]"  # Fallback

        # --- Continue with other generic types ---
        slice_type_str = parse_ast_node_to_type_str(slice_node, constants_module, type_map)

        # Map Sequence and Mapping
        if value_type == 'Sequence':
            return f"List[{slice_type_str}]"
        if value_type == 'Mapping':
            if isinstance(slice_node, ast.Tuple) and len(slice_node.elts) == 2:
                key_type = parse_ast_node_to_type_str(slice_node.elts[0], constants_module, type_map)
                val_type = parse_ast_node_to_type_str(slice_node.elts[1], constants_module, type_map)
                return f"Dict[{key_type}, {val_type}]"
            else:
                logging.warning(f"Encountered Mapping with non-tuple slice: {ast.dump(node)}. Falling back.")
                return f"Dict[Any, {slice_type_str}]"  # Fallback

        # Standard generics like List, Dict, Union, Optional
        # Avoid Optional[None] -> None
        if value_type == 'Optional' and slice_type_str == 'None':
            return 'None'
        # Avoid Union[X, None] -> Optional[X] (handled by BinOp)
        # Avoid Union[X] -> X
        if value_type == 'Union':
            # If slice_type_str contains only one type after parsing tuple
            if ',' not in slice_type_str:
                return slice_type_str  # Return the single type directly

        return f"{value_type}[{slice_type_str}]"

    elif isinstance(node, ast.Tuple):  # Represents multiple args for Union, Dict etc.
        elements = [parse_ast_node_to_type_str(elt, constants_module, type_map) for elt in node.elts]
        return ", ".join(elements)

    elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.BitOr):  # Python 3.10+ Union syntax
        # This logic remains the same, relying on recursive calls to handle components
        left = parse_ast_node_to_type_str(node.left, constants_module, type_map)
        right = parse_ast_node_to_type_str(node.right, constants_module, type_map)
        types_in_union = set()
        for part in [left, right]:
            part = part.strip()
            if part.startswith("Optional[Union[") and part.endswith("]]"):
                inner = part[15:-2]
                types_in_union.update(t.strip() for t in inner.split(','))
                types_in_union.add('None')
            elif part.startswith("Optional[") and part.endswith("]"):
                types_in_union.add(part[9:-1].strip())
                types_in_union.add('None')
            elif part.startswith("Union[") and part.endswith("]"):
                inner = part[6:-1]
                types_in_union.update(t.strip() for t in inner.split(','))
            elif part != 'None':  # Don't add None directly if it comes from left/right
                types_in_union.add(part)
            elif part == 'None':  # Track if None was originally present
                types_in_union.add('None')

        has_none = 'None' in types_in_union
        types_without_none = sorted([t for t in types_in_union if t != 'None'])

        if not types_without_none: return 'None'  # Only None was present

        union_content = ", ".join(types_without_none)
        # Create Union[...] only if more than one type remains
        final_type = f"Union[{union_content}]" if len(types_without_none) > 1 else union_content

        # Wrap with Optional[] if None was present
        return f"Optional[{final_type}]" if has_none else final_type
    else:
        logging.warning(f"Unsupported AST node type for type hint: {type(node)}")
        return "Any"


def generate_constants_file(literals_file: Path, output_file: Path):
    """Parses a literals.py file and generates a constants file (Literals only)."""
    if not literals_file.exists():
        logging.warning(f"Literals file not found: {literals_file}")
        return
    try:
        content = literals_file.read_text()
        tree = ast.parse(content)
    except Exception as e:
        logging.error(f"Failed to parse {literals_file}: {e}")
        return

    constants_content = [
        "from typing import Literal",
        "from datetime import datetime",
        "\n"
    ]
    literal_defs = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            if len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                var_name = node.targets[0].id
                # Check assignment to Literal[...]
                is_literal_assign = False
                if isinstance(node.value, ast.Subscript) and isinstance(node.value.value,
                                                                        ast.Name) and node.value.value.id == 'Literal':
                    is_literal_assign = True
                # Check assignment to typing.Literal[...]
                elif isinstance(node.value, ast.Subscript) and isinstance(node.value.value, ast.Attribute) and \
                        isinstance(node.value.value.value,
                                   ast.Name) and node.value.value.value.id == 'typing' and node.value.value.attr == 'Literal':
                    is_literal_assign = True

                if is_literal_assign:
                    literal_values = []
                    slice_node = node.value.slice
                    elements_to_process = []
                    if isinstance(slice_node, ast.Tuple):
                        elements_to_process = slice_node.elts
                    else:  # Handle single value Literal[X]
                        elements_to_process = [slice_node]

                    for elt in elements_to_process:
                        literal_values.append(format_literal_element(elt))  # Use helper

                    if literal_values:
                        literal_defs.append(f'{var_name} = Literal[{", ".join(literal_values)}]')

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text("\n".join(constants_content + sorted(literal_defs)))
    logging.info(f"Generated constants file: {output_file}")


def generate_classes_file(
        type_defs_file: Path,
        constants_module: str,
        local_type_map: Dict[str, str],  # Map original name -> sanitized name
        output_file: Path
):
    """
    Parses a type_defs.py file and generates Pydantic models and Union aliases inline,
    assuming types are defined before use in the source file.
    """
    if not type_defs_file.exists():
        logging.warning(f"TypeDefs file not found: {type_defs_file}")
        return

    try:
        content = type_defs_file.read_text()
        tree = ast.parse(content)
    except Exception as e:
        logging.error(f"Failed to parse {type_defs_file}: {e}")
        return

    imports = [
        "from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union",
        "from datetime import datetime",
        "from pydantic import BaseModel, Field",
        "from botocore.response import StreamingBody",
        f"from {constants_module} import *",
        "from ..base_validator_model import BaseValidatorModel, EventStream",
        "\n"
    ]
    output_definitions = []

    for node in tree.body:
        definition_string = None
        if isinstance(node, ast.ClassDef) and any(isinstance(b, ast.Name) and b.id == 'TypedDict' for b in node.bases):
            original_class_name = node.name
            class_name = local_type_map.get(original_class_name, sanitize_name(original_class_name))
            base_class = "BaseValidatorModel"
            if "EventStreamTypeDef" in original_class_name:
                event_type_node = None
                for item in node.body:
                    if isinstance(item, ast.AnnAssign) and item.annotation:
                        event_type_node = item.annotation
                        break
                if (event_type_node and isinstance(event_type_node, ast.Subscript) and
                        isinstance(event_type_node.value, ast.Name) and event_type_node.value.id == 'EventStream'):
                    inner_type_str = parse_ast_node_to_type_str(event_type_node.slice, constants_module, local_type_map)
                    base_class = f"EventStream[{inner_type_str}]"

            class_def_lines = [f"class {class_name}({base_class}):"]
            fields_added = False
            if not base_class.startswith("EventStream"):
                for item in node.body:
                    if isinstance(item, ast.AnnAssign):
                        target_node = item.target
                        if isinstance(target_node, ast.Name):
                            field_name = target_node.id
                            field_type_str = parse_ast_node_to_type_str(item.annotation, constants_module,
                                                                        local_type_map)
                            if field_type_str.startswith("Optional["):
                                class_def_lines.append(f"    {field_name}: {field_type_str} = None")
                            else:
                                class_def_lines.append(f"    {field_name}: {field_type_str}")
                            fields_added = True
                    elif isinstance(item, (ast.Pass, ast.FunctionDef, ast.ClassDef)) or \
                            (isinstance(item, ast.Expr) and isinstance(item.value, ast.Constant) and isinstance(
                                item.value.value, str)):
                        continue
                if not fields_added: class_def_lines.append("    pass")
            definition_string = "\n\n" + "\n".join(class_def_lines)

        elif isinstance(node, ast.Assign):
            if len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                target_name = node.targets[0].id
                original_name = target_name
                sanitized_target_name = local_type_map.get(original_name, sanitize_name(target_name))

                if isinstance(node.value, ast.Call) and isinstance(node.value.func,
                                                                   ast.Name) and node.value.func.id == 'TypedDict':
                    class_def_lines = [f"class {sanitized_target_name}(BaseValidatorModel):"]
                    fields_added = False
                    if len(node.value.args) >= 2 and isinstance(node.value.args[1], ast.Dict):
                        fields_dict = node.value.args[1]
                        for key_node, type_node in zip(fields_dict.keys, fields_dict.values):
                            if isinstance(key_node, ast.Constant) and isinstance(key_node.value, str):
                                field_name = key_node.value
                                field_type_str = parse_ast_node_to_type_str(type_node, constants_module, local_type_map)
                                if field_type_str.startswith("Optional["):
                                    class_def_lines.append(f"    {field_name}: {field_type_str} = None")
                                else:
                                    class_def_lines.append(f"    {field_name}: {field_type_str}")
                                fields_added = True
                    if not fields_added: class_def_lines.append("    pass")
                    definition_string = "\n\n" + "\n".join(class_def_lines)

                elif (isinstance(node.value, ast.Subscript) and isinstance(node.value.value,
                                                                           ast.Name) and node.value.value.id == 'Union') or \
                        (isinstance(node.value, ast.BinOp) and isinstance(node.value.op, ast.BitOr)):
                    union_type_str = parse_ast_node_to_type_str(node.value, constants_module, local_type_map)
                    definition_string = f"\n{sanitized_target_name} = {union_type_str}"

        if definition_string:
            output_definitions.append(definition_string)

    output_content = imports + output_definitions

    output_file.parent.mkdir(parents=True, exist_ok=True)
    create_init_file(output_file.parent)
    try:
        import black
        mode = black.FileMode(line_length=100)
        output_text = black.format_str("\n".join(output_content), mode=mode)
        output_file.write_text(output_text)
        logging.info(f"Generated and formatted classes file: {output_file}")
    except ImportError:
        logging.warning("black not found. Writing unformatted code.")
        output_file.write_text("\n".join(output_content))
        logging.info(f"Generated classes file (unformatted): {output_file}")
    except Exception as format_err:
        # Catch potential formatting errors on complex generated code
        logging.error(f"Error formatting code with black: {format_err}. Writing unformatted.")
        output_file.write_text("\n".join(output_content))
        logging.info(f"Generated classes file (unformatted): {output_file}")


# --- Main Execution ---
# (Main function remains the same as the previous version)
def main():
    logging.info(f"Starting Pydantic model generation.")
    logging.info(f"Project Root: {PROJECT_ROOT}")
    logging.info(f"Script Dir: {SCRIPT_DIR}")
    logging.info(f"Output Dir: {OUTPUT_DIR}")
    if VENV_PATH:
        logging.info(f"Using Venv Path: {VENV_PATH}")
    else:
        logging.error("VENV_PATH could not be determined. Exiting.")
        return

    if not VENV_PATH.is_dir():
        logging.error(f"Virtual environment path not found or not a directory: {VENV_PATH}")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    service_count = 0
    for item in VENV_PATH.iterdir():
        if item.is_dir() and item.name.startswith('mypy_boto3_'):
            service_name_full = item.name
            service_name = service_name_full.replace('mypy_boto3_', '')
            logging.info(f"--- Processing service: {service_name} ---")
            service_count += 1

            literals_file = item / 'literals.py'
            type_defs_file = item / 'type_defs.py'

            service_output_dir = OUTPUT_DIR / service_name
            constants_output_file = service_output_dir / f"{service_name}_constants.py"
            classes_output_file = service_output_dir / f"{service_name}_classes.py"

            local_type_map = {}
            if type_defs_file.exists():
                try:
                    content = type_defs_file.read_text()
                    tree = ast.parse(content)
                    for node in ast.walk(tree):
                        original_name = None
                        if isinstance(node, ast.ClassDef) and any(
                                isinstance(b, ast.Name) and b.id == 'TypedDict' for b in node.bases):
                            original_name = node.name
                        elif isinstance(node, ast.Assign):
                            if len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                                target_name = node.targets[0].id
                                is_td_constructor = isinstance(node.value, ast.Call) and isinstance(node.value.func,
                                                                                                    ast.Name) and node.value.func.id == 'TypedDict'
                                is_union_alias = (isinstance(node.value, ast.Subscript) and isinstance(node.value.value,
                                                                                                       ast.Name) and node.value.value.id == 'Union') or \
                                                 (isinstance(node.value, ast.BinOp) and isinstance(node.value.op,
                                                                                                   ast.BitOr))
                                if is_td_constructor or is_union_alias:
                                    original_name = target_name
                        if original_name:
                            sanitized = sanitize_name(original_name)
                            local_type_map[original_name] = sanitized
                except Exception as e:
                    logging.error(f"Failed to pre-parse {type_defs_file} for type map: {e}")
            else:
                logging.warning(f"TypeDefs file not found, cannot build type map: {type_defs_file}")

            constants_module_path = f"aws_resource_validator.pydantic_models.{service_name}.{service_name}_constants"
            generate_constants_file(literals_file, constants_output_file)
            generate_classes_file(
                type_defs_file,
                constants_module_path,
                local_type_map,
                classes_output_file
            )

    if service_count == 0:
        logging.warning(f"No 'mypy_boto3_*' directories found in {VENV_PATH}")
    else:
        logging.info(f"Finished processing {service_count} services.")


if __name__ == "__main__":
    main()
