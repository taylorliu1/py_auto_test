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


class LocalUserCreate(object):
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
        'password': 'str',
        'role_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'password': 'password',
        'role_id': 'role_id'
    }

    def __init__(self, name=None, password=None, role_id=None, _configuration=None):  # noqa: E501
        """LocalUserCreate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._password = None
        self._role_id = None
        self.discriminator = None

        self.name = name
        self.password = password
        self.role_id = role_id

    @property
    def name(self):
        """Gets the name of this LocalUserCreate.  # noqa: E501

        Name of the new local user account to be created. The name value can be 1 to 64 UTF-8 characters long, and may only use alphanumeric characters. Dot(.) is the only special character allowed.  # noqa: E501

        :return: The name of this LocalUserCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LocalUserCreate.

        Name of the new local user account to be created. The name value can be 1 to 64 UTF-8 characters long, and may only use alphanumeric characters. Dot(.) is the only special character allowed.  # noqa: E501

        :param name: The name of this LocalUserCreate.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 64):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def password(self):
        """Gets the password of this LocalUserCreate.  # noqa: E501

        Password for the new local user account to be created. The password value can be 8 to 40 UTF-8 characters long, and include as a minimum one uppercase character, one lowercase character, one numeric character, and one special character from (!,@#$%^*?_~).  # noqa: E501

        :return: The password of this LocalUserCreate.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this LocalUserCreate.

        Password for the new local user account to be created. The password value can be 8 to 40 UTF-8 characters long, and include as a minimum one uppercase character, one lowercase character, one numeric character, and one special character from (!,@#$%^*?_~).  # noqa: E501

        :param password: The password of this LocalUserCreate.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                password is not None and len(password) > 40):
            raise ValueError("Invalid value for `password`, length must be less than or equal to `40`")  # noqa: E501
        if (self._configuration.client_side_validation and
                password is not None and len(password) < 8):
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `8`")  # noqa: E501

        self._password = password

    @property
    def role_id(self):
        """Gets the role_id of this LocalUserCreate.  # noqa: E501

        The unique identifier of the role to which the new local user will be mapped. Where role_id \"1\" is for Administrator, \"2\" is for Storage Administrator, \"3\" is for Operator, \"4\" is for VM Administrator and \"5\" is for Security Administrator roles. name:{name} can be used instead of {id}. For example:'role_id':'name:role_name'  # noqa: E501

        :return: The role_id of this LocalUserCreate.  # noqa: E501
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this LocalUserCreate.

        The unique identifier of the role to which the new local user will be mapped. Where role_id \"1\" is for Administrator, \"2\" is for Storage Administrator, \"3\" is for Operator, \"4\" is for VM Administrator and \"5\" is for Security Administrator roles. name:{name} can be used instead of {id}. For example:'role_id':'name:role_name'  # noqa: E501

        :param role_id: The role_id of this LocalUserCreate.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and role_id is None:
            raise ValueError("Invalid value for `role_id`, must not be `None`")  # noqa: E501

        self._role_id = role_id

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
        if issubclass(LocalUserCreate, dict):
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
        if not isinstance(other, LocalUserCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LocalUserCreate):
            return True

        return self.to_dict() != other.to_dict()
