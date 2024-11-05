#!/usr/bin/env python3
"""Unit tests for client.py"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient"""

    @parameterized.expand([
        ("google", {"repos_url": "https://api.github.com/orgs/google/repos"}),
        ("abc", {"repos_url": "https://api.github.com/orgs/abc/repos"})
    ])
    @patch("client.get_json")
    def test_org(self, org_name, expected, mock_get_json):
        """Test org method returns correct result from get_json"""
        mock_get_json.return_value = expected
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """Test _public_repos_url returns correct URL from org property"""
        with patch.object(GithubOrgClient, "org",
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "http://example.com/repos"}
            client = GithubOrgClient("example")
            self.assertEqual(client._public_repos_url,
                             "http://example.com/repos")

    @patch("client.get_json")
    def test_repos_payload(self, mock_get_json):
        """Test repos_payload method fetches the correct payload"""
        mock_get_json.return_value = {"repos": []}
        with patch.object(GithubOrgClient, "_public_repos_url",
                          new_callable=PropertyMock) as mock_url:
            mock_url.return_value = "http://example.com/repos"
            client = GithubOrgClient("example")
            self.assertEqual(client.repos_payload, {"repos": []})
            mock_get_json.assert_called_once_with("http://example.com/repos")

    @parameterized.expand([
        ({"license": {"key": "mit"}}, "mit", True),
        ({"license": {"key": "apache-2.0"}}, "mit", False),
        ({}, "mit", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license checks for license key correctly"""
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key), expected
        )


if __name__ == "__main__":
    unittest.main()
