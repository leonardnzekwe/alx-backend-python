#!/usr/bin/env python3
"""
A module for testing the client module.
"""
import unittest
from typing import Dict
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from parameterized import parameterized, parameterized_class
from requests import HTTPError
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test case for the GithubOrgClient class."""

    @parameterized.expand(
        [
            ("google", {"login": "google"}),
            ("abc", {"login": "abc"}),
        ]
    )
    @patch("client.get_json")
    def test_org(
        self, org: str, expected_response: Dict, mocked_function: MagicMock
    ) -> None:
        """Test the org method of GithubOrgClient."""
        mocked_function.return_value = MagicMock(
            return_value=expected_response
        )
        goclient = GithubOrgClient(org)
        self.assertEqual(goclient.org(), expected_response)
        mocked_function.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    @patch("client.get_json")
    def test_public_repos_url(self, mock_get_json: MagicMock) -> None:
        """Test the _public_repos_url method of GithubOrgClient."""
        mock_get_json.return_value = {
            "repos_url": "https://api.github.com/users/google/repos"
        }
        self.assertEqual(
            GithubOrgClient("google")._public_repos_url,
            "https://api.github.com/users/google/repos",
        )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Test the public_repos method of GithubOrgClient."""
        test_payload = {
            "repos_url": "https://api.github.com/users/google/repos",
            "repos": [
                {"name": "episodes.dart", "license": {"key": "mit"}},
                {"name": "kratu", "license": {"key": "apache-2.0"}},
            ],
        }
        mock_get_json.return_value = test_payload["repos"]
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                ["episodes.dart", "kratu"]
            )
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "bsd-3-clause"}}, "bsd-3-clause", True),
            ({"license": {"key": "bsl-1.0"}}, "bsd-3-clause", False),
        ]
    )
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """Test the has_license method of GithubOrgClient."""
        gh_org_client = GithubOrgClient("google")
        client_has_license = gh_org_client.has_license(repo, key)
        self.assertEqual(client_has_license, expected)


@parameterized_class(
    [
        {
            "org_payload": TEST_PAYLOAD[0][0],
            "repos_payload": TEST_PAYLOAD[0][1],
            "expected_repos": TEST_PAYLOAD[0][2],
            "apache2_repos": TEST_PAYLOAD[0][3],
        },
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test case for the GithubOrgClient class."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up class method for the integration test."""
        route_payload = {
            "https://api.github.com/orgs/google": cls.org_payload,
            "https://api.github.com/orgs/google/repos": cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{"json.return_value": route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Integration test for the public_repos method."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(), self.expected_repos
        )

    def test_public_repos_with_license(self) -> None:
        """Integration test for the public_repos method with license."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Tear down class method for the integration test."""
        cls.get_patcher.stop()


if __name__ == "__main__":
    unittest.main()
