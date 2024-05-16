from typing import Dict
from aws_resource_validator.class_generator import generate_static_classes
from aws_resource_validator.scrapper import fetch_and_parse_github

# TODO: get token dynamically somehow...
github_api_token: str = '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'  # your github api token
headers: Dict[str, str] = {'Authorization': f'Bearer {github_api_token}'}

if __name__ == "__main__":
    api_registry = fetch_and_parse_github(headers=headers)
    generate_static_classes(api_registry)
