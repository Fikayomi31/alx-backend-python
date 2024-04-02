#!/usr/bin/env python3
""" Testing utils file"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import path, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Unittest class for testing function
    access_nested_map from utils.py
    Args:
        TestCase: the base unittest
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_output)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_output):
        """
        """
        with self.assertRaises(expected_output) as context:
            access_nested_map(nested_map, path)