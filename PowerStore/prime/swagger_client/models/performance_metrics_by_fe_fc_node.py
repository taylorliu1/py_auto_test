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


class PerformanceMetricsByFeFcNode(object):
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
        'timestamp': 'datetime',
        'avg_read_latency': 'float',
        'avg_write_latency': 'float',
        'avg_latency': 'float',
        'avg_read_size': 'float',
        'avg_write_size': 'float',
        'avg_io_size': 'float',
        'read_iops': 'float',
        'write_iops': 'float',
        'total_iops': 'float',
        'read_bandwidth': 'float',
        'write_bandwidth': 'float',
        'total_bandwidth': 'float',
        'unaligned_read_iops': 'float',
        'unaligned_write_iops': 'float',
        'unaligned_iops': 'float',
        'unaligned_read_bandwidth': 'float',
        'unaligned_write_bandwidth': 'float',
        'unaligned_bandwidth': 'float',
        'current_logins': 'int',
        'dumped_frames_ps': 'float',
        'loss_of_signal_count_ps': 'float',
        'loss_of_sync_count_ps': 'float',
        'invalid_crc_count_ps': 'float',
        'invalid_tx_word_count_ps': 'float',
        'prim_seq_prot_err_count_ps': 'float',
        'link_failure_count_ps': 'float',
        'repeat_count': 'int'
    }

    attribute_map = {
        'node_id': 'node_id',
        'timestamp': 'timestamp',
        'avg_read_latency': 'avg_read_latency',
        'avg_write_latency': 'avg_write_latency',
        'avg_latency': 'avg_latency',
        'avg_read_size': 'avg_read_size',
        'avg_write_size': 'avg_write_size',
        'avg_io_size': 'avg_io_size',
        'read_iops': 'read_iops',
        'write_iops': 'write_iops',
        'total_iops': 'total_iops',
        'read_bandwidth': 'read_bandwidth',
        'write_bandwidth': 'write_bandwidth',
        'total_bandwidth': 'total_bandwidth',
        'unaligned_read_iops': 'unaligned_read_iops',
        'unaligned_write_iops': 'unaligned_write_iops',
        'unaligned_iops': 'unaligned_iops',
        'unaligned_read_bandwidth': 'unaligned_read_bandwidth',
        'unaligned_write_bandwidth': 'unaligned_write_bandwidth',
        'unaligned_bandwidth': 'unaligned_bandwidth',
        'current_logins': 'current_logins',
        'dumped_frames_ps': 'dumped_frames_ps',
        'loss_of_signal_count_ps': 'loss_of_signal_count_ps',
        'loss_of_sync_count_ps': 'loss_of_sync_count_ps',
        'invalid_crc_count_ps': 'invalid_crc_count_ps',
        'invalid_tx_word_count_ps': 'invalid_tx_word_count_ps',
        'prim_seq_prot_err_count_ps': 'prim_seq_prot_err_count_ps',
        'link_failure_count_ps': 'link_failure_count_ps',
        'repeat_count': 'repeat_count'
    }

    def __init__(self, node_id=None, timestamp=None, avg_read_latency=None, avg_write_latency=None, avg_latency=None, avg_read_size=None, avg_write_size=None, avg_io_size=None, read_iops=None, write_iops=None, total_iops=None, read_bandwidth=None, write_bandwidth=None, total_bandwidth=None, unaligned_read_iops=None, unaligned_write_iops=None, unaligned_iops=None, unaligned_read_bandwidth=None, unaligned_write_bandwidth=None, unaligned_bandwidth=None, current_logins=None, dumped_frames_ps=None, loss_of_signal_count_ps=None, loss_of_sync_count_ps=None, invalid_crc_count_ps=None, invalid_tx_word_count_ps=None, prim_seq_prot_err_count_ps=None, link_failure_count_ps=None, repeat_count=None, _configuration=None):  # noqa: E501
        """PerformanceMetricsByFeFcNode - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._node_id = None
        self._timestamp = None
        self._avg_read_latency = None
        self._avg_write_latency = None
        self._avg_latency = None
        self._avg_read_size = None
        self._avg_write_size = None
        self._avg_io_size = None
        self._read_iops = None
        self._write_iops = None
        self._total_iops = None
        self._read_bandwidth = None
        self._write_bandwidth = None
        self._total_bandwidth = None
        self._unaligned_read_iops = None
        self._unaligned_write_iops = None
        self._unaligned_iops = None
        self._unaligned_read_bandwidth = None
        self._unaligned_write_bandwidth = None
        self._unaligned_bandwidth = None
        self._current_logins = None
        self._dumped_frames_ps = None
        self._loss_of_signal_count_ps = None
        self._loss_of_sync_count_ps = None
        self._invalid_crc_count_ps = None
        self._invalid_tx_word_count_ps = None
        self._prim_seq_prot_err_count_ps = None
        self._link_failure_count_ps = None
        self._repeat_count = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if timestamp is not None:
            self.timestamp = timestamp
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
        if read_iops is not None:
            self.read_iops = read_iops
        if write_iops is not None:
            self.write_iops = write_iops
        if total_iops is not None:
            self.total_iops = total_iops
        if read_bandwidth is not None:
            self.read_bandwidth = read_bandwidth
        if write_bandwidth is not None:
            self.write_bandwidth = write_bandwidth
        if total_bandwidth is not None:
            self.total_bandwidth = total_bandwidth
        if unaligned_read_iops is not None:
            self.unaligned_read_iops = unaligned_read_iops
        if unaligned_write_iops is not None:
            self.unaligned_write_iops = unaligned_write_iops
        if unaligned_iops is not None:
            self.unaligned_iops = unaligned_iops
        if unaligned_read_bandwidth is not None:
            self.unaligned_read_bandwidth = unaligned_read_bandwidth
        if unaligned_write_bandwidth is not None:
            self.unaligned_write_bandwidth = unaligned_write_bandwidth
        if unaligned_bandwidth is not None:
            self.unaligned_bandwidth = unaligned_bandwidth
        if current_logins is not None:
            self.current_logins = current_logins
        if dumped_frames_ps is not None:
            self.dumped_frames_ps = dumped_frames_ps
        if loss_of_signal_count_ps is not None:
            self.loss_of_signal_count_ps = loss_of_signal_count_ps
        if loss_of_sync_count_ps is not None:
            self.loss_of_sync_count_ps = loss_of_sync_count_ps
        if invalid_crc_count_ps is not None:
            self.invalid_crc_count_ps = invalid_crc_count_ps
        if invalid_tx_word_count_ps is not None:
            self.invalid_tx_word_count_ps = invalid_tx_word_count_ps
        if prim_seq_prot_err_count_ps is not None:
            self.prim_seq_prot_err_count_ps = prim_seq_prot_err_count_ps
        if link_failure_count_ps is not None:
            self.link_failure_count_ps = link_failure_count_ps
        if repeat_count is not None:
            self.repeat_count = repeat_count

    @property
    def node_id(self):
        """Gets the node_id of this PerformanceMetricsByFeFcNode.  # noqa: E501

        Reference to the associated node on which these metrics were recorded.  # noqa: E501

        :return: The node_id of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this PerformanceMetricsByFeFcNode.

        Reference to the associated node on which these metrics were recorded.  # noqa: E501

        :param node_id: The node_id of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def timestamp(self):
        """Gets the timestamp of this PerformanceMetricsByFeFcNode.  # noqa: E501

        End of sample period.  # noqa: E501

        :return: The timestamp of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this PerformanceMetricsByFeFcNode.

        End of sample period.  # noqa: E501

        :param timestamp: The timestamp of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def avg_read_latency(self):
        """Gets the avg_read_latency of this PerformanceMetricsByFeFcNode.  # noqa: E501

        Average read latency in microseconds.  # noqa: E501

        :return: The avg_read_latency of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: float
        """
        return self._avg_read_latency

    @avg_read_latency.setter
    def avg_read_latency(self, avg_read_latency):
        """Sets the avg_read_latency of this PerformanceMetricsByFeFcNode.

        Average read latency in microseconds.  # noqa: E501

        :param avg_read_latency: The avg_read_latency of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: float
        """

        self._avg_read_latency = avg_read_latency

    @property
    def avg_write_latency(self):
        """Gets the avg_write_latency of this PerformanceMetricsByFeFcNode.  # noqa: E501

        Average write latency in microseconds.  # noqa: E501

        :return: The avg_write_latency of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: float
        """
        return self._avg_write_latency

    @avg_write_latency.setter
    def avg_write_latency(self, avg_write_latency):
        """Sets the avg_write_latency of this PerformanceMetricsByFeFcNode.

        Average write latency in microseconds.  # noqa: E501

        :param avg_write_latency: The avg_write_latency of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: float
        """

        self._avg_write_latency = avg_write_latency

    @property
    def avg_latency(self):
        """Gets the avg_latency of this PerformanceMetricsByFeFcNode.  # noqa: E501

        Average read and write latency in microseconds.  # noqa: E501

        :return: The avg_latency of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: float
        """
        return self._avg_latency

    @avg_latency.setter
    def avg_latency(self, avg_latency):
        """Sets the avg_latency of this PerformanceMetricsByFeFcNode.

        Average read and write latency in microseconds.  # noqa: E501

        :param avg_latency: The avg_latency of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: float
        """

        self._avg_latency = avg_latency

    @property
    def avg_read_size(self):
        """Gets the avg_read_size of this PerformanceMetricsByFeFcNode.  # noqa: E501

        Average read size in bytes.  # noqa: E501

        :return: The avg_read_size of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: float
        """
        return self._avg_read_size

    @avg_read_size.setter
    def avg_read_size(self, avg_read_size):
        """Sets the avg_read_size of this PerformanceMetricsByFeFcNode.

        Average read size in bytes.  # noqa: E501

        :param avg_read_size: The avg_read_size of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: float
        """

        self._avg_read_size = avg_read_size

    @property
    def avg_write_size(self):
        """Gets the avg_write_size of this PerformanceMetricsByFeFcNode.  # noqa: E501

        Average write size in bytes.  # noqa: E501

        :return: The avg_write_size of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: float
        """
        return self._avg_write_size

    @avg_write_size.setter
    def avg_write_size(self, avg_write_size):
        """Sets the avg_write_size of this PerformanceMetricsByFeFcNode.

        Average write size in bytes.  # noqa: E501

        :param avg_write_size: The avg_write_size of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: float
        """

        self._avg_write_size = avg_write_size

    @property
    def avg_io_size(self):
        """Gets the avg_io_size of this PerformanceMetricsByFeFcNode.  # noqa: E501

        Average size of read and write operations in bytes.  # noqa: E501

        :return: The avg_io_size of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: float
        """
        return self._avg_io_size

    @avg_io_size.setter
    def avg_io_size(self, avg_io_size):
        """Sets the avg_io_size of this PerformanceMetricsByFeFcNode.

        Average size of read and write operations in bytes.  # noqa: E501

        :param avg_io_size: The avg_io_size of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: float
        """

        self._avg_io_size = avg_io_size

    @property
    def read_iops(self):
        """Gets the read_iops of this PerformanceMetricsByFeFcNode.  # noqa: E501

        Total number of read operations by the node.  # noqa: E501

        :return: The read_iops of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: float
        """
        return self._read_iops

    @read_iops.setter
    def read_iops(self, read_iops):
        """Sets the read_iops of this PerformanceMetricsByFeFcNode.

        Total number of read operations by the node.  # noqa: E501

        :param read_iops: The read_iops of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: float
        """

        self._read_iops = read_iops

    @property
    def write_iops(self):
        """Gets the write_iops of this PerformanceMetricsByFeFcNode.  # noqa: E501

        Total write operations per second.  # noqa: E501

        :return: The write_iops of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: float
        """
        return self._write_iops

    @write_iops.setter
    def write_iops(self, write_iops):
        """Sets the write_iops of this PerformanceMetricsByFeFcNode.

        Total write operations per second.  # noqa: E501

        :param write_iops: The write_iops of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: float
        """

        self._write_iops = write_iops

    @property
    def total_iops(self):
        """Gets the total_iops of this PerformanceMetricsByFeFcNode.  # noqa: E501

        Total read and write operations per second.  # noqa: E501

        :return: The total_iops of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: float
        """
        return self._total_iops

    @total_iops.setter
    def total_iops(self, total_iops):
        """Sets the total_iops of this PerformanceMetricsByFeFcNode.

        Total read and write operations per second.  # noqa: E501

        :param total_iops: The total_iops of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: float
        """

        self._total_iops = total_iops

    @property
    def read_bandwidth(self):
        """Gets the read_bandwidth of this PerformanceMetricsByFeFcNode.  # noqa: E501

        Read rate in bytes per second.  # noqa: E501

        :return: The read_bandwidth of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: float
        """
        return self._read_bandwidth

    @read_bandwidth.setter
    def read_bandwidth(self, read_bandwidth):
        """Sets the read_bandwidth of this PerformanceMetricsByFeFcNode.

        Read rate in bytes per second.  # noqa: E501

        :param read_bandwidth: The read_bandwidth of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: float
        """

        self._read_bandwidth = read_bandwidth

    @property
    def write_bandwidth(self):
        """Gets the write_bandwidth of this PerformanceMetricsByFeFcNode.  # noqa: E501

        Write rate in byte/sec.  # noqa: E501

        :return: The write_bandwidth of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: float
        """
        return self._write_bandwidth

    @write_bandwidth.setter
    def write_bandwidth(self, write_bandwidth):
        """Sets the write_bandwidth of this PerformanceMetricsByFeFcNode.

        Write rate in byte/sec.  # noqa: E501

        :param write_bandwidth: The write_bandwidth of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: float
        """

        self._write_bandwidth = write_bandwidth

    @property
    def total_bandwidth(self):
        """Gets the total_bandwidth of this PerformanceMetricsByFeFcNode.  # noqa: E501

        Total data transfer rate in bytes per second.  # noqa: E501

        :return: The total_bandwidth of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: float
        """
        return self._total_bandwidth

    @total_bandwidth.setter
    def total_bandwidth(self, total_bandwidth):
        """Sets the total_bandwidth of this PerformanceMetricsByFeFcNode.

        Total data transfer rate in bytes per second.  # noqa: E501

        :param total_bandwidth: The total_bandwidth of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: float
        """

        self._total_bandwidth = total_bandwidth

    @property
    def unaligned_read_iops(self):
        """Gets the unaligned_read_iops of this PerformanceMetricsByFeFcNode.  # noqa: E501

        Unaligned read input/output per second. Was deprecated in version 2.1.0.0.  # noqa: E501

        :return: The unaligned_read_iops of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: float
        """
        return self._unaligned_read_iops

    @unaligned_read_iops.setter
    def unaligned_read_iops(self, unaligned_read_iops):
        """Sets the unaligned_read_iops of this PerformanceMetricsByFeFcNode.

        Unaligned read input/output per second. Was deprecated in version 2.1.0.0.  # noqa: E501

        :param unaligned_read_iops: The unaligned_read_iops of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: float
        """

        self._unaligned_read_iops = unaligned_read_iops

    @property
    def unaligned_write_iops(self):
        """Gets the unaligned_write_iops of this PerformanceMetricsByFeFcNode.  # noqa: E501

        Unaligned write input/output per second. Was deprecated in version 2.1.0.0.  # noqa: E501

        :return: The unaligned_write_iops of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: float
        """
        return self._unaligned_write_iops

    @unaligned_write_iops.setter
    def unaligned_write_iops(self, unaligned_write_iops):
        """Sets the unaligned_write_iops of this PerformanceMetricsByFeFcNode.

        Unaligned write input/output per second. Was deprecated in version 2.1.0.0.  # noqa: E501

        :param unaligned_write_iops: The unaligned_write_iops of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: float
        """

        self._unaligned_write_iops = unaligned_write_iops

    @property
    def unaligned_iops(self):
        """Gets the unaligned_iops of this PerformanceMetricsByFeFcNode.  # noqa: E501

        Unaligned total input/output per second. Was deprecated in version 2.1.0.0.  # noqa: E501

        :return: The unaligned_iops of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: float
        """
        return self._unaligned_iops

    @unaligned_iops.setter
    def unaligned_iops(self, unaligned_iops):
        """Sets the unaligned_iops of this PerformanceMetricsByFeFcNode.

        Unaligned total input/output per second. Was deprecated in version 2.1.0.0.  # noqa: E501

        :param unaligned_iops: The unaligned_iops of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: float
        """

        self._unaligned_iops = unaligned_iops

    @property
    def unaligned_read_bandwidth(self):
        """Gets the unaligned_read_bandwidth of this PerformanceMetricsByFeFcNode.  # noqa: E501

        Unaligned read rate in bytes per second. Was deprecated in version 2.1.0.0.  # noqa: E501

        :return: The unaligned_read_bandwidth of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: float
        """
        return self._unaligned_read_bandwidth

    @unaligned_read_bandwidth.setter
    def unaligned_read_bandwidth(self, unaligned_read_bandwidth):
        """Sets the unaligned_read_bandwidth of this PerformanceMetricsByFeFcNode.

        Unaligned read rate in bytes per second. Was deprecated in version 2.1.0.0.  # noqa: E501

        :param unaligned_read_bandwidth: The unaligned_read_bandwidth of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: float
        """

        self._unaligned_read_bandwidth = unaligned_read_bandwidth

    @property
    def unaligned_write_bandwidth(self):
        """Gets the unaligned_write_bandwidth of this PerformanceMetricsByFeFcNode.  # noqa: E501

        Unaligned write rate in bytes per second. Was deprecated in version 2.1.0.0.  # noqa: E501

        :return: The unaligned_write_bandwidth of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: float
        """
        return self._unaligned_write_bandwidth

    @unaligned_write_bandwidth.setter
    def unaligned_write_bandwidth(self, unaligned_write_bandwidth):
        """Sets the unaligned_write_bandwidth of this PerformanceMetricsByFeFcNode.

        Unaligned write rate in bytes per second. Was deprecated in version 2.1.0.0.  # noqa: E501

        :param unaligned_write_bandwidth: The unaligned_write_bandwidth of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: float
        """

        self._unaligned_write_bandwidth = unaligned_write_bandwidth

    @property
    def unaligned_bandwidth(self):
        """Gets the unaligned_bandwidth of this PerformanceMetricsByFeFcNode.  # noqa: E501

        Unaligned read/write rate in bytes per second. Was deprecated in version 2.1.0.0.  # noqa: E501

        :return: The unaligned_bandwidth of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: float
        """
        return self._unaligned_bandwidth

    @unaligned_bandwidth.setter
    def unaligned_bandwidth(self, unaligned_bandwidth):
        """Sets the unaligned_bandwidth of this PerformanceMetricsByFeFcNode.

        Unaligned read/write rate in bytes per second. Was deprecated in version 2.1.0.0.  # noqa: E501

        :param unaligned_bandwidth: The unaligned_bandwidth of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: float
        """

        self._unaligned_bandwidth = unaligned_bandwidth

    @property
    def current_logins(self):
        """Gets the current_logins of this PerformanceMetricsByFeFcNode.  # noqa: E501

        The number of logins to the target from initiators.  # noqa: E501

        :return: The current_logins of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: int
        """
        return self._current_logins

    @current_logins.setter
    def current_logins(self, current_logins):
        """Sets the current_logins of this PerformanceMetricsByFeFcNode.

        The number of logins to the target from initiators.  # noqa: E501

        :param current_logins: The current_logins of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                current_logins is not None and current_logins > -9223372036854775616):  # noqa: E501
            raise ValueError("Invalid value for `current_logins`, must be a value less than or equal to `-9223372036854775616`")  # noqa: E501
        if (self._configuration.client_side_validation and
                current_logins is not None and current_logins < 0):  # noqa: E501
            raise ValueError("Invalid value for `current_logins`, must be a value greater than or equal to `0`")  # noqa: E501

        self._current_logins = current_logins

    @property
    def dumped_frames_ps(self):
        """Gets the dumped_frames_ps of this PerformanceMetricsByFeFcNode.  # noqa: E501

        Dumped frames per second.  # noqa: E501

        :return: The dumped_frames_ps of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: float
        """
        return self._dumped_frames_ps

    @dumped_frames_ps.setter
    def dumped_frames_ps(self, dumped_frames_ps):
        """Sets the dumped_frames_ps of this PerformanceMetricsByFeFcNode.

        Dumped frames per second.  # noqa: E501

        :param dumped_frames_ps: The dumped_frames_ps of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: float
        """

        self._dumped_frames_ps = dumped_frames_ps

    @property
    def loss_of_signal_count_ps(self):
        """Gets the loss_of_signal_count_ps of this PerformanceMetricsByFeFcNode.  # noqa: E501

        Loss of signal count per second.  # noqa: E501

        :return: The loss_of_signal_count_ps of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: float
        """
        return self._loss_of_signal_count_ps

    @loss_of_signal_count_ps.setter
    def loss_of_signal_count_ps(self, loss_of_signal_count_ps):
        """Sets the loss_of_signal_count_ps of this PerformanceMetricsByFeFcNode.

        Loss of signal count per second.  # noqa: E501

        :param loss_of_signal_count_ps: The loss_of_signal_count_ps of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: float
        """

        self._loss_of_signal_count_ps = loss_of_signal_count_ps

    @property
    def loss_of_sync_count_ps(self):
        """Gets the loss_of_sync_count_ps of this PerformanceMetricsByFeFcNode.  # noqa: E501

        Loss of sync count per second.  # noqa: E501

        :return: The loss_of_sync_count_ps of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: float
        """
        return self._loss_of_sync_count_ps

    @loss_of_sync_count_ps.setter
    def loss_of_sync_count_ps(self, loss_of_sync_count_ps):
        """Sets the loss_of_sync_count_ps of this PerformanceMetricsByFeFcNode.

        Loss of sync count per second.  # noqa: E501

        :param loss_of_sync_count_ps: The loss_of_sync_count_ps of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: float
        """

        self._loss_of_sync_count_ps = loss_of_sync_count_ps

    @property
    def invalid_crc_count_ps(self):
        """Gets the invalid_crc_count_ps of this PerformanceMetricsByFeFcNode.  # noqa: E501

        Invalid crc count per second.  # noqa: E501

        :return: The invalid_crc_count_ps of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: float
        """
        return self._invalid_crc_count_ps

    @invalid_crc_count_ps.setter
    def invalid_crc_count_ps(self, invalid_crc_count_ps):
        """Sets the invalid_crc_count_ps of this PerformanceMetricsByFeFcNode.

        Invalid crc count per second.  # noqa: E501

        :param invalid_crc_count_ps: The invalid_crc_count_ps of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: float
        """

        self._invalid_crc_count_ps = invalid_crc_count_ps

    @property
    def invalid_tx_word_count_ps(self):
        """Gets the invalid_tx_word_count_ps of this PerformanceMetricsByFeFcNode.  # noqa: E501

        Invalid transmission word count per second.  # noqa: E501

        :return: The invalid_tx_word_count_ps of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: float
        """
        return self._invalid_tx_word_count_ps

    @invalid_tx_word_count_ps.setter
    def invalid_tx_word_count_ps(self, invalid_tx_word_count_ps):
        """Sets the invalid_tx_word_count_ps of this PerformanceMetricsByFeFcNode.

        Invalid transmission word count per second.  # noqa: E501

        :param invalid_tx_word_count_ps: The invalid_tx_word_count_ps of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: float
        """

        self._invalid_tx_word_count_ps = invalid_tx_word_count_ps

    @property
    def prim_seq_prot_err_count_ps(self):
        """Gets the prim_seq_prot_err_count_ps of this PerformanceMetricsByFeFcNode.  # noqa: E501

        Primitive sequence protocol error count per second.  # noqa: E501

        :return: The prim_seq_prot_err_count_ps of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: float
        """
        return self._prim_seq_prot_err_count_ps

    @prim_seq_prot_err_count_ps.setter
    def prim_seq_prot_err_count_ps(self, prim_seq_prot_err_count_ps):
        """Sets the prim_seq_prot_err_count_ps of this PerformanceMetricsByFeFcNode.

        Primitive sequence protocol error count per second.  # noqa: E501

        :param prim_seq_prot_err_count_ps: The prim_seq_prot_err_count_ps of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: float
        """

        self._prim_seq_prot_err_count_ps = prim_seq_prot_err_count_ps

    @property
    def link_failure_count_ps(self):
        """Gets the link_failure_count_ps of this PerformanceMetricsByFeFcNode.  # noqa: E501

        Link failure count per second.  # noqa: E501

        :return: The link_failure_count_ps of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: float
        """
        return self._link_failure_count_ps

    @link_failure_count_ps.setter
    def link_failure_count_ps(self, link_failure_count_ps):
        """Sets the link_failure_count_ps of this PerformanceMetricsByFeFcNode.

        Link failure count per second.  # noqa: E501

        :param link_failure_count_ps: The link_failure_count_ps of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :type: float
        """

        self._link_failure_count_ps = link_failure_count_ps

    @property
    def repeat_count(self):
        """Gets the repeat_count of this PerformanceMetricsByFeFcNode.  # noqa: E501

        Number of times the metrics are repeated.  # noqa: E501

        :return: The repeat_count of this PerformanceMetricsByFeFcNode.  # noqa: E501
        :rtype: int
        """
        return self._repeat_count

    @repeat_count.setter
    def repeat_count(self, repeat_count):
        """Sets the repeat_count of this PerformanceMetricsByFeFcNode.

        Number of times the metrics are repeated.  # noqa: E501

        :param repeat_count: The repeat_count of this PerformanceMetricsByFeFcNode.  # noqa: E501
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
        if issubclass(PerformanceMetricsByFeFcNode, dict):
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
        if not isinstance(other, PerformanceMetricsByFeFcNode):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PerformanceMetricsByFeFcNode):
            return True

        return self.to_dict() != other.to_dict()
