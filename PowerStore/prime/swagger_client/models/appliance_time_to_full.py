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


class ApplianceTimeToFull(object):
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
        'metric_type': 'ForecastMetricTypeEnum'
    }

    attribute_map = {
        'metric_type': 'metric_type'
    }

    def __init__(self, metric_type=None, _configuration=None):  # noqa: E501
        """ApplianceTimeToFull - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._metric_type = None
        self.discriminator = None

        self.metric_type = metric_type

    @property
    def metric_type(self):
        """Gets the metric_type of this ApplianceTimeToFull.  # noqa: E501


        :return: The metric_type of this ApplianceTimeToFull.  # noqa: E501
        :rtype: ForecastMetricTypeEnum
        """
        return self._metric_type

    @metric_type.setter
    def metric_type(self, metric_type):
        """Sets the metric_type of this ApplianceTimeToFull.


        :param metric_type: The metric_type of this ApplianceTimeToFull.  # noqa: E501
        :type: ForecastMetricTypeEnum
        """
        if self._configuration.client_side_validation and metric_type is None:
            raise ValueError("Invalid value for `metric_type`, must not be `None`")  # noqa: E501

        self._metric_type = metric_type

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
        if issubclass(ApplianceTimeToFull, dict):
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
        if not isinstance(other, ApplianceTimeToFull):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplianceTimeToFull):
            return True

        return self.to_dict() != other.to_dict()
