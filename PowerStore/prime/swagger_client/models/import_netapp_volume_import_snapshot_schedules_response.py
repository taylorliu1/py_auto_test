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


class ImportNetappVolumeImportSnapshotSchedulesResponse(object):
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
        'snap_policy_name': 'str',
        'schedules': 'ImportNetappSnapshotScheduleInstance'
    }

    attribute_map = {
        'snap_policy_name': 'snap_policy_name',
        'schedules': 'schedules'
    }

    def __init__(self, snap_policy_name=None, schedules=None, _configuration=None):  # noqa: E501
        """ImportNetappVolumeImportSnapshotSchedulesResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._snap_policy_name = None
        self._schedules = None
        self.discriminator = None

        if snap_policy_name is not None:
            self.snap_policy_name = snap_policy_name
        if schedules is not None:
            self.schedules = schedules

    @property
    def snap_policy_name(self):
        """Gets the snap_policy_name of this ImportNetappVolumeImportSnapshotSchedulesResponse.  # noqa: E501

        Name of the NetApp snapshot policy.  # noqa: E501

        :return: The snap_policy_name of this ImportNetappVolumeImportSnapshotSchedulesResponse.  # noqa: E501
        :rtype: str
        """
        return self._snap_policy_name

    @snap_policy_name.setter
    def snap_policy_name(self, snap_policy_name):
        """Sets the snap_policy_name of this ImportNetappVolumeImportSnapshotSchedulesResponse.

        Name of the NetApp snapshot policy.  # noqa: E501

        :param snap_policy_name: The snap_policy_name of this ImportNetappVolumeImportSnapshotSchedulesResponse.  # noqa: E501
        :type: str
        """

        self._snap_policy_name = snap_policy_name

    @property
    def schedules(self):
        """Gets the schedules of this ImportNetappVolumeImportSnapshotSchedulesResponse.  # noqa: E501


        :return: The schedules of this ImportNetappVolumeImportSnapshotSchedulesResponse.  # noqa: E501
        :rtype: ImportNetappSnapshotScheduleInstance
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        """Sets the schedules of this ImportNetappVolumeImportSnapshotSchedulesResponse.


        :param schedules: The schedules of this ImportNetappVolumeImportSnapshotSchedulesResponse.  # noqa: E501
        :type: ImportNetappSnapshotScheduleInstance
        """

        self._schedules = schedules

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
        if issubclass(ImportNetappVolumeImportSnapshotSchedulesResponse, dict):
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
        if not isinstance(other, ImportNetappVolumeImportSnapshotSchedulesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImportNetappVolumeImportSnapshotSchedulesResponse):
            return True

        return self.to_dict() != other.to_dict()
