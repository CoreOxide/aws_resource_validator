import unittest
from aws_resource_validator.models import APIObject, Service, APIRegistry


class TestAPIObject(unittest.TestCase):
    def setUp(self):
        self.api_object = APIObject('test_object', 'test_type', r'\d+', 1, 10)

    def test_validate(self):
        self.assertTrue(self.api_object.validate('123'))
        self.assertFalse(self.api_object.validate('abc'))

    def test_generate(self):
        generated_value = self.api_object.generate()
        self.assertTrue(self.api_object.validate(generated_value))

    def test_min_length(self):
        self.assertEqual(self.api_object.min_length, 1)

    def test_max_length(self):
        self.assertEqual(self.api_object.max_length, 10)

    def test_type(self):
        self.assertEqual(self.api_object.type, 'test_type')


class TestService(unittest.TestCase):
    def setUp(self):
        self.service = Service('test_service')
        self.api_object = APIObject('test_object', 'test_type', r'\d+', 1, 10)
        self.service.add_api_object('test_object', self.api_object)

    def test_add_api_object(self):
        self.assertEqual(self.service.api_objects['test_object'], self.api_object)

    def test_to_snake_case(self):
        self.assertEqual(self.service.to_snake_case('TestObject'), 'test_object')

    def test_to_valid_python_identifier(self):
        self.assertEqual(self.service.to_valid_python_identifier('test-object'), 'test_object')

    def test_normalize_name(self):
        self.assertEqual(self.service.normalize_name('test-service'), 'TestService')

    def test_service_name(self):
        self.assertEqual(self.service.service_name_, 'TestService')


class TestAPIRegistry(unittest.TestCase):
    def setUp(self):
        self.api_registry = APIRegistry()
        self.service = Service('test_service')
        self.api_registry.add_service(self.service)

    def test_add_service(self):
        self.assertEqual(self.api_registry.services['TestService'], self.service)

    def test_getattr(self):
        self.assertEqual(self.api_registry.TestService, self.service)

    def test_getattr_not_found(self):
        with self.assertRaises(AttributeError):
            self.api_registry.NonExistentService

    def test_services(self):
        self.assertIn('TestService', self.api_registry.services)

    def test_service_name(self):
        self.assertEqual(self.service.service_name_, 'TestService')
