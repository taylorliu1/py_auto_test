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


class MigrationSessionInstance(object):
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
        'name': 'str',
        'resource_type': 'MigrationResourceTypeEnum',
        'source_appliance_id': 'str',
        'family_id': 'str',
        'destination_appliance_id': 'str',
        'state': 'MigrationSessionStateEnum',
        'created_timestamp': 'datetime',
        'last_sync_timestamp': 'datetime',
        'current_transfer_rate': 'int',
        'progress_percentage': 'int',
        'estimated_completion_timestamp': 'datetime',
        'resource_type_l10n': 'str',
        'state_l10n': 'str',
        'virtual_volumes': 'list[VirtualVolumeInstance]',
        'volumes': 'list[VolumeInstance]',
        'volume_groups': 'list[VolumeGroupInstance]',
        'replication_sessions': 'list[ReplicationSessionInstance]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'resource_type': 'resource_type',
        'source_appliance_id': 'source_appliance_id',
        'family_id': 'family_id',
        'destination_appliance_id': 'destination_appliance_id',
        'state': 'state',
        'created_timestamp': 'created_timestamp',
        'last_sync_timestamp': 'last_sync_timestamp',
        'current_transfer_rate': 'current_transfer_rate',
        'progress_percentage': 'progress_percentage',
        'estimated_completion_timestamp': 'estimated_completion_timestamp',
        'resource_type_l10n': 'resource_type_l10n',
        'state_l10n': 'state_l10n',
        'virtual_volumes': 'virtual_volumes',
        'volumes': 'volumes',
        'volume_groups': 'volume_groups',
        'replication_sessions': 'replication_sessions'
    }

    def __init__(self, id=None, name=None, resource_type=None, source_appliance_id=None, family_id=None, destination_appliance_id=None, state=None, created_timestamp=None, last_sync_timestamp=None, current_transfer_rate=None, progress_percentage=None, estimated_completion_timestamp=None, resource_type_l10n=None, state_l10n=None, virtual_volumes=None, volumes=None, volume_groups=None, replication_sessions=None, _configuration=None):  # noqa: E501
        """MigrationSessionInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._resource_type = None
        self._source_appliance_id = None
        self._family_id = None
        self._destination_appliance_id = None
        self._state = None
        self._created_timestamp = None
        self._last_sync_timestamp = None
        self._current_transfer_rate = None
        self._progress_percentage = None
        self._estimated_completion_timestamp = None
        self._resource_type_l10n = None
        self._state_l10n = None
        self._virtual_volumes = None
        self._volumes = None
        self._volume_groups = None
        self._replication_sessions = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if resource_type is not None:
            self.resource_type = resource_type
        if source_appliance_id is not None:
            self.source_appliance_id = source_appliance_id
        if family_id is not None:
            self.family_id = family_id
        if destination_appliance_id is not None:
            self.destination_appliance_id = destination_appliance_id
        if state is not None:
            self.state = state
        if created_timestamp is not None:
            self.created_timestamp = created_timestamp
        if last_sync_timestamp is not None:
            self.last_sync_timestamp = last_sync_timestamp
        if current_transfer_rate is not None:
            self.current_transfer_rate = current_transfer_rate
        if progress_percentage is not None:
            self.progress_percentage = progress_percentage
        if estimated_completion_timestamp is not None:
            self.estimated_completion_timestamp = estimated_completion_timestamp
        if resource_type_l10n is not None:
            self.resource_type_l10n = resource_type_l10n
        if state_l10n is not None:
            self.state_l10n = state_l10n
        if virtual_volumes is not None:
            self.virtual_volumes = virtual_volumes
        if volumes is not None:
            self.volumes = volumes
        if volume_groups is not None:
            self.volume_groups = volume_groups
        if replication_sessions is not None:
            self.replication_sessions = replication_sessions

    @property
    def id(self):
        """Gets the id of this MigrationSessionInstance.  # noqa: E501

        Unique identifier of the migration session instance.  # noqa: E501

        :return: The id of this MigrationSessionInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MigrationSessionInstance.

        Unique identifier of the migration session instance.  # noqa: E501

        :param id: The id of this MigrationSessionInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this MigrationSessionInstance.  # noqa: E501

        User-specified friendly name of the migration session instance.  This property supports case-insensitive filtering.  # noqa: E501

        :return: The name of this MigrationSessionInstance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MigrationSessionInstance.

        User-specified friendly name of the migration session instance.  This property supports case-insensitive filtering.  # noqa: E501

        :param name: The name of this MigrationSessionInstance.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def resource_type(self):
        """Gets the resource_type of this MigrationSessionInstance.  # noqa: E501


        :return: The resource_type of this MigrationSessionInstance.  # noqa: E501
        :rtype: MigrationResourceTypeEnum
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this MigrationSessionInstance.


        :param resource_type: The resource_type of this MigrationSessionInstance.  # noqa: E501
        :type: MigrationResourceTypeEnum
        """

        self._resource_type = resource_type

    @property
    def source_appliance_id(self):
        """Gets the source_appliance_id of this MigrationSessionInstance.  # noqa: E501

        Unique identifier of the source appliance instance.  # noqa: E501

        :return: The source_appliance_id of this MigrationSessionInstance.  # noqa: E501
        :rtype: str
        """
        return self._source_appliance_id

    @source_appliance_id.setter
    def source_appliance_id(self, source_appliance_id):
        """Sets the source_appliance_id of this MigrationSessionInstance.

        Unique identifier of the source appliance instance.  # noqa: E501

        :param source_appliance_id: The source_appliance_id of this MigrationSessionInstance.  # noqa: E501
        :type: str
        """

        self._source_appliance_id = source_appliance_id

    @property
    def family_id(self):
        """Gets the family_id of this MigrationSessionInstance.  # noqa: E501

        Family identifier designating the storage resource or resources being migrated. For volume or virtual_volume migrations, the family is moved together because they share data among the primary object, snapshots, and clones. For volume_group migration, the family of each volume in the group is moved because it is a grouping of volumes.  # noqa: E501

        :return: The family_id of this MigrationSessionInstance.  # noqa: E501
        :rtype: str
        """
        return self._family_id

    @family_id.setter
    def family_id(self, family_id):
        """Sets the family_id of this MigrationSessionInstance.

        Family identifier designating the storage resource or resources being migrated. For volume or virtual_volume migrations, the family is moved together because they share data among the primary object, snapshots, and clones. For volume_group migration, the family of each volume in the group is moved because it is a grouping of volumes.  # noqa: E501

        :param family_id: The family_id of this MigrationSessionInstance.  # noqa: E501
        :type: str
        """

        self._family_id = family_id

    @property
    def destination_appliance_id(self):
        """Gets the destination_appliance_id of this MigrationSessionInstance.  # noqa: E501

        Unique identifier of the destination appliance instance.  # noqa: E501

        :return: The destination_appliance_id of this MigrationSessionInstance.  # noqa: E501
        :rtype: str
        """
        return self._destination_appliance_id

    @destination_appliance_id.setter
    def destination_appliance_id(self, destination_appliance_id):
        """Sets the destination_appliance_id of this MigrationSessionInstance.

        Unique identifier of the destination appliance instance.  # noqa: E501

        :param destination_appliance_id: The destination_appliance_id of this MigrationSessionInstance.  # noqa: E501
        :type: str
        """

        self._destination_appliance_id = destination_appliance_id

    @property
    def state(self):
        """Gets the state of this MigrationSessionInstance.  # noqa: E501


        :return: The state of this MigrationSessionInstance.  # noqa: E501
        :rtype: MigrationSessionStateEnum
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this MigrationSessionInstance.


        :param state: The state of this MigrationSessionInstance.  # noqa: E501
        :type: MigrationSessionStateEnum
        """

        self._state = state

    @property
    def created_timestamp(self):
        """Gets the created_timestamp of this MigrationSessionInstance.  # noqa: E501

        Time when the migration session was created.  # noqa: E501

        :return: The created_timestamp of this MigrationSessionInstance.  # noqa: E501
        :rtype: datetime
        """
        return self._created_timestamp

    @created_timestamp.setter
    def created_timestamp(self, created_timestamp):
        """Sets the created_timestamp of this MigrationSessionInstance.

        Time when the migration session was created.  # noqa: E501

        :param created_timestamp: The created_timestamp of this MigrationSessionInstance.  # noqa: E501
        :type: datetime
        """

        self._created_timestamp = created_timestamp

    @property
    def last_sync_timestamp(self):
        """Gets the last_sync_timestamp of this MigrationSessionInstance.  # noqa: E501

        Time of the last successful sync operation.  # noqa: E501

        :return: The last_sync_timestamp of this MigrationSessionInstance.  # noqa: E501
        :rtype: datetime
        """
        return self._last_sync_timestamp

    @last_sync_timestamp.setter
    def last_sync_timestamp(self, last_sync_timestamp):
        """Sets the last_sync_timestamp of this MigrationSessionInstance.

        Time of the last successful sync operation.  # noqa: E501

        :param last_sync_timestamp: The last_sync_timestamp of this MigrationSessionInstance.  # noqa: E501
        :type: datetime
        """

        self._last_sync_timestamp = last_sync_timestamp

    @property
    def current_transfer_rate(self):
        """Gets the current_transfer_rate of this MigrationSessionInstance.  # noqa: E501

        Transfer rate of the current sync operation in bytes/sec.  # noqa: E501

        :return: The current_transfer_rate of this MigrationSessionInstance.  # noqa: E501
        :rtype: int
        """
        return self._current_transfer_rate

    @current_transfer_rate.setter
    def current_transfer_rate(self, current_transfer_rate):
        """Sets the current_transfer_rate of this MigrationSessionInstance.

        Transfer rate of the current sync operation in bytes/sec.  # noqa: E501

        :param current_transfer_rate: The current_transfer_rate of this MigrationSessionInstance.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                current_transfer_rate is not None and current_transfer_rate > -9223372036854775616):  # noqa: E501
            raise ValueError("Invalid value for `current_transfer_rate`, must be a value less than or equal to `-9223372036854775616`")  # noqa: E501
        if (self._configuration.client_side_validation and
                current_transfer_rate is not None and current_transfer_rate < 0):  # noqa: E501
            raise ValueError("Invalid value for `current_transfer_rate`, must be a value greater than or equal to `0`")  # noqa: E501

        self._current_transfer_rate = current_transfer_rate

    @property
    def progress_percentage(self):
        """Gets the progress_percentage of this MigrationSessionInstance.  # noqa: E501

        Progress percentage of the current sync operation.  # noqa: E501

        :return: The progress_percentage of this MigrationSessionInstance.  # noqa: E501
        :rtype: int
        """
        return self._progress_percentage

    @progress_percentage.setter
    def progress_percentage(self, progress_percentage):
        """Sets the progress_percentage of this MigrationSessionInstance.

        Progress percentage of the current sync operation.  # noqa: E501

        :param progress_percentage: The progress_percentage of this MigrationSessionInstance.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                progress_percentage is not None and progress_percentage > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `progress_percentage`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self._configuration.client_side_validation and
                progress_percentage is not None and progress_percentage < 0):  # noqa: E501
            raise ValueError("Invalid value for `progress_percentage`, must be a value greater than or equal to `0`")  # noqa: E501

        self._progress_percentage = progress_percentage

    @property
    def estimated_completion_timestamp(self):
        """Gets the estimated_completion_timestamp of this MigrationSessionInstance.  # noqa: E501

        Estimated completion time of the current sync operation.  # noqa: E501

        :return: The estimated_completion_timestamp of this MigrationSessionInstance.  # noqa: E501
        :rtype: datetime
        """
        return self._estimated_completion_timestamp

    @estimated_completion_timestamp.setter
    def estimated_completion_timestamp(self, estimated_completion_timestamp):
        """Sets the estimated_completion_timestamp of this MigrationSessionInstance.

        Estimated completion time of the current sync operation.  # noqa: E501

        :param estimated_completion_timestamp: The estimated_completion_timestamp of this MigrationSessionInstance.  # noqa: E501
        :type: datetime
        """

        self._estimated_completion_timestamp = estimated_completion_timestamp

    @property
    def resource_type_l10n(self):
        """Gets the resource_type_l10n of this MigrationSessionInstance.  # noqa: E501

        Localized message string corresponding to resource_type  # noqa: E501

        :return: The resource_type_l10n of this MigrationSessionInstance.  # noqa: E501
        :rtype: str
        """
        return self._resource_type_l10n

    @resource_type_l10n.setter
    def resource_type_l10n(self, resource_type_l10n):
        """Sets the resource_type_l10n of this MigrationSessionInstance.

        Localized message string corresponding to resource_type  # noqa: E501

        :param resource_type_l10n: The resource_type_l10n of this MigrationSessionInstance.  # noqa: E501
        :type: str
        """

        self._resource_type_l10n = resource_type_l10n

    @property
    def state_l10n(self):
        """Gets the state_l10n of this MigrationSessionInstance.  # noqa: E501

        Localized message string corresponding to state  # noqa: E501

        :return: The state_l10n of this MigrationSessionInstance.  # noqa: E501
        :rtype: str
        """
        return self._state_l10n

    @state_l10n.setter
    def state_l10n(self, state_l10n):
        """Sets the state_l10n of this MigrationSessionInstance.

        Localized message string corresponding to state  # noqa: E501

        :param state_l10n: The state_l10n of this MigrationSessionInstance.  # noqa: E501
        :type: str
        """

        self._state_l10n = state_l10n

    @property
    def virtual_volumes(self):
        """Gets the virtual_volumes of this MigrationSessionInstance.  # noqa: E501

        This is the inverse of the resource type virtual_volume association.  # noqa: E501

        :return: The virtual_volumes of this MigrationSessionInstance.  # noqa: E501
        :rtype: list[VirtualVolumeInstance]
        """
        return self._virtual_volumes

    @virtual_volumes.setter
    def virtual_volumes(self, virtual_volumes):
        """Sets the virtual_volumes of this MigrationSessionInstance.

        This is the inverse of the resource type virtual_volume association.  # noqa: E501

        :param virtual_volumes: The virtual_volumes of this MigrationSessionInstance.  # noqa: E501
        :type: list[VirtualVolumeInstance]
        """

        self._virtual_volumes = virtual_volumes

    @property
    def volumes(self):
        """Gets the volumes of this MigrationSessionInstance.  # noqa: E501

        This is the inverse of the resource type volume association.  # noqa: E501

        :return: The volumes of this MigrationSessionInstance.  # noqa: E501
        :rtype: list[VolumeInstance]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this MigrationSessionInstance.

        This is the inverse of the resource type volume association.  # noqa: E501

        :param volumes: The volumes of this MigrationSessionInstance.  # noqa: E501
        :type: list[VolumeInstance]
        """

        self._volumes = volumes

    @property
    def volume_groups(self):
        """Gets the volume_groups of this MigrationSessionInstance.  # noqa: E501

        This is the inverse of the resource type volume_group association.  # noqa: E501

        :return: The volume_groups of this MigrationSessionInstance.  # noqa: E501
        :rtype: list[VolumeGroupInstance]
        """
        return self._volume_groups

    @volume_groups.setter
    def volume_groups(self, volume_groups):
        """Sets the volume_groups of this MigrationSessionInstance.

        This is the inverse of the resource type volume_group association.  # noqa: E501

        :param volume_groups: The volume_groups of this MigrationSessionInstance.  # noqa: E501
        :type: list[VolumeGroupInstance]
        """

        self._volume_groups = volume_groups

    @property
    def replication_sessions(self):
        """Gets the replication_sessions of this MigrationSessionInstance.  # noqa: E501

        This is the inverse of the resource type replication_session association.  # noqa: E501

        :return: The replication_sessions of this MigrationSessionInstance.  # noqa: E501
        :rtype: list[ReplicationSessionInstance]
        """
        return self._replication_sessions

    @replication_sessions.setter
    def replication_sessions(self, replication_sessions):
        """Sets the replication_sessions of this MigrationSessionInstance.

        This is the inverse of the resource type replication_session association.  # noqa: E501

        :param replication_sessions: The replication_sessions of this MigrationSessionInstance.  # noqa: E501
        :type: list[ReplicationSessionInstance]
        """

        self._replication_sessions = replication_sessions

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
        if issubclass(MigrationSessionInstance, dict):
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
        if not isinstance(other, MigrationSessionInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MigrationSessionInstance):
            return True

        return self.to_dict() != other.to_dict()
