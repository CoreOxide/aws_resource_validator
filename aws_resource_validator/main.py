""" Main module to run the AWS Resource Validator. """

from typing import Dict
from aws_resource_validator.class_generator import generate_static_classes
from aws_resource_validator.pydantic_generator import generate_models
from aws_resource_validator.scrapper import fetch_and_parse_github

# get token dynamically somehow...?
github_api_token: str = ''  # your github api token
headers: Dict[str, str] = {'Authorization': f'Bearer {github_api_token}'}

if __name__ == "__main__":
    generate_models()
    api_registry = fetch_and_parse_github(headers=headers)
    generate_static_classes(api_registry)
