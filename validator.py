import time

import requests
import json
import re
import base64
import keyword

headers = {'Authorization': 'token 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'}


# Function to handle rate limiting
def check_rate_limit(response):
    if 'X-RateLimit-Remaining' in response.headers and int(response.headers['X-RateLimit-Remaining']) == 0:
        reset_time = int(response.headers['X-RateLimit-Reset'])
        sleep_time = reset_time - time.time() + 10  # Adding 10 seconds to ensure limit is reset
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
        self.name = self.normalize_name(name)
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
        return name.replace("_", "")

class APIRegistry:
    def __init__(self):
        self.services = {}

    def add_service(self, service):
        setattr(self, service.name, service)
        self.services[service.name] = service

    def __getattr__(self, name):
        if name in self.services:
            return self.services[name]
        raise AttributeError(f"{name} not found in API registry")


def fetch_and_parse_github():
    base_url = "https://api.github.com/repos/boto/botocore/contents/botocore/data"
    response = requests.get(base_url, headers=headers, timeout=10)
    services_data = response.json()

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
            service_latest_url = service_response['url']
            service_latest_response = requests.get(service_latest_url, headers=headers, timeout=10)
            check_rate_limit(service_latest_response)
            service_files = service_latest_response.json()

            for file in service_files:
                if file['name'] == 'service-2.json':
                    service_json_url = file['url']
                    break

            service_response = requests.get(service_json_url, headers=headers, timeout=10)

            print("Fetching:", service_json_url, "Status:", service_response.status_code)
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


api_registry = fetch_and_parse_github()

# Example usage
try:
    print(api_registry.lambda_.FunctionName.pattern)
    print(api_registry.lambda_.function_name.validate("my-function-name"))
except AttributeError as e:
    print(e)
