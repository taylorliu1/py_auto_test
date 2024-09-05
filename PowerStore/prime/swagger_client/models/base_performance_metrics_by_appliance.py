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


class BasePerformanceMetricsByAppliance(object):
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
        'timestamp': 'datetime',
        'avg_read_latency': 'float',
        'avg_read_size': 'float',
        'avg_mirror_overhead_latency': 'float',
        'avg_latency': 'float',
        'avg_write_latency': 'float',
        'avg_mirror_write_latency': 'float',
        'avg_write_size': 'float',
        'read_iops': 'float',
        'read_bandwidth': 'float',
        'total_iops': 'float',
        'total_bandwidth': 'float',
        'write_iops': 'float',
        'mirror_write_iops': 'float',
        'write_bandwidth': 'float',
        'mirror_write_bandwidth': 'float',
        'io_workload_cpu_utilization': 'float',
        'avg_io_size': 'float',
        'repeat_count': 'int'
    }

    attribute_map = {
        'appliance_id': 'appliance_id',
        'timestamp': 'timestamp',
        'avg_read_latency': 'avg_read_latency',
        'avg_read_size': 'avg_read_size',
        'avg_mirror_overhead_latency': 'avg_mirror_overhead_latency',
        'avg_latency': 'avg_latency',
        'avg_write_latency': 'avg_write_latency',
        'avg_mirror_write_latency': 'avg_mirror_write_latency',
        'avg_write_size': 'avg_write_size',
        'read_iops': 'read_iops',
        'read_bandwidth': 'read_bandwidth',
        'total_iops': 'total_iops',
        'total_bandwidth': 'total_bandwidth',
        'write_iops': 'write_iops',
        'mirror_write_iops': 'mirror_write_iops',
        'write_bandwidth': 'write_bandwidth',
        'mirror_write_bandwidth': 'mirror_write_bandwidth',
        'io_workload_cpu_utilization': 'io_workload_cpu_utilization',
        'avg_io_size': 'avg_io_size',
        'repeat_count': 'repeat_count'
    }

    def __init__(self, appliance_id=None, timestamp=None, avg_read_latency=None, avg_read_size=None, avg_mirror_overhead_latency=None, avg_latency=None, avg_write_latency=None, avg_mirror_write_latency=None, avg_write_size=None, read_iops=None, read_bandwidth=None, total_iops=None, total_bandwidth=None, write_iops=None, mirror_write_iops=None, write_bandwidth=None, mirror_write_bandwidth=None, io_workload_cpu_utilization=None, avg_io_size=None, repeat_count=None, _configuration=None):  # noqa: E501
        """BasePerformanceMetricsByAppliance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._appliance_id = None
        self._timestamp = None
        self._avg_read_latency = None
        self._avg_read_size = None
        self._avg_mirror_overhead_latency = None
        self._avg_latency = None
        self._avg_write_latency = None
        self._avg_mirror_write_latency = None
        self._avg_write_size = None
        self._read_iops = None
        self._read_bandwidth = None
        self._total_iops = None
        self._total_bandwidth = None
        self._write_iops = None
        self._mirror_write_iops = None
        self._write_bandwidth = None
        self._mirror_write_bandwidth = None
        self._io_workload_cpu_utilization = None
        self._avg_io_size = None
        self._repeat_count = None
        self.discriminator = None

        if appliance_id is not None:
            self.appliance_id = appliance_id
        if timestamp is not None:
            self.timestamp = timestamp
        if avg_read_latency is not None:
            self.avg_read_latency = avg_read_latency
        if avg_read_size is not None:
            self.avg_read_size = avg_read_size
        if avg_mirror_overhead_latency is not None:
            self.avg_mirror_overhead_latency = avg_mirror_overhead_latency
        if avg_latency is not None:
            self.avg_latency = avg_latency
        if avg_write_latency is not None:
            self.avg_write_latency = avg_write_latency
        if avg_mirror_write_latency is not None:
            self.avg_mirror_write_latency = avg_mirror_write_latency
        if avg_write_size is not None:
            self.avg_write_size = avg_write_size
        if read_iops is not None:
            self.read_iops = read_iops
        if read_bandwidth is not None:
            self.read_bandwidth = read_bandwidth
        if total_iops is not None:
            self.total_iops = total_iops
        if total_bandwidth is not None:
            self.total_bandwidth = total_bandwidth
        if write_iops is not None:
            self.write_iops = write_iops
        if mirror_write_iops is not None:
            self.mirror_write_iops = mirror_write_iops
        if write_bandwidth is not None:
            self.write_bandwidth = write_bandwidth
        if mirror_write_bandwidth is not None:
            self.mirror_write_bandwidth = mirror_write_bandwidth
        if io_workload_cpu_utilization is not None:
            self.io_workload_cpu_utilization = io_workload_cpu_utilization
        if avg_io_size is not None:
            self.avg_io_size = avg_io_size
        if repeat_count is not None:
            self.repeat_count = repeat_count

    @property
    def appliance_id(self):
        """Gets the appliance_id of this BasePerformanceMetricsByAppliance.  # noqa: E501

        Unique identifier representing a specific appliance.  # noqa: E501

        :return: The appliance_id of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :rtype: str
        """
        return self._appliance_id

    @appliance_id.setter
    def appliance_id(self, appliance_id):
        """Sets the appliance_id of this BasePerformanceMetricsByAppliance.

        Unique identifier representing a specific appliance.  # noqa: E501

        :param appliance_id: The appliance_id of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :type: str
        """

        self._appliance_id = appliance_id

    @property
    def timestamp(self):
        """Gets the timestamp of this BasePerformanceMetricsByAppliance.  # noqa: E501

        End of sample period.  # noqa: E501

        :return: The timestamp of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this BasePerformanceMetricsByAppliance.

        End of sample period.  # noqa: E501

        :param timestamp: The timestamp of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def avg_read_latency(self):
        """Gets the avg_read_latency of this BasePerformanceMetricsByAppliance.  # noqa: E501

        Average read latency in microseconds.  # noqa: E501

        :return: The avg_read_latency of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :rtype: float
        """
        return self._avg_read_latency

    @avg_read_latency.setter
    def avg_read_latency(self, avg_read_latency):
        """Sets the avg_read_latency of this BasePerformanceMetricsByAppliance.

        Average read latency in microseconds.  # noqa: E501

        :param avg_read_latency: The avg_read_latency of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :type: float
        """

        self._avg_read_latency = avg_read_latency

    @property
    def avg_read_size(self):
        """Gets the avg_read_size of this BasePerformanceMetricsByAppliance.  # noqa: E501

        Average read size in bytes.  # noqa: E501

        :return: The avg_read_size of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :rtype: float
        """
        return self._avg_read_size

    @avg_read_size.setter
    def avg_read_size(self, avg_read_size):
        """Sets the avg_read_size of this BasePerformanceMetricsByAppliance.

        Average read size in bytes.  # noqa: E501

        :param avg_read_size: The avg_read_size of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :type: float
        """

        self._avg_read_size = avg_read_size

    @property
    def avg_mirror_overhead_latency(self):
        """Gets the avg_mirror_overhead_latency of this BasePerformanceMetricsByAppliance.  # noqa: E501

        Average additional latency incurred on the source in order to do the remote mirror writes in microseconds. This applies to metro volumes in the active-active state. Was added in version 3.0.0.0.  # noqa: E501

        :return: The avg_mirror_overhead_latency of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :rtype: float
        """
        return self._avg_mirror_overhead_latency

    @avg_mirror_overhead_latency.setter
    def avg_mirror_overhead_latency(self, avg_mirror_overhead_latency):
        """Sets the avg_mirror_overhead_latency of this BasePerformanceMetricsByAppliance.

        Average additional latency incurred on the source in order to do the remote mirror writes in microseconds. This applies to metro volumes in the active-active state. Was added in version 3.0.0.0.  # noqa: E501

        :param avg_mirror_overhead_latency: The avg_mirror_overhead_latency of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :type: float
        """

        self._avg_mirror_overhead_latency = avg_mirror_overhead_latency

    @property
    def avg_latency(self):
        """Gets the avg_latency of this BasePerformanceMetricsByAppliance.  # noqa: E501

        Average read and write latency in microseconds.  # noqa: E501

        :return: The avg_latency of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :rtype: float
        """
        return self._avg_latency

    @avg_latency.setter
    def avg_latency(self, avg_latency):
        """Sets the avg_latency of this BasePerformanceMetricsByAppliance.

        Average read and write latency in microseconds.  # noqa: E501

        :param avg_latency: The avg_latency of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :type: float
        """

        self._avg_latency = avg_latency

    @property
    def avg_write_latency(self):
        """Gets the avg_write_latency of this BasePerformanceMetricsByAppliance.  # noqa: E501

        Average write latency in microseconds.  # noqa: E501

        :return: The avg_write_latency of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :rtype: float
        """
        return self._avg_write_latency

    @avg_write_latency.setter
    def avg_write_latency(self, avg_write_latency):
        """Sets the avg_write_latency of this BasePerformanceMetricsByAppliance.

        Average write latency in microseconds.  # noqa: E501

        :param avg_write_latency: The avg_write_latency of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :type: float
        """

        self._avg_write_latency = avg_write_latency

    @property
    def avg_mirror_write_latency(self):
        """Gets the avg_mirror_write_latency of this BasePerformanceMetricsByAppliance.  # noqa: E501

        Average mirror write latency in microseconds.  This applies to metro volumes in the active-active state. Was added in version 3.0.0.0.  # noqa: E501

        :return: The avg_mirror_write_latency of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :rtype: float
        """
        return self._avg_mirror_write_latency

    @avg_mirror_write_latency.setter
    def avg_mirror_write_latency(self, avg_mirror_write_latency):
        """Sets the avg_mirror_write_latency of this BasePerformanceMetricsByAppliance.

        Average mirror write latency in microseconds.  This applies to metro volumes in the active-active state. Was added in version 3.0.0.0.  # noqa: E501

        :param avg_mirror_write_latency: The avg_mirror_write_latency of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :type: float
        """

        self._avg_mirror_write_latency = avg_mirror_write_latency

    @property
    def avg_write_size(self):
        """Gets the avg_write_size of this BasePerformanceMetricsByAppliance.  # noqa: E501

        Average write size in bytes.  # noqa: E501

        :return: The avg_write_size of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :rtype: float
        """
        return self._avg_write_size

    @avg_write_size.setter
    def avg_write_size(self, avg_write_size):
        """Sets the avg_write_size of this BasePerformanceMetricsByAppliance.

        Average write size in bytes.  # noqa: E501

        :param avg_write_size: The avg_write_size of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :type: float
        """

        self._avg_write_size = avg_write_size

    @property
    def read_iops(self):
        """Gets the read_iops of this BasePerformanceMetricsByAppliance.  # noqa: E501

        Total read operations per second.  # noqa: E501

        :return: The read_iops of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :rtype: float
        """
        return self._read_iops

    @read_iops.setter
    def read_iops(self, read_iops):
        """Sets the read_iops of this BasePerformanceMetricsByAppliance.

        Total read operations per second.  # noqa: E501

        :param read_iops: The read_iops of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :type: float
        """

        self._read_iops = read_iops

    @property
    def read_bandwidth(self):
        """Gets the read_bandwidth of this BasePerformanceMetricsByAppliance.  # noqa: E501

        Read rate in bytes per second.  # noqa: E501

        :return: The read_bandwidth of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :rtype: float
        """
        return self._read_bandwidth

    @read_bandwidth.setter
    def read_bandwidth(self, read_bandwidth):
        """Sets the read_bandwidth of this BasePerformanceMetricsByAppliance.

        Read rate in bytes per second.  # noqa: E501

        :param read_bandwidth: The read_bandwidth of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :type: float
        """

        self._read_bandwidth = read_bandwidth

    @property
    def total_iops(self):
        """Gets the total_iops of this BasePerformanceMetricsByAppliance.  # noqa: E501

        Total read and write operations per second.  # noqa: E501

        :return: The total_iops of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :rtype: float
        """
        return self._total_iops

    @total_iops.setter
    def total_iops(self, total_iops):
        """Sets the total_iops of this BasePerformanceMetricsByAppliance.

        Total read and write operations per second.  # noqa: E501

        :param total_iops: The total_iops of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :type: float
        """

        self._total_iops = total_iops

    @property
    def total_bandwidth(self):
        """Gets the total_bandwidth of this BasePerformanceMetricsByAppliance.  # noqa: E501

        Total data transfer rate in bytes per second.  # noqa: E501

        :return: The total_bandwidth of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :rtype: float
        """
        return self._total_bandwidth

    @total_bandwidth.setter
    def total_bandwidth(self, total_bandwidth):
        """Sets the total_bandwidth of this BasePerformanceMetricsByAppliance.

        Total data transfer rate in bytes per second.  # noqa: E501

        :param total_bandwidth: The total_bandwidth of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :type: float
        """

        self._total_bandwidth = total_bandwidth

    @property
    def write_iops(self):
        """Gets the write_iops of this BasePerformanceMetricsByAppliance.  # noqa: E501

        Total write operations per second.  # noqa: E501

        :return: The write_iops of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :rtype: float
        """
        return self._write_iops

    @write_iops.setter
    def write_iops(self, write_iops):
        """Sets the write_iops of this BasePerformanceMetricsByAppliance.

        Total write operations per second.  # noqa: E501

        :param write_iops: The write_iops of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :type: float
        """

        self._write_iops = write_iops

    @property
    def mirror_write_iops(self):
        """Gets the mirror_write_iops of this BasePerformanceMetricsByAppliance.  # noqa: E501

        Total mirror write operations per second.  This applies to metro volumes in the active-active state. Was added in version 3.0.0.0.  # noqa: E501

        :return: The mirror_write_iops of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :rtype: float
        """
        return self._mirror_write_iops

    @mirror_write_iops.setter
    def mirror_write_iops(self, mirror_write_iops):
        """Sets the mirror_write_iops of this BasePerformanceMetricsByAppliance.

        Total mirror write operations per second.  This applies to metro volumes in the active-active state. Was added in version 3.0.0.0.  # noqa: E501

        :param mirror_write_iops: The mirror_write_iops of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :type: float
        """

        self._mirror_write_iops = mirror_write_iops

    @property
    def write_bandwidth(self):
        """Gets the write_bandwidth of this BasePerformanceMetricsByAppliance.  # noqa: E501

        Write rate in bytes per second.  # noqa: E501

        :return: The write_bandwidth of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :rtype: float
        """
        return self._write_bandwidth

    @write_bandwidth.setter
    def write_bandwidth(self, write_bandwidth):
        """Sets the write_bandwidth of this BasePerformanceMetricsByAppliance.

        Write rate in bytes per second.  # noqa: E501

        :param write_bandwidth: The write_bandwidth of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :type: float
        """

        self._write_bandwidth = write_bandwidth

    @property
    def mirror_write_bandwidth(self):
        """Gets the mirror_write_bandwidth of this BasePerformanceMetricsByAppliance.  # noqa: E501

        Metro write rate in bytes per second.  This applies to metro volumes in the active-active state. Was added in version 3.0.0.0.  # noqa: E501

        :return: The mirror_write_bandwidth of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :rtype: float
        """
        return self._mirror_write_bandwidth

    @mirror_write_bandwidth.setter
    def mirror_write_bandwidth(self, mirror_write_bandwidth):
        """Sets the mirror_write_bandwidth of this BasePerformanceMetricsByAppliance.

        Metro write rate in bytes per second.  This applies to metro volumes in the active-active state. Was added in version 3.0.0.0.  # noqa: E501

        :param mirror_write_bandwidth: The mirror_write_bandwidth of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :type: float
        """

        self._mirror_write_bandwidth = mirror_write_bandwidth

    @property
    def io_workload_cpu_utilization(self):
        """Gets the io_workload_cpu_utilization of this BasePerformanceMetricsByAppliance.  # noqa: E501

        The percentage of CPU Utilization on the cores dedicated to servicing storage I/O requests.  # noqa: E501

        :return: The io_workload_cpu_utilization of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :rtype: float
        """
        return self._io_workload_cpu_utilization

    @io_workload_cpu_utilization.setter
    def io_workload_cpu_utilization(self, io_workload_cpu_utilization):
        """Sets the io_workload_cpu_utilization of this BasePerformanceMetricsByAppliance.

        The percentage of CPU Utilization on the cores dedicated to servicing storage I/O requests.  # noqa: E501

        :param io_workload_cpu_utilization: The io_workload_cpu_utilization of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :type: float
        """

        self._io_workload_cpu_utilization = io_workload_cpu_utilization

    @property
    def avg_io_size(self):
        """Gets the avg_io_size of this BasePerformanceMetricsByAppliance.  # noqa: E501

        Average size of read and write operations in bytes.  # noqa: E501

        :return: The avg_io_size of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :rtype: float
        """
        return self._avg_io_size

    @avg_io_size.setter
    def avg_io_size(self, avg_io_size):
        """Sets the avg_io_size of this BasePerformanceMetricsByAppliance.

        Average size of read and write operations in bytes.  # noqa: E501

        :param avg_io_size: The avg_io_size of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :type: float
        """

        self._avg_io_size = avg_io_size

    @property
    def repeat_count(self):
        """Gets the repeat_count of this BasePerformanceMetricsByAppliance.  # noqa: E501

        Number of times the metrics are repeated.  # noqa: E501

        :return: The repeat_count of this BasePerformanceMetricsByAppliance.  # noqa: E501
        :rtype: int
        """
        return self._repeat_count

    @repeat_count.setter
    def repeat_count(self, repeat_count):
        """Sets the repeat_count of this BasePerformanceMetricsByAppliance.

        Number of times the metrics are repeated.  # noqa: E501

        :param repeat_count: The repeat_count of this BasePerformanceMetricsByAppliance.  # noqa: E501
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
        if issubclass(BasePerformanceMetricsByAppliance, dict):
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
        if not isinstance(other, BasePerformanceMetricsByAppliance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BasePerformanceMetricsByAppliance):
            return True

        return self.to_dict() != other.to_dict()
