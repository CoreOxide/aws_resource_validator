""" This module is responsible for fetching and parsing AWS API data from the botocore repository on GitHub. """

import base64
import json
import time
from typing import Dict, Optional

import requests
from requests import Response

from aws_resource_validator.models import APIRegistry, Service, APIObject
from aws_resource_validator.utils import check_rate_limit


# this needs a refactor...
# pylint: disable=too-many-locals,too-many-nested-blocks,too-many-branches
def fetch_and_parse_github(headers: Dict[str, str]) -> Optional[APIRegistry]:
    """
    Fetches and parses AWS API data from the botocore repository on GitHub.
    :param headers: headers for the request
    :return: an APIRegistry object containing the parsed API data
    """
    base_url: str = "https://api.github.com/repos/boto/botocore/contents/botocore/data"
    request_counter: int = 0

    def make_request(url: str) -> Response:
        """
        Makes a request to the given URL. Sleeps every 30 requests, so that github won't think this is DDOS
        """
        nonlocal request_counter
        request_counter += 1
        if request_counter % 30 == 0:
            print("Reached 30 requests, sleeping for 60 seconds...")
            time.sleep(60)
        response = requests.get(url, headers=headers, timeout=10)
        check_rate_limit(response)
        return response

    response: Response = make_request(base_url)
    services_data = response.json()

    if not isinstance(services_data, list):
        print("Failed to fetch services:", services_data)
        return None

    api_registry: APIRegistry = APIRegistry()

    for service_data in services_data:
        if service_data['type'] == 'dir':  # Ensure it's a directory
            service_name: str = service_data['name']
            service_url: str = service_data['url']
            service_response: Response = make_request(service_url)
            service_latest_url: str = service_response.json()[0]['url']
            service_latest_response: Response = make_request(service_latest_url)
            service_files = service_latest_response.json()

            for file in service_files:
                if file['name'] == 'service-2.json':
                    service_json_url: str = file['url']
                    break

            if 'service_json_url' not in locals():
                print(f"Failed to find service-2.json for {service_name}")
                continue

            print("Fetching:", service_json_url, "Status:", service_response.status_code)
            service_response: Response = make_request(service_json_url)

            if service_response.status_code == 200:
                service_content: str = base64.b64decode(service_response.json()['content']).decode('utf-8')
                if not service_content:
                    print(f"Failed to fetch service data for {service_name} or is empty")
                    continue
                service_json: Dict = json.loads(service_content)

                service: Service = Service(service_name)

                if 'shapes' in service_json:
                    for obj_name, obj_data in service_json['shapes'].items():
                        if 'type' in obj_data and 'pattern' in obj_data:
                            api_obj: APIObject = APIObject(
                                name=obj_name,
                                object_type=obj_data['type'],
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
