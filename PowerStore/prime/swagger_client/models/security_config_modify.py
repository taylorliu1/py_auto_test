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


class SecurityConfigModify(object):
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
        'protocol_mode': 'SecurityProtocolModeEnum',
        'is_http_redirect_enabled': 'bool'
    }

    attribute_map = {
        'protocol_mode': 'protocol_mode',
        'is_http_redirect_enabled': 'is_http_redirect_enabled'
    }

    def __init__(self, protocol_mode=None, is_http_redirect_enabled=None, _configuration=None):  # noqa: E501
        """SecurityConfigModify - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._protocol_mode = None
        self._is_http_redirect_enabled = None
        self.discriminator = None

        if protocol_mode is not None:
            self.protocol_mode = protocol_mode
        if is_http_redirect_enabled is not None:
            self.is_http_redirect_enabled = is_http_redirect_enabled

    @property
    def protocol_mode(self):
        """Gets the protocol_mode of this SecurityConfigModify.  # noqa: E501


        :return: The protocol_mode of this SecurityConfigModify.  # noqa: E501
        :rtype: SecurityProtocolModeEnum
        """
        return self._protocol_mode

    @protocol_mode.setter
    def protocol_mode(self, protocol_mode):
        """Sets the protocol_mode of this SecurityConfigModify.


        :param protocol_mode: The protocol_mode of this SecurityConfigModify.  # noqa: E501
        :type: SecurityProtocolModeEnum
        """

        self._protocol_mode = protocol_mode

    @property
    def is_http_redirect_enabled(self):
        """Gets the is_http_redirect_enabled of this SecurityConfigModify.  # noqa: E501

        If true, redirecting HTTP requests to HTTPs is enabled. If false, HTTP redirection is disabled and only HTTPs is supported. Was added in version 3.0.0.0.  # noqa: E501

        :return: The is_http_redirect_enabled of this SecurityConfigModify.  # noqa: E501
        :rtype: bool
        """
        return self._is_http_redirect_enabled

    @is_http_redirect_enabled.setter
    def is_http_redirect_enabled(self, is_http_redirect_enabled):
        """Sets the is_http_redirect_enabled of this SecurityConfigModify.

        If true, redirecting HTTP requests to HTTPs is enabled. If false, HTTP redirection is disabled and only HTTPs is supported. Was added in version 3.0.0.0.  # noqa: E501

        :param is_http_redirect_enabled: The is_http_redirect_enabled of this SecurityConfigModify.  # noqa: E501
        :type: bool
        """

        self._is_http_redirect_enabled = is_http_redirect_enabled

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
        if issubclass(SecurityConfigModify, dict):
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
        if not isinstance(other, SecurityConfigModify):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SecurityConfigModify):
            return True

        return self.to_dict() != other.to_dict()
