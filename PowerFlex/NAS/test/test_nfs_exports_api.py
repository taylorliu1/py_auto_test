# coding: utf-8

"""
    PowerFlex NAS Management REST API

    NAS Storage Management REST API definition.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.nfs_exports_api import NfsExportsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestNfsExportsApi(unittest.TestCase):
    """NfsExportsApi unit test stubs"""

    def setUp(self):
        self.api = NfsExportsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_nfs_exports_get(self):
        """Test case for nfs_exports_get

        Collection Query  # noqa: E501
        """
        pass

    def test_nfs_exports_id_delete(self):
        """Test case for nfs_exports_id_delete

        Delete  # noqa: E501
        """
        pass

    def test_nfs_exports_id_get(self):
        """Test case for nfs_exports_id_get

        Instance Query  # noqa: E501
        """
        pass

    def test_nfs_exports_id_patch(self):
        """Test case for nfs_exports_id_patch

        Modify  # noqa: E501
        """
        pass

    def test_nfs_exports_post(self):
        """Test case for nfs_exports_post

        Create  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
