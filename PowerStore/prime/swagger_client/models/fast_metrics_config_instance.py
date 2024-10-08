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


class FastMetricsConfigInstance(object):
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
        'resource_id': 'str',
        'resource_type': 'FastMetricsResourceTypeEnum',
        'resource_type_l10n': 'str'
    }

    attribute_map = {
        'id': 'id',
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'resource_type_l10n': 'resource_type_l10n'
    }

    def __init__(self, id=None, resource_id=None, resource_type=None, resource_type_l10n=None, _configuration=None):  # noqa: E501
        """FastMetricsConfigInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._resource_id = None
        self._resource_type = None
        self._resource_type_l10n = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_type_l10n is not None:
            self.resource_type_l10n = resource_type_l10n

    @property
    def id(self):
        """Gets the id of this FastMetricsConfigInstance.  # noqa: E501

        Unique identifier of the fast_metrics_config instance.  # noqa: E501

        :return: The id of this FastMetricsConfigInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FastMetricsConfigInstance.

        Unique identifier of the fast_metrics_config instance.  # noqa: E501

        :param id: The id of this FastMetricsConfigInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def resource_id(self):
        """Gets the resource_id of this FastMetricsConfigInstance.  # noqa: E501

        Unique identifier of the resource.  # noqa: E501

        :return: The resource_id of this FastMetricsConfigInstance.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this FastMetricsConfigInstance.

        Unique identifier of the resource.  # noqa: E501

        :param resource_id: The resource_id of this FastMetricsConfigInstance.  # noqa: E501
        :type: str
        """

        self._resource_id = resource_id

    @property
    def resource_type(self):
        """Gets the resource_type of this FastMetricsConfigInstance.  # noqa: E501


        :return: The resource_type of this FastMetricsConfigInstance.  # noqa: E501
        :rtype: FastMetricsResourceTypeEnum
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this FastMetricsConfigInstance.


        :param resource_type: The resource_type of this FastMetricsConfigInstance.  # noqa: E501
        :type: FastMetricsResourceTypeEnum
        """

        self._resource_type = resource_type

    @property
    def resource_type_l10n(self):
        """Gets the resource_type_l10n of this FastMetricsConfigInstance.  # noqa: E501

        Localized message string corresponding to resource_type Was added in version 3.0.0.0.  # noqa: E501

        :return: The resource_type_l10n of this FastMetricsConfigInstance.  # noqa: E501
        :rtype: str
        """
        return self._resource_type_l10n

    @resource_type_l10n.setter
    def resource_type_l10n(self, resource_type_l10n):
        """Sets the resource_type_l10n of this FastMetricsConfigInstance.

        Localized message string corresponding to resource_type Was added in version 3.0.0.0.  # noqa: E501

        :param resource_type_l10n: The resource_type_l10n of this FastMetricsConfigInstance.  # noqa: E501
        :type: str
        """

        self._resource_type_l10n = resource_type_l10n

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
        if issubclass(FastMetricsConfigInstance, dict):
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
        if not isinstance(other, FastMetricsConfigInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FastMetricsConfigInstance):
            return True

        return self.to_dict() != other.to_dict()
