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

class FileUserQuotaModify(object):
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
        'hard_limit': 'int',
        'soft_limit': 'int'
    }

    attribute_map = {
        'hard_limit': 'hard_limit',
        'soft_limit': 'soft_limit'
    }

    def __init__(self, hard_limit=None, soft_limit=None):  # noqa: E501
        """FileUserQuotaModify - a model defined in Swagger"""  # noqa: E501
        self._hard_limit = None
        self._soft_limit = None
        self.discriminator = None
        if hard_limit is not None:
            self.hard_limit = hard_limit
        if soft_limit is not None:
            self.soft_limit = soft_limit

    @property
    def hard_limit(self):
        """Gets the hard_limit of this FileUserQuotaModify.  # noqa: E501

        Hard limit of the user quota, in bytes. No hard limit when set to 0. This value can be used to compute amount of space that is consumed without limiting the space. Value is rounded up to match the physical block size of the filesystem.  # noqa: E501

        :return: The hard_limit of this FileUserQuotaModify.  # noqa: E501
        :rtype: int
        """
        return self._hard_limit

    @hard_limit.setter
    def hard_limit(self, hard_limit):
        """Sets the hard_limit of this FileUserQuotaModify.

        Hard limit of the user quota, in bytes. No hard limit when set to 0. This value can be used to compute amount of space that is consumed without limiting the space. Value is rounded up to match the physical block size of the filesystem.  # noqa: E501

        :param hard_limit: The hard_limit of this FileUserQuotaModify.  # noqa: E501
        :type: int
        """

        self._hard_limit = hard_limit

    @property
    def soft_limit(self):
        """Gets the soft_limit of this FileUserQuotaModify.  # noqa: E501

        Soft limit of the user quota, in bytes. No hard limit when set to 0. Value is rounded up to match the physical block size of the filesystem.  # noqa: E501

        :return: The soft_limit of this FileUserQuotaModify.  # noqa: E501
        :rtype: int
        """
        return self._soft_limit

    @soft_limit.setter
    def soft_limit(self, soft_limit):
        """Sets the soft_limit of this FileUserQuotaModify.

        Soft limit of the user quota, in bytes. No hard limit when set to 0. Value is rounded up to match the physical block size of the filesystem.  # noqa: E501

        :param soft_limit: The soft_limit of this FileUserQuotaModify.  # noqa: E501
        :type: int
        """

        self._soft_limit = soft_limit

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
        if issubclass(FileUserQuotaModify, dict):
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
        if not isinstance(other, FileUserQuotaModify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
