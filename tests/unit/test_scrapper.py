import unittest
from unittest.mock import patch, MagicMock
import requests
import base64
import json

from aws_resource_validator.models import APIRegistry
from aws_resource_validator.scrapper import fetch_and_parse_github


class TestFetchAndParseGithub(unittest.TestCase):

    @patch('aws_resource_validator.scrapper.requests.get')
    def test_no_services_returned(self, mock_get):
        base_url_response = MagicMock()
        base_url_response.json.return_value = {}
        mock_get.return_value = base_url_response

        headers = {"Authorization": "token testtoken"}
        result = fetch_and_parse_github(headers)

        self.assertIsNone(result)

    @patch('aws_resource_validator.scrapper.requests.get')
    def test_no_service_json_file(self, mock_get):
        base_url_response = MagicMock()
        base_url_response.json.return_value = [
            {"type": "dir", "name": "s3", "url": "https://api.github.com/repos/boto/botocore/contents/botocore/data/s3"}
        ]
        service_response = MagicMock()
        service_response.json.return_value = [{"url": "https://api.github.com/repos/boto/botocore/contents/botocore/data/s3/2021-06-20"}]
        service_latest_response = MagicMock()
        service_latest_response.json.return_value = []

        mock_get.side_effect = [base_url_response, service_response, service_latest_response]

        headers = {"Authorization": "token testtoken"}
        result = fetch_and_parse_github(headers)

        self.assertIsInstance(result, APIRegistry)
        self.assertNotIn("s3", result.services)

    @patch('aws_resource_validator.scrapper.requests.get')
    def test_empty_service_content(self, mock_get):
        base_url_response = MagicMock()
        base_url_response.json.return_value = [
            {"type": "dir", "name": "s3", "url": "https://api.github.com/repos/boto/botocore/contents/botocore/data/s3"}
        ]
        service_response = MagicMock()
        service_response.json.return_value = [{"url": "https://api.github.com/repos/boto/botocore/contents/botocore/data/s3/2021-06-20"}]
        service_latest_response = MagicMock()
        service_latest_response.json.return_value = [{"name": "service-2.json", "url": "https://api.github.com/repos/boto/botocore/contents/botocore/data/s3/2021-06-20/service-2.json"}]
        service_json_response = MagicMock()
        service_json_response.json.return_value = {"content": base64.b64encode(b'').decode('utf-8')}

        mock_get.side_effect = [base_url_response, service_response, service_latest_response, service_json_response]

        headers = {"Authorization": "token testtoken"}
        result = fetch_and_parse_github(headers)

        self.assertIsInstance(result, APIRegistry)
        self.assertNotIn("s3", result.services)

    @patch('aws_resource_validator.scrapper.requests.get')
    def test_no_shapes_in_service_json(self, mock_get):
        base_url_response = MagicMock()
        base_url_response.json.return_value = [
            {"type": "dir", "name": "s3", "url": "https://api.github.com/repos/boto/botocore/contents/botocore/data/s3"}
        ]
        service_response = MagicMock()
        service_response.json.return_value = [{"url": "https://api.github.com/repos/boto/botocore/contents/botocore/data/s3/2021-06-20"}]
        service_latest_response = MagicMock()
        service_latest_response.json.return_value = [{"name": "service-2.json", "url": "https://api.github.com/repos/boto/botocore/contents/botocore/data/s3/2021-06-20/service-2.json"}]
        service_json_response = MagicMock()
        service_json_response.json.return_value = {"content": base64.b64encode(json.dumps({}).encode('utf-8')).decode('utf-8')}

        mock_get.side_effect = [base_url_response, service_response, service_latest_response, service_json_response]

        headers = {"Authorization": "token testtoken"}
        result = fetch_and_parse_github(headers)

        self.assertIsInstance(result, APIRegistry)
        self.assertNotIn("s3", result.services)

    @patch('aws_resource_validator.scrapper.requests.get')
    def test_service_json_has_shapes(self, mock_get):
        base_url_response = MagicMock()
        base_url_response.json.return_value = [
            {"type": "dir", "name": "s3", "url": "https://api.github.com/repos/boto/botocore/contents/botocore/data/s3"}
        ]
        service_response = MagicMock()
        service_response.json.return_value = [{"url": "https://api.github.com/repos/boto/botocore/contents/botocore/data/s3/2021-06-20"}]
        service_latest_response = MagicMock()
        service_latest_response.json.return_value = [{"name": "service-2.json", "url": "https://api.github.com/repos/boto/botocore/contents/botocore/data/s3/2021-06-20/service-2.json"}]
        service_json_response = MagicMock()
        service_json_response.json.return_value = {"content": base64.b64encode(json.dumps({"shapes": {}}).encode('utf-8')).decode('utf-8')}

        mock_get.side_effect = [base_url_response, service_response, service_latest_response, service_json_response]

        headers = {"Authorization": "token testtoken"}
        result = fetch_and_parse_github(headers)

        self.assertIsInstance(result, APIRegistry)
        self.assertNotIn("s3", result.services)

    @patch('aws_resource_validator.scrapper.requests.get')
    def test_service_json_content_decoding_failure(self, mock_get):
        base_url_response = MagicMock()
        base_url_response.json.return_value = [
            {"type": "dir", "name": "s3", "url": "https://api.github.com/repos/boto/botocore/contents/botocore/data/s3"}
        ]
        service_response = MagicMock()
        service_response.json.return_value = [{"url": "https://api.github.com/repos/boto/botocore/contents/botocore/data/s3/2021-06-20"}]
        service_latest_response = MagicMock()
        service_latest_response.json.return_value = [{"name": "service-2.json", "url": "https://api.github.com/repos/boto/botocore/contents/botocore/data/s3/2021-06-20/service-2.json"}]
        service_json_response = MagicMock()
        service_json_response.json.return_value = {"content": "notbase64"}

        mock_get.side_effect = [base_url_response, service_response, service_latest_response, service_json_response]

        headers = {"Authorization": "token testtoken"}
        result = fetch_and_parse_github(headers)

        self.assertIsInstance(result, APIRegistry)
        self.assertNotIn("s3", result.services)

    @patch('aws_resource_validator.scrapper.requests.get')
    def test_handle_rate_limiting(self, mock_get):
        base_url_response = MagicMock()
        base_url_response.json.return_value = [
            {"type": "dir", "name": "s3", "url": "https://api.github.com/repos/boto/botocore/contents/botocore/data/s3"}
        ]
        service_response = MagicMock()
        service_response.json.return_value = [{"url": "https://api.github.com/repos/boto/botocore/contents/botocore/data/s3/2021-06-20"}]
        service_latest_response = MagicMock()
        service_latest_response.json.return_value = [{"name": "service-2.json", "url": "https://api.github.com/repos/boto/botocore/contents/botocore/data/s3/2021-06-20/service-2.json"}]
        rate_limit_response = MagicMock()
        rate_limit_response.status_code = 403

        mock_get.side_effect = [base_url_response, service_response, service_latest_response, rate_limit_response]

        headers = {"Authorization": "token testtoken"}
        result = fetch_and_parse_github(headers)

        self.assertIsInstance(result, APIRegistry)
        self.assertNotIn("s3", result.services)

    @patch('aws_resource_validator.scrapper.requests.get')
    def test_handle_service_response_failure(self, mock_get):
        base_url_response = MagicMock()
        base_url_response.json.return_value = [
            {"type": "dir", "name": "s3", "url": "https://api.github.com/repos/boto/botocore/contents/botocore/data/s3"}
        ]
        service_response = MagicMock()
        service_response.json.return_value = [{"url": "https://api.github.com/repos/boto/botocore/contents/botocore/data/s3/2021-06-20"}]
        service_latest_response = MagicMock()
        service_latest_response.json.return_value = [{"name": "service-2.json", "url": "https://api.github.com/repos/boto/botocore/contents/botocore/data/s3/2021-06-20/service-2.json"}]
        service_json_response = MagicMock()
        service_json_response.status_code = 500

        mock_get.side_effect = [base_url_response, service_response, service_latest_response, service_json_response]

        headers = {"Authorization": "token testtoken"}
        result = fetch_and_parse_github(headers)

        self.assertIsInstance(result, APIRegistry)
        self.assertNotIn("s3", result.services)

    @patch('aws_resource_validator.scrapper.requests.get')
    def test_handle_malformed_json_response(self, mock_get):
        base_url_response = MagicMock()
        base_url_response.json.return_value = [
            {"type": "dir", "name": "s3", "url": "https://api.github.com/repos/boto/botocore/contents/botocore/data/s3"}
        ]
        service_response = MagicMock()
        service_response.json.return_value = [{"url": "https://api.github.com/repos/boto/botocore/contents/botocore/data/s3/2021-06-20"}]
        service_latest_response = MagicMock()
        service_latest_response.json.return_value = [{"name": "service-2.json", "url": "https://api.github.com/repos/boto/botocore/contents/botocore/data/s3/2021-06-20/service-2.json"}]
        service_json_response = MagicMock()
        service_json_response.json.side_effect = ValueError("Malformed JSON")

        mock_get.side_effect = [base_url_response, service_response, service_latest_response, service_json_response]

        headers = {"Authorization": "token testtoken"}
        result = fetch_and_parse_github(headers)

        self.assertIsInstance(result, APIRegistry)
        self.assertNotIn("s3", result.services)

    @patch('aws_resource_validator.scrapper.requests.get')
    def test_handle_malformed_shapes_json(self, mock_get):
        base_url_response = MagicMock()
        base_url_response.json.return_value = [
            {"type": "dir", "name": "s3", "url": "https://api.github.com/repos/boto/botocore/contents/botocore/data/s3"}
        ]
        service_response = MagicMock()
        service_response.json.return_value = [{"url": "https://api.github.com/repos/boto/botocore/contents/botocore/data/s3/2021-06-20"}]
        service_latest_response = MagicMock()
        service_latest_response.json.return_value = [{"name": "service-2.json", "url": "https://api.github.com/repos/boto/botocore/contents/botocore/data/s3/2021-06-20/service-2.json"}]
        malformed_shapes_response = MagicMock()
        malformed_shapes_response.json.return_value = {"content": base64.b64encode(json.dumps({"shapes": "notadict"}).encode('utf-8')).decode('utf-8')}

        mock_get.side_effect = [base_url_response, service_response, service_latest_response, malformed_shapes_response]

        headers = {"Authorization": "token testtoken"}
        result = fetch_and_parse_github(headers)

        self.assertIsInstance(result, APIRegistry)
        self.assertNotIn("s3", result.services)

    @patch('aws_resource_validator.scrapper.requests.get')
    def test_handle_connection_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.ConnectionError

        headers = {"Authorization": "token testtoken"}
        with self.assertRaises(requests.exceptions.ConnectionError):
            fetch_and_parse_github(headers)
