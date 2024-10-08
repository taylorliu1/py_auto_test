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
from prime.swagger_client.api.appliance_api import ApplianceApi  # noqa: E501
from prime.swagger_client.rest import ApiException


class TestApplianceApi(unittest.TestCase):
    """ApplianceApi unit test stubs"""

    def setUp(self):
        self.api = prime.swagger_client.api.appliance_api.ApplianceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_appliance_get(self):
        """Test case for appliance_get

        Collection Query  # noqa: E501
        """
        pass

    def test_appliance_id_delete(self):
        """Test case for appliance_id_delete

        Delete  # noqa: E501
        """
        pass

    def test_appliance_id_forecast_post(self):
        """Test case for appliance_id_forecast_post

        """
        pass

    def test_appliance_id_get(self):
        """Test case for appliance_id_get

        Instance Query  # noqa: E501
        """
        pass

    def test_appliance_id_patch(self):
        """Test case for appliance_id_patch

        Modify  # noqa: E501
        """
        pass

    def test_appliance_id_time_to_full_post(self):
        """Test case for appliance_id_time_to_full_post

        """
        pass

    def test_appliance_post(self):
        """Test case for appliance_post

        Add Appliance  # noqa: E501
        """
        pass

    def test_appliance_validate_create_post(self):
        """Test case for appliance_validate_create_post

        Validate Add Appliance  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
