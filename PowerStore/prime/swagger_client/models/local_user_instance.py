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


class LocalUserInstance(object):
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
        'name': 'str',
        'is_built_in': 'bool',
        'is_locked': 'bool',
        'is_default_password': 'bool',
        'role_id': 'str',
        'password_expiration_timestamp': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'is_built_in': 'is_built_in',
        'is_locked': 'is_locked',
        'is_default_password': 'is_default_password',
        'role_id': 'role_id',
        'password_expiration_timestamp': 'password_expiration_timestamp'
    }

    def __init__(self, id=None, name=None, is_built_in=None, is_locked=None, is_default_password=None, role_id=None, password_expiration_timestamp=None, _configuration=None):  # noqa: E501
        """LocalUserInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._is_built_in = None
        self._is_locked = None
        self._is_default_password = None
        self._role_id = None
        self._password_expiration_timestamp = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if is_built_in is not None:
            self.is_built_in = is_built_in
        if is_locked is not None:
            self.is_locked = is_locked
        if is_default_password is not None:
            self.is_default_password = is_default_password
        if role_id is not None:
            self.role_id = role_id
        if password_expiration_timestamp is not None:
            self.password_expiration_timestamp = password_expiration_timestamp

    @property
    def id(self):
        """Gets the id of this LocalUserInstance.  # noqa: E501

        Unique identifier of the local user account.  # noqa: E501

        :return: The id of this LocalUserInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LocalUserInstance.

        Unique identifier of the local user account.  # noqa: E501

        :param id: The id of this LocalUserInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this LocalUserInstance.  # noqa: E501

        Name of the local user account.  # noqa: E501

        :return: The name of this LocalUserInstance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LocalUserInstance.

        Name of the local user account.  # noqa: E501

        :param name: The name of this LocalUserInstance.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_built_in(self):
        """Gets the is_built_in of this LocalUserInstance.  # noqa: E501

        Whether the user account is built-in or not.  # noqa: E501

        :return: The is_built_in of this LocalUserInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_built_in

    @is_built_in.setter
    def is_built_in(self, is_built_in):
        """Sets the is_built_in of this LocalUserInstance.

        Whether the user account is built-in or not.  # noqa: E501

        :param is_built_in: The is_built_in of this LocalUserInstance.  # noqa: E501
        :type: bool
        """

        self._is_built_in = is_built_in

    @property
    def is_locked(self):
        """Gets the is_locked of this LocalUserInstance.  # noqa: E501

        Whether the user account is locked or not. Defaults to false at creation time.  # noqa: E501

        :return: The is_locked of this LocalUserInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_locked

    @is_locked.setter
    def is_locked(self, is_locked):
        """Sets the is_locked of this LocalUserInstance.

        Whether the user account is locked or not. Defaults to false at creation time.  # noqa: E501

        :param is_locked: The is_locked of this LocalUserInstance.  # noqa: E501
        :type: bool
        """

        self._is_locked = is_locked

    @property
    def is_default_password(self):
        """Gets the is_default_password of this LocalUserInstance.  # noqa: E501

        Whether the user account has a default password or not. Only applies to default user accounts.  # noqa: E501

        :return: The is_default_password of this LocalUserInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_default_password

    @is_default_password.setter
    def is_default_password(self, is_default_password):
        """Sets the is_default_password of this LocalUserInstance.

        Whether the user account has a default password or not. Only applies to default user accounts.  # noqa: E501

        :param is_default_password: The is_default_password of this LocalUserInstance.  # noqa: E501
        :type: bool
        """

        self._is_default_password = is_default_password

    @property
    def role_id(self):
        """Gets the role_id of this LocalUserInstance.  # noqa: E501

        Unique identifier of the role local user account is mapped to.  # noqa: E501

        :return: The role_id of this LocalUserInstance.  # noqa: E501
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this LocalUserInstance.

        Unique identifier of the role local user account is mapped to.  # noqa: E501

        :param role_id: The role_id of this LocalUserInstance.  # noqa: E501
        :type: str
        """

        self._role_id = role_id

    @property
    def password_expiration_timestamp(self):
        """Gets the password_expiration_timestamp of this LocalUserInstance.  # noqa: E501

        Timestamp when the password will expire. Was added in version 3.0.0.0.  # noqa: E501

        :return: The password_expiration_timestamp of this LocalUserInstance.  # noqa: E501
        :rtype: datetime
        """
        return self._password_expiration_timestamp

    @password_expiration_timestamp.setter
    def password_expiration_timestamp(self, password_expiration_timestamp):
        """Sets the password_expiration_timestamp of this LocalUserInstance.

        Timestamp when the password will expire. Was added in version 3.0.0.0.  # noqa: E501

        :param password_expiration_timestamp: The password_expiration_timestamp of this LocalUserInstance.  # noqa: E501
        :type: datetime
        """

        self._password_expiration_timestamp = password_expiration_timestamp

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
        if issubclass(LocalUserInstance, dict):
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
        if not isinstance(other, LocalUserInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LocalUserInstance):
            return True

        return self.to_dict() != other.to_dict()
