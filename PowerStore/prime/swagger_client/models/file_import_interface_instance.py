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


class FileImportInterfaceInstance(object):
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
        'ip_address': 'str',
        'prefix_length': 'int',
        'gateway': 'str',
        'vlan_id': 'int',
        'ip_port_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'ip_address': 'ip_address',
        'prefix_length': 'prefix_length',
        'gateway': 'gateway',
        'vlan_id': 'vlan_id',
        'ip_port_id': 'ip_port_id'
    }

    def __init__(self, id=None, ip_address=None, prefix_length=None, gateway=None, vlan_id=0, ip_port_id=None, _configuration=None):  # noqa: E501
        """FileImportInterfaceInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._ip_address = None
        self._prefix_length = None
        self._gateway = None
        self._vlan_id = None
        self._ip_port_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if ip_address is not None:
            self.ip_address = ip_address
        if prefix_length is not None:
            self.prefix_length = prefix_length
        if gateway is not None:
            self.gateway = gateway
        if vlan_id is not None:
            self.vlan_id = vlan_id
        if ip_port_id is not None:
            self.ip_port_id = ip_port_id

    @property
    def id(self):
        """Gets the id of this FileImportInterfaceInstance.  # noqa: E501

        Unique identifier of the file import interface.  # noqa: E501

        :return: The id of this FileImportInterfaceInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FileImportInterfaceInstance.

        Unique identifier of the file import interface.  # noqa: E501

        :param id: The id of this FileImportInterfaceInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def ip_address(self):
        """Gets the ip_address of this FileImportInterfaceInstance.  # noqa: E501

        IP address of the import interface. IPv4 and IPv6 are supported.  # noqa: E501

        :return: The ip_address of this FileImportInterfaceInstance.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this FileImportInterfaceInstance.

        IP address of the import interface. IPv4 and IPv6 are supported.  # noqa: E501

        :param ip_address: The ip_address of this FileImportInterfaceInstance.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def prefix_length(self):
        """Gets the prefix_length of this FileImportInterfaceInstance.  # noqa: E501

        Prefix length for the import interface. IPv4 and IPv6 are supported.  # noqa: E501

        :return: The prefix_length of this FileImportInterfaceInstance.  # noqa: E501
        :rtype: int
        """
        return self._prefix_length

    @prefix_length.setter
    def prefix_length(self, prefix_length):
        """Sets the prefix_length of this FileImportInterfaceInstance.

        Prefix length for the import interface. IPv4 and IPv6 are supported.  # noqa: E501

        :param prefix_length: The prefix_length of this FileImportInterfaceInstance.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                prefix_length is not None and prefix_length > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `prefix_length`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self._configuration.client_side_validation and
                prefix_length is not None and prefix_length < 0):  # noqa: E501
            raise ValueError("Invalid value for `prefix_length`, must be a value greater than or equal to `0`")  # noqa: E501

        self._prefix_length = prefix_length

    @property
    def gateway(self):
        """Gets the gateway of this FileImportInterfaceInstance.  # noqa: E501

        Gateway address for the import interface. IPv4 and IPv6 are supported.  # noqa: E501

        :return: The gateway of this FileImportInterfaceInstance.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this FileImportInterfaceInstance.

        Gateway address for the import interface. IPv4 and IPv6 are supported.  # noqa: E501

        :param gateway: The gateway of this FileImportInterfaceInstance.  # noqa: E501
        :type: str
        """

        self._gateway = gateway

    @property
    def vlan_id(self):
        """Gets the vlan_id of this FileImportInterfaceInstance.  # noqa: E501

        Virtual Local Area Network (VLAN) identifier for the import interface. The import interface uses the identifier to accept packets that have matching VLAN tags.  # noqa: E501

        :return: The vlan_id of this FileImportInterfaceInstance.  # noqa: E501
        :rtype: int
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this FileImportInterfaceInstance.

        Virtual Local Area Network (VLAN) identifier for the import interface. The import interface uses the identifier to accept packets that have matching VLAN tags.  # noqa: E501

        :param vlan_id: The vlan_id of this FileImportInterfaceInstance.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                vlan_id is not None and vlan_id > 4094):  # noqa: E501
            raise ValueError("Invalid value for `vlan_id`, must be a value less than or equal to `4094`")  # noqa: E501
        if (self._configuration.client_side_validation and
                vlan_id is not None and vlan_id < 0):  # noqa: E501
            raise ValueError("Invalid value for `vlan_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._vlan_id = vlan_id

    @property
    def ip_port_id(self):
        """Gets the ip_port_id of this FileImportInterfaceInstance.  # noqa: E501

        Unique indentifier of the IP Port.  # noqa: E501

        :return: The ip_port_id of this FileImportInterfaceInstance.  # noqa: E501
        :rtype: str
        """
        return self._ip_port_id

    @ip_port_id.setter
    def ip_port_id(self, ip_port_id):
        """Sets the ip_port_id of this FileImportInterfaceInstance.

        Unique indentifier of the IP Port.  # noqa: E501

        :param ip_port_id: The ip_port_id of this FileImportInterfaceInstance.  # noqa: E501
        :type: str
        """

        self._ip_port_id = ip_port_id

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
        if issubclass(FileImportInterfaceInstance, dict):
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
        if not isinstance(other, FileImportInterfaceInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileImportInterfaceInstance):
            return True

        return self.to_dict() != other.to_dict()
