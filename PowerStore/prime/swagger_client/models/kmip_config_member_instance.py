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


class KmipConfigMemberInstance(object):
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
        'status': 'KMIPConfigStatusEnum',
        'status_l10n': 'str'
    }

    attribute_map = {
        'address': 'address',
        'status': 'status',
        'status_l10n': 'status_l10n'
    }

    def __init__(self, address=None, status=None, status_l10n=None, _configuration=None):  # noqa: E501
        """KmipConfigMemberInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._address = None
        self._status = None
        self._status_l10n = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if status is not None:
            self.status = status
        if status_l10n is not None:
            self.status_l10n = status_l10n

    @property
    def address(self):
        """Gets the address of this KmipConfigMemberInstance.  # noqa: E501

        Network address of a KMIP server. It may be specified as IPv4, IPv6, or as a host name.  # noqa: E501

        :return: The address of this KmipConfigMemberInstance.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this KmipConfigMemberInstance.

        Network address of a KMIP server. It may be specified as IPv4, IPv6, or as a host name.  # noqa: E501

        :param address: The address of this KmipConfigMemberInstance.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def status(self):
        """Gets the status of this KmipConfigMemberInstance.  # noqa: E501


        :return: The status of this KmipConfigMemberInstance.  # noqa: E501
        :rtype: KMIPConfigStatusEnum
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this KmipConfigMemberInstance.


        :param status: The status of this KmipConfigMemberInstance.  # noqa: E501
        :type: KMIPConfigStatusEnum
        """

        self._status = status

    @property
    def status_l10n(self):
        """Gets the status_l10n of this KmipConfigMemberInstance.  # noqa: E501

        Localized message string corresponding to status Was added in version 3.0.0.0.  # noqa: E501

        :return: The status_l10n of this KmipConfigMemberInstance.  # noqa: E501
        :rtype: str
        """
        return self._status_l10n

    @status_l10n.setter
    def status_l10n(self, status_l10n):
        """Sets the status_l10n of this KmipConfigMemberInstance.

        Localized message string corresponding to status Was added in version 3.0.0.0.  # noqa: E501

        :param status_l10n: The status_l10n of this KmipConfigMemberInstance.  # noqa: E501
        :type: str
        """

        self._status_l10n = status_l10n

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
        if issubclass(KmipConfigMemberInstance, dict):
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
        if not isinstance(other, KmipConfigMemberInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KmipConfigMemberInstance):
            return True

        return self.to_dict() != other.to_dict()
