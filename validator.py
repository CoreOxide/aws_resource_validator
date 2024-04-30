import time

import requests
import json
import re
import base64
import keyword
# TODO: get token dynamically somehow...
headers = {'Authorization': 'Bearer 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'}
max_calls = 5


# Function to handle rate limiting
def check_rate_limit(response):
    if 'X-RateLimit-Remaining' in response.headers and int(response.headers['X-RateLimit-Remaining']) == 0:
        reset_time = int(response.headers['X-RateLimit-Reset'])
        sleep_time = reset_time - time.time() + 10  # Adding 10 seconds to ensure limit is reset
        # TODO: use logging instead of print
        print(f"Rate limit exceeded. Sleeping for {sleep_time} seconds.")
        time.sleep(sleep_time)


class APIObject:
    def __init__(self, name, type, pattern, min_length=None, max_length=None):
        self.name = name
        self.type = type
        self.pattern = pattern
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, value):
        if self.min_length is not None and len(value) < self.min_length:
            return False
        if self.max_length is not None and len(value) > self.max_length:
            return False
        return re.match(self.pattern, value) is not None

class Service:
    def __init__(self, name):
        self.service_name_ = self.normalize_name(name)
        self.api_objects = {}

    def add_api_object(self, name, api_object):
        camel_case_name = self.to_valid_python_identifier(name)
        snake_case_name = self.to_snake_case(name)
        setattr(self, camel_case_name, api_object)
        setattr(self, snake_case_name, api_object)
        self.api_objects[camel_case_name] = api_object

    @staticmethod
    def to_snake_case(name):
        return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

    @staticmethod
    def to_valid_python_identifier(name):
        new_name = name.replace("_", "")
        if keyword.iskeyword(new_name):
            new_name += "_"
        return new_name

    @staticmethod
    def normalize_name(name):
        """Converts service names into valid Python class names in CamelCase."""
        # Replace any non-alphanumeric characters (like '-') with '_'
        name = re.sub(r'[^a-zA-Z0-9]', '_', name)
        # Split the name into parts and capitalize each part, then join them without underscores
        parts = name.split('_')
        camel_case_name = ''.join(part.capitalize() for part in parts if part)
        # If the resulting name is a Python keyword, append an underscore
        if keyword.iskeyword(camel_case_name):
            camel_case_name += '_'
        return camel_case_name

class APIRegistry:
    def __init__(self):
        self.services = {}

    def add_service(self, service: Service):
        setattr(self, service.service_name_, service)
        self.services[service.service_name_] = service

    def __getattr__(self, name):
        if name in self.services:
            return self.services[name]
        raise AttributeError(f"{name} not found in API registry")


def fetch_and_parse_github():
    base_url = "https://api.github.com/repos/boto/botocore/contents/botocore/data"
    response = requests.get(base_url, headers=headers, timeout=10)
    services_data = response.json()
    current_calls = 0

    if not isinstance(services_data, list):
        print("Failed to fetch services:", services_data)
        return None

    api_registry = APIRegistry()

    for service_data in services_data:
        if service_data['type'] == 'dir':  # Ensure it's a directory
            service_name = service_data['name']
            service_url = service_data['url']
            service_response = requests.get(service_url, headers=headers, timeout=10)
            check_rate_limit(service_response)
            service_latest_url = service_response.json()[0]['url']
            service_latest_response = requests.get(service_latest_url, headers=headers, timeout=10)
            check_rate_limit(service_latest_response)
            service_files = service_latest_response.json()

            for file in service_files:
                if file['name'] == 'service-2.json':
                    service_json_url = file['url']
                    break

            if 'service_json_url' not in locals():
                print(f"Failed to find service-2.json for {service_name}")
                continue

            print("Fetching:", service_json_url, "Status:", service_response.status_code)
            # TODO: for testing, remove in full version
            current_calls += 1
            if current_calls >= max_calls:
                print("Max calls reached. Exiting.")
                break
            service_response = requests.get(service_json_url, headers=headers, timeout=10)

            if service_response.status_code == 200:
                service_content = base64.b64decode(service_response.json()['content']).decode('utf-8')
                service_json = json.loads(service_content)

                service = Service(service_name)

                if 'shapes' in service_json:
                    for obj_name, obj_data in service_json['shapes'].items():
                        if 'type' in obj_data and 'pattern' in obj_data:
                            api_obj = APIObject(
                                name=obj_name,
                                type=obj_data['type'],
                                pattern=obj_data['pattern'],
                                min_length=obj_data.get('min'),
                                max_length=obj_data.get('max')
                            )
                            service.add_api_object(obj_name, api_obj)

                    api_registry.add_service(service)
                else:
                    print(f"No 'shapes' in JSON for {service_name}")
            else:
                print(f"Failed to fetch service data for {service_name}")

    return api_registry

def generate_static_classes(api_registry, filename='api_registry_definitions.py'):
    with open(filename, 'w') as f:
        # Write imports and any needed boilerplate
        f.write("from validator import Service\n")
        f.write("from validator import APIObject\n")
        f.write("from validator import APIRegistry\n\n\n")

        # Generate classes dynamically based on the registry
        for service_name, service in api_registry.services.items():
            # Define the service class
            f.write(f"class {service_name}(Service):\n")
            f.write(f"    def __init__(self):\n")
            f.write(f"        super().__init__('{service_name}')\n")

            for obj_name, api_obj in service.api_objects.items():
                # Define APIObject within the service class
                pattern = api_obj.pattern.replace("'", "\\'")
                f.write(f"        self.{obj_name} = APIObject('{obj_name}', '{api_obj.type}', r'{pattern}', {api_obj.min_length}, {api_obj.max_length})\n")
                f.write(f"        self.add_api_object('{obj_name}', self.{obj_name})\n")

            f.write("\n")

        # Instantiate each service and add to the registry at module level
        f.write("api_registry = APIRegistry()\n")
        for service_name in api_registry.services:
            f.write(f"{service_name.lower()} = {service_name}()\n")
            f.write(f"api_registry.add_service({service_name.lower()})\n")

    print(f"Generated Python module: {filename}")


if __name__ == "__main__":
    api_registry = fetch_and_parse_github()
    generate_static_classes(api_registry)
