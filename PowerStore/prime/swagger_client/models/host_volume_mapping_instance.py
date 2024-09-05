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


class HostVolumeMappingInstance(object):
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
        'host_id': 'str',
        'host_group_id': 'str',
        'volume_id': 'str',
        'logical_unit_number': 'int',
        'host': 'HostInstance',
        'host_group': 'HostGroupInstance',
        'volume': 'VolumeInstance'
    }

    attribute_map = {
        'id': 'id',
        'host_id': 'host_id',
        'host_group_id': 'host_group_id',
        'volume_id': 'volume_id',
        'logical_unit_number': 'logical_unit_number',
        'host': 'host',
        'host_group': 'host_group',
        'volume': 'volume'
    }

    def __init__(self, id=None, host_id=None, host_group_id=None, volume_id=None, logical_unit_number=None, host=None, host_group=None, volume=None, _configuration=None):  # noqa: E501
        """HostVolumeMappingInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._host_id = None
        self._host_group_id = None
        self._volume_id = None
        self._logical_unit_number = None
        self._host = None
        self._host_group = None
        self._volume = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if host_id is not None:
            self.host_id = host_id
        if host_group_id is not None:
            self.host_group_id = host_group_id
        if volume_id is not None:
            self.volume_id = volume_id
        if logical_unit_number is not None:
            self.logical_unit_number = logical_unit_number
        if host is not None:
            self.host = host
        if host_group is not None:
            self.host_group = host_group
        if volume is not None:
            self.volume = volume

    @property
    def id(self):
        """Gets the id of this HostVolumeMappingInstance.  # noqa: E501

        Unique identifier of a mapping between a host and a volume.  # noqa: E501

        :return: The id of this HostVolumeMappingInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HostVolumeMappingInstance.

        Unique identifier of a mapping between a host and a volume.  # noqa: E501

        :param id: The id of this HostVolumeMappingInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def host_id(self):
        """Gets the host_id of this HostVolumeMappingInstance.  # noqa: E501

        Unique identifier of a host attached to a volume. The host_id and host_group_id cannot both be set.  # noqa: E501

        :return: The host_id of this HostVolumeMappingInstance.  # noqa: E501
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this HostVolumeMappingInstance.

        Unique identifier of a host attached to a volume. The host_id and host_group_id cannot both be set.  # noqa: E501

        :param host_id: The host_id of this HostVolumeMappingInstance.  # noqa: E501
        :type: str
        """

        self._host_id = host_id

    @property
    def host_group_id(self):
        """Gets the host_group_id of this HostVolumeMappingInstance.  # noqa: E501

        Unique identifier of a host group attached to a volume. The host_id and host_group_id cannot both be set.  # noqa: E501

        :return: The host_group_id of this HostVolumeMappingInstance.  # noqa: E501
        :rtype: str
        """
        return self._host_group_id

    @host_group_id.setter
    def host_group_id(self, host_group_id):
        """Sets the host_group_id of this HostVolumeMappingInstance.

        Unique identifier of a host group attached to a volume. The host_id and host_group_id cannot both be set.  # noqa: E501

        :param host_group_id: The host_group_id of this HostVolumeMappingInstance.  # noqa: E501
        :type: str
        """

        self._host_group_id = host_group_id

    @property
    def volume_id(self):
        """Gets the volume_id of this HostVolumeMappingInstance.  # noqa: E501

        Unique identifier of the volume to which the host is attached.  # noqa: E501

        :return: The volume_id of this HostVolumeMappingInstance.  # noqa: E501
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this HostVolumeMappingInstance.

        Unique identifier of the volume to which the host is attached.  # noqa: E501

        :param volume_id: The volume_id of this HostVolumeMappingInstance.  # noqa: E501
        :type: str
        """

        self._volume_id = volume_id

    @property
    def logical_unit_number(self):
        """Gets the logical_unit_number of this HostVolumeMappingInstance.  # noqa: E501

        Logical unit number for the host volume access.  # noqa: E501

        :return: The logical_unit_number of this HostVolumeMappingInstance.  # noqa: E501
        :rtype: int
        """
        return self._logical_unit_number

    @logical_unit_number.setter
    def logical_unit_number(self, logical_unit_number):
        """Sets the logical_unit_number of this HostVolumeMappingInstance.

        Logical unit number for the host volume access.  # noqa: E501

        :param logical_unit_number: The logical_unit_number of this HostVolumeMappingInstance.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                logical_unit_number is not None and logical_unit_number > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `logical_unit_number`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self._configuration.client_side_validation and
                logical_unit_number is not None and logical_unit_number < 0):  # noqa: E501
            raise ValueError("Invalid value for `logical_unit_number`, must be a value greater than or equal to `0`")  # noqa: E501

        self._logical_unit_number = logical_unit_number

    @property
    def host(self):
        """Gets the host of this HostVolumeMappingInstance.  # noqa: E501

        This is the embeddable reference form of host_id attribute.  # noqa: E501

        :return: The host of this HostVolumeMappingInstance.  # noqa: E501
        :rtype: HostInstance
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this HostVolumeMappingInstance.

        This is the embeddable reference form of host_id attribute.  # noqa: E501

        :param host: The host of this HostVolumeMappingInstance.  # noqa: E501
        :type: HostInstance
        """

        self._host = host

    @property
    def host_group(self):
        """Gets the host_group of this HostVolumeMappingInstance.  # noqa: E501

        This is the embeddable reference form of host_group_id attribute.  # noqa: E501

        :return: The host_group of this HostVolumeMappingInstance.  # noqa: E501
        :rtype: HostGroupInstance
        """
        return self._host_group

    @host_group.setter
    def host_group(self, host_group):
        """Sets the host_group of this HostVolumeMappingInstance.

        This is the embeddable reference form of host_group_id attribute.  # noqa: E501

        :param host_group: The host_group of this HostVolumeMappingInstance.  # noqa: E501
        :type: HostGroupInstance
        """

        self._host_group = host_group

    @property
    def volume(self):
        """Gets the volume of this HostVolumeMappingInstance.  # noqa: E501

        This is the embeddable reference form of volume_id attribute.  # noqa: E501

        :return: The volume of this HostVolumeMappingInstance.  # noqa: E501
        :rtype: VolumeInstance
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this HostVolumeMappingInstance.

        This is the embeddable reference form of volume_id attribute.  # noqa: E501

        :param volume: The volume of this HostVolumeMappingInstance.  # noqa: E501
        :type: VolumeInstance
        """

        self._volume = volume

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
        if issubclass(HostVolumeMappingInstance, dict):
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
        if not isinstance(other, HostVolumeMappingInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HostVolumeMappingInstance):
            return True

        return self.to_dict() != other.to_dict()
