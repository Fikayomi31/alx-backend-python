#!/usr/bin/env python3
""" Testing utils file"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
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
