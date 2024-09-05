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


class IpPoolAddressInstance(object):
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
        'id': 'str',
        'name': 'str',
        'network_id': 'str',
        'ip_port_id': 'str',
        'appliance_id': 'str',
        'node_id': 'str',
        'address': 'str',
        'purposes': 'list[IpPurposeTypeEnum]',
        'purposes_l10n': 'list[str]',
        'nvme_discovered_cdcs': 'list[NvmeDiscoveredCdcInstance]',
        'network': 'NetworkInstance',
        'ip_port': 'IpPortInstance',
        'appliance': 'ApplianceInstance',
        'node': 'NodeInstance'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'network_id': 'network_id',
        'ip_port_id': 'ip_port_id',
        'appliance_id': 'appliance_id',
        'node_id': 'node_id',
        'address': 'address',
        'purposes': 'purposes',
        'purposes_l10n': 'purposes_l10n',
        'nvme_discovered_cdcs': 'nvme_discovered_cdcs',
        'network': 'network',
        'ip_port': 'ip_port',
        'appliance': 'appliance',
        'node': 'node'
    }

    def __init__(self, id=None, name=None, network_id=None, ip_port_id=None, appliance_id=None, node_id=None, address=None, purposes=None, purposes_l10n=None, nvme_discovered_cdcs=None, network=None, ip_port=None, appliance=None, node=None, _configuration=None):  # noqa: E501
        """IpPoolAddressInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._network_id = None
        self._ip_port_id = None
        self._appliance_id = None
        self._node_id = None
        self._address = None
        self._purposes = None
        self._purposes_l10n = None
        self._nvme_discovered_cdcs = None
        self._network = None
        self._ip_port = None
        self._appliance = None
        self._node = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if network_id is not None:
            self.network_id = network_id
        if ip_port_id is not None:
            self.ip_port_id = ip_port_id
        if appliance_id is not None:
            self.appliance_id = appliance_id
        if node_id is not None:
            self.node_id = node_id
        if address is not None:
            self.address = address
        if purposes is not None:
            self.purposes = purposes
        if purposes_l10n is not None:
            self.purposes_l10n = purposes_l10n
        if nvme_discovered_cdcs is not None:
            self.nvme_discovered_cdcs = nvme_discovered_cdcs
        if network is not None:
            self.network = network
        if ip_port is not None:
            self.ip_port = ip_port
        if appliance is not None:
            self.appliance = appliance
        if node is not None:
            self.node = node

    @property
    def id(self):
        """Gets the id of this IpPoolAddressInstance.  # noqa: E501

        Unique identifier of the IP address.  # noqa: E501

        :return: The id of this IpPoolAddressInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IpPoolAddressInstance.

        Unique identifier of the IP address.  # noqa: E501

        :param id: The id of this IpPoolAddressInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this IpPoolAddressInstance.  # noqa: E501

        Name of the IP address.  This property supports case-insensitive filtering. Was added in version 2.0.0.0.  # noqa: E501

        :return: The name of this IpPoolAddressInstance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IpPoolAddressInstance.

        Name of the IP address.  This property supports case-insensitive filtering. Was added in version 2.0.0.0.  # noqa: E501

        :param name: The name of this IpPoolAddressInstance.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 256):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `256`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def network_id(self):
        """Gets the network_id of this IpPoolAddressInstance.  # noqa: E501

        Unique identifier of the network to which the IP address belongs.  # noqa: E501

        :return: The network_id of this IpPoolAddressInstance.  # noqa: E501
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this IpPoolAddressInstance.

        Unique identifier of the network to which the IP address belongs.  # noqa: E501

        :param network_id: The network_id of this IpPoolAddressInstance.  # noqa: E501
        :type: str
        """

        self._network_id = network_id

    @property
    def ip_port_id(self):
        """Gets the ip_port_id of this IpPoolAddressInstance.  # noqa: E501

        Unique identifier of the port that uses this IP address to provide access to storage network services, such as iSCSI. This attribute can be set only for an IP address used by networks of type Storage.  # noqa: E501

        :return: The ip_port_id of this IpPoolAddressInstance.  # noqa: E501
        :rtype: str
        """
        return self._ip_port_id

    @ip_port_id.setter
    def ip_port_id(self, ip_port_id):
        """Sets the ip_port_id of this IpPoolAddressInstance.

        Unique identifier of the port that uses this IP address to provide access to storage network services, such as iSCSI. This attribute can be set only for an IP address used by networks of type Storage.  # noqa: E501

        :param ip_port_id: The ip_port_id of this IpPoolAddressInstance.  # noqa: E501
        :type: str
        """

        self._ip_port_id = ip_port_id

    @property
    def appliance_id(self):
        """Gets the appliance_id of this IpPoolAddressInstance.  # noqa: E501

        Unique identifier of the appliance to which the IP address belongs.  # noqa: E501

        :return: The appliance_id of this IpPoolAddressInstance.  # noqa: E501
        :rtype: str
        """
        return self._appliance_id

    @appliance_id.setter
    def appliance_id(self, appliance_id):
        """Sets the appliance_id of this IpPoolAddressInstance.

        Unique identifier of the appliance to which the IP address belongs.  # noqa: E501

        :param appliance_id: The appliance_id of this IpPoolAddressInstance.  # noqa: E501
        :type: str
        """

        self._appliance_id = appliance_id

    @property
    def node_id(self):
        """Gets the node_id of this IpPoolAddressInstance.  # noqa: E501

        Unique identifier of the cluster node to which the IP address belongs.  # noqa: E501

        :return: The node_id of this IpPoolAddressInstance.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this IpPoolAddressInstance.

        Unique identifier of the cluster node to which the IP address belongs.  # noqa: E501

        :param node_id: The node_id of this IpPoolAddressInstance.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def address(self):
        """Gets the address of this IpPoolAddressInstance.  # noqa: E501

        IP address value, in IPv4 or IPv6 format.  # noqa: E501

        :return: The address of this IpPoolAddressInstance.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this IpPoolAddressInstance.

        IP address value, in IPv4 or IPv6 format.  # noqa: E501

        :param address: The address of this IpPoolAddressInstance.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def purposes(self):
        """Gets the purposes of this IpPoolAddressInstance.  # noqa: E501

        IP address purposes.  # noqa: E501

        :return: The purposes of this IpPoolAddressInstance.  # noqa: E501
        :rtype: list[IpPurposeTypeEnum]
        """
        return self._purposes

    @purposes.setter
    def purposes(self, purposes):
        """Sets the purposes of this IpPoolAddressInstance.

        IP address purposes.  # noqa: E501

        :param purposes: The purposes of this IpPoolAddressInstance.  # noqa: E501
        :type: list[IpPurposeTypeEnum]
        """

        self._purposes = purposes

    @property
    def purposes_l10n(self):
        """Gets the purposes_l10n of this IpPoolAddressInstance.  # noqa: E501

        Localized message array corresponding to purposes  # noqa: E501

        :return: The purposes_l10n of this IpPoolAddressInstance.  # noqa: E501
        :rtype: list[str]
        """
        return self._purposes_l10n

    @purposes_l10n.setter
    def purposes_l10n(self, purposes_l10n):
        """Sets the purposes_l10n of this IpPoolAddressInstance.

        Localized message array corresponding to purposes  # noqa: E501

        :param purposes_l10n: The purposes_l10n of this IpPoolAddressInstance.  # noqa: E501
        :type: list[str]
        """

        self._purposes_l10n = purposes_l10n

    @property
    def nvme_discovered_cdcs(self):
        """Gets the nvme_discovered_cdcs of this IpPoolAddressInstance.  # noqa: E501

        This is the inverse of the resource type nvme_discovered_cdc association.  # noqa: E501

        :return: The nvme_discovered_cdcs of this IpPoolAddressInstance.  # noqa: E501
        :rtype: list[NvmeDiscoveredCdcInstance]
        """
        return self._nvme_discovered_cdcs

    @nvme_discovered_cdcs.setter
    def nvme_discovered_cdcs(self, nvme_discovered_cdcs):
        """Sets the nvme_discovered_cdcs of this IpPoolAddressInstance.

        This is the inverse of the resource type nvme_discovered_cdc association.  # noqa: E501

        :param nvme_discovered_cdcs: The nvme_discovered_cdcs of this IpPoolAddressInstance.  # noqa: E501
        :type: list[NvmeDiscoveredCdcInstance]
        """

        self._nvme_discovered_cdcs = nvme_discovered_cdcs

    @property
    def network(self):
        """Gets the network of this IpPoolAddressInstance.  # noqa: E501

        This is the embeddable reference form of network_id attribute.  # noqa: E501

        :return: The network of this IpPoolAddressInstance.  # noqa: E501
        :rtype: NetworkInstance
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this IpPoolAddressInstance.

        This is the embeddable reference form of network_id attribute.  # noqa: E501

        :param network: The network of this IpPoolAddressInstance.  # noqa: E501
        :type: NetworkInstance
        """

        self._network = network

    @property
    def ip_port(self):
        """Gets the ip_port of this IpPoolAddressInstance.  # noqa: E501

        This is the embeddable reference form of ip_port_id attribute.  # noqa: E501

        :return: The ip_port of this IpPoolAddressInstance.  # noqa: E501
        :rtype: IpPortInstance
        """
        return self._ip_port

    @ip_port.setter
    def ip_port(self, ip_port):
        """Sets the ip_port of this IpPoolAddressInstance.

        This is the embeddable reference form of ip_port_id attribute.  # noqa: E501

        :param ip_port: The ip_port of this IpPoolAddressInstance.  # noqa: E501
        :type: IpPortInstance
        """

        self._ip_port = ip_port

    @property
    def appliance(self):
        """Gets the appliance of this IpPoolAddressInstance.  # noqa: E501

        This is the embeddable reference form of appliance_id attribute.  # noqa: E501

        :return: The appliance of this IpPoolAddressInstance.  # noqa: E501
        :rtype: ApplianceInstance
        """
        return self._appliance

    @appliance.setter
    def appliance(self, appliance):
        """Sets the appliance of this IpPoolAddressInstance.

        This is the embeddable reference form of appliance_id attribute.  # noqa: E501

        :param appliance: The appliance of this IpPoolAddressInstance.  # noqa: E501
        :type: ApplianceInstance
        """

        self._appliance = appliance

    @property
    def node(self):
        """Gets the node of this IpPoolAddressInstance.  # noqa: E501

        This is the embeddable reference form of node_id attribute.  # noqa: E501

        :return: The node of this IpPoolAddressInstance.  # noqa: E501
        :rtype: NodeInstance
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this IpPoolAddressInstance.

        This is the embeddable reference form of node_id attribute.  # noqa: E501

        :param node: The node of this IpPoolAddressInstance.  # noqa: E501
        :type: NodeInstance
        """

        self._node = node

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
        if issubclass(IpPoolAddressInstance, dict):
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
        if not isinstance(other, IpPoolAddressInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IpPoolAddressInstance):
            return True

        return self.to_dict() != other.to_dict()
