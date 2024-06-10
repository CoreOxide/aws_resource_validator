""" Module that holds al class definitions for this project. """

from typing import Dict, Optional, Union, List

import keyword
import re
import exrex


class APIObject:
    """ Represents an API object with constraints. """
    def __init__(self, name: str, object_type: str, pattern: str, min_length: Optional[int] = None, max_length: Optional[int] = None):
        """
        Initialize an APIObject instance.

        :param name: The name of the API object.
        :param object_type: The type of the API object.
        :param pattern: The pattern of the API object.
        :param min_length: The minimum length of the API object.
        :param max_length: The maximum length of the API object.
        """
        self.name: str = name
        self.type: str = object_type
        self.pattern: str = pattern
        self.min_length: Optional[int] = min_length
        self.max_length: Optional[int] = max_length

    def validate(self, value: str) -> bool:
        """
        Validate the value against the API object's constraints.

        :param value: The value to validate.
        :return: True if the value is valid, False otherwise.
        """
        if self.min_length is not None and len(value) < self.min_length:
            return False
        if self.max_length is not None and len(value) > self.max_length:
            return False
        return re.match(self.pattern, value) is not None

    def generate(self) -> str:
        """
        Generates a string that conforms to the regex pattern.

        :return: A string that matches the pattern.
        """
        return exrex.getone(self.pattern, limit=self.max_length)


class Service:
    """ Represents an AWS service. """
    def __init__(self, name: str):
        """
        Initialize a Service instance.

        :param name: The name of the service.
        """
        self.service_name_: str = self.normalize_name(name)
        self.api_objects: Dict[str, APIObject] = {}

    def add_api_object(self, name: str, api_object: APIObject):
        """
        Add an API object to the service.

        :param name: The name of the API object.
        :param api_object: The API object to add.
        """
        camel_case_name: str = self.to_valid_python_identifier(name)
        snake_case_name: str = self.to_snake_case(name)
        setattr(self, camel_case_name, api_object)
        setattr(self, snake_case_name, api_object)
        self.api_objects[camel_case_name] = api_object

    @staticmethod
    def to_snake_case(name: str) -> str:
        """
        Convert a string to snake case.

        :param name: The string to convert.
        :return: The string in snake case.
        """
        return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

    @staticmethod
    def to_valid_python_identifier(name: str) -> str:
        """
        Convert a string to a valid Python identifier.

        :param name: The string to convert.
        :return: The string as a valid Python identifier.
        """
        new_name: str = name.replace("-", "_")
        if keyword.iskeyword(new_name):
            new_name += "_"
        return new_name

    @staticmethod
    def normalize_name(name: str) -> str:
        """
        Converts service names into valid Python class names in CamelCase.

        :param name: The service name to normalize.
        :return: The normalized service name.
        """
        # Replace any non-alphanumeric characters (like '-') with '_'
        name: str = re.sub(r'[^a-zA-Z0-9]', '_', name)
        # Split the name into parts and capitalize each part, then join them without underscores
        parts: List[str] = name.split('_')
        camel_case_name: str = ''.join(part.capitalize() for part in parts if part)
        # If the resulting name is a Python keyword, append an underscore
        if keyword.iskeyword(camel_case_name):
            camel_case_name += '_'
        return camel_case_name


class APIRegistry:
    """ Represents a registry of AWS services. """
    def __init__(self):
        """
        Initialize an APIRegistry instance.
        """
        self.services: Dict[str, Service] = {}

    def add_service(self, service: Service):
        """
        Add a service to the registry.

        :param service: The service to add.
        """
        setattr(self, service.service_name_, service)
        self.services[service.service_name_] = service

    def __getattr__(self, name: str) -> Union[Service, str]:
        if name in self.services:
            return self.services[name]
        raise AttributeError(f"{name} not found in API registry")
