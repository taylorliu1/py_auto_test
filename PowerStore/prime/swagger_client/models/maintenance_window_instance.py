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


class MaintenanceWindowInstance(object):
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
        'id': 'str',
        'appliance_id': 'str',
        'is_enabled': 'bool',
        'end_time': 'datetime',
        'appliance': 'ApplianceInstance'
    }

    attribute_map = {
        'id': 'id',
        'appliance_id': 'appliance_id',
        'is_enabled': 'is_enabled',
        'end_time': 'end_time',
        'appliance': 'appliance'
    }

    def __init__(self, id=None, appliance_id=None, is_enabled=None, end_time=None, appliance=None, _configuration=None):  # noqa: E501
        """MaintenanceWindowInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._appliance_id = None
        self._is_enabled = None
        self._end_time = None
        self._appliance = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if appliance_id is not None:
            self.appliance_id = appliance_id
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if end_time is not None:
            self.end_time = end_time
        if appliance is not None:
            self.appliance = appliance

    @property
    def id(self):
        """Gets the id of this MaintenanceWindowInstance.  # noqa: E501

        Unique identifier of the maintenance window.  # noqa: E501

        :return: The id of this MaintenanceWindowInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MaintenanceWindowInstance.

        Unique identifier of the maintenance window.  # noqa: E501

        :param id: The id of this MaintenanceWindowInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def appliance_id(self):
        """Gets the appliance_id of this MaintenanceWindowInstance.  # noqa: E501

        Appliance id on which this maintenance window is configured.  # noqa: E501

        :return: The appliance_id of this MaintenanceWindowInstance.  # noqa: E501
        :rtype: str
        """
        return self._appliance_id

    @appliance_id.setter
    def appliance_id(self, appliance_id):
        """Sets the appliance_id of this MaintenanceWindowInstance.

        Appliance id on which this maintenance window is configured.  # noqa: E501

        :param appliance_id: The appliance_id of this MaintenanceWindowInstance.  # noqa: E501
        :type: str
        """

        self._appliance_id = appliance_id

    @property
    def is_enabled(self):
        """Gets the is_enabled of this MaintenanceWindowInstance.  # noqa: E501

        Whether the maintenance window is active.  # noqa: E501

        :return: The is_enabled of this MaintenanceWindowInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this MaintenanceWindowInstance.

        Whether the maintenance window is active.  # noqa: E501

        :param is_enabled: The is_enabled of this MaintenanceWindowInstance.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def end_time(self):
        """Gets the end_time of this MaintenanceWindowInstance.  # noqa: E501

        Time when the maintenance window will close (or did close).  # noqa: E501

        :return: The end_time of this MaintenanceWindowInstance.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this MaintenanceWindowInstance.

        Time when the maintenance window will close (or did close).  # noqa: E501

        :param end_time: The end_time of this MaintenanceWindowInstance.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def appliance(self):
        """Gets the appliance of this MaintenanceWindowInstance.  # noqa: E501

        This is the embeddable reference form of appliance_id attribute.  # noqa: E501

        :return: The appliance of this MaintenanceWindowInstance.  # noqa: E501
        :rtype: ApplianceInstance
        """
        return self._appliance

    @appliance.setter
    def appliance(self, appliance):
        """Sets the appliance of this MaintenanceWindowInstance.

        This is the embeddable reference form of appliance_id attribute.  # noqa: E501

        :param appliance: The appliance of this MaintenanceWindowInstance.  # noqa: E501
        :type: ApplianceInstance
        """

        self._appliance = appliance

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
        if issubclass(MaintenanceWindowInstance, dict):
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
        if not isinstance(other, MaintenanceWindowInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MaintenanceWindowInstance):
            return True

        return self.to_dict() != other.to_dict()
