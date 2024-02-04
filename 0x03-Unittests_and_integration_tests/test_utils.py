#!/usr/bin/env python3
"""Unit tests for utils module."""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Test case for the access_nested_map function."""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, input_nested_map, input_path, expected_output
    ):
        """Test access_nested_map function."""
        result = access_nested_map(input_nested_map, input_path)
        self.assertEqual(result, expected_output)

    @parameterized.expand(
            [({}, ("a",), KeyError), ({"a": 1}, ("a", "b"), KeyError)]
    )
    def test_access_nested_map_exception(
        self, input_nested_map, input_path, expected_exception
    ):
        """Test access_nested_map function with exception."""
        with self.assertRaises(expected_exception) as context:
            access_nested_map(input_nested_map, input_path)


class TestGetJson(unittest.TestCase):
    """Test case for the get_json function."""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, input_url, expected_output):
        """Test get_json function."""
        mock_response = Mock()
        mock_response.json.return_value = expected_output
        with patch("requests.get", return_value=mock_response):
            response = get_json(input_url)

            self.assertEqual(response, expected_output)


class TestMemoize(unittest.TestCase):
    """Test case for the memoize decorator."""

    def test_memoize(self):
        """Test memoize decorator."""

        class TestClass:
            """Test class with memoized method."""

            def a_method(self):
                """A simple method."""
                return 42

            @memoize
            def a_property(self):
                """A memoized property."""
                return self.a_method()

        test_instance = TestClass()

        with patch.object(test_instance, "a_method") as mock_method:
            mock_method.return_value = 42

            result_first_call = test_instance.a_property
            result_second_call = test_instance.a_property

            self.assertEqual(result_first_call, 42)
            self.assertEqual(result_second_call, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
