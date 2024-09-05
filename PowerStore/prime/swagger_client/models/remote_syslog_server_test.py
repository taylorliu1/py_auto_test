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


class RemoteSyslogServerTest(object):
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
        'message': 'str'
    }

    attribute_map = {
        'message': 'message'
    }

    def __init__(self, message=None, _configuration=None):  # noqa: E501
        """RemoteSyslogServerTest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._message = None
        self.discriminator = None

        if message is not None:
            self.message = message

    @property
    def message(self):
        """Gets the message of this RemoteSyslogServerTest.  # noqa: E501

        Custom text message to be sent as part of the remote syslog server test operation.  # noqa: E501

        :return: The message of this RemoteSyslogServerTest.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this RemoteSyslogServerTest.

        Custom text message to be sent as part of the remote syslog server test operation.  # noqa: E501

        :param message: The message of this RemoteSyslogServerTest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                message is not None and len(message) > 256):
            raise ValueError("Invalid value for `message`, length must be less than or equal to `256`")  # noqa: E501

        self._message = message

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
        if issubclass(RemoteSyslogServerTest, dict):
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
        if not isinstance(other, RemoteSyslogServerTest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RemoteSyslogServerTest):
            return True

        return self.to_dict() != other.to_dict()
