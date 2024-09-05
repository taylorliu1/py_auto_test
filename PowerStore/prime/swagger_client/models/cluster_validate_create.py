# coding: utf-8

"""
    PowerStore REST API

    Storage cluster REST API definition. ( For \"Try It Out\", use the cluster management IP address to load this swaggerui interface. )  # noqa: E501

    OpenAPI spec version: 3.0.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from prime.swagger_client.configuration import Configuration


class ClusterValidateCreate(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'cluster': 'ClusterCreateCluster',
        'appliances': 'list[ClusterCreateAppliances]',
        'dns_servers': 'list[str]',
        'ntp_servers': 'list[str]',
        'physical_switches': 'list[ClusterCreatePhysicalSwitches]',
        'networks': 'list[ClusterCreateNetworks]',
        'vcenters': 'list[ClusterCreateVcenters]',
        'security_config': 'ClusterCreateSecurityConfig'
    }

    attribute_map = {
        'cluster': 'cluster',
        'appliances': 'appliances',
        'dns_servers': 'dns_servers',
        'ntp_servers': 'ntp_servers',
        'physical_switches': 'physical_switches',
        'networks': 'networks',
        'vcenters': 'vcenters',
        'security_config': 'security_config'
    }

    def __init__(self, cluster=None, appliances=None, dns_servers=None, ntp_servers=None, physical_switches=None, networks=None, vcenters=None, security_config=None, _configuration=None):  # noqa: E501
        """ClusterValidateCreate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cluster = None
        self._appliances = None
        self._dns_servers = None
        self._ntp_servers = None
        self._physical_switches = None
        self._networks = None
        self._vcenters = None
        self._security_config = None
        self.discriminator = None

        self.cluster = cluster
        self.appliances = appliances
        self.dns_servers = dns_servers
        self.ntp_servers = ntp_servers
        if physical_switches is not None:
            self.physical_switches = physical_switches
        self.networks = networks
        if vcenters is not None:
            self.vcenters = vcenters
        if security_config is not None:
            self.security_config = security_config

    @property
    def cluster(self):
        """Gets the cluster of this ClusterValidateCreate.  # noqa: E501


        :return: The cluster of this ClusterValidateCreate.  # noqa: E501
        :rtype: ClusterCreateCluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this ClusterValidateCreate.


        :param cluster: The cluster of this ClusterValidateCreate.  # noqa: E501
        :type: ClusterCreateCluster
        """
        if self._configuration.client_side_validation and cluster is None:
            raise ValueError("Invalid value for `cluster`, must not be `None`")  # noqa: E501

        self._cluster = cluster

    @property
    def appliances(self):
        """Gets the appliances of this ClusterValidateCreate.  # noqa: E501

        The configuration settings for adding appliances during cluster creation. At least one appliance is required.  # noqa: E501

        :return: The appliances of this ClusterValidateCreate.  # noqa: E501
        :rtype: list[ClusterCreateAppliances]
        """
        return self._appliances

    @appliances.setter
    def appliances(self, appliances):
        """Sets the appliances of this ClusterValidateCreate.

        The configuration settings for adding appliances during cluster creation. At least one appliance is required.  # noqa: E501

        :param appliances: The appliances of this ClusterValidateCreate.  # noqa: E501
        :type: list[ClusterCreateAppliances]
        """
        if self._configuration.client_side_validation and appliances is None:
            raise ValueError("Invalid value for `appliances`, must not be `None`")  # noqa: E501

        self._appliances = appliances

    @property
    def dns_servers(self):
        """Gets the dns_servers of this ClusterValidateCreate.  # noqa: E501


        :return: The dns_servers of this ClusterValidateCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._dns_servers

    @dns_servers.setter
    def dns_servers(self, dns_servers):
        """Sets the dns_servers of this ClusterValidateCreate.


        :param dns_servers: The dns_servers of this ClusterValidateCreate.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and dns_servers is None:
            raise ValueError("Invalid value for `dns_servers`, must not be `None`")  # noqa: E501

        self._dns_servers = dns_servers

    @property
    def ntp_servers(self):
        """Gets the ntp_servers of this ClusterValidateCreate.  # noqa: E501


        :return: The ntp_servers of this ClusterValidateCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._ntp_servers

    @ntp_servers.setter
    def ntp_servers(self, ntp_servers):
        """Sets the ntp_servers of this ClusterValidateCreate.


        :param ntp_servers: The ntp_servers of this ClusterValidateCreate.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and ntp_servers is None:
            raise ValueError("Invalid value for `ntp_servers`, must not be `None`")  # noqa: E501

        self._ntp_servers = ntp_servers

    @property
    def physical_switches(self):
        """Gets the physical_switches of this ClusterValidateCreate.  # noqa: E501

        Create physical switch settings for a cluster.  # noqa: E501

        :return: The physical_switches of this ClusterValidateCreate.  # noqa: E501
        :rtype: list[ClusterCreatePhysicalSwitches]
        """
        return self._physical_switches

    @physical_switches.setter
    def physical_switches(self, physical_switches):
        """Sets the physical_switches of this ClusterValidateCreate.

        Create physical switch settings for a cluster.  # noqa: E501

        :param physical_switches: The physical_switches of this ClusterValidateCreate.  # noqa: E501
        :type: list[ClusterCreatePhysicalSwitches]
        """

        self._physical_switches = physical_switches

    @property
    def networks(self):
        """Gets the networks of this ClusterValidateCreate.  # noqa: E501

        Configuration of one or more network(s) based on network type  # noqa: E501

        :return: The networks of this ClusterValidateCreate.  # noqa: E501
        :rtype: list[ClusterCreateNetworks]
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """Sets the networks of this ClusterValidateCreate.

        Configuration of one or more network(s) based on network type  # noqa: E501

        :param networks: The networks of this ClusterValidateCreate.  # noqa: E501
        :type: list[ClusterCreateNetworks]
        """
        if self._configuration.client_side_validation and networks is None:
            raise ValueError("Invalid value for `networks`, must not be `None`")  # noqa: E501

        self._networks = networks

    @property
    def vcenters(self):
        """Gets the vcenters of this ClusterValidateCreate.  # noqa: E501

        Configure vCenter settings when creating cluster. Parameters are required when creating PowerStore X cluster and optional for PowerStore cluster.  * Note - currently only single element is supported.  # noqa: E501

        :return: The vcenters of this ClusterValidateCreate.  # noqa: E501
        :rtype: list[ClusterCreateVcenters]
        """
        return self._vcenters

    @vcenters.setter
    def vcenters(self, vcenters):
        """Sets the vcenters of this ClusterValidateCreate.

        Configure vCenter settings when creating cluster. Parameters are required when creating PowerStore X cluster and optional for PowerStore cluster.  * Note - currently only single element is supported.  # noqa: E501

        :param vcenters: The vcenters of this ClusterValidateCreate.  # noqa: E501
        :type: list[ClusterCreateVcenters]
        """

        self._vcenters = vcenters

    @property
    def security_config(self):
        """Gets the security_config of this ClusterValidateCreate.  # noqa: E501

         Was added in version 3.0.0.0.  # noqa: E501

        :return: The security_config of this ClusterValidateCreate.  # noqa: E501
        :rtype: ClusterCreateSecurityConfig
        """
        return self._security_config

    @security_config.setter
    def security_config(self, security_config):
        """Sets the security_config of this ClusterValidateCreate.

         Was added in version 3.0.0.0.  # noqa: E501

        :param security_config: The security_config of this ClusterValidateCreate.  # noqa: E501
        :type: ClusterCreateSecurityConfig
        """

        self._security_config = security_config

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ClusterValidateCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ClusterValidateCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterValidateCreate):
            return True

        return self.to_dict() != other.to_dict()
