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


class BasePerformanceMetricsByFileSystemRollup(object):
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
        'file_system_id': 'str',
        'timestamp': 'datetime',
        'repeat_count': 'int',
        'avg_read_iops': 'float',
        'avg_write_iops': 'float',
        'avg_total_iops': 'float',
        'max_read_iops': 'float',
        'max_write_iops': 'float',
        'max_iops': 'float',
        'avg_read_bandwidth': 'float',
        'avg_write_bandwidth': 'float',
        'avg_total_bandwidth': 'float',
        'max_read_bandwidth': 'float',
        'max_write_bandwidth': 'float',
        'max_total_bandwidth': 'float',
        'avg_read_latency': 'float',
        'avg_write_latency': 'float',
        'avg_latency': 'float',
        'max_avg_read_latency': 'float',
        'max_avg_write_latency': 'float',
        'max_avg_latency': 'float',
        'avg_read_size': 'float',
        'avg_write_size': 'float',
        'avg_size': 'float',
        'max_avg_read_size': 'float',
        'max_avg_write_size': 'float',
        'max_avg_size': 'float'
    }

    attribute_map = {
        'appliance_id': 'appliance_id',
        'file_system_id': 'file_system_id',
        'timestamp': 'timestamp',
        'repeat_count': 'repeat_count',
        'avg_read_iops': 'avg_read_iops',
        'avg_write_iops': 'avg_write_iops',
        'avg_total_iops': 'avg_total_iops',
        'max_read_iops': 'max_read_iops',
        'max_write_iops': 'max_write_iops',
        'max_iops': 'max_iops',
        'avg_read_bandwidth': 'avg_read_bandwidth',
        'avg_write_bandwidth': 'avg_write_bandwidth',
        'avg_total_bandwidth': 'avg_total_bandwidth',
        'max_read_bandwidth': 'max_read_bandwidth',
        'max_write_bandwidth': 'max_write_bandwidth',
        'max_total_bandwidth': 'max_total_bandwidth',
        'avg_read_latency': 'avg_read_latency',
        'avg_write_latency': 'avg_write_latency',
        'avg_latency': 'avg_latency',
        'max_avg_read_latency': 'max_avg_read_latency',
        'max_avg_write_latency': 'max_avg_write_latency',
        'max_avg_latency': 'max_avg_latency',
        'avg_read_size': 'avg_read_size',
        'avg_write_size': 'avg_write_size',
        'avg_size': 'avg_size',
        'max_avg_read_size': 'max_avg_read_size',
        'max_avg_write_size': 'max_avg_write_size',
        'max_avg_size': 'max_avg_size'
    }

    def __init__(self, appliance_id=None, file_system_id=None, timestamp=None, repeat_count=None, avg_read_iops=None, avg_write_iops=None, avg_total_iops=None, max_read_iops=None, max_write_iops=None, max_iops=None, avg_read_bandwidth=None, avg_write_bandwidth=None, avg_total_bandwidth=None, max_read_bandwidth=None, max_write_bandwidth=None, max_total_bandwidth=None, avg_read_latency=None, avg_write_latency=None, avg_latency=None, max_avg_read_latency=None, max_avg_write_latency=None, max_avg_latency=None, avg_read_size=None, avg_write_size=None, avg_size=None, max_avg_read_size=None, max_avg_write_size=None, max_avg_size=None, _configuration=None):  # noqa: E501
        """BasePerformanceMetricsByFileSystemRollup - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._appliance_id = None
        self._file_system_id = None
        self._timestamp = None
        self._repeat_count = None
        self._avg_read_iops = None
        self._avg_write_iops = None
        self._avg_total_iops = None
        self._max_read_iops = None
        self._max_write_iops = None
        self._max_iops = None
        self._avg_read_bandwidth = None
        self._avg_write_bandwidth = None
        self._avg_total_bandwidth = None
        self._max_read_bandwidth = None
        self._max_write_bandwidth = None
        self._max_total_bandwidth = None
        self._avg_read_latency = None
        self._avg_write_latency = None
        self._avg_latency = None
        self._max_avg_read_latency = None
        self._max_avg_write_latency = None
        self._max_avg_latency = None
        self._avg_read_size = None
        self._avg_write_size = None
        self._avg_size = None
        self._max_avg_read_size = None
        self._max_avg_write_size = None
        self._max_avg_size = None
        self.discriminator = None

        if appliance_id is not None:
            self.appliance_id = appliance_id
        if file_system_id is not None:
            self.file_system_id = file_system_id
        if timestamp is not None:
            self.timestamp = timestamp
        if repeat_count is not None:
            self.repeat_count = repeat_count
        if avg_read_iops is not None:
            self.avg_read_iops = avg_read_iops
        if avg_write_iops is not None:
            self.avg_write_iops = avg_write_iops
        if avg_total_iops is not None:
            self.avg_total_iops = avg_total_iops
        if max_read_iops is not None:
            self.max_read_iops = max_read_iops
        if max_write_iops is not None:
            self.max_write_iops = max_write_iops
        if max_iops is not None:
            self.max_iops = max_iops
        if avg_read_bandwidth is not None:
            self.avg_read_bandwidth = avg_read_bandwidth
        if avg_write_bandwidth is not None:
            self.avg_write_bandwidth = avg_write_bandwidth
        if avg_total_bandwidth is not None:
            self.avg_total_bandwidth = avg_total_bandwidth
        if max_read_bandwidth is not None:
            self.max_read_bandwidth = max_read_bandwidth
        if max_write_bandwidth is not None:
            self.max_write_bandwidth = max_write_bandwidth
        if max_total_bandwidth is not None:
            self.max_total_bandwidth = max_total_bandwidth
        if avg_read_latency is not None:
            self.avg_read_latency = avg_read_latency
        if avg_write_latency is not None:
            self.avg_write_latency = avg_write_latency
        if avg_latency is not None:
            self.avg_latency = avg_latency
        if max_avg_read_latency is not None:
            self.max_avg_read_latency = max_avg_read_latency
        if max_avg_write_latency is not None:
            self.max_avg_write_latency = max_avg_write_latency
        if max_avg_latency is not None:
            self.max_avg_latency = max_avg_latency
        if avg_read_size is not None:
            self.avg_read_size = avg_read_size
        if avg_write_size is not None:
            self.avg_write_size = avg_write_size
        if avg_size is not None:
            self.avg_size = avg_size
        if max_avg_read_size is not None:
            self.max_avg_read_size = max_avg_read_size
        if max_avg_write_size is not None:
            self.max_avg_write_size = max_avg_write_size
        if max_avg_size is not None:
            self.max_avg_size = max_avg_size

    @property
    def appliance_id(self):
        """Gets the appliance_id of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Unique identifier of the appliance. Was added in version 3.0.0.0.  # noqa: E501

        :return: The appliance_id of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: str
        """
        return self._appliance_id

    @appliance_id.setter
    def appliance_id(self, appliance_id):
        """Sets the appliance_id of this BasePerformanceMetricsByFileSystemRollup.

        Unique identifier of the appliance. Was added in version 3.0.0.0.  # noqa: E501

        :param appliance_id: The appliance_id of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :type: str
        """

        self._appliance_id = appliance_id

    @property
    def file_system_id(self):
        """Gets the file_system_id of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Unique identifier of the file system.  # noqa: E501

        :return: The file_system_id of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: str
        """
        return self._file_system_id

    @file_system_id.setter
    def file_system_id(self, file_system_id):
        """Sets the file_system_id of this BasePerformanceMetricsByFileSystemRollup.

        Unique identifier of the file system.  # noqa: E501

        :param file_system_id: The file_system_id of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :type: str
        """

        self._file_system_id = file_system_id

    @property
    def timestamp(self):
        """Gets the timestamp of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Time at the beginning of sample period.  # noqa: E501

        :return: The timestamp of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this BasePerformanceMetricsByFileSystemRollup.

        Time at the beginning of sample period.  # noqa: E501

        :param timestamp: The timestamp of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def repeat_count(self):
        """Gets the repeat_count of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Number of consecutive sampling periods during which there were no changes in the metrics values. If the value is omitted from the response, it is 1 (no additional repeats).   # noqa: E501

        :return: The repeat_count of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: int
        """
        return self._repeat_count

    @repeat_count.setter
    def repeat_count(self, repeat_count):
        """Sets the repeat_count of this BasePerformanceMetricsByFileSystemRollup.

        Number of consecutive sampling periods during which there were no changes in the metrics values. If the value is omitted from the response, it is 1 (no additional repeats).   # noqa: E501

        :param repeat_count: The repeat_count of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
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
    def avg_read_iops(self):
        """Gets the avg_read_iops of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Average read operations per second.  # noqa: E501

        :return: The avg_read_iops of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: float
        """
        return self._avg_read_iops

    @avg_read_iops.setter
    def avg_read_iops(self, avg_read_iops):
        """Sets the avg_read_iops of this BasePerformanceMetricsByFileSystemRollup.

        Average read operations per second.  # noqa: E501

        :param avg_read_iops: The avg_read_iops of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :type: float
        """

        self._avg_read_iops = avg_read_iops

    @property
    def avg_write_iops(self):
        """Gets the avg_write_iops of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Average write operations per second.  # noqa: E501

        :return: The avg_write_iops of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: float
        """
        return self._avg_write_iops

    @avg_write_iops.setter
    def avg_write_iops(self, avg_write_iops):
        """Sets the avg_write_iops of this BasePerformanceMetricsByFileSystemRollup.

        Average write operations per second.  # noqa: E501

        :param avg_write_iops: The avg_write_iops of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :type: float
        """

        self._avg_write_iops = avg_write_iops

    @property
    def avg_total_iops(self):
        """Gets the avg_total_iops of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Average read and write operations per second.  # noqa: E501

        :return: The avg_total_iops of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: float
        """
        return self._avg_total_iops

    @avg_total_iops.setter
    def avg_total_iops(self, avg_total_iops):
        """Sets the avg_total_iops of this BasePerformanceMetricsByFileSystemRollup.

        Average read and write operations per second.  # noqa: E501

        :param avg_total_iops: The avg_total_iops of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :type: float
        """

        self._avg_total_iops = avg_total_iops

    @property
    def max_read_iops(self):
        """Gets the max_read_iops of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Maximum read operations per second.  # noqa: E501

        :return: The max_read_iops of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: float
        """
        return self._max_read_iops

    @max_read_iops.setter
    def max_read_iops(self, max_read_iops):
        """Sets the max_read_iops of this BasePerformanceMetricsByFileSystemRollup.

        Maximum read operations per second.  # noqa: E501

        :param max_read_iops: The max_read_iops of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :type: float
        """

        self._max_read_iops = max_read_iops

    @property
    def max_write_iops(self):
        """Gets the max_write_iops of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Maximum write operations per second.  # noqa: E501

        :return: The max_write_iops of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: float
        """
        return self._max_write_iops

    @max_write_iops.setter
    def max_write_iops(self, max_write_iops):
        """Sets the max_write_iops of this BasePerformanceMetricsByFileSystemRollup.

        Maximum write operations per second.  # noqa: E501

        :param max_write_iops: The max_write_iops of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :type: float
        """

        self._max_write_iops = max_write_iops

    @property
    def max_iops(self):
        """Gets the max_iops of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Maximum read and write operations per second.  # noqa: E501

        :return: The max_iops of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: float
        """
        return self._max_iops

    @max_iops.setter
    def max_iops(self, max_iops):
        """Sets the max_iops of this BasePerformanceMetricsByFileSystemRollup.

        Maximum read and write operations per second.  # noqa: E501

        :param max_iops: The max_iops of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :type: float
        """

        self._max_iops = max_iops

    @property
    def avg_read_bandwidth(self):
        """Gets the avg_read_bandwidth of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Average read rate in bytes per second.  # noqa: E501

        :return: The avg_read_bandwidth of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: float
        """
        return self._avg_read_bandwidth

    @avg_read_bandwidth.setter
    def avg_read_bandwidth(self, avg_read_bandwidth):
        """Sets the avg_read_bandwidth of this BasePerformanceMetricsByFileSystemRollup.

        Average read rate in bytes per second.  # noqa: E501

        :param avg_read_bandwidth: The avg_read_bandwidth of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :type: float
        """

        self._avg_read_bandwidth = avg_read_bandwidth

    @property
    def avg_write_bandwidth(self):
        """Gets the avg_write_bandwidth of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Average write rate in bytes per second.  # noqa: E501

        :return: The avg_write_bandwidth of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: float
        """
        return self._avg_write_bandwidth

    @avg_write_bandwidth.setter
    def avg_write_bandwidth(self, avg_write_bandwidth):
        """Sets the avg_write_bandwidth of this BasePerformanceMetricsByFileSystemRollup.

        Average write rate in bytes per second.  # noqa: E501

        :param avg_write_bandwidth: The avg_write_bandwidth of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :type: float
        """

        self._avg_write_bandwidth = avg_write_bandwidth

    @property
    def avg_total_bandwidth(self):
        """Gets the avg_total_bandwidth of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Average data transfer rate in bytes per second.  # noqa: E501

        :return: The avg_total_bandwidth of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: float
        """
        return self._avg_total_bandwidth

    @avg_total_bandwidth.setter
    def avg_total_bandwidth(self, avg_total_bandwidth):
        """Sets the avg_total_bandwidth of this BasePerformanceMetricsByFileSystemRollup.

        Average data transfer rate in bytes per second.  # noqa: E501

        :param avg_total_bandwidth: The avg_total_bandwidth of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :type: float
        """

        self._avg_total_bandwidth = avg_total_bandwidth

    @property
    def max_read_bandwidth(self):
        """Gets the max_read_bandwidth of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Maximum read rate in bytes per second.  # noqa: E501

        :return: The max_read_bandwidth of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: float
        """
        return self._max_read_bandwidth

    @max_read_bandwidth.setter
    def max_read_bandwidth(self, max_read_bandwidth):
        """Sets the max_read_bandwidth of this BasePerformanceMetricsByFileSystemRollup.

        Maximum read rate in bytes per second.  # noqa: E501

        :param max_read_bandwidth: The max_read_bandwidth of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :type: float
        """

        self._max_read_bandwidth = max_read_bandwidth

    @property
    def max_write_bandwidth(self):
        """Gets the max_write_bandwidth of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Maximum write rate in bytes per second.  # noqa: E501

        :return: The max_write_bandwidth of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: float
        """
        return self._max_write_bandwidth

    @max_write_bandwidth.setter
    def max_write_bandwidth(self, max_write_bandwidth):
        """Sets the max_write_bandwidth of this BasePerformanceMetricsByFileSystemRollup.

        Maximum write rate in bytes per second.  # noqa: E501

        :param max_write_bandwidth: The max_write_bandwidth of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :type: float
        """

        self._max_write_bandwidth = max_write_bandwidth

    @property
    def max_total_bandwidth(self):
        """Gets the max_total_bandwidth of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Maximum data transfer rate in bytes per second.  # noqa: E501

        :return: The max_total_bandwidth of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: float
        """
        return self._max_total_bandwidth

    @max_total_bandwidth.setter
    def max_total_bandwidth(self, max_total_bandwidth):
        """Sets the max_total_bandwidth of this BasePerformanceMetricsByFileSystemRollup.

        Maximum data transfer rate in bytes per second.  # noqa: E501

        :param max_total_bandwidth: The max_total_bandwidth of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :type: float
        """

        self._max_total_bandwidth = max_total_bandwidth

    @property
    def avg_read_latency(self):
        """Gets the avg_read_latency of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Maximum of average read latency in microseconds.  # noqa: E501

        :return: The avg_read_latency of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: float
        """
        return self._avg_read_latency

    @avg_read_latency.setter
    def avg_read_latency(self, avg_read_latency):
        """Sets the avg_read_latency of this BasePerformanceMetricsByFileSystemRollup.

        Maximum of average read latency in microseconds.  # noqa: E501

        :param avg_read_latency: The avg_read_latency of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :type: float
        """

        self._avg_read_latency = avg_read_latency

    @property
    def avg_write_latency(self):
        """Gets the avg_write_latency of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Maximum of average write latency in microseconds.  # noqa: E501

        :return: The avg_write_latency of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: float
        """
        return self._avg_write_latency

    @avg_write_latency.setter
    def avg_write_latency(self, avg_write_latency):
        """Sets the avg_write_latency of this BasePerformanceMetricsByFileSystemRollup.

        Maximum of average write latency in microseconds.  # noqa: E501

        :param avg_write_latency: The avg_write_latency of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :type: float
        """

        self._avg_write_latency = avg_write_latency

    @property
    def avg_latency(self):
        """Gets the avg_latency of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Maximum of average read and write latency in microseconds.  # noqa: E501

        :return: The avg_latency of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: float
        """
        return self._avg_latency

    @avg_latency.setter
    def avg_latency(self, avg_latency):
        """Sets the avg_latency of this BasePerformanceMetricsByFileSystemRollup.

        Maximum of average read and write latency in microseconds.  # noqa: E501

        :param avg_latency: The avg_latency of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :type: float
        """

        self._avg_latency = avg_latency

    @property
    def max_avg_read_latency(self):
        """Gets the max_avg_read_latency of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Maximum of average read latency in microseconds.  # noqa: E501

        :return: The max_avg_read_latency of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: float
        """
        return self._max_avg_read_latency

    @max_avg_read_latency.setter
    def max_avg_read_latency(self, max_avg_read_latency):
        """Sets the max_avg_read_latency of this BasePerformanceMetricsByFileSystemRollup.

        Maximum of average read latency in microseconds.  # noqa: E501

        :param max_avg_read_latency: The max_avg_read_latency of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :type: float
        """

        self._max_avg_read_latency = max_avg_read_latency

    @property
    def max_avg_write_latency(self):
        """Gets the max_avg_write_latency of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Maximum of average write latency in microseconds.  # noqa: E501

        :return: The max_avg_write_latency of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: float
        """
        return self._max_avg_write_latency

    @max_avg_write_latency.setter
    def max_avg_write_latency(self, max_avg_write_latency):
        """Sets the max_avg_write_latency of this BasePerformanceMetricsByFileSystemRollup.

        Maximum of average write latency in microseconds.  # noqa: E501

        :param max_avg_write_latency: The max_avg_write_latency of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :type: float
        """

        self._max_avg_write_latency = max_avg_write_latency

    @property
    def max_avg_latency(self):
        """Gets the max_avg_latency of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Maximum of average read and write latency in microseconds.  # noqa: E501

        :return: The max_avg_latency of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: float
        """
        return self._max_avg_latency

    @max_avg_latency.setter
    def max_avg_latency(self, max_avg_latency):
        """Sets the max_avg_latency of this BasePerformanceMetricsByFileSystemRollup.

        Maximum of average read and write latency in microseconds.  # noqa: E501

        :param max_avg_latency: The max_avg_latency of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :type: float
        """

        self._max_avg_latency = max_avg_latency

    @property
    def avg_read_size(self):
        """Gets the avg_read_size of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Average read size in bytes.  # noqa: E501

        :return: The avg_read_size of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: float
        """
        return self._avg_read_size

    @avg_read_size.setter
    def avg_read_size(self, avg_read_size):
        """Sets the avg_read_size of this BasePerformanceMetricsByFileSystemRollup.

        Average read size in bytes.  # noqa: E501

        :param avg_read_size: The avg_read_size of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :type: float
        """

        self._avg_read_size = avg_read_size

    @property
    def avg_write_size(self):
        """Gets the avg_write_size of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Average write size in bytes.  # noqa: E501

        :return: The avg_write_size of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: float
        """
        return self._avg_write_size

    @avg_write_size.setter
    def avg_write_size(self, avg_write_size):
        """Sets the avg_write_size of this BasePerformanceMetricsByFileSystemRollup.

        Average write size in bytes.  # noqa: E501

        :param avg_write_size: The avg_write_size of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :type: float
        """

        self._avg_write_size = avg_write_size

    @property
    def avg_size(self):
        """Gets the avg_size of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Average read and write size in bytes.  # noqa: E501

        :return: The avg_size of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: float
        """
        return self._avg_size

    @avg_size.setter
    def avg_size(self, avg_size):
        """Sets the avg_size of this BasePerformanceMetricsByFileSystemRollup.

        Average read and write size in bytes.  # noqa: E501

        :param avg_size: The avg_size of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :type: float
        """

        self._avg_size = avg_size

    @property
    def max_avg_read_size(self):
        """Gets the max_avg_read_size of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Maximum of average read size in bytes.  # noqa: E501

        :return: The max_avg_read_size of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: float
        """
        return self._max_avg_read_size

    @max_avg_read_size.setter
    def max_avg_read_size(self, max_avg_read_size):
        """Sets the max_avg_read_size of this BasePerformanceMetricsByFileSystemRollup.

        Maximum of average read size in bytes.  # noqa: E501

        :param max_avg_read_size: The max_avg_read_size of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :type: float
        """

        self._max_avg_read_size = max_avg_read_size

    @property
    def max_avg_write_size(self):
        """Gets the max_avg_write_size of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Maximum of average write size in bytes.  # noqa: E501

        :return: The max_avg_write_size of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: float
        """
        return self._max_avg_write_size

    @max_avg_write_size.setter
    def max_avg_write_size(self, max_avg_write_size):
        """Sets the max_avg_write_size of this BasePerformanceMetricsByFileSystemRollup.

        Maximum of average write size in bytes.  # noqa: E501

        :param max_avg_write_size: The max_avg_write_size of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :type: float
        """

        self._max_avg_write_size = max_avg_write_size

    @property
    def max_avg_size(self):
        """Gets the max_avg_size of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501

        Maximum of average read and write size in bytes.  # noqa: E501

        :return: The max_avg_size of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :rtype: float
        """
        return self._max_avg_size

    @max_avg_size.setter
    def max_avg_size(self, max_avg_size):
        """Sets the max_avg_size of this BasePerformanceMetricsByFileSystemRollup.

        Maximum of average read and write size in bytes.  # noqa: E501

        :param max_avg_size: The max_avg_size of this BasePerformanceMetricsByFileSystemRollup.  # noqa: E501
        :type: float
        """

        self._max_avg_size = max_avg_size

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
        if issubclass(BasePerformanceMetricsByFileSystemRollup, dict):
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
        if not isinstance(other, BasePerformanceMetricsByFileSystemRollup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BasePerformanceMetricsByFileSystemRollup):
            return True

        return self.to_dict() != other.to_dict()
