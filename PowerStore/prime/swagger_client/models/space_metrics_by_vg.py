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


class SpaceMetricsByVg(object):
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
        'vg_id': 'str',
        'timestamp': 'datetime',
        'logical_provisioned': 'int',
        'logical_used': 'int',
        'snap_clone_logical_used': 'int',
        'thin_savings': 'float',
        'snapshot_savings': 'float',
        'repeat_count': 'int'
    }

    attribute_map = {
        'vg_id': 'vg_id',
        'timestamp': 'timestamp',
        'logical_provisioned': 'logical_provisioned',
        'logical_used': 'logical_used',
        'snap_clone_logical_used': 'snap_clone_logical_used',
        'thin_savings': 'thin_savings',
        'snapshot_savings': 'snapshot_savings',
        'repeat_count': 'repeat_count'
    }

    def __init__(self, vg_id=None, timestamp=None, logical_provisioned=None, logical_used=None, snap_clone_logical_used=None, thin_savings=None, snapshot_savings=None, repeat_count=None, _configuration=None):  # noqa: E501
        """SpaceMetricsByVg - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._vg_id = None
        self._timestamp = None
        self._logical_provisioned = None
        self._logical_used = None
        self._snap_clone_logical_used = None
        self._thin_savings = None
        self._snapshot_savings = None
        self._repeat_count = None
        self.discriminator = None

        if vg_id is not None:
            self.vg_id = vg_id
        if timestamp is not None:
            self.timestamp = timestamp
        if logical_provisioned is not None:
            self.logical_provisioned = logical_provisioned
        if logical_used is not None:
            self.logical_used = logical_used
        if snap_clone_logical_used is not None:
            self.snap_clone_logical_used = snap_clone_logical_used
        if thin_savings is not None:
            self.thin_savings = thin_savings
        if snapshot_savings is not None:
            self.snapshot_savings = snapshot_savings
        if repeat_count is not None:
            self.repeat_count = repeat_count

    @property
    def vg_id(self):
        """Gets the vg_id of this SpaceMetricsByVg.  # noqa: E501

        Unique identifier representing a volume group.  # noqa: E501

        :return: The vg_id of this SpaceMetricsByVg.  # noqa: E501
        :rtype: str
        """
        return self._vg_id

    @vg_id.setter
    def vg_id(self, vg_id):
        """Sets the vg_id of this SpaceMetricsByVg.

        Unique identifier representing a volume group.  # noqa: E501

        :param vg_id: The vg_id of this SpaceMetricsByVg.  # noqa: E501
        :type: str
        """

        self._vg_id = vg_id

    @property
    def timestamp(self):
        """Gets the timestamp of this SpaceMetricsByVg.  # noqa: E501

        End of sample period.  # noqa: E501

        :return: The timestamp of this SpaceMetricsByVg.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this SpaceMetricsByVg.

        End of sample period.  # noqa: E501

        :param timestamp: The timestamp of this SpaceMetricsByVg.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def logical_provisioned(self):
        """Gets the logical_provisioned of this SpaceMetricsByVg.  # noqa: E501

        Total configured size in bytes of all member volumes in a volume group.  # noqa: E501

        :return: The logical_provisioned of this SpaceMetricsByVg.  # noqa: E501
        :rtype: int
        """
        return self._logical_provisioned

    @logical_provisioned.setter
    def logical_provisioned(self, logical_provisioned):
        """Sets the logical_provisioned of this SpaceMetricsByVg.

        Total configured size in bytes of all member volumes in a volume group.  # noqa: E501

        :param logical_provisioned: The logical_provisioned of this SpaceMetricsByVg.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                logical_provisioned is not None and logical_provisioned > -9223372036854775616):  # noqa: E501
            raise ValueError("Invalid value for `logical_provisioned`, must be a value less than or equal to `-9223372036854775616`")  # noqa: E501
        if (self._configuration.client_side_validation and
                logical_provisioned is not None and logical_provisioned < 0):  # noqa: E501
            raise ValueError("Invalid value for `logical_provisioned`, must be a value greater than or equal to `0`")  # noqa: E501

        self._logical_provisioned = logical_provisioned

    @property
    def logical_used(self):
        """Gets the logical_used of this SpaceMetricsByVg.  # noqa: E501

        Total amount of data in bytes written to all member volumes in a volume group.  # noqa: E501

        :return: The logical_used of this SpaceMetricsByVg.  # noqa: E501
        :rtype: int
        """
        return self._logical_used

    @logical_used.setter
    def logical_used(self, logical_used):
        """Sets the logical_used of this SpaceMetricsByVg.

        Total amount of data in bytes written to all member volumes in a volume group.  # noqa: E501

        :param logical_used: The logical_used of this SpaceMetricsByVg.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                logical_used is not None and logical_used > -9223372036854775616):  # noqa: E501
            raise ValueError("Invalid value for `logical_used`, must be a value less than or equal to `-9223372036854775616`")  # noqa: E501
        if (self._configuration.client_side_validation and
                logical_used is not None and logical_used < 0):  # noqa: E501
            raise ValueError("Invalid value for `logical_used`, must be a value greater than or equal to `0`")  # noqa: E501

        self._logical_used = logical_used

    @property
    def snap_clone_logical_used(self):
        """Gets the snap_clone_logical_used of this SpaceMetricsByVg.  # noqa: E501

        Total amount of data in bytes host has written to all volumes in the volume group without any deduplication, compression or sharing. This metric includes used snaps and clones in the volume group.  # noqa: E501

        :return: The snap_clone_logical_used of this SpaceMetricsByVg.  # noqa: E501
        :rtype: int
        """
        return self._snap_clone_logical_used

    @snap_clone_logical_used.setter
    def snap_clone_logical_used(self, snap_clone_logical_used):
        """Sets the snap_clone_logical_used of this SpaceMetricsByVg.

        Total amount of data in bytes host has written to all volumes in the volume group without any deduplication, compression or sharing. This metric includes used snaps and clones in the volume group.  # noqa: E501

        :param snap_clone_logical_used: The snap_clone_logical_used of this SpaceMetricsByVg.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                snap_clone_logical_used is not None and snap_clone_logical_used > -9223372036854775616):  # noqa: E501
            raise ValueError("Invalid value for `snap_clone_logical_used`, must be a value less than or equal to `-9223372036854775616`")  # noqa: E501
        if (self._configuration.client_side_validation and
                snap_clone_logical_used is not None and snap_clone_logical_used < 0):  # noqa: E501
            raise ValueError("Invalid value for `snap_clone_logical_used`, must be a value greater than or equal to `0`")  # noqa: E501

        self._snap_clone_logical_used = snap_clone_logical_used

    @property
    def thin_savings(self):
        """Gets the thin_savings of this SpaceMetricsByVg.  # noqa: E501

        Ratio of all the volumes provisioned to data being written to them. For example, a volume group has two 2 GB volumes and have written 500 MB of data to them. The thin savings would be (2 * 2 GB) / (2 * 0.5 GB) or 4:1, so the thin_savings value would be 4.0.  # noqa: E501

        :return: The thin_savings of this SpaceMetricsByVg.  # noqa: E501
        :rtype: float
        """
        return self._thin_savings

    @thin_savings.setter
    def thin_savings(self, thin_savings):
        """Sets the thin_savings of this SpaceMetricsByVg.

        Ratio of all the volumes provisioned to data being written to them. For example, a volume group has two 2 GB volumes and have written 500 MB of data to them. The thin savings would be (2 * 2 GB) / (2 * 0.5 GB) or 4:1, so the thin_savings value would be 4.0.  # noqa: E501

        :param thin_savings: The thin_savings of this SpaceMetricsByVg.  # noqa: E501
        :type: float
        """

        self._thin_savings = thin_savings

    @property
    def snapshot_savings(self):
        """Gets the snapshot_savings of this SpaceMetricsByVg.  # noqa: E501

        Ratio of the amount of space that would have been used by snapshots in the volume group if space efficiency was not applied to logical space used solely by snapshots. For example, two volumes are provisioned as 1 GB and each has two snapshots. Each snapshot has 200 MB of data. Snapshot savings will be (1 GB * 2 + 1 GB * 2) / (0.2 GB * 2 + 0.2 GB * 2) or 5:1. The snapshot_savings value will be 5 in this case.  # noqa: E501

        :return: The snapshot_savings of this SpaceMetricsByVg.  # noqa: E501
        :rtype: float
        """
        return self._snapshot_savings

    @snapshot_savings.setter
    def snapshot_savings(self, snapshot_savings):
        """Sets the snapshot_savings of this SpaceMetricsByVg.

        Ratio of the amount of space that would have been used by snapshots in the volume group if space efficiency was not applied to logical space used solely by snapshots. For example, two volumes are provisioned as 1 GB and each has two snapshots. Each snapshot has 200 MB of data. Snapshot savings will be (1 GB * 2 + 1 GB * 2) / (0.2 GB * 2 + 0.2 GB * 2) or 5:1. The snapshot_savings value will be 5 in this case.  # noqa: E501

        :param snapshot_savings: The snapshot_savings of this SpaceMetricsByVg.  # noqa: E501
        :type: float
        """

        self._snapshot_savings = snapshot_savings

    @property
    def repeat_count(self):
        """Gets the repeat_count of this SpaceMetricsByVg.  # noqa: E501

        Number of times the metrics are repeated.  # noqa: E501

        :return: The repeat_count of this SpaceMetricsByVg.  # noqa: E501
        :rtype: int
        """
        return self._repeat_count

    @repeat_count.setter
    def repeat_count(self, repeat_count):
        """Sets the repeat_count of this SpaceMetricsByVg.

        Number of times the metrics are repeated.  # noqa: E501

        :param repeat_count: The repeat_count of this SpaceMetricsByVg.  # noqa: E501
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
        if issubclass(SpaceMetricsByVg, dict):
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
        if not isinstance(other, SpaceMetricsByVg):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SpaceMetricsByVg):
            return True

        return self.to_dict() != other.to_dict()
