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


class NetworkReplacePhysicalSwitchConnection(object):
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
        'address': 'str',
        'port': 'int',
        'connect_method': 'PhysicalSwitchConnectMethodEnum',
        'username': 'str',
        'ssh_password': 'str',
        'snmp_community_string': 'str'
    }

    attribute_map = {
        'address': 'address',
        'port': 'port',
        'connect_method': 'connect_method',
        'username': 'username',
        'ssh_password': 'ssh_password',
        'snmp_community_string': 'snmp_community_string'
    }

    def __init__(self, address=None, port=None, connect_method=None, username=None, ssh_password=None, snmp_community_string=None, _configuration=None):  # noqa: E501
        """NetworkReplacePhysicalSwitchConnection - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._address = None
        self._port = None
        self._connect_method = None
        self._username = None
        self._ssh_password = None
        self._snmp_community_string = None
        self.discriminator = None

        self.address = address
        if port is not None:
            self.port = port
        self.connect_method = connect_method
        if username is not None:
            self.username = username
        if ssh_password is not None:
            self.ssh_password = ssh_password
        if snmp_community_string is not None:
            self.snmp_community_string = snmp_community_string

    @property
    def address(self):
        """Gets the address of this NetworkReplacePhysicalSwitchConnection.  # noqa: E501

        Physical switch address in IPv4 or IPv6 or DNS hostname format.  # noqa: E501

        :return: The address of this NetworkReplacePhysicalSwitchConnection.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this NetworkReplacePhysicalSwitchConnection.

        Physical switch address in IPv4 or IPv6 or DNS hostname format.  # noqa: E501

        :param address: The address of this NetworkReplacePhysicalSwitchConnection.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def port(self):
        """Gets the port of this NetworkReplacePhysicalSwitchConnection.  # noqa: E501

        Port used for connection to switch.  # noqa: E501

        :return: The port of this NetworkReplacePhysicalSwitchConnection.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this NetworkReplacePhysicalSwitchConnection.

        Port used for connection to switch.  # noqa: E501

        :param port: The port of this NetworkReplacePhysicalSwitchConnection.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                port is not None and port > 65535):  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value less than or equal to `65535`")  # noqa: E501
        if (self._configuration.client_side_validation and
                port is not None and port < 0):  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value greater than or equal to `0`")  # noqa: E501

        self._port = port

    @property
    def connect_method(self):
        """Gets the connect_method of this NetworkReplacePhysicalSwitchConnection.  # noqa: E501


        :return: The connect_method of this NetworkReplacePhysicalSwitchConnection.  # noqa: E501
        :rtype: PhysicalSwitchConnectMethodEnum
        """
        return self._connect_method

    @connect_method.setter
    def connect_method(self, connect_method):
        """Sets the connect_method of this NetworkReplacePhysicalSwitchConnection.


        :param connect_method: The connect_method of this NetworkReplacePhysicalSwitchConnection.  # noqa: E501
        :type: PhysicalSwitchConnectMethodEnum
        """
        if self._configuration.client_side_validation and connect_method is None:
            raise ValueError("Invalid value for `connect_method`, must not be `None`")  # noqa: E501

        self._connect_method = connect_method

    @property
    def username(self):
        """Gets the username of this NetworkReplacePhysicalSwitchConnection.  # noqa: E501

        Username to connect a physical switch for SSH connection method.  # noqa: E501

        :return: The username of this NetworkReplacePhysicalSwitchConnection.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this NetworkReplacePhysicalSwitchConnection.

        Username to connect a physical switch for SSH connection method.  # noqa: E501

        :param username: The username of this NetworkReplacePhysicalSwitchConnection.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def ssh_password(self):
        """Gets the ssh_password of this NetworkReplacePhysicalSwitchConnection.  # noqa: E501

        SSH password to connect a physical switch if SSH connect method is specified.  # noqa: E501

        :return: The ssh_password of this NetworkReplacePhysicalSwitchConnection.  # noqa: E501
        :rtype: str
        """
        return self._ssh_password

    @ssh_password.setter
    def ssh_password(self, ssh_password):
        """Sets the ssh_password of this NetworkReplacePhysicalSwitchConnection.

        SSH password to connect a physical switch if SSH connect method is specified.  # noqa: E501

        :param ssh_password: The ssh_password of this NetworkReplacePhysicalSwitchConnection.  # noqa: E501
        :type: str
        """

        self._ssh_password = ssh_password

    @property
    def snmp_community_string(self):
        """Gets the snmp_community_string of this NetworkReplacePhysicalSwitchConnection.  # noqa: E501

        SNMPv2 community string, if SNMPv2c connect method is specified.  # noqa: E501

        :return: The snmp_community_string of this NetworkReplacePhysicalSwitchConnection.  # noqa: E501
        :rtype: str
        """
        return self._snmp_community_string

    @snmp_community_string.setter
    def snmp_community_string(self, snmp_community_string):
        """Sets the snmp_community_string of this NetworkReplacePhysicalSwitchConnection.

        SNMPv2 community string, if SNMPv2c connect method is specified.  # noqa: E501

        :param snmp_community_string: The snmp_community_string of this NetworkReplacePhysicalSwitchConnection.  # noqa: E501
        :type: str
        """

        self._snmp_community_string = snmp_community_string

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
        if issubclass(NetworkReplacePhysicalSwitchConnection, dict):
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
        if not isinstance(other, NetworkReplacePhysicalSwitchConnection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NetworkReplacePhysicalSwitchConnection):
            return True

        return self.to_dict() != other.to_dict()
