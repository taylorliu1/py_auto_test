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


class PhysicalSwitchModify(object):
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
        'purpose': 'PhysicalSwitchPurposeEnum',
        'connections': 'list[PhysicalSwitchConnectionModify]'
    }

    attribute_map = {
        'name': 'name',
        'purpose': 'purpose',
        'connections': 'connections'
    }

    def __init__(self, name=None, purpose=None, connections=None, _configuration=None):  # noqa: E501
        """PhysicalSwitchModify - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._purpose = None
        self._connections = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if purpose is not None:
            self.purpose = purpose
        if connections is not None:
            self.connections = connections

    @property
    def name(self):
        """Gets the name of this PhysicalSwitchModify.  # noqa: E501

        Name of physical switch.  # noqa: E501

        :return: The name of this PhysicalSwitchModify.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PhysicalSwitchModify.

        Name of physical switch.  # noqa: E501

        :param name: The name of this PhysicalSwitchModify.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 128):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def purpose(self):
        """Gets the purpose of this PhysicalSwitchModify.  # noqa: E501


        :return: The purpose of this PhysicalSwitchModify.  # noqa: E501
        :rtype: PhysicalSwitchPurposeEnum
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """Sets the purpose of this PhysicalSwitchModify.


        :param purpose: The purpose of this PhysicalSwitchModify.  # noqa: E501
        :type: PhysicalSwitchPurposeEnum
        """

        self._purpose = purpose

    @property
    def connections(self):
        """Gets the connections of this PhysicalSwitchModify.  # noqa: E501

        Supported connections for a physical switch.  # noqa: E501

        :return: The connections of this PhysicalSwitchModify.  # noqa: E501
        :rtype: list[PhysicalSwitchConnectionModify]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        """Sets the connections of this PhysicalSwitchModify.

        Supported connections for a physical switch.  # noqa: E501

        :param connections: The connections of this PhysicalSwitchModify.  # noqa: E501
        :type: list[PhysicalSwitchConnectionModify]
        """

        self._connections = connections

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
        if issubclass(PhysicalSwitchModify, dict):
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
        if not isinstance(other, PhysicalSwitchModify):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PhysicalSwitchModify):
            return True

        return self.to_dict() != other.to_dict()
