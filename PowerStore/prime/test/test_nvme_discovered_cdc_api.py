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
from prime.swagger_client.api.nvme_discovered_cdc_api import NvmeDiscoveredCdcApi  # noqa: E501
from prime.swagger_client.rest import ApiException


class TestNvmeDiscoveredCdcApi(unittest.TestCase):
    """NvmeDiscoveredCdcApi unit test stubs"""

    def setUp(self):
        self.api = prime.swagger_client.api.nvme_discovered_cdc_api.NvmeDiscoveredCdcApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_nvme_discovered_cdc_get(self):
        """Test case for nvme_discovered_cdc_get

        Collection Query  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
