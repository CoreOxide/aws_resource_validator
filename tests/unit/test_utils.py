import time
import unittest
from unittest.mock import Mock
from aws_resource_validator.utils import check_rate_limit


class TestCheckRateLimit(unittest.TestCase):
    def setUp(self):
        self.response = Mock()

    def test_rate_limit_not_exceeded(self):
        self.response.headers = {'X-RateLimit-Remaining': '10'}
        check_rate_limit(self.response)

    def test_rate_limit_exceeded(self):
        self.response.headers = {'X-RateLimit-Remaining': '0', 'X-RateLimit-Reset': '10'}
        with self.assertRaises(ValueError):
            check_rate_limit(self.response)

    def test_no_rate_limit_header(self):
        self.response.headers = {}
        check_rate_limit(self.response)

    def test_rate_limit_reset_time_in_past(self):
        self.response.headers = {'X-RateLimit-Remaining': '0', 'X-RateLimit-Reset': '0'}
        with self.assertRaises(ValueError):
            check_rate_limit(self.response)

    def test_rate_limit_reset_time_in_future(self):
        self.response.headers = {'X-RateLimit-Remaining': '0', 'X-RateLimit-Reset': str(int(time.time()) + 1)}
        with unittest.mock.patch('time.sleep') as mock_sleep:
            check_rate_limit(self.response)
            mock_sleep.assert_called_once()
            call_args = mock_sleep.call_args
            assert call_args[0][0] > 10, "Sleep time is not more than 10 seconds"
