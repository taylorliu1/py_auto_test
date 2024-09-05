# coding: utf-8

"""
    PowerStore REST API

    Storage cluster REST API definition. ( For \"Try It Out\", use the cluster management IP address to load this swaggerui interface. )  # noqa: E501

    OpenAPI spec version: 3.0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import prime.swagger_client
from prime.swagger_client.api.file_user_quota_api import FileUserQuotaApi  # noqa: E501
from prime.swagger_client.rest import ApiException


class TestFileUserQuotaApi(unittest.TestCase):
    """FileUserQuotaApi unit test stubs"""

    def setUp(self):
        self.api = prime.swagger_client.api.file_user_quota_api.FileUserQuotaApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_file_user_quota_get(self):
        """Test case for file_user_quota_get

        Collection Query  # noqa: E501
        """
        pass

    def test_file_user_quota_id_get(self):
        """Test case for file_user_quota_id_get

        Instance Query  # noqa: E501
        """
        pass

    def test_file_user_quota_id_patch(self):
        """Test case for file_user_quota_id_patch

        Modify  # noqa: E501
        """
        pass

    def test_file_user_quota_id_refresh_post(self):
        """Test case for file_user_quota_id_refresh_post

        Refresh  # noqa: E501
        """
        pass

    def test_file_user_quota_post(self):
        """Test case for file_user_quota_post

        Create  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
