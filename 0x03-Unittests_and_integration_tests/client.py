#!/usr/bin/env python3
"""This module provides a client
"""
from typing import (
    List,
    Dict,
)

from utils import (
    get_json,
    access_nested_map,
    memoize,
)


class GithubOrgClient:
    """A client for GitHub organization data.
    """
    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        """Initialize the client with the organization name."""
        self._org_name = org_name

    @memoize
    def org(self) -> Dict:
        """Get organization data from GitHub."""
        return get_json(self.ORG_URL.format(org=self._org_name))

    @property
    def _public_repos_url(self) -> str:
        """Get the URL for the public repositories of the organization"""
        return self.org["repos_url"]

    @memoize
    def repos_payload(self) -> Dict:
        """Get the payload of the public repositories."""
        return get_json(self._public_repos_url)

    def public_repos(self, license: str = None) -> List[str]:
        """Get a list of public repositories"""
        json_payload = self.repos_payload
        public_repos = [
            repo["name"] for repo in json_payload
            if license is None or self.has_license(repo, license)
        ]

        return public_repos

    @staticmethod
    def has_license(repo: Dict[str, Dict], license_key: str) -> bool:
        """"Check if a repository has a specific license."""
        assert license_key is not None, "license_key cannot be None"
        try:
            has_license = access_nested_map(repo, ("license", "key")) == license_key
        except KeyError:
            return False
        return has_license
