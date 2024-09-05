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


class ClusterForecastResponse(object):
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
        'timestamp': 'datetime',
        'low_value': 'int',
        'mean_value': 'int',
        'high_value': 'int'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'low_value': 'low_value',
        'mean_value': 'mean_value',
        'high_value': 'high_value'
    }

    def __init__(self, timestamp=None, low_value=None, mean_value=None, high_value=None, _configuration=None):  # noqa: E501
        """ClusterForecastResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._timestamp = None
        self._low_value = None
        self._mean_value = None
        self._high_value = None
        self.discriminator = None

        if timestamp is not None:
            self.timestamp = timestamp
        if low_value is not None:
            self.low_value = low_value
        if mean_value is not None:
            self.mean_value = mean_value
        if high_value is not None:
            self.high_value = high_value

    @property
    def timestamp(self):
        """Gets the timestamp of this ClusterForecastResponse.  # noqa: E501

        Timestamp when the forecast was performed.  # noqa: E501

        :return: The timestamp of this ClusterForecastResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ClusterForecastResponse.

        Timestamp when the forecast was performed.  # noqa: E501

        :param timestamp: The timestamp of this ClusterForecastResponse.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def low_value(self):
        """Gets the low_value of this ClusterForecastResponse.  # noqa: E501

        Estimate of the lower bound of the 95% confidence interval for the forecast value at the given timestamp.  # noqa: E501

        :return: The low_value of this ClusterForecastResponse.  # noqa: E501
        :rtype: int
        """
        return self._low_value

    @low_value.setter
    def low_value(self, low_value):
        """Sets the low_value of this ClusterForecastResponse.

        Estimate of the lower bound of the 95% confidence interval for the forecast value at the given timestamp.  # noqa: E501

        :param low_value: The low_value of this ClusterForecastResponse.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                low_value is not None and low_value > -9223372036854775616):  # noqa: E501
            raise ValueError("Invalid value for `low_value`, must be a value less than or equal to `-9223372036854775616`")  # noqa: E501
        if (self._configuration.client_side_validation and
                low_value is not None and low_value < 0):  # noqa: E501
            raise ValueError("Invalid value for `low_value`, must be a value greater than or equal to `0`")  # noqa: E501

        self._low_value = low_value

    @property
    def mean_value(self):
        """Gets the mean_value of this ClusterForecastResponse.  # noqa: E501

        Estimate for the mean forecast value at the given timestamp.  # noqa: E501

        :return: The mean_value of this ClusterForecastResponse.  # noqa: E501
        :rtype: int
        """
        return self._mean_value

    @mean_value.setter
    def mean_value(self, mean_value):
        """Sets the mean_value of this ClusterForecastResponse.

        Estimate for the mean forecast value at the given timestamp.  # noqa: E501

        :param mean_value: The mean_value of this ClusterForecastResponse.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                mean_value is not None and mean_value > -9223372036854775616):  # noqa: E501
            raise ValueError("Invalid value for `mean_value`, must be a value less than or equal to `-9223372036854775616`")  # noqa: E501
        if (self._configuration.client_side_validation and
                mean_value is not None and mean_value < 0):  # noqa: E501
            raise ValueError("Invalid value for `mean_value`, must be a value greater than or equal to `0`")  # noqa: E501

        self._mean_value = mean_value

    @property
    def high_value(self):
        """Gets the high_value of this ClusterForecastResponse.  # noqa: E501

        Estimate of the upper bound of the 95% confidence interval for the forecast value at the given timestamp.  # noqa: E501

        :return: The high_value of this ClusterForecastResponse.  # noqa: E501
        :rtype: int
        """
        return self._high_value

    @high_value.setter
    def high_value(self, high_value):
        """Sets the high_value of this ClusterForecastResponse.

        Estimate of the upper bound of the 95% confidence interval for the forecast value at the given timestamp.  # noqa: E501

        :param high_value: The high_value of this ClusterForecastResponse.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                high_value is not None and high_value > -9223372036854775616):  # noqa: E501
            raise ValueError("Invalid value for `high_value`, must be a value less than or equal to `-9223372036854775616`")  # noqa: E501
        if (self._configuration.client_side_validation and
                high_value is not None and high_value < 0):  # noqa: E501
            raise ValueError("Invalid value for `high_value`, must be a value greater than or equal to `0`")  # noqa: E501

        self._high_value = high_value

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
        if issubclass(ClusterForecastResponse, dict):
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
        if not isinstance(other, ClusterForecastResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterForecastResponse):
            return True

        return self.to_dict() != other.to_dict()
