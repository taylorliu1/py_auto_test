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


class LoginSessionInstance(object):
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
        'user': 'str',
        'role_ids': 'list[str]',
        'idle_timeout': 'int',
        'is_password_change_required': 'bool',
        'is_built_in_user': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'user': 'user',
        'role_ids': 'role_ids',
        'idle_timeout': 'idle_timeout',
        'is_password_change_required': 'is_password_change_required',
        'is_built_in_user': 'is_built_in_user'
    }

    def __init__(self, id=None, user=None, role_ids=None, idle_timeout=None, is_password_change_required=None, is_built_in_user=None, _configuration=None):  # noqa: E501
        """LoginSessionInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._user = None
        self._role_ids = None
        self._idle_timeout = None
        self._is_password_change_required = None
        self._is_built_in_user = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user is not None:
            self.user = user
        if role_ids is not None:
            self.role_ids = role_ids
        if idle_timeout is not None:
            self.idle_timeout = idle_timeout
        if is_password_change_required is not None:
            self.is_password_change_required = is_password_change_required
        if is_built_in_user is not None:
            self.is_built_in_user = is_built_in_user

    @property
    def id(self):
        """Gets the id of this LoginSessionInstance.  # noqa: E501

        Unique identifier of the login session.  # noqa: E501

        :return: The id of this LoginSessionInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LoginSessionInstance.

        Unique identifier of the login session.  # noqa: E501

        :param id: The id of this LoginSessionInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def user(self):
        """Gets the user of this LoginSessionInstance.  # noqa: E501

        Fully qualified user account name being used to log in.  # noqa: E501

        :return: The user of this LoginSessionInstance.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this LoginSessionInstance.

        Fully qualified user account name being used to log in.  # noqa: E501

        :param user: The user of this LoginSessionInstance.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def role_ids(self):
        """Gets the role_ids of this LoginSessionInstance.  # noqa: E501

        Roles to which the logged-in user is mapped.  # noqa: E501

        :return: The role_ids of this LoginSessionInstance.  # noqa: E501
        :rtype: list[str]
        """
        return self._role_ids

    @role_ids.setter
    def role_ids(self, role_ids):
        """Sets the role_ids of this LoginSessionInstance.

        Roles to which the logged-in user is mapped.  # noqa: E501

        :param role_ids: The role_ids of this LoginSessionInstance.  # noqa: E501
        :type: list[str]
        """

        self._role_ids = role_ids

    @property
    def idle_timeout(self):
        """Gets the idle_timeout of this LoginSessionInstance.  # noqa: E501

        Remaining idle time until the session will expire, in seconds.  # noqa: E501

        :return: The idle_timeout of this LoginSessionInstance.  # noqa: E501
        :rtype: int
        """
        return self._idle_timeout

    @idle_timeout.setter
    def idle_timeout(self, idle_timeout):
        """Sets the idle_timeout of this LoginSessionInstance.

        Remaining idle time until the session will expire, in seconds.  # noqa: E501

        :param idle_timeout: The idle_timeout of this LoginSessionInstance.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                idle_timeout is not None and idle_timeout > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `idle_timeout`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self._configuration.client_side_validation and
                idle_timeout is not None and idle_timeout < 0):  # noqa: E501
            raise ValueError("Invalid value for `idle_timeout`, must be a value greater than or equal to `0`")  # noqa: E501

        self._idle_timeout = idle_timeout

    @property
    def is_password_change_required(self):
        """Gets the is_password_change_required of this LoginSessionInstance.  # noqa: E501

        Indicates whether the logged-in user requires a password change.  # noqa: E501

        :return: The is_password_change_required of this LoginSessionInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_password_change_required

    @is_password_change_required.setter
    def is_password_change_required(self, is_password_change_required):
        """Sets the is_password_change_required of this LoginSessionInstance.

        Indicates whether the logged-in user requires a password change.  # noqa: E501

        :param is_password_change_required: The is_password_change_required of this LoginSessionInstance.  # noqa: E501
        :type: bool
        """

        self._is_password_change_required = is_password_change_required

    @property
    def is_built_in_user(self):
        """Gets the is_built_in_user of this LoginSessionInstance.  # noqa: E501

        Indicates whether the logged-in user is predefined.  # noqa: E501

        :return: The is_built_in_user of this LoginSessionInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_built_in_user

    @is_built_in_user.setter
    def is_built_in_user(self, is_built_in_user):
        """Sets the is_built_in_user of this LoginSessionInstance.

        Indicates whether the logged-in user is predefined.  # noqa: E501

        :param is_built_in_user: The is_built_in_user of this LoginSessionInstance.  # noqa: E501
        :type: bool
        """

        self._is_built_in_user = is_built_in_user

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
        if issubclass(LoginSessionInstance, dict):
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
        if not isinstance(other, LoginSessionInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LoginSessionInstance):
            return True

        return self.to_dict() != other.to_dict()
