# coding: utf-8

"""
    PowerFlex NAS Management REST API

    NAS Storage Management REST API definition.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FileTreeQuotaModify(object):
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
        'description': 'str',
        'hard_limit': 'int',
        'soft_limit': 'int',
        'is_user_quotas_enforced': 'bool',
        'grace_period': 'int'
    }

    attribute_map = {
        'description': 'description',
        'hard_limit': 'hard_limit',
        'soft_limit': 'soft_limit',
        'is_user_quotas_enforced': 'is_user_quotas_enforced',
        'grace_period': 'grace_period'
    }

    def __init__(self, description=None, hard_limit=None, soft_limit=None, is_user_quotas_enforced=None, grace_period=0):  # noqa: E501
        """FileTreeQuotaModify - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._hard_limit = None
        self._soft_limit = None
        self._is_user_quotas_enforced = None
        self._grace_period = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if hard_limit is not None:
            self.hard_limit = hard_limit
        if soft_limit is not None:
            self.soft_limit = soft_limit
        if is_user_quotas_enforced is not None:
            self.is_user_quotas_enforced = is_user_quotas_enforced
        if grace_period is not None:
            self.grace_period = grace_period

    @property
    def description(self):
        """Gets the description of this FileTreeQuotaModify.  # noqa: E501

        Description of the tree quota.  # noqa: E501

        :return: The description of this FileTreeQuotaModify.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FileTreeQuotaModify.

        Description of the tree quota.  # noqa: E501

        :param description: The description of this FileTreeQuotaModify.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def hard_limit(self):
        """Gets the hard_limit of this FileTreeQuotaModify.  # noqa: E501

        Hard limit of the tree quota, in bytes. No hard limit when set to 0. This value can be used to compute amount of space that is consumed without limiting the space. Value is always rounded up to match the physical block size of the filesystem.  # noqa: E501

        :return: The hard_limit of this FileTreeQuotaModify.  # noqa: E501
        :rtype: int
        """
        return self._hard_limit

    @hard_limit.setter
    def hard_limit(self, hard_limit):
        """Sets the hard_limit of this FileTreeQuotaModify.

        Hard limit of the tree quota, in bytes. No hard limit when set to 0. This value can be used to compute amount of space that is consumed without limiting the space. Value is always rounded up to match the physical block size of the filesystem.  # noqa: E501

        :param hard_limit: The hard_limit of this FileTreeQuotaModify.  # noqa: E501
        :type: int
        """

        self._hard_limit = hard_limit

    @property
    def soft_limit(self):
        """Gets the soft_limit of this FileTreeQuotaModify.  # noqa: E501

        Soft limit of the tree quota, in bytes. No hard limit when set to 0. Value is always rounded up to match the physical block size of the filesystem.  # noqa: E501

        :return: The soft_limit of this FileTreeQuotaModify.  # noqa: E501
        :rtype: int
        """
        return self._soft_limit

    @soft_limit.setter
    def soft_limit(self, soft_limit):
        """Sets the soft_limit of this FileTreeQuotaModify.

        Soft limit of the tree quota, in bytes. No hard limit when set to 0. Value is always rounded up to match the physical block size of the filesystem.  # noqa: E501

        :param soft_limit: The soft_limit of this FileTreeQuotaModify.  # noqa: E501
        :type: int
        """

        self._soft_limit = soft_limit

    @property
    def is_user_quotas_enforced(self):
        """Gets the is_user_quotas_enforced of this FileTreeQuotaModify.  # noqa: E501

        Whether the quota must be enabled for all users, and whether user quota limits, if any, are enforced. Values are: - true - start tracking usage for all users on the quota tree, and enforce user quota limits. - false - stop tracking usage for all users on the quota tree, and do not enforce user quota limits.   # noqa: E501

        :return: The is_user_quotas_enforced of this FileTreeQuotaModify.  # noqa: E501
        :rtype: bool
        """
        return self._is_user_quotas_enforced

    @is_user_quotas_enforced.setter
    def is_user_quotas_enforced(self, is_user_quotas_enforced):
        """Sets the is_user_quotas_enforced of this FileTreeQuotaModify.

        Whether the quota must be enabled for all users, and whether user quota limits, if any, are enforced. Values are: - true - start tracking usage for all users on the quota tree, and enforce user quota limits. - false - stop tracking usage for all users on the quota tree, and do not enforce user quota limits.   # noqa: E501

        :param is_user_quotas_enforced: The is_user_quotas_enforced of this FileTreeQuotaModify.  # noqa: E501
        :type: bool
        """

        self._is_user_quotas_enforced = is_user_quotas_enforced

    @property
    def grace_period(self):
        """Gets the grace_period of this FileTreeQuotaModify.  # noqa: E501

        Grace period of tree quota, in seconds. No hard limit when set to -1. This will override the default grace period set at filesystem level.  # noqa: E501

        :return: The grace_period of this FileTreeQuotaModify.  # noqa: E501
        :rtype: int
        """
        return self._grace_period

    @grace_period.setter
    def grace_period(self, grace_period):
        """Sets the grace_period of this FileTreeQuotaModify.

        Grace period of tree quota, in seconds. No hard limit when set to -1. This will override the default grace period set at filesystem level.  # noqa: E501

        :param grace_period: The grace_period of this FileTreeQuotaModify.  # noqa: E501
        :type: int
        """

        self._grace_period = grace_period

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
        if issubclass(FileTreeQuotaModify, dict):
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
        if not isinstance(other, FileTreeQuotaModify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
