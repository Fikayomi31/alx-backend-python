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
    """Testing utils.memoize function
    """
    def test_memorize(self):
        class TestClass:

            def a_method(self):
                """doc
                """
                return 42

            @memoize
            def a_property(self):
                """doc
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            test_class = TestClass()
            mock_method.return_value = 42
            result = test_class.a_property
            result_2 = test_class.a_property
            self.assertEqual(result, 42)
            self.assertEqual(result_2, 42)
