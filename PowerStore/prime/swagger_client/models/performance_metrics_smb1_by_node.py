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


class PerformanceMetricsSmb1ByNode(object):
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
        'appliance_id': 'str',
        'node_id': 'str',
        'timestamp': 'datetime',
        'repeat_count': 'int',
        'read_iops': 'float',
        'write_iops': 'float',
        'total_iops': 'float',
        'total_calls': 'float',
        'avg_read_latency': 'float',
        'avg_write_latency': 'float',
        'avg_latency': 'float',
        'avg_read_size': 'float',
        'avg_write_size': 'float',
        'avg_io_size': 'float'
    }

    attribute_map = {
        'appliance_id': 'appliance_id',
        'node_id': 'node_id',
        'timestamp': 'timestamp',
        'repeat_count': 'repeat_count',
        'read_iops': 'read_iops',
        'write_iops': 'write_iops',
        'total_iops': 'total_iops',
        'total_calls': 'total_calls',
        'avg_read_latency': 'avg_read_latency',
        'avg_write_latency': 'avg_write_latency',
        'avg_latency': 'avg_latency',
        'avg_read_size': 'avg_read_size',
        'avg_write_size': 'avg_write_size',
        'avg_io_size': 'avg_io_size'
    }

    def __init__(self, appliance_id=None, node_id=None, timestamp=None, repeat_count=None, read_iops=None, write_iops=None, total_iops=None, total_calls=None, avg_read_latency=None, avg_write_latency=None, avg_latency=None, avg_read_size=None, avg_write_size=None, avg_io_size=None, _configuration=None):  # noqa: E501
        """PerformanceMetricsSmb1ByNode - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._appliance_id = None
        self._node_id = None
        self._timestamp = None
        self._repeat_count = None
        self._read_iops = None
        self._write_iops = None
        self._total_iops = None
        self._total_calls = None
        self._avg_read_latency = None
        self._avg_write_latency = None
        self._avg_latency = None
        self._avg_read_size = None
        self._avg_write_size = None
        self._avg_io_size = None
        self.discriminator = None

        if appliance_id is not None:
            self.appliance_id = appliance_id
        if node_id is not None:
            self.node_id = node_id
        if timestamp is not None:
            self.timestamp = timestamp
        if repeat_count is not None:
            self.repeat_count = repeat_count
        if read_iops is not None:
            self.read_iops = read_iops
        if write_iops is not None:
            self.write_iops = write_iops
        if total_iops is not None:
            self.total_iops = total_iops
        if total_calls is not None:
            self.total_calls = total_calls
        if avg_read_latency is not None:
            self.avg_read_latency = avg_read_latency
        if avg_write_latency is not None:
            self.avg_write_latency = avg_write_latency
        if avg_latency is not None:
            self.avg_latency = avg_latency
        if avg_read_size is not None:
            self.avg_read_size = avg_read_size
        if avg_write_size is not None:
            self.avg_write_size = avg_write_size
        if avg_io_size is not None:
            self.avg_io_size = avg_io_size

    @property
    def appliance_id(self):
        """Gets the appliance_id of this PerformanceMetricsSmb1ByNode.  # noqa: E501

        Unique identifier of the appliance. Was added in version 3.0.0.0.  # noqa: E501

        :return: The appliance_id of this PerformanceMetricsSmb1ByNode.  # noqa: E501
        :rtype: str
        """
        return self._appliance_id

    @appliance_id.setter
    def appliance_id(self, appliance_id):
        """Sets the appliance_id of this PerformanceMetricsSmb1ByNode.

        Unique identifier of the appliance. Was added in version 3.0.0.0.  # noqa: E501

        :param appliance_id: The appliance_id of this PerformanceMetricsSmb1ByNode.  # noqa: E501
        :type: str
        """

        self._appliance_id = appliance_id

    @property
    def node_id(self):
        """Gets the node_id of this PerformanceMetricsSmb1ByNode.  # noqa: E501

        Unique identifier of the node.  # noqa: E501

        :return: The node_id of this PerformanceMetricsSmb1ByNode.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this PerformanceMetricsSmb1ByNode.

        Unique identifier of the node.  # noqa: E501

        :param node_id: The node_id of this PerformanceMetricsSmb1ByNode.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def timestamp(self):
        """Gets the timestamp of this PerformanceMetricsSmb1ByNode.  # noqa: E501

        End of sample period.  # noqa: E501

        :return: The timestamp of this PerformanceMetricsSmb1ByNode.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this PerformanceMetricsSmb1ByNode.

        End of sample period.  # noqa: E501

        :param timestamp: The timestamp of this PerformanceMetricsSmb1ByNode.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def repeat_count(self):
        """Gets the repeat_count of this PerformanceMetricsSmb1ByNode.  # noqa: E501

        Number of consecutive sampling periods during which there were no changes in the metrics values. If the value is omitted from the response, it is 1 (no additional repeats).   # noqa: E501

        :return: The repeat_count of this PerformanceMetricsSmb1ByNode.  # noqa: E501
        :rtype: int
        """
        return self._repeat_count

    @repeat_count.setter
    def repeat_count(self, repeat_count):
        """Sets the repeat_count of this PerformanceMetricsSmb1ByNode.

        Number of consecutive sampling periods during which there were no changes in the metrics values. If the value is omitted from the response, it is 1 (no additional repeats).   # noqa: E501

        :param repeat_count: The repeat_count of this PerformanceMetricsSmb1ByNode.  # noqa: E501
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
    def read_iops(self):
        """Gets the read_iops of this PerformanceMetricsSmb1ByNode.  # noqa: E501

        Total read operations per second.  # noqa: E501

        :return: The read_iops of this PerformanceMetricsSmb1ByNode.  # noqa: E501
        :rtype: float
        """
        return self._read_iops

    @read_iops.setter
    def read_iops(self, read_iops):
        """Sets the read_iops of this PerformanceMetricsSmb1ByNode.

        Total read operations per second.  # noqa: E501

        :param read_iops: The read_iops of this PerformanceMetricsSmb1ByNode.  # noqa: E501
        :type: float
        """

        self._read_iops = read_iops

    @property
    def write_iops(self):
        """Gets the write_iops of this PerformanceMetricsSmb1ByNode.  # noqa: E501

        Total write operations per second.  # noqa: E501

        :return: The write_iops of this PerformanceMetricsSmb1ByNode.  # noqa: E501
        :rtype: float
        """
        return self._write_iops

    @write_iops.setter
    def write_iops(self, write_iops):
        """Sets the write_iops of this PerformanceMetricsSmb1ByNode.

        Total write operations per second.  # noqa: E501

        :param write_iops: The write_iops of this PerformanceMetricsSmb1ByNode.  # noqa: E501
        :type: float
        """

        self._write_iops = write_iops

    @property
    def total_iops(self):
        """Gets the total_iops of this PerformanceMetricsSmb1ByNode.  # noqa: E501

        Total read and write operations per second.  # noqa: E501

        :return: The total_iops of this PerformanceMetricsSmb1ByNode.  # noqa: E501
        :rtype: float
        """
        return self._total_iops

    @total_iops.setter
    def total_iops(self, total_iops):
        """Sets the total_iops of this PerformanceMetricsSmb1ByNode.

        Total read and write operations per second.  # noqa: E501

        :param total_iops: The total_iops of this PerformanceMetricsSmb1ByNode.  # noqa: E501
        :type: float
        """

        self._total_iops = total_iops

    @property
    def total_calls(self):
        """Gets the total_calls of this PerformanceMetricsSmb1ByNode.  # noqa: E501

        Total calls.  # noqa: E501

        :return: The total_calls of this PerformanceMetricsSmb1ByNode.  # noqa: E501
        :rtype: float
        """
        return self._total_calls

    @total_calls.setter
    def total_calls(self, total_calls):
        """Sets the total_calls of this PerformanceMetricsSmb1ByNode.

        Total calls.  # noqa: E501

        :param total_calls: The total_calls of this PerformanceMetricsSmb1ByNode.  # noqa: E501
        :type: float
        """

        self._total_calls = total_calls

    @property
    def avg_read_latency(self):
        """Gets the avg_read_latency of this PerformanceMetricsSmb1ByNode.  # noqa: E501

        Average read latency in microseconds.  # noqa: E501

        :return: The avg_read_latency of this PerformanceMetricsSmb1ByNode.  # noqa: E501
        :rtype: float
        """
        return self._avg_read_latency

    @avg_read_latency.setter
    def avg_read_latency(self, avg_read_latency):
        """Sets the avg_read_latency of this PerformanceMetricsSmb1ByNode.

        Average read latency in microseconds.  # noqa: E501

        :param avg_read_latency: The avg_read_latency of this PerformanceMetricsSmb1ByNode.  # noqa: E501
        :type: float
        """

        self._avg_read_latency = avg_read_latency

    @property
    def avg_write_latency(self):
        """Gets the avg_write_latency of this PerformanceMetricsSmb1ByNode.  # noqa: E501

        Average write latency in microseconds.  # noqa: E501

        :return: The avg_write_latency of this PerformanceMetricsSmb1ByNode.  # noqa: E501
        :rtype: float
        """
        return self._avg_write_latency

    @avg_write_latency.setter
    def avg_write_latency(self, avg_write_latency):
        """Sets the avg_write_latency of this PerformanceMetricsSmb1ByNode.

        Average write latency in microseconds.  # noqa: E501

        :param avg_write_latency: The avg_write_latency of this PerformanceMetricsSmb1ByNode.  # noqa: E501
        :type: float
        """

        self._avg_write_latency = avg_write_latency

    @property
    def avg_latency(self):
        """Gets the avg_latency of this PerformanceMetricsSmb1ByNode.  # noqa: E501

        Average read and write latency in microseconds.  # noqa: E501

        :return: The avg_latency of this PerformanceMetricsSmb1ByNode.  # noqa: E501
        :rtype: float
        """
        return self._avg_latency

    @avg_latency.setter
    def avg_latency(self, avg_latency):
        """Sets the avg_latency of this PerformanceMetricsSmb1ByNode.

        Average read and write latency in microseconds.  # noqa: E501

        :param avg_latency: The avg_latency of this PerformanceMetricsSmb1ByNode.  # noqa: E501
        :type: float
        """

        self._avg_latency = avg_latency

    @property
    def avg_read_size(self):
        """Gets the avg_read_size of this PerformanceMetricsSmb1ByNode.  # noqa: E501

        Average read size in bytes.  # noqa: E501

        :return: The avg_read_size of this PerformanceMetricsSmb1ByNode.  # noqa: E501
        :rtype: float
        """
        return self._avg_read_size

    @avg_read_size.setter
    def avg_read_size(self, avg_read_size):
        """Sets the avg_read_size of this PerformanceMetricsSmb1ByNode.

        Average read size in bytes.  # noqa: E501

        :param avg_read_size: The avg_read_size of this PerformanceMetricsSmb1ByNode.  # noqa: E501
        :type: float
        """

        self._avg_read_size = avg_read_size

    @property
    def avg_write_size(self):
        """Gets the avg_write_size of this PerformanceMetricsSmb1ByNode.  # noqa: E501

        Average write size in bytes.  # noqa: E501

        :return: The avg_write_size of this PerformanceMetricsSmb1ByNode.  # noqa: E501
        :rtype: float
        """
        return self._avg_write_size

    @avg_write_size.setter
    def avg_write_size(self, avg_write_size):
        """Sets the avg_write_size of this PerformanceMetricsSmb1ByNode.

        Average write size in bytes.  # noqa: E501

        :param avg_write_size: The avg_write_size of this PerformanceMetricsSmb1ByNode.  # noqa: E501
        :type: float
        """

        self._avg_write_size = avg_write_size

    @property
    def avg_io_size(self):
        """Gets the avg_io_size of this PerformanceMetricsSmb1ByNode.  # noqa: E501

        Average read and write size in bytes.  # noqa: E501

        :return: The avg_io_size of this PerformanceMetricsSmb1ByNode.  # noqa: E501
        :rtype: float
        """
        return self._avg_io_size

    @avg_io_size.setter
    def avg_io_size(self, avg_io_size):
        """Sets the avg_io_size of this PerformanceMetricsSmb1ByNode.

        Average read and write size in bytes.  # noqa: E501

        :param avg_io_size: The avg_io_size of this PerformanceMetricsSmb1ByNode.  # noqa: E501
        :type: float
        """

        self._avg_io_size = avg_io_size

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
        if issubclass(PerformanceMetricsSmb1ByNode, dict):
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
        if not isinstance(other, PerformanceMetricsSmb1ByNode):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PerformanceMetricsSmb1ByNode):
            return True

        return self.to_dict() != other.to_dict()
