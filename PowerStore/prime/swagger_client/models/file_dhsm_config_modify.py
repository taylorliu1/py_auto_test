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


class FileDhsmConfigModify(object):
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
        'user_name': 'str',
        'password': 'str'
    }

    attribute_map = {
        'user_name': 'user_name',
        'password': 'password'
    }

    def __init__(self, user_name=None, password=None, _configuration=None):  # noqa: E501
        """FileDhsmConfigModify - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._user_name = None
        self._password = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if password is not None:
            self.password = password

    @property
    def user_name(self):
        """Gets the user_name of this FileDhsmConfigModify.  # noqa: E501

        User name for authentication to the DHSM server.  # noqa: E501

        :return: The user_name of this FileDhsmConfigModify.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this FileDhsmConfigModify.

        User name for authentication to the DHSM server.  # noqa: E501

        :param user_name: The user_name of this FileDhsmConfigModify.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                user_name is not None and len(user_name) > 64):
            raise ValueError("Invalid value for `user_name`, length must be less than or equal to `64`")  # noqa: E501
        if (self._configuration.client_side_validation and
                user_name is not None and len(user_name) < 1):
            raise ValueError("Invalid value for `user_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._user_name = user_name

    @property
    def password(self):
        """Gets the password of this FileDhsmConfigModify.  # noqa: E501

        The password for authentication to the DHSM server.  # noqa: E501

        :return: The password of this FileDhsmConfigModify.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this FileDhsmConfigModify.

        The password for authentication to the DHSM server.  # noqa: E501

        :param password: The password of this FileDhsmConfigModify.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                password is not None and len(password) > 15):
            raise ValueError("Invalid value for `password`, length must be less than or equal to `15`")  # noqa: E501
        if (self._configuration.client_side_validation and
                password is not None and len(password) < 1):
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `1`")  # noqa: E501

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
        if issubclass(FileDhsmConfigModify, dict):
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
        if not isinstance(other, FileDhsmConfigModify):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileDhsmConfigModify):
            return True

        return self.to_dict() != other.to_dict()
