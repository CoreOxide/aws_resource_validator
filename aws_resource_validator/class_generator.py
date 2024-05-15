from models import APIRegistry

def generate_static_classes(api_registry: APIRegistry, filename: str = 'api_registry_definitions.py') -> None:
    """
    This function generates static classes based on the services and API objects in the given API registry.
    The generated classes are written to a Python file with the given filename.

    :param api_registry: The API registry containing the services and API objects.
    :param filename: The name of the Python file to which the generated classes will be written.
    """
    with open(filename, 'w') as f:
        f.write("# --- this is an auto-generate file ---\n\n")
        # Write imports and any needed boilerplate
        f.write("from aws_resource_validator.models import Service, APIObject, APIRegistry\n\n\n")

        # Generate classes dynamically based on the registry
        for service_name, service in api_registry.services.items():
            # Define the service class
            f.write(f"class {service_name}(Service):\n")
            f.write(f"    def __init__(self):\n")
            f.write(f"        super().__init__('{service_name}')\n")

            for obj_name, api_obj in service.api_objects.items():
                # Define APIObject within the service class
                pattern: str = api_obj.pattern.replace("'", "\\'")
                f.write(f"        self.{obj_name} = APIObject('{obj_name}', '{api_obj.type}', r'{pattern}', {api_obj.min_length}, {api_obj.max_length})\n")
                f.write(f"        self.add_api_object('{obj_name}', self.{obj_name})\n")

            f.write("\n")

        # Instantiate each service and add to the registry at module level
        f.write("api_registry = APIRegistry()\n")
        for service_name in api_registry.services:
            f.write(f"{service_name.lower()} = {service_name}()\n")
            f.write(f"api_registry.add_service({service_name.lower()})\n")

    print(f"Generated Python module: {filename}")