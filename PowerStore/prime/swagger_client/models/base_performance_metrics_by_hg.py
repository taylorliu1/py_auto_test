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


class BasePerformanceMetricsByHg(object):
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
        'hg_id': 'str',
        'timestamp': 'datetime',
        'read_iops': 'float',
        'write_iops': 'float',
        'total_iops': 'float',
        'avg_read_latency': 'float',
        'avg_write_latency': 'float',
        'avg_latency': 'float',
        'read_bandwidth': 'float',
        'write_bandwidth': 'float',
        'total_bandwidth': 'float',
        'avg_read_size': 'float',
        'avg_write_size': 'float',
        'avg_io_size': 'float',
        'repeat_count': 'int'
    }

    attribute_map = {
        'hg_id': 'hg_id',
        'timestamp': 'timestamp',
        'read_iops': 'read_iops',
        'write_iops': 'write_iops',
        'total_iops': 'total_iops',
        'avg_read_latency': 'avg_read_latency',
        'avg_write_latency': 'avg_write_latency',
        'avg_latency': 'avg_latency',
        'read_bandwidth': 'read_bandwidth',
        'write_bandwidth': 'write_bandwidth',
        'total_bandwidth': 'total_bandwidth',
        'avg_read_size': 'avg_read_size',
        'avg_write_size': 'avg_write_size',
        'avg_io_size': 'avg_io_size',
        'repeat_count': 'repeat_count'
    }

    def __init__(self, hg_id=None, timestamp=None, read_iops=None, write_iops=None, total_iops=None, avg_read_latency=None, avg_write_latency=None, avg_latency=None, read_bandwidth=None, write_bandwidth=None, total_bandwidth=None, avg_read_size=None, avg_write_size=None, avg_io_size=None, repeat_count=None, _configuration=None):  # noqa: E501
        """BasePerformanceMetricsByHg - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._hg_id = None
        self._timestamp = None
        self._read_iops = None
        self._write_iops = None
        self._total_iops = None
        self._avg_read_latency = None
        self._avg_write_latency = None
        self._avg_latency = None
        self._read_bandwidth = None
        self._write_bandwidth = None
        self._total_bandwidth = None
        self._avg_read_size = None
        self._avg_write_size = None
        self._avg_io_size = None
        self._repeat_count = None
        self.discriminator = None

        if hg_id is not None:
            self.hg_id = hg_id
        if timestamp is not None:
            self.timestamp = timestamp
        if read_iops is not None:
            self.read_iops = read_iops
        if write_iops is not None:
            self.write_iops = write_iops
        if total_iops is not None:
            self.total_iops = total_iops
        if avg_read_latency is not None:
            self.avg_read_latency = avg_read_latency
        if avg_write_latency is not None:
            self.avg_write_latency = avg_write_latency
        if avg_latency is not None:
            self.avg_latency = avg_latency
        if read_bandwidth is not None:
            self.read_bandwidth = read_bandwidth
        if write_bandwidth is not None:
            self.write_bandwidth = write_bandwidth
        if total_bandwidth is not None:
            self.total_bandwidth = total_bandwidth
        if avg_read_size is not None:
            self.avg_read_size = avg_read_size
        if avg_write_size is not None:
            self.avg_write_size = avg_write_size
        if avg_io_size is not None:
            self.avg_io_size = avg_io_size
        if repeat_count is not None:
            self.repeat_count = repeat_count

    @property
    def hg_id(self):
        """Gets the hg_id of this BasePerformanceMetricsByHg.  # noqa: E501

        Reference to the associated host group for which these metrics were recorded.  # noqa: E501

        :return: The hg_id of this BasePerformanceMetricsByHg.  # noqa: E501
        :rtype: str
        """
        return self._hg_id

    @hg_id.setter
    def hg_id(self, hg_id):
        """Sets the hg_id of this BasePerformanceMetricsByHg.

        Reference to the associated host group for which these metrics were recorded.  # noqa: E501

        :param hg_id: The hg_id of this BasePerformanceMetricsByHg.  # noqa: E501
        :type: str
        """

        self._hg_id = hg_id

    @property
    def timestamp(self):
        """Gets the timestamp of this BasePerformanceMetricsByHg.  # noqa: E501

        End of sample period.  # noqa: E501

        :return: The timestamp of this BasePerformanceMetricsByHg.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this BasePerformanceMetricsByHg.

        End of sample period.  # noqa: E501

        :param timestamp: The timestamp of this BasePerformanceMetricsByHg.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def read_iops(self):
        """Gets the read_iops of this BasePerformanceMetricsByHg.  # noqa: E501

        Total read operations per second.  # noqa: E501

        :return: The read_iops of this BasePerformanceMetricsByHg.  # noqa: E501
        :rtype: float
        """
        return self._read_iops

    @read_iops.setter
    def read_iops(self, read_iops):
        """Sets the read_iops of this BasePerformanceMetricsByHg.

        Total read operations per second.  # noqa: E501

        :param read_iops: The read_iops of this BasePerformanceMetricsByHg.  # noqa: E501
        :type: float
        """

        self._read_iops = read_iops

    @property
    def write_iops(self):
        """Gets the write_iops of this BasePerformanceMetricsByHg.  # noqa: E501

        Total write operations per second.  # noqa: E501

        :return: The write_iops of this BasePerformanceMetricsByHg.  # noqa: E501
        :rtype: float
        """
        return self._write_iops

    @write_iops.setter
    def write_iops(self, write_iops):
        """Sets the write_iops of this BasePerformanceMetricsByHg.

        Total write operations per second.  # noqa: E501

        :param write_iops: The write_iops of this BasePerformanceMetricsByHg.  # noqa: E501
        :type: float
        """

        self._write_iops = write_iops

    @property
    def total_iops(self):
        """Gets the total_iops of this BasePerformanceMetricsByHg.  # noqa: E501

        Total read and write operations per second.  # noqa: E501

        :return: The total_iops of this BasePerformanceMetricsByHg.  # noqa: E501
        :rtype: float
        """
        return self._total_iops

    @total_iops.setter
    def total_iops(self, total_iops):
        """Sets the total_iops of this BasePerformanceMetricsByHg.

        Total read and write operations per second.  # noqa: E501

        :param total_iops: The total_iops of this BasePerformanceMetricsByHg.  # noqa: E501
        :type: float
        """

        self._total_iops = total_iops

    @property
    def avg_read_latency(self):
        """Gets the avg_read_latency of this BasePerformanceMetricsByHg.  # noqa: E501

        Average read latency in microseconds.  # noqa: E501

        :return: The avg_read_latency of this BasePerformanceMetricsByHg.  # noqa: E501
        :rtype: float
        """
        return self._avg_read_latency

    @avg_read_latency.setter
    def avg_read_latency(self, avg_read_latency):
        """Sets the avg_read_latency of this BasePerformanceMetricsByHg.

        Average read latency in microseconds.  # noqa: E501

        :param avg_read_latency: The avg_read_latency of this BasePerformanceMetricsByHg.  # noqa: E501
        :type: float
        """

        self._avg_read_latency = avg_read_latency

    @property
    def avg_write_latency(self):
        """Gets the avg_write_latency of this BasePerformanceMetricsByHg.  # noqa: E501

        Average write latency in microseconds.  # noqa: E501

        :return: The avg_write_latency of this BasePerformanceMetricsByHg.  # noqa: E501
        :rtype: float
        """
        return self._avg_write_latency

    @avg_write_latency.setter
    def avg_write_latency(self, avg_write_latency):
        """Sets the avg_write_latency of this BasePerformanceMetricsByHg.

        Average write latency in microseconds.  # noqa: E501

        :param avg_write_latency: The avg_write_latency of this BasePerformanceMetricsByHg.  # noqa: E501
        :type: float
        """

        self._avg_write_latency = avg_write_latency

    @property
    def avg_latency(self):
        """Gets the avg_latency of this BasePerformanceMetricsByHg.  # noqa: E501

        Average read and write latency in microseconds.  # noqa: E501

        :return: The avg_latency of this BasePerformanceMetricsByHg.  # noqa: E501
        :rtype: float
        """
        return self._avg_latency

    @avg_latency.setter
    def avg_latency(self, avg_latency):
        """Sets the avg_latency of this BasePerformanceMetricsByHg.

        Average read and write latency in microseconds.  # noqa: E501

        :param avg_latency: The avg_latency of this BasePerformanceMetricsByHg.  # noqa: E501
        :type: float
        """

        self._avg_latency = avg_latency

    @property
    def read_bandwidth(self):
        """Gets the read_bandwidth of this BasePerformanceMetricsByHg.  # noqa: E501

        Read rate in bytes per second.  # noqa: E501

        :return: The read_bandwidth of this BasePerformanceMetricsByHg.  # noqa: E501
        :rtype: float
        """
        return self._read_bandwidth

    @read_bandwidth.setter
    def read_bandwidth(self, read_bandwidth):
        """Sets the read_bandwidth of this BasePerformanceMetricsByHg.

        Read rate in bytes per second.  # noqa: E501

        :param read_bandwidth: The read_bandwidth of this BasePerformanceMetricsByHg.  # noqa: E501
        :type: float
        """

        self._read_bandwidth = read_bandwidth

    @property
    def write_bandwidth(self):
        """Gets the write_bandwidth of this BasePerformanceMetricsByHg.  # noqa: E501

        Write rate in bytes per second.  # noqa: E501

        :return: The write_bandwidth of this BasePerformanceMetricsByHg.  # noqa: E501
        :rtype: float
        """
        return self._write_bandwidth

    @write_bandwidth.setter
    def write_bandwidth(self, write_bandwidth):
        """Sets the write_bandwidth of this BasePerformanceMetricsByHg.

        Write rate in bytes per second.  # noqa: E501

        :param write_bandwidth: The write_bandwidth of this BasePerformanceMetricsByHg.  # noqa: E501
        :type: float
        """

        self._write_bandwidth = write_bandwidth

    @property
    def total_bandwidth(self):
        """Gets the total_bandwidth of this BasePerformanceMetricsByHg.  # noqa: E501

        Total data transfer rate in bytes per second.  # noqa: E501

        :return: The total_bandwidth of this BasePerformanceMetricsByHg.  # noqa: E501
        :rtype: float
        """
        return self._total_bandwidth

    @total_bandwidth.setter
    def total_bandwidth(self, total_bandwidth):
        """Sets the total_bandwidth of this BasePerformanceMetricsByHg.

        Total data transfer rate in bytes per second.  # noqa: E501

        :param total_bandwidth: The total_bandwidth of this BasePerformanceMetricsByHg.  # noqa: E501
        :type: float
        """

        self._total_bandwidth = total_bandwidth

    @property
    def avg_read_size(self):
        """Gets the avg_read_size of this BasePerformanceMetricsByHg.  # noqa: E501

        Average read size in bytes.  # noqa: E501

        :return: The avg_read_size of this BasePerformanceMetricsByHg.  # noqa: E501
        :rtype: float
        """
        return self._avg_read_size

    @avg_read_size.setter
    def avg_read_size(self, avg_read_size):
        """Sets the avg_read_size of this BasePerformanceMetricsByHg.

        Average read size in bytes.  # noqa: E501

        :param avg_read_size: The avg_read_size of this BasePerformanceMetricsByHg.  # noqa: E501
        :type: float
        """

        self._avg_read_size = avg_read_size

    @property
    def avg_write_size(self):
        """Gets the avg_write_size of this BasePerformanceMetricsByHg.  # noqa: E501

        Average write size in bytes.  # noqa: E501

        :return: The avg_write_size of this BasePerformanceMetricsByHg.  # noqa: E501
        :rtype: float
        """
        return self._avg_write_size

    @avg_write_size.setter
    def avg_write_size(self, avg_write_size):
        """Sets the avg_write_size of this BasePerformanceMetricsByHg.

        Average write size in bytes.  # noqa: E501

        :param avg_write_size: The avg_write_size of this BasePerformanceMetricsByHg.  # noqa: E501
        :type: float
        """

        self._avg_write_size = avg_write_size

    @property
    def avg_io_size(self):
        """Gets the avg_io_size of this BasePerformanceMetricsByHg.  # noqa: E501

        Average size of read and write operations in bytes.  # noqa: E501

        :return: The avg_io_size of this BasePerformanceMetricsByHg.  # noqa: E501
        :rtype: float
        """
        return self._avg_io_size

    @avg_io_size.setter
    def avg_io_size(self, avg_io_size):
        """Sets the avg_io_size of this BasePerformanceMetricsByHg.

        Average size of read and write operations in bytes.  # noqa: E501

        :param avg_io_size: The avg_io_size of this BasePerformanceMetricsByHg.  # noqa: E501
        :type: float
        """

        self._avg_io_size = avg_io_size

    @property
    def repeat_count(self):
        """Gets the repeat_count of this BasePerformanceMetricsByHg.  # noqa: E501

        Number of times the metrics are repeated.  # noqa: E501

        :return: The repeat_count of this BasePerformanceMetricsByHg.  # noqa: E501
        :rtype: int
        """
        return self._repeat_count

    @repeat_count.setter
    def repeat_count(self, repeat_count):
        """Sets the repeat_count of this BasePerformanceMetricsByHg.

        Number of times the metrics are repeated.  # noqa: E501

        :param repeat_count: The repeat_count of this BasePerformanceMetricsByHg.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                repeat_count is not None and repeat_count > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `repeat_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self._configuration.client_side_validation and
                repeat_count is not None and repeat_count < 0):  # noqa: E501
            raise ValueError("Invalid value for `repeat_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._repeat_count = repeat_count

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
        if issubclass(BasePerformanceMetricsByHg, dict):
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
        if not isinstance(other, BasePerformanceMetricsByHg):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BasePerformanceMetricsByHg):
            return True

        return self.to_dict() != other.to_dict()
