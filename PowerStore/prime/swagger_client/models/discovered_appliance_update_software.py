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


class DiscoveredApplianceUpdateSoftware(object):
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
        'appliance_address': 'str',
        'appliance_dst': 'str',
        'mode': 'DiscoveredApplianceModeEnum',
        'password': 'str'
    }

    attribute_map = {
        'appliance_address': 'appliance_address',
        'appliance_dst': 'appliance_dst',
        'mode': 'mode',
        'password': 'password'
    }

    def __init__(self, appliance_address=None, appliance_dst=None, mode=None, password=None, _configuration=None):  # noqa: E501
        """DiscoveredApplianceUpdateSoftware - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._appliance_address = None
        self._appliance_dst = None
        self._mode = None
        self._password = None
        self.discriminator = None

        if appliance_address is not None:
            self.appliance_address = appliance_address
        if appliance_dst is not None:
            self.appliance_dst = appliance_dst
        if mode is not None:
            self.mode = mode
        if password is not None:
            self.password = password

    @property
    def appliance_address(self):
        """Gets the appliance_address of this DiscoveredApplianceUpdateSoftware.  # noqa: E501

        Link local address of unconfigured appliance.  # noqa: E501

        :return: The appliance_address of this DiscoveredApplianceUpdateSoftware.  # noqa: E501
        :rtype: str
        """
        return self._appliance_address

    @appliance_address.setter
    def appliance_address(self, appliance_address):
        """Sets the appliance_address of this DiscoveredApplianceUpdateSoftware.

        Link local address of unconfigured appliance.  # noqa: E501

        :param appliance_address: The appliance_address of this DiscoveredApplianceUpdateSoftware.  # noqa: E501
        :type: str
        """

        self._appliance_address = appliance_address

    @property
    def appliance_dst(self):
        """Gets the appliance_dst of this DiscoveredApplianceUpdateSoftware.  # noqa: E501

        Appliance service tag.  # noqa: E501

        :return: The appliance_dst of this DiscoveredApplianceUpdateSoftware.  # noqa: E501
        :rtype: str
        """
        return self._appliance_dst

    @appliance_dst.setter
    def appliance_dst(self, appliance_dst):
        """Sets the appliance_dst of this DiscoveredApplianceUpdateSoftware.

        Appliance service tag.  # noqa: E501

        :param appliance_dst: The appliance_dst of this DiscoveredApplianceUpdateSoftware.  # noqa: E501
        :type: str
        """

        self._appliance_dst = appliance_dst

    @property
    def mode(self):
        """Gets the mode of this DiscoveredApplianceUpdateSoftware.  # noqa: E501


        :return: The mode of this DiscoveredApplianceUpdateSoftware.  # noqa: E501
        :rtype: DiscoveredApplianceModeEnum
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this DiscoveredApplianceUpdateSoftware.


        :param mode: The mode of this DiscoveredApplianceUpdateSoftware.  # noqa: E501
        :type: DiscoveredApplianceModeEnum
        """

        self._mode = mode

    @property
    def password(self):
        """Gets the password of this DiscoveredApplianceUpdateSoftware.  # noqa: E501

        Service user password to access unconfigured appliance.  # noqa: E501

        :return: The password of this DiscoveredApplianceUpdateSoftware.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this DiscoveredApplianceUpdateSoftware.

        Service user password to access unconfigured appliance.  # noqa: E501

        :param password: The password of this DiscoveredApplianceUpdateSoftware.  # noqa: E501
        :type: str
        """

        self._password = password

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
        if issubclass(DiscoveredApplianceUpdateSoftware, dict):
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
        if not isinstance(other, DiscoveredApplianceUpdateSoftware):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DiscoveredApplianceUpdateSoftware):
            return True

        return self.to_dict() != other.to_dict()
