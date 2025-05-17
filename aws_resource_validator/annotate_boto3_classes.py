import os
import re

# Constants
VENV_PACKAGES_DIR = "../.venv/lib/python3.11/site-packages"
MODELS_ROOT_DIR = "pydantic_models"

def extract_function_info(client_py_path):
    """
    Extract function name, input type, and output type from client.py files
    """
    with open(client_py_path, 'r', encoding='utf-8') as f:
        content = f.read()


    # Regular expression to find function definitions with Unpack and return type
    # Matches pattern: def function_name(self, **kwargs: Unpack[InputTypeDef]) -> OutputTypeDef:
    pattern = r'def\s+(\w+)\s*\(\s*self\s*,\s*\*\*kwargs\s*:\s*Unpack\s*\[\s*(\w+)\s*\]\s*\)\s*->\s*(\w+)\s*:'
    matches = re.findall(pattern, content)

    return [(func_name, input_type, output_type) for func_name, input_type, output_type in matches]


def find_classes_file(service_name):
    """
    Find the corresponding classes file for a service in our pydantic models directory
    """
    classes_path = os.path.join(MODELS_ROOT_DIR, service_name, f"{service_name}_classes.py")
    if os.path.exists(classes_path):
        return classes_path
    return None


def add_comments_to_classes_file(classes_path, function_info_list):
    """
    Add comments to input and output classes in the classes file
    """
    with open(classes_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Build a dictionary: class_name -> comment
    class_comments = {}
    for func_name, input_type, output_type in function_info_list:
        # Remove "TypeDef" suffix
        input_class = input_type.replace("TypeDef", "")
        output_class = output_type.replace("TypeDef", "")
        
        class_comments[input_class] = f"# This class is the input for the '{func_name}' function.\n"
        class_comments[output_class] = f"# This class is the output for the '{func_name}' function.\n"

    # Find class definitions and add comments
    new_lines = []
    added_comments = 0
    i = 0
    while i < len(lines):
        line = lines[i]

        # Check if this line starts a class definition
        match = re.match(r'^class\s+(\w+)\s*\(', line)
        if match:
            class_name = match.group(1)
            if class_name in class_comments:
                # Check if there's already a similar comment
                comment_exists = False
                if i > 0:
                    prev_line = lines[i - 1].strip()
                    if prev_line.startswith("# This class is the") and "function" in prev_line:
                        comment_exists = True

                if not comment_exists:
                    new_lines.append(class_comments[class_name])
                    added_comments += 1

        new_lines.append(line)
        i += 1

    # Write the modified content back to the file
    with open(classes_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    return added_comments, len(class_comments)


def main():
    total_folders = 0
    processed_folders = 0
    total_classes_to_comment = 0
    total_commented_classes = 0

    # Find all mypy_boto3_* folders
    for folder in os.listdir(VENV_PACKAGES_DIR):
        if folder.startswith("mypy_boto3_") and "dist" not in folder:
            total_folders += 1
            # Extract service name (e.g., "dynamodb" from "mypy_boto3_dynamodb")
            service_name = folder.replace("mypy_boto3_", "")

            # Check if client.py exists
            client_py_path = os.path.join(VENV_PACKAGES_DIR, folder, "client.py")
            if not os.path.exists(client_py_path):
                print(f"Skipping {service_name}: No client.py found")
                continue

            # Find the corresponding classes file
            classes_path = find_classes_file(service_name)
            if not classes_path:
                print(f"Skipping {service_name}: No classes file found at {os.path.join(MODELS_ROOT_DIR, service_name)}")
                continue

            # Extract function info from client.py
            function_info_list = extract_function_info(client_py_path)

            if not function_info_list:
                print(f"Skipping {service_name}: No function definitions found")
                continue

            # Add comments to classes file
            commented_classes, classes_to_comment = add_comments_to_classes_file(classes_path, function_info_list)

            total_commented_classes += commented_classes
            total_classes_to_comment += classes_to_comment
            processed_folders += 1

            print(f"{service_name}: Added {commented_classes} comments (found {len(function_info_list)} methods)")

    print("\nSummary:")
    print(f"Processed {processed_folders}/{total_folders} folders")
    print(f"Added comments to {total_commented_classes}/{total_classes_to_comment} classes")


if __name__ == "__main__":
    main()
