#!/usr/bin/env python3
"""Testing the GithubOrgClient
"""
import unittest
from unittest.mock import Mock, patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient, get_json
from typing import Any, Dict, Mapping, Sequence, List


class TestGithubOrgClient(unittest.TestCase):
    """Representation of the test class
    """
    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    # the get.json must return the retyrn_value
    @patch('client.get_json',  return_value={"payload": True})
    def test_org(self, org_name: str, mock_get: Mock) -> None:
        """Testing test_org function
        """
        github_client = GithubOrgClient(org_name)
        self.assertEqual(github_client.org, {"payload": True})
        url = f"https://api.github.com/orgs/{org_name}"
        mock_get.assert_called_once_with(url)

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org) -> None:
        """Testing test_public_repos_url function
        """
        payload = {"repos_url": "https://github.com/orgs/google/repos"}
        mock_org.return_value = payload
        github_client = GithubOrgClient("google")
        self.assertEqual(github_client._public_repos_url,
                         payload['repos_url'])