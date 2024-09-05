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
from prime.swagger_client.api.file_virus_checker_api import FileVirusCheckerApi  # noqa: E501
from prime.swagger_client.rest import ApiException


class TestFileVirusCheckerApi(unittest.TestCase):
    """FileVirusCheckerApi unit test stubs"""

    def setUp(self):
        self.api = prime.swagger_client.api.file_virus_checker_api.FileVirusCheckerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_file_virus_checker_get(self):
        """Test case for file_virus_checker_get

        Collection Query  # noqa: E501
        """
        pass

    def test_file_virus_checker_id_delete(self):
        """Test case for file_virus_checker_id_delete

        Delete  # noqa: E501
        """
        pass

    def test_file_virus_checker_id_download_config_get(self):
        """Test case for file_virus_checker_id_download_config_get

        Download Config File  # noqa: E501
        """
        pass

    def test_file_virus_checker_id_get(self):
        """Test case for file_virus_checker_id_get

        Instance Query  # noqa: E501
        """
        pass

    def test_file_virus_checker_id_patch(self):
        """Test case for file_virus_checker_id_patch

        Modify  # noqa: E501
        """
        pass

    def test_file_virus_checker_id_upload_config_post(self):
        """Test case for file_virus_checker_id_upload_config_post

        Upload Config File  # noqa: E501
        """
        pass

    def test_file_virus_checker_post(self):
        """Test case for file_virus_checker_post

        Create  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
