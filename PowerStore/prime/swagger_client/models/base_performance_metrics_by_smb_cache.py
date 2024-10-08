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


class BasePerformanceMetricsBySmbCache(object):
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
        'node_id': 'str',
        'appliance_id': 'str',
        'timestamp': 'datetime',
        'repeat_count': 'int',
        'hash_max_size': 'float',
        'hash_min_size': 'float',
        'hash_avg_size': 'float',
        'hash_max_latency': 'float',
        'hash_min_latency': 'float',
        'hash_avg_latency': 'float',
        'total_tasks': 'float',
        'total_rejected_tasks': 'float',
        'max_used_threads': 'float'
    }

    attribute_map = {
        'node_id': 'node_id',
        'appliance_id': 'appliance_id',
        'timestamp': 'timestamp',
        'repeat_count': 'repeat_count',
        'hash_max_size': 'hash_max_size',
        'hash_min_size': 'hash_min_size',
        'hash_avg_size': 'hash_avg_size',
        'hash_max_latency': 'hash_max_latency',
        'hash_min_latency': 'hash_min_latency',
        'hash_avg_latency': 'hash_avg_latency',
        'total_tasks': 'total_tasks',
        'total_rejected_tasks': 'total_rejected_tasks',
        'max_used_threads': 'max_used_threads'
    }

    def __init__(self, node_id=None, appliance_id=None, timestamp=None, repeat_count=None, hash_max_size=None, hash_min_size=None, hash_avg_size=None, hash_max_latency=None, hash_min_latency=None, hash_avg_latency=None, total_tasks=None, total_rejected_tasks=None, max_used_threads=None, _configuration=None):  # noqa: E501
        """BasePerformanceMetricsBySmbCache - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._node_id = None
        self._appliance_id = None
        self._timestamp = None
        self._repeat_count = None
        self._hash_max_size = None
        self._hash_min_size = None
        self._hash_avg_size = None
        self._hash_max_latency = None
        self._hash_min_latency = None
        self._hash_avg_latency = None
        self._total_tasks = None
        self._total_rejected_tasks = None
        self._max_used_threads = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if appliance_id is not None:
            self.appliance_id = appliance_id
        if timestamp is not None:
            self.timestamp = timestamp
        if repeat_count is not None:
            self.repeat_count = repeat_count
        if hash_max_size is not None:
            self.hash_max_size = hash_max_size
        if hash_min_size is not None:
            self.hash_min_size = hash_min_size
        if hash_avg_size is not None:
            self.hash_avg_size = hash_avg_size
        if hash_max_latency is not None:
            self.hash_max_latency = hash_max_latency
        if hash_min_latency is not None:
            self.hash_min_latency = hash_min_latency
        if hash_avg_latency is not None:
            self.hash_avg_latency = hash_avg_latency
        if total_tasks is not None:
            self.total_tasks = total_tasks
        if total_rejected_tasks is not None:
            self.total_rejected_tasks = total_rejected_tasks
        if max_used_threads is not None:
            self.max_used_threads = max_used_threads

    @property
    def node_id(self):
        """Gets the node_id of this BasePerformanceMetricsBySmbCache.  # noqa: E501

        Unique identifier of the node.  # noqa: E501

        :return: The node_id of this BasePerformanceMetricsBySmbCache.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this BasePerformanceMetricsBySmbCache.

        Unique identifier of the node.  # noqa: E501

        :param node_id: The node_id of this BasePerformanceMetricsBySmbCache.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def appliance_id(self):
        """Gets the appliance_id of this BasePerformanceMetricsBySmbCache.  # noqa: E501

        Unique identifier of the appliance. Was added in version 3.0.0.0.  # noqa: E501

        :return: The appliance_id of this BasePerformanceMetricsBySmbCache.  # noqa: E501
        :rtype: str
        """
        return self._appliance_id

    @appliance_id.setter
    def appliance_id(self, appliance_id):
        """Sets the appliance_id of this BasePerformanceMetricsBySmbCache.

        Unique identifier of the appliance. Was added in version 3.0.0.0.  # noqa: E501

        :param appliance_id: The appliance_id of this BasePerformanceMetricsBySmbCache.  # noqa: E501
        :type: str
        """

        self._appliance_id = appliance_id

    @property
    def timestamp(self):
        """Gets the timestamp of this BasePerformanceMetricsBySmbCache.  # noqa: E501

        End of sample period.  # noqa: E501

        :return: The timestamp of this BasePerformanceMetricsBySmbCache.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this BasePerformanceMetricsBySmbCache.

        End of sample period.  # noqa: E501

        :param timestamp: The timestamp of this BasePerformanceMetricsBySmbCache.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def repeat_count(self):
        """Gets the repeat_count of this BasePerformanceMetricsBySmbCache.  # noqa: E501

        Number of consecutive sampling periods during which there were no changes in the metrics values. If the value is omitted from the response, it is 1 (no additional repeats).   # noqa: E501

        :return: The repeat_count of this BasePerformanceMetricsBySmbCache.  # noqa: E501
        :rtype: int
        """
        return self._repeat_count

    @repeat_count.setter
    def repeat_count(self, repeat_count):
        """Sets the repeat_count of this BasePerformanceMetricsBySmbCache.

        Number of consecutive sampling periods during which there were no changes in the metrics values. If the value is omitted from the response, it is 1 (no additional repeats).   # noqa: E501

        :param repeat_count: The repeat_count of this BasePerformanceMetricsBySmbCache.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                repeat_count is not None and repeat_count > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `repeat_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self._configuration.client_side_validation and
                repeat_count is not None and repeat_count < 0):  # noqa: E501
            raise ValueError("Invalid value for `repeat_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._repeat_count = repeat_count

    @property
    def hash_max_size(self):
        """Gets the hash_max_size of this BasePerformanceMetricsBySmbCache.  # noqa: E501

        Max hash size.  # noqa: E501

        :return: The hash_max_size of this BasePerformanceMetricsBySmbCache.  # noqa: E501
        :rtype: float
        """
        return self._hash_max_size

    @hash_max_size.setter
    def hash_max_size(self, hash_max_size):
        """Sets the hash_max_size of this BasePerformanceMetricsBySmbCache.

        Max hash size.  # noqa: E501

        :param hash_max_size: The hash_max_size of this BasePerformanceMetricsBySmbCache.  # noqa: E501
        :type: float
        """

        self._hash_max_size = hash_max_size

    @property
    def hash_min_size(self):
        """Gets the hash_min_size of this BasePerformanceMetricsBySmbCache.  # noqa: E501

        Max hash size.  # noqa: E501

        :return: The hash_min_size of this BasePerformanceMetricsBySmbCache.  # noqa: E501
        :rtype: float
        """
        return self._hash_min_size

    @hash_min_size.setter
    def hash_min_size(self, hash_min_size):
        """Sets the hash_min_size of this BasePerformanceMetricsBySmbCache.

        Max hash size.  # noqa: E501

        :param hash_min_size: The hash_min_size of this BasePerformanceMetricsBySmbCache.  # noqa: E501
        :type: float
        """

        self._hash_min_size = hash_min_size

    @property
    def hash_avg_size(self):
        """Gets the hash_avg_size of this BasePerformanceMetricsBySmbCache.  # noqa: E501

        Average hash size.  # noqa: E501

        :return: The hash_avg_size of this BasePerformanceMetricsBySmbCache.  # noqa: E501
        :rtype: float
        """
        return self._hash_avg_size

    @hash_avg_size.setter
    def hash_avg_size(self, hash_avg_size):
        """Sets the hash_avg_size of this BasePerformanceMetricsBySmbCache.

        Average hash size.  # noqa: E501

        :param hash_avg_size: The hash_avg_size of this BasePerformanceMetricsBySmbCache.  # noqa: E501
        :type: float
        """

        self._hash_avg_size = hash_avg_size

    @property
    def hash_max_latency(self):
        """Gets the hash_max_latency of this BasePerformanceMetricsBySmbCache.  # noqa: E501

        Max hash latency.  # noqa: E501

        :return: The hash_max_latency of this BasePerformanceMetricsBySmbCache.  # noqa: E501
        :rtype: float
        """
        return self._hash_max_latency

    @hash_max_latency.setter
    def hash_max_latency(self, hash_max_latency):
        """Sets the hash_max_latency of this BasePerformanceMetricsBySmbCache.

        Max hash latency.  # noqa: E501

        :param hash_max_latency: The hash_max_latency of this BasePerformanceMetricsBySmbCache.  # noqa: E501
        :type: float
        """

        self._hash_max_latency = hash_max_latency

    @property
    def hash_min_latency(self):
        """Gets the hash_min_latency of this BasePerformanceMetricsBySmbCache.  # noqa: E501

        Min hash latency.  # noqa: E501

        :return: The hash_min_latency of this BasePerformanceMetricsBySmbCache.  # noqa: E501
        :rtype: float
        """
        return self._hash_min_latency

    @hash_min_latency.setter
    def hash_min_latency(self, hash_min_latency):
        """Sets the hash_min_latency of this BasePerformanceMetricsBySmbCache.

        Min hash latency.  # noqa: E501

        :param hash_min_latency: The hash_min_latency of this BasePerformanceMetricsBySmbCache.  # noqa: E501
        :type: float
        """

        self._hash_min_latency = hash_min_latency

    @property
    def hash_avg_latency(self):
        """Gets the hash_avg_latency of this BasePerformanceMetricsBySmbCache.  # noqa: E501

        Average hash latency.  # noqa: E501

        :return: The hash_avg_latency of this BasePerformanceMetricsBySmbCache.  # noqa: E501
        :rtype: float
        """
        return self._hash_avg_latency

    @hash_avg_latency.setter
    def hash_avg_latency(self, hash_avg_latency):
        """Sets the hash_avg_latency of this BasePerformanceMetricsBySmbCache.

        Average hash latency.  # noqa: E501

        :param hash_avg_latency: The hash_avg_latency of this BasePerformanceMetricsBySmbCache.  # noqa: E501
        :type: float
        """

        self._hash_avg_latency = hash_avg_latency

    @property
    def total_tasks(self):
        """Gets the total_tasks of this BasePerformanceMetricsBySmbCache.  # noqa: E501

        Total tasks.  # noqa: E501

        :return: The total_tasks of this BasePerformanceMetricsBySmbCache.  # noqa: E501
        :rtype: float
        """
        return self._total_tasks

    @total_tasks.setter
    def total_tasks(self, total_tasks):
        """Sets the total_tasks of this BasePerformanceMetricsBySmbCache.

        Total tasks.  # noqa: E501

        :param total_tasks: The total_tasks of this BasePerformanceMetricsBySmbCache.  # noqa: E501
        :type: float
        """

        self._total_tasks = total_tasks

    @property
    def total_rejected_tasks(self):
        """Gets the total_rejected_tasks of this BasePerformanceMetricsBySmbCache.  # noqa: E501

        Total rejected task.  # noqa: E501

        :return: The total_rejected_tasks of this BasePerformanceMetricsBySmbCache.  # noqa: E501
        :rtype: float
        """
        return self._total_rejected_tasks

    @total_rejected_tasks.setter
    def total_rejected_tasks(self, total_rejected_tasks):
        """Sets the total_rejected_tasks of this BasePerformanceMetricsBySmbCache.

        Total rejected task.  # noqa: E501

        :param total_rejected_tasks: The total_rejected_tasks of this BasePerformanceMetricsBySmbCache.  # noqa: E501
        :type: float
        """

        self._total_rejected_tasks = total_rejected_tasks

    @property
    def max_used_threads(self):
        """Gets the max_used_threads of this BasePerformanceMetricsBySmbCache.  # noqa: E501

        Max used threads  # noqa: E501

        :return: The max_used_threads of this BasePerformanceMetricsBySmbCache.  # noqa: E501
        :rtype: float
        """
        return self._max_used_threads

    @max_used_threads.setter
    def max_used_threads(self, max_used_threads):
        """Sets the max_used_threads of this BasePerformanceMetricsBySmbCache.

        Max used threads  # noqa: E501

        :param max_used_threads: The max_used_threads of this BasePerformanceMetricsBySmbCache.  # noqa: E501
        :type: float
        """

        self._max_used_threads = max_used_threads

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
        if issubclass(BasePerformanceMetricsBySmbCache, dict):
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
        if not isinstance(other, BasePerformanceMetricsBySmbCache):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BasePerformanceMetricsBySmbCache):
            return True

        return self.to_dict() != other.to_dict()
