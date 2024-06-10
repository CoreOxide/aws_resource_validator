import unittest
from unittest.mock import patch, mock_open
from aws_resource_validator.class_generator import generate_static_classes
from aws_resource_validator.models import APIRegistry, Service, APIObject


class TestGenerateStaticClasses(unittest.TestCase):
    def setUp(self):
        self.api_registry = APIRegistry()
        service = Service('test_service')
        api_object = APIObject('test_object', 'test_type', 'test_pattern', 1, 10)
        service.add_api_object('test_object', api_object)
        self.api_registry.add_service(service)

    @patch("builtins.open", new_callable=mock_open)
    def test_file_creation(self, mock_file):
        generate_static_classes(self.api_registry, 'test_file.py')
        mock_file.assert_called_once_with('test_file.py', 'w', encoding='utf-8')

    @patch("builtins.open", new_callable=mock_open)
    def test_file_content(self, mock_file):
        generate_static_classes(self.api_registry, 'test_file.py')
        mock_file().write.assert_any_call("from aws_resource_validator.models import Service, APIObject, APIRegistry\n\n\n")

    @patch("builtins.open", new_callable=mock_open)
    def test_service_class_generation(self, mock_file):
        generate_static_classes(self.api_registry, 'test_file.py')
        mock_file().write.assert_any_call("class TestService(Service):\n")

    @patch("builtins.open", new_callable=mock_open)
    def test_api_object_generation(self, mock_file):
        generate_static_classes(self.api_registry, 'test_file.py')
        mock_file().write.assert_any_call("        self.test_object = APIObject('test_object', 'test_type', r'test_pattern', 1, 10)\n")

    @patch("builtins.open", new_callable=mock_open)
    def test_service_instantiation(self, mock_file):
        generate_static_classes(self.api_registry, 'test_file.py')
        mock_file().write.assert_any_call("testservice = TestService()\n")
