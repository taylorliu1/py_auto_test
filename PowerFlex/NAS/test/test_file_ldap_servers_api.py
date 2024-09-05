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
from swagger_client.api.file_ldap_servers_api import FileLdapServersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestFileLdapServersApi(unittest.TestCase):
    """FileLdapServersApi unit test stubs"""

    def setUp(self):
        self.api = FileLdapServersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_file_ldap_servers_get(self):
        """Test case for file_ldap_servers_get

        Collection Query  # noqa: E501
        """
        pass

    def test_file_ldap_servers_id_delete(self):
        """Test case for file_ldap_servers_id_delete

        Delete  # noqa: E501
        """
        pass

    def test_file_ldap_servers_id_get(self):
        """Test case for file_ldap_servers_id_get

        Instance Query  # noqa: E501
        """
        pass

    def test_file_ldap_servers_id_patch(self):
        """Test case for file_ldap_servers_id_patch

        Modify  # noqa: E501
        """
        pass

    def test_file_ldap_servers_post(self):
        """Test case for file_ldap_servers_post

        Create  # noqa: E501
        """
        pass

    def test_files_file_ldap_servers_id_certificate_get(self):
        """Test case for files_file_ldap_servers_id_certificate_get

        Download Certificate  # noqa: E501
        """
        pass

    def test_files_file_ldap_servers_id_certificate_post(self):
        """Test case for files_file_ldap_servers_id_certificate_post

        Upload Certificate  # noqa: E501
        """
        pass

    def test_files_file_ldap_servers_id_config_get(self):
        """Test case for files_file_ldap_servers_id_config_get

        Download Config  # noqa: E501
        """
        pass

    def test_files_file_ldap_servers_id_config_post(self):
        """Test case for files_file_ldap_servers_id_config_post

        Upload Config  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
