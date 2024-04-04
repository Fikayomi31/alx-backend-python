#!/usr/bin/env python3
""" Testing utils file"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """

    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """Testing access_nested_map function of utils.py
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_output)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError)
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_output):
        """Test that raise key error when the key is not in dict
        """
        with self.assertRaises(expected_output) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Testing utils.get_json function
    """
    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]
    )
    @patch('requests.get')
    def test_get_json(self, url, expected_output, mock_get: Mock):
        """method to test that utils.get_json
        """
        mock_get.return_value.json.return_value = expected_output
        self.assertEqual(get_json(url), expected_output)
        mock_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """Testing memoize
    """

    def test_memoize(self):
        """function test_memoize
        """

        class TestClass:
            """Creation of instance of TestClass
            """

            def a_method(self):
                """a_method function
                """
                return 42

            @memoize
            def a_property(self):
                """a_property function
                """
                return self.a_method()
        # Patch the 'a_method' method of TestClass with a mock
        with patch.object(TestClass, "a_method", return_value=42) as mocked:
            test_class = TestClass()
            # Assert that the result is correct
            self.assertEqual(test_class.a_property, 42)
            self.assertEqual(test_class.a_property, 42)
            # Assert that a_method was called only once
            mocked.assert_called_once()
