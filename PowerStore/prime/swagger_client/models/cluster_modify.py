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


class ClusterModify(object):
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
        'name': 'str',
        'physical_mtu': 'int'
    }

    attribute_map = {
        'name': 'name',
        'physical_mtu': 'physical_mtu'
    }

    def __init__(self, name=None, physical_mtu=None, _configuration=None):  # noqa: E501
        """ClusterModify - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._physical_mtu = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if physical_mtu is not None:
            self.physical_mtu = physical_mtu

    @property
    def name(self):
        """Gets the name of this ClusterModify.  # noqa: E501

        The new name for the cluster. The name can be up to 64 UTF-8 characters and cannot be an empty string.  # noqa: E501

        :return: The name of this ClusterModify.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterModify.

        The new name for the cluster. The name can be up to 64 UTF-8 characters and cannot be an empty string.  # noqa: E501

        :param name: The name of this ClusterModify.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 64):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def physical_mtu(self):
        """Gets the physical_mtu of this ClusterModify.  # noqa: E501

        The physical ethernet port (eth_port resource) MTU setting is global for all ports in the cluster. This is the default MTU setting for IP traffic, and the upper limit on network-specific MTU settings (network resource), where this can be overridden for some specific kinds of traffic (management, data, and vmotion). This value must be in the range 1500-9000.  # noqa: E501

        :return: The physical_mtu of this ClusterModify.  # noqa: E501
        :rtype: int
        """
        return self._physical_mtu

    @physical_mtu.setter
    def physical_mtu(self, physical_mtu):
        """Sets the physical_mtu of this ClusterModify.

        The physical ethernet port (eth_port resource) MTU setting is global for all ports in the cluster. This is the default MTU setting for IP traffic, and the upper limit on network-specific MTU settings (network resource), where this can be overridden for some specific kinds of traffic (management, data, and vmotion). This value must be in the range 1500-9000.  # noqa: E501

        :param physical_mtu: The physical_mtu of this ClusterModify.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                physical_mtu is not None and physical_mtu > 9000):  # noqa: E501
            raise ValueError("Invalid value for `physical_mtu`, must be a value less than or equal to `9000`")  # noqa: E501
        if (self._configuration.client_side_validation and
                physical_mtu is not None and physical_mtu < 1500):  # noqa: E501
            raise ValueError("Invalid value for `physical_mtu`, must be a value greater than or equal to `1500`")  # noqa: E501

        self._physical_mtu = physical_mtu

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
        if issubclass(ClusterModify, dict):
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
        if not isinstance(other, ClusterModify):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterModify):
            return True

        return self.to_dict() != other.to_dict()
