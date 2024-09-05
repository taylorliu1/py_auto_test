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


class SnapshotRuleClone(object):
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
        'force': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'force': 'force'
    }

    def __init__(self, name=None, force=False, _configuration=None):  # noqa: E501
        """SnapshotRuleClone - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._force = None
        self.discriminator = None

        self.name = name
        if force is not None:
            self.force = force

    @property
    def name(self):
        """Gets the name of this SnapshotRuleClone.  # noqa: E501

        Name of the newly created snapshot rule.  # noqa: E501

        :return: The name of this SnapshotRuleClone.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SnapshotRuleClone.

        Name of the newly created snapshot rule.  # noqa: E501

        :param name: The name of this SnapshotRuleClone.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def force(self):
        """Gets the force of this SnapshotRuleClone.  # noqa: E501

        Normally, this operation is only supported for user-managed snapshot rules. However, a non user-managed snapshot rule can be cloned when force is set to true.  # noqa: E501

        :return: The force of this SnapshotRuleClone.  # noqa: E501
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this SnapshotRuleClone.

        Normally, this operation is only supported for user-managed snapshot rules. However, a non user-managed snapshot rule can be cloned when force is set to true.  # noqa: E501

        :param force: The force of this SnapshotRuleClone.  # noqa: E501
        :type: bool
        """

        self._force = force

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
        if issubclass(SnapshotRuleClone, dict):
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
        if not isinstance(other, SnapshotRuleClone):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SnapshotRuleClone):
            return True

        return self.to_dict() != other.to_dict()
