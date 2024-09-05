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


class BasePerformanceMetricsByNfsv4(object):
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
        'md_ops': 'float',
        'failed_md_ops': 'float',
        'avg_md_latency': 'float',
        'read_iops': 'float',
        'write_iops': 'float',
        'total_iops': 'float'
    }

    attribute_map = {
        'node_id': 'node_id',
        'appliance_id': 'appliance_id',
        'timestamp': 'timestamp',
        'repeat_count': 'repeat_count',
        'md_ops': 'md_ops',
        'failed_md_ops': 'failed_md_ops',
        'avg_md_latency': 'avg_md_latency',
        'read_iops': 'read_iops',
        'write_iops': 'write_iops',
        'total_iops': 'total_iops'
    }

    def __init__(self, node_id=None, appliance_id=None, timestamp=None, repeat_count=None, md_ops=None, failed_md_ops=None, avg_md_latency=None, read_iops=None, write_iops=None, total_iops=None, _configuration=None):  # noqa: E501
        """BasePerformanceMetricsByNfsv4 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._node_id = None
        self._appliance_id = None
        self._timestamp = None
        self._repeat_count = None
        self._md_ops = None
        self._failed_md_ops = None
        self._avg_md_latency = None
        self._read_iops = None
        self._write_iops = None
        self._total_iops = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if appliance_id is not None:
            self.appliance_id = appliance_id
        if timestamp is not None:
            self.timestamp = timestamp
        if repeat_count is not None:
            self.repeat_count = repeat_count
        if md_ops is not None:
            self.md_ops = md_ops
        if failed_md_ops is not None:
            self.failed_md_ops = failed_md_ops
        if avg_md_latency is not None:
            self.avg_md_latency = avg_md_latency
        if read_iops is not None:
            self.read_iops = read_iops
        if write_iops is not None:
            self.write_iops = write_iops
        if total_iops is not None:
            self.total_iops = total_iops

    @property
    def node_id(self):
        """Gets the node_id of this BasePerformanceMetricsByNfsv4.  # noqa: E501

        Unique identifier of the nfs.  # noqa: E501

        :return: The node_id of this BasePerformanceMetricsByNfsv4.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this BasePerformanceMetricsByNfsv4.

        Unique identifier of the nfs.  # noqa: E501

        :param node_id: The node_id of this BasePerformanceMetricsByNfsv4.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def appliance_id(self):
        """Gets the appliance_id of this BasePerformanceMetricsByNfsv4.  # noqa: E501

        Unique identifier of the appliance. Was added in version 3.0.0.0.  # noqa: E501

        :return: The appliance_id of this BasePerformanceMetricsByNfsv4.  # noqa: E501
        :rtype: str
        """
        return self._appliance_id

    @appliance_id.setter
    def appliance_id(self, appliance_id):
        """Sets the appliance_id of this BasePerformanceMetricsByNfsv4.

        Unique identifier of the appliance. Was added in version 3.0.0.0.  # noqa: E501

        :param appliance_id: The appliance_id of this BasePerformanceMetricsByNfsv4.  # noqa: E501
        :type: str
        """

        self._appliance_id = appliance_id

    @property
    def timestamp(self):
        """Gets the timestamp of this BasePerformanceMetricsByNfsv4.  # noqa: E501

        End of sample period.  # noqa: E501

        :return: The timestamp of this BasePerformanceMetricsByNfsv4.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this BasePerformanceMetricsByNfsv4.

        End of sample period.  # noqa: E501

        :param timestamp: The timestamp of this BasePerformanceMetricsByNfsv4.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def repeat_count(self):
        """Gets the repeat_count of this BasePerformanceMetricsByNfsv4.  # noqa: E501

        Number of consecutive sampling periods during which there were no changes in the metrics values. If the value is omitted from the response, it is 1 (no additional repeats).   # noqa: E501

        :return: The repeat_count of this BasePerformanceMetricsByNfsv4.  # noqa: E501
        :rtype: int
        """
        return self._repeat_count

    @repeat_count.setter
    def repeat_count(self, repeat_count):
        """Sets the repeat_count of this BasePerformanceMetricsByNfsv4.

        Number of consecutive sampling periods during which there were no changes in the metrics values. If the value is omitted from the response, it is 1 (no additional repeats).   # noqa: E501

        :param repeat_count: The repeat_count of this BasePerformanceMetricsByNfsv4.  # noqa: E501
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
    def md_ops(self):
        """Gets the md_ops of this BasePerformanceMetricsByNfsv4.  # noqa: E501

        Total md operations per second.  # noqa: E501

        :return: The md_ops of this BasePerformanceMetricsByNfsv4.  # noqa: E501
        :rtype: float
        """
        return self._md_ops

    @md_ops.setter
    def md_ops(self, md_ops):
        """Sets the md_ops of this BasePerformanceMetricsByNfsv4.

        Total md operations per second.  # noqa: E501

        :param md_ops: The md_ops of this BasePerformanceMetricsByNfsv4.  # noqa: E501
        :type: float
        """

        self._md_ops = md_ops

    @property
    def failed_md_ops(self):
        """Gets the failed_md_ops of this BasePerformanceMetricsByNfsv4.  # noqa: E501

        Total failed md operations per second.  # noqa: E501

        :return: The failed_md_ops of this BasePerformanceMetricsByNfsv4.  # noqa: E501
        :rtype: float
        """
        return self._failed_md_ops

    @failed_md_ops.setter
    def failed_md_ops(self, failed_md_ops):
        """Sets the failed_md_ops of this BasePerformanceMetricsByNfsv4.

        Total failed md operations per second.  # noqa: E501

        :param failed_md_ops: The failed_md_ops of this BasePerformanceMetricsByNfsv4.  # noqa: E501
        :type: float
        """

        self._failed_md_ops = failed_md_ops

    @property
    def avg_md_latency(self):
        """Gets the avg_md_latency of this BasePerformanceMetricsByNfsv4.  # noqa: E501

        Average md latency operations per second.  # noqa: E501

        :return: The avg_md_latency of this BasePerformanceMetricsByNfsv4.  # noqa: E501
        :rtype: float
        """
        return self._avg_md_latency

    @avg_md_latency.setter
    def avg_md_latency(self, avg_md_latency):
        """Sets the avg_md_latency of this BasePerformanceMetricsByNfsv4.

        Average md latency operations per second.  # noqa: E501

        :param avg_md_latency: The avg_md_latency of this BasePerformanceMetricsByNfsv4.  # noqa: E501
        :type: float
        """

        self._avg_md_latency = avg_md_latency

    @property
    def read_iops(self):
        """Gets the read_iops of this BasePerformanceMetricsByNfsv4.  # noqa: E501

        Total read iops in microseconds.  # noqa: E501

        :return: The read_iops of this BasePerformanceMetricsByNfsv4.  # noqa: E501
        :rtype: float
        """
        return self._read_iops

    @read_iops.setter
    def read_iops(self, read_iops):
        """Sets the read_iops of this BasePerformanceMetricsByNfsv4.

        Total read iops in microseconds.  # noqa: E501

        :param read_iops: The read_iops of this BasePerformanceMetricsByNfsv4.  # noqa: E501
        :type: float
        """

        self._read_iops = read_iops

    @property
    def write_iops(self):
        """Gets the write_iops of this BasePerformanceMetricsByNfsv4.  # noqa: E501

        Total write iops in microseconds.  # noqa: E501

        :return: The write_iops of this BasePerformanceMetricsByNfsv4.  # noqa: E501
        :rtype: float
        """
        return self._write_iops

    @write_iops.setter
    def write_iops(self, write_iops):
        """Sets the write_iops of this BasePerformanceMetricsByNfsv4.

        Total write iops in microseconds.  # noqa: E501

        :param write_iops: The write_iops of this BasePerformanceMetricsByNfsv4.  # noqa: E501
        :type: float
        """

        self._write_iops = write_iops

    @property
    def total_iops(self):
        """Gets the total_iops of this BasePerformanceMetricsByNfsv4.  # noqa: E501

        Total read and write iops in microseconds.  # noqa: E501

        :return: The total_iops of this BasePerformanceMetricsByNfsv4.  # noqa: E501
        :rtype: float
        """
        return self._total_iops

    @total_iops.setter
    def total_iops(self, total_iops):
        """Sets the total_iops of this BasePerformanceMetricsByNfsv4.

        Total read and write iops in microseconds.  # noqa: E501

        :param total_iops: The total_iops of this BasePerformanceMetricsByNfsv4.  # noqa: E501
        :type: float
        """

        self._total_iops = total_iops

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
        if issubclass(BasePerformanceMetricsByNfsv4, dict):
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
        if not isinstance(other, BasePerformanceMetricsByNfsv4):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BasePerformanceMetricsByNfsv4):
            return True

        return self.to_dict() != other.to_dict()
