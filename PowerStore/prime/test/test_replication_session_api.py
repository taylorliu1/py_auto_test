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
from prime.swagger_client.api.replication_session_api import ReplicationSessionApi  # noqa: E501
from prime.swagger_client.rest import ApiException


class TestReplicationSessionApi(unittest.TestCase):
    """ReplicationSessionApi unit test stubs"""

    def setUp(self):
        self.api = prime.swagger_client.api.replication_session_api.ReplicationSessionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_replication_session_get(self):
        """Test case for replication_session_get

        Collection Query  # noqa: E501
        """
        pass

    def test_replication_session_id_demote_post(self):
        """Test case for replication_session_id_demote_post

        Demote replication session  # noqa: E501
        """
        pass

    def test_replication_session_id_failover_post(self):
        """Test case for replication_session_id_failover_post

        Failover  # noqa: E501
        """
        pass

    def test_replication_session_id_get(self):
        """Test case for replication_session_id_get

        Instance Query  # noqa: E501
        """
        pass

    def test_replication_session_id_pause_post(self):
        """Test case for replication_session_id_pause_post

        Pause  # noqa: E501
        """
        pass

    def test_replication_session_id_promote_post(self):
        """Test case for replication_session_id_promote_post

        Promote replication session  # noqa: E501
        """
        pass

    def test_replication_session_id_reprotect_post(self):
        """Test case for replication_session_id_reprotect_post

        Reprotect  # noqa: E501
        """
        pass

    def test_replication_session_id_resume_post(self):
        """Test case for replication_session_id_resume_post

        Resume  # noqa: E501
        """
        pass

    def test_replication_session_id_start_failover_test_post(self):
        """Test case for replication_session_id_start_failover_test_post

        Start DR Failover Simulation Test  # noqa: E501
        """
        pass

    def test_replication_session_id_stop_failover_test_post(self):
        """Test case for replication_session_id_stop_failover_test_post

        Stop DR Failover Simulation Test  # noqa: E501
        """
        pass

    def test_replication_session_id_sync_post(self):
        """Test case for replication_session_id_sync_post

        Synchronize  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
