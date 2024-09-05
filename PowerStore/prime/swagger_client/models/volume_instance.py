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


class VolumeInstance(object):
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
        'description': 'str',
        'type': 'VolumeTypeEnum',
        'wwn': 'str',
        'nsid': 'int',
        'nguid': 'str',
        'appliance_id': 'str',
        'state': 'VolumeStateEnum',
        'size': 'int',
        'logical_used': 'int',
        'node_affinity': 'NodeAffinityEnum',
        'creation_timestamp': 'datetime',
        'protection_policy_id': 'str',
        'performance_policy_id': 'str',
        'is_replication_destination': 'bool',
        'migration_session_id': 'str',
        'metro_replication_session_id': 'str',
        'is_host_access_available': 'bool',
        'protection_data': 'ProtectionDataInstance',
        'location_history': 'list[LocationHistoryInstance]',
        'app_type': 'AppTypeEnum',
        'app_type_other': 'str',
        'type_l10n': 'str',
        'state_l10n': 'str',
        'node_affinity_l10n': 'str',
        'app_type_l10n': 'str',
        'appliance': 'ApplianceInstance',
        'protection_policy': 'PolicyInstance',
        'migration_session': 'MigrationSessionInstance',
        'mapped_volumes': 'list[HostVolumeMappingInstance]',
        'volume_groups': 'list[VolumeGroupInstance]',
        'datastores': 'list[DatastoreInstance]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'wwn': 'wwn',
        'nsid': 'nsid',
        'nguid': 'nguid',
        'appliance_id': 'appliance_id',
        'state': 'state',
        'size': 'size',
        'logical_used': 'logical_used',
        'node_affinity': 'node_affinity',
        'creation_timestamp': 'creation_timestamp',
        'protection_policy_id': 'protection_policy_id',
        'performance_policy_id': 'performance_policy_id',
        'is_replication_destination': 'is_replication_destination',
        'migration_session_id': 'migration_session_id',
        'metro_replication_session_id': 'metro_replication_session_id',
        'is_host_access_available': 'is_host_access_available',
        'protection_data': 'protection_data',
        'location_history': 'location_history',
        'app_type': 'app_type',
        'app_type_other': 'app_type_other',
        'type_l10n': 'type_l10n',
        'state_l10n': 'state_l10n',
        'node_affinity_l10n': 'node_affinity_l10n',
        'app_type_l10n': 'app_type_l10n',
        'appliance': 'appliance',
        'protection_policy': 'protection_policy',
        'migration_session': 'migration_session',
        'mapped_volumes': 'mapped_volumes',
        'volume_groups': 'volume_groups',
        'datastores': 'datastores'
    }

    def __init__(self, id=None, name=None, description=None, type=None, wwn=None, nsid=None, nguid=None, appliance_id=None, state=None, size=None, logical_used=None, node_affinity=None, creation_timestamp=None, protection_policy_id=None, performance_policy_id=None, is_replication_destination=False, migration_session_id=None, metro_replication_session_id=None, is_host_access_available=None, protection_data=None, location_history=None, app_type=None, app_type_other=None, type_l10n=None, state_l10n=None, node_affinity_l10n=None, app_type_l10n=None, appliance=None, protection_policy=None, migration_session=None, mapped_volumes=None, volume_groups=None, datastores=None, _configuration=None):  # noqa: E501
        """VolumeInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._description = None
        self._type = None
        self._wwn = None
        self._nsid = None
        self._nguid = None
        self._appliance_id = None
        self._state = None
        self._size = None
        self._logical_used = None
        self._node_affinity = None
        self._creation_timestamp = None
        self._protection_policy_id = None
        self._performance_policy_id = None
        self._is_replication_destination = None
        self._migration_session_id = None
        self._metro_replication_session_id = None
        self._is_host_access_available = None
        self._protection_data = None
        self._location_history = None
        self._app_type = None
        self._app_type_other = None
        self._type_l10n = None
        self._state_l10n = None
        self._node_affinity_l10n = None
        self._app_type_l10n = None
        self._appliance = None
        self._protection_policy = None
        self._migration_session = None
        self._mapped_volumes = None
        self._volume_groups = None
        self._datastores = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if wwn is not None:
            self.wwn = wwn
        if nsid is not None:
            self.nsid = nsid
        if nguid is not None:
            self.nguid = nguid
        if appliance_id is not None:
            self.appliance_id = appliance_id
        if state is not None:
            self.state = state
        if size is not None:
            self.size = size
        if logical_used is not None:
            self.logical_used = logical_used
        if node_affinity is not None:
            self.node_affinity = node_affinity
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if protection_policy_id is not None:
            self.protection_policy_id = protection_policy_id
        if performance_policy_id is not None:
            self.performance_policy_id = performance_policy_id
        if is_replication_destination is not None:
            self.is_replication_destination = is_replication_destination
        if migration_session_id is not None:
            self.migration_session_id = migration_session_id
        if metro_replication_session_id is not None:
            self.metro_replication_session_id = metro_replication_session_id
        if is_host_access_available is not None:
            self.is_host_access_available = is_host_access_available
        if protection_data is not None:
            self.protection_data = protection_data
        if location_history is not None:
            self.location_history = location_history
        if app_type is not None:
            self.app_type = app_type
        if app_type_other is not None:
            self.app_type_other = app_type_other
        if type_l10n is not None:
            self.type_l10n = type_l10n
        if state_l10n is not None:
            self.state_l10n = state_l10n
        if node_affinity_l10n is not None:
            self.node_affinity_l10n = node_affinity_l10n
        if app_type_l10n is not None:
            self.app_type_l10n = app_type_l10n
        if appliance is not None:
            self.appliance = appliance
        if protection_policy is not None:
            self.protection_policy = protection_policy
        if migration_session is not None:
            self.migration_session = migration_session
        if mapped_volumes is not None:
            self.mapped_volumes = mapped_volumes
        if volume_groups is not None:
            self.volume_groups = volume_groups
        if datastores is not None:
            self.datastores = datastores

    @property
    def id(self):
        """Gets the id of this VolumeInstance.  # noqa: E501

        Unique identifier of the volume instance.  # noqa: E501

        :return: The id of this VolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VolumeInstance.

        Unique identifier of the volume instance.  # noqa: E501

        :param id: The id of this VolumeInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this VolumeInstance.  # noqa: E501

        Name of the volume. This value must contain 128 or fewer printable Unicode characters.  This property supports case-insensitive filtering.  # noqa: E501

        :return: The name of this VolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VolumeInstance.

        Name of the volume. This value must contain 128 or fewer printable Unicode characters.  This property supports case-insensitive filtering.  # noqa: E501

        :param name: The name of this VolumeInstance.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 128):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this VolumeInstance.  # noqa: E501

        Description of the volume. This value must contain 128 or fewer printable Unicode characters.  # noqa: E501

        :return: The description of this VolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VolumeInstance.

        Description of the volume. This value must contain 128 or fewer printable Unicode characters.  # noqa: E501

        :param description: The description of this VolumeInstance.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                description is not None and len(description) > 128):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `128`")  # noqa: E501

        self._description = description

    @property
    def type(self):
        """Gets the type of this VolumeInstance.  # noqa: E501


        :return: The type of this VolumeInstance.  # noqa: E501
        :rtype: VolumeTypeEnum
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VolumeInstance.


        :param type: The type of this VolumeInstance.  # noqa: E501
        :type: VolumeTypeEnum
        """

        self._type = type

    @property
    def wwn(self):
        """Gets the wwn of this VolumeInstance.  # noqa: E501

        World wide name of the volume.  # noqa: E501

        :return: The wwn of this VolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._wwn

    @wwn.setter
    def wwn(self, wwn):
        """Sets the wwn of this VolumeInstance.

        World wide name of the volume.  # noqa: E501

        :param wwn: The wwn of this VolumeInstance.  # noqa: E501
        :type: str
        """

        self._wwn = wwn

    @property
    def nsid(self):
        """Gets the nsid of this VolumeInstance.  # noqa: E501

        NVMe Namespace unique identifier in the NVME subsystem. Used for volumes attached to NVMEoF hosts. Was added in version 2.0.0.0.  # noqa: E501

        :return: The nsid of this VolumeInstance.  # noqa: E501
        :rtype: int
        """
        return self._nsid

    @nsid.setter
    def nsid(self, nsid):
        """Sets the nsid of this VolumeInstance.

        NVMe Namespace unique identifier in the NVME subsystem. Used for volumes attached to NVMEoF hosts. Was added in version 2.0.0.0.  # noqa: E501

        :param nsid: The nsid of this VolumeInstance.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                nsid is not None and nsid > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `nsid`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self._configuration.client_side_validation and
                nsid is not None and nsid < 0):  # noqa: E501
            raise ValueError("Invalid value for `nsid`, must be a value greater than or equal to `0`")  # noqa: E501

        self._nsid = nsid

    @property
    def nguid(self):
        """Gets the nguid of this VolumeInstance.  # noqa: E501

        NVMe Namespace globally unique identifier. Used for volumes attached to NVMEoF hosts. Was added in version 2.0.0.0.  # noqa: E501

        :return: The nguid of this VolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._nguid

    @nguid.setter
    def nguid(self, nguid):
        """Sets the nguid of this VolumeInstance.

        NVMe Namespace globally unique identifier. Used for volumes attached to NVMEoF hosts. Was added in version 2.0.0.0.  # noqa: E501

        :param nguid: The nguid of this VolumeInstance.  # noqa: E501
        :type: str
        """

        self._nguid = nguid

    @property
    def appliance_id(self):
        """Gets the appliance_id of this VolumeInstance.  # noqa: E501

        Unique identifier of the appliance on which the volume is provisioned.  # noqa: E501

        :return: The appliance_id of this VolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._appliance_id

    @appliance_id.setter
    def appliance_id(self, appliance_id):
        """Sets the appliance_id of this VolumeInstance.

        Unique identifier of the appliance on which the volume is provisioned.  # noqa: E501

        :param appliance_id: The appliance_id of this VolumeInstance.  # noqa: E501
        :type: str
        """

        self._appliance_id = appliance_id

    @property
    def state(self):
        """Gets the state of this VolumeInstance.  # noqa: E501


        :return: The state of this VolumeInstance.  # noqa: E501
        :rtype: VolumeStateEnum
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this VolumeInstance.


        :param state: The state of this VolumeInstance.  # noqa: E501
        :type: VolumeStateEnum
        """

        self._state = state

    @property
    def size(self):
        """Gets the size of this VolumeInstance.  # noqa: E501

         Size of the volume in bytes. Minimum volume size is 1MB. Maximum volume size is 256TB. Size must be a multiple of 8192.  # noqa: E501

        :return: The size of this VolumeInstance.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this VolumeInstance.

         Size of the volume in bytes. Minimum volume size is 1MB. Maximum volume size is 256TB. Size must be a multiple of 8192.  # noqa: E501

        :param size: The size of this VolumeInstance.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                size is not None and size > 281474976710656):  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value less than or equal to `281474976710656`")  # noqa: E501
        if (self._configuration.client_side_validation and
                size is not None and size < 1048576):  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value greater than or equal to `1048576`")  # noqa: E501

        self._size = size

    @property
    def logical_used(self):
        """Gets the logical_used of this VolumeInstance.  # noqa: E501

        Current amount of data (in bytes) host has written to a volume without dedupe, compression or sharing. This metric applies to primaries, snaps and clones. The value is null initially when a volume is created and is collected at 5 minute intervals. Was added in version 3.0.0.0.  # noqa: E501

        :return: The logical_used of this VolumeInstance.  # noqa: E501
        :rtype: int
        """
        return self._logical_used

    @logical_used.setter
    def logical_used(self, logical_used):
        """Sets the logical_used of this VolumeInstance.

        Current amount of data (in bytes) host has written to a volume without dedupe, compression or sharing. This metric applies to primaries, snaps and clones. The value is null initially when a volume is created and is collected at 5 minute intervals. Was added in version 3.0.0.0.  # noqa: E501

        :param logical_used: The logical_used of this VolumeInstance.  # noqa: E501
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
    def node_affinity(self):
        """Gets the node_affinity of this VolumeInstance.  # noqa: E501

        Node affinity.  Node which offers optimized IO for volume, values are:  # noqa: E501

        :return: The node_affinity of this VolumeInstance.  # noqa: E501
        :rtype: NodeAffinityEnum
        """
        return self._node_affinity

    @node_affinity.setter
    def node_affinity(self, node_affinity):
        """Sets the node_affinity of this VolumeInstance.

        Node affinity.  Node which offers optimized IO for volume, values are:  # noqa: E501

        :param node_affinity: The node_affinity of this VolumeInstance.  # noqa: E501
        :type: NodeAffinityEnum
        """

        self._node_affinity = node_affinity

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this VolumeInstance.  # noqa: E501

        Time when the volume was created.  # noqa: E501

        :return: The creation_timestamp of this VolumeInstance.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this VolumeInstance.

        Time when the volume was created.  # noqa: E501

        :param creation_timestamp: The creation_timestamp of this VolumeInstance.  # noqa: E501
        :type: datetime
        """

        self._creation_timestamp = creation_timestamp

    @property
    def protection_policy_id(self):
        """Gets the protection_policy_id of this VolumeInstance.  # noqa: E501

        Unique identifier of the protection policy assigned to the volume. Only applicable to primary and clone volumes.  # noqa: E501

        :return: The protection_policy_id of this VolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._protection_policy_id

    @protection_policy_id.setter
    def protection_policy_id(self, protection_policy_id):
        """Sets the protection_policy_id of this VolumeInstance.

        Unique identifier of the protection policy assigned to the volume. Only applicable to primary and clone volumes.  # noqa: E501

        :param protection_policy_id: The protection_policy_id of this VolumeInstance.  # noqa: E501
        :type: str
        """

        self._protection_policy_id = protection_policy_id

    @property
    def performance_policy_id(self):
        """Gets the performance_policy_id of this VolumeInstance.  # noqa: E501

        Unique identifier of the performance policy assigned to the volume.  # noqa: E501

        :return: The performance_policy_id of this VolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._performance_policy_id

    @performance_policy_id.setter
    def performance_policy_id(self, performance_policy_id):
        """Sets the performance_policy_id of this VolumeInstance.

        Unique identifier of the performance policy assigned to the volume.  # noqa: E501

        :param performance_policy_id: The performance_policy_id of this VolumeInstance.  # noqa: E501
        :type: str
        """

        self._performance_policy_id = performance_policy_id

    @property
    def is_replication_destination(self):
        """Gets the is_replication_destination of this VolumeInstance.  # noqa: E501

        Indicates whether this volume is a replication destination. This field is false on both ends when a volume is a metro volume. Areplication destination will be created by the system when a replication session is created. When there is an active replication session, all the user operations are restricted including modification, deletion, host operation, snapshot, clone, etc. After the replication session is deleted, the replication destination volume will remain as it is until the end user changes it to be a non-replication destination. After the change, it becomes a primary volume. If the end user keeps it as a replication destination, when the replication session is recreated, the replication destination volume could potentially be reused in the new session to avoid a time-consuming full sync. This property is only valid for primary and clone volumes.  # noqa: E501

        :return: The is_replication_destination of this VolumeInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_replication_destination

    @is_replication_destination.setter
    def is_replication_destination(self, is_replication_destination):
        """Sets the is_replication_destination of this VolumeInstance.

        Indicates whether this volume is a replication destination. This field is false on both ends when a volume is a metro volume. Areplication destination will be created by the system when a replication session is created. When there is an active replication session, all the user operations are restricted including modification, deletion, host operation, snapshot, clone, etc. After the replication session is deleted, the replication destination volume will remain as it is until the end user changes it to be a non-replication destination. After the change, it becomes a primary volume. If the end user keeps it as a replication destination, when the replication session is recreated, the replication destination volume could potentially be reused in the new session to avoid a time-consuming full sync. This property is only valid for primary and clone volumes.  # noqa: E501

        :param is_replication_destination: The is_replication_destination of this VolumeInstance.  # noqa: E501
        :type: bool
        """

        self._is_replication_destination = is_replication_destination

    @property
    def migration_session_id(self):
        """Gets the migration_session_id of this VolumeInstance.  # noqa: E501

        Unique identifier of the migration session assigned to the volume if it is part of a migration activity.  # noqa: E501

        :return: The migration_session_id of this VolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._migration_session_id

    @migration_session_id.setter
    def migration_session_id(self, migration_session_id):
        """Sets the migration_session_id of this VolumeInstance.

        Unique identifier of the migration session assigned to the volume if it is part of a migration activity.  # noqa: E501

        :param migration_session_id: The migration_session_id of this VolumeInstance.  # noqa: E501
        :type: str
        """

        self._migration_session_id = migration_session_id

    @property
    def metro_replication_session_id(self):
        """Gets the metro_replication_session_id of this VolumeInstance.  # noqa: E501

        Unique identifier of the replication session assigned to the volume if it has been configured as a metro volume between two PowerStore clusters. The volume can only be modified, refreshed, or restored when the metro_replication_session is in the paused state. Was added in version 3.0.0.0.  # noqa: E501

        :return: The metro_replication_session_id of this VolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._metro_replication_session_id

    @metro_replication_session_id.setter
    def metro_replication_session_id(self, metro_replication_session_id):
        """Sets the metro_replication_session_id of this VolumeInstance.

        Unique identifier of the replication session assigned to the volume if it has been configured as a metro volume between two PowerStore clusters. The volume can only be modified, refreshed, or restored when the metro_replication_session is in the paused state. Was added in version 3.0.0.0.  # noqa: E501

        :param metro_replication_session_id: The metro_replication_session_id of this VolumeInstance.  # noqa: E501
        :type: str
        """

        self._metro_replication_session_id = metro_replication_session_id

    @property
    def is_host_access_available(self):
        """Gets the is_host_access_available of this VolumeInstance.  # noqa: E501

        Indicates whether the volume is available to host. This attribute is only applicable to primary volumes and clones. Was added in version 3.0.0.0.  # noqa: E501

        :return: The is_host_access_available of this VolumeInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_host_access_available

    @is_host_access_available.setter
    def is_host_access_available(self, is_host_access_available):
        """Sets the is_host_access_available of this VolumeInstance.

        Indicates whether the volume is available to host. This attribute is only applicable to primary volumes and clones. Was added in version 3.0.0.0.  # noqa: E501

        :param is_host_access_available: The is_host_access_available of this VolumeInstance.  # noqa: E501
        :type: bool
        """

        self._is_host_access_available = is_host_access_available

    @property
    def protection_data(self):
        """Gets the protection_data of this VolumeInstance.  # noqa: E501


        :return: The protection_data of this VolumeInstance.  # noqa: E501
        :rtype: ProtectionDataInstance
        """
        return self._protection_data

    @protection_data.setter
    def protection_data(self, protection_data):
        """Sets the protection_data of this VolumeInstance.


        :param protection_data: The protection_data of this VolumeInstance.  # noqa: E501
        :type: ProtectionDataInstance
        """

        self._protection_data = protection_data

    @property
    def location_history(self):
        """Gets the location_history of this VolumeInstance.  # noqa: E501

        Filtering on the fields of this embedded resource is not supported.  # noqa: E501

        :return: The location_history of this VolumeInstance.  # noqa: E501
        :rtype: list[LocationHistoryInstance]
        """
        return self._location_history

    @location_history.setter
    def location_history(self, location_history):
        """Sets the location_history of this VolumeInstance.

        Filtering on the fields of this embedded resource is not supported.  # noqa: E501

        :param location_history: The location_history of this VolumeInstance.  # noqa: E501
        :type: list[LocationHistoryInstance]
        """

        self._location_history = location_history

    @property
    def app_type(self):
        """Gets the app_type of this VolumeInstance.  # noqa: E501

         Was added in version 2.1.0.0.  # noqa: E501

        :return: The app_type of this VolumeInstance.  # noqa: E501
        :rtype: AppTypeEnum
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this VolumeInstance.

         Was added in version 2.1.0.0.  # noqa: E501

        :param app_type: The app_type of this VolumeInstance.  # noqa: E501
        :type: AppTypeEnum
        """

        self._app_type = app_type

    @property
    def app_type_other(self):
        """Gets the app_type_other of this VolumeInstance.  # noqa: E501

        An optional field used to describe application type usage for a volume. This field can only be set if app_type is set to Relational_Databases_Other, Big_Data_Analytics_Other, Business_Applications_Other, Healthcare_Other, Virtualization_Other or Other. If the app_type attribute is set to anything other than one of these values, the attribute will be cleared. Was added in version 2.1.0.0.  # noqa: E501

        :return: The app_type_other of this VolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._app_type_other

    @app_type_other.setter
    def app_type_other(self, app_type_other):
        """Sets the app_type_other of this VolumeInstance.

        An optional field used to describe application type usage for a volume. This field can only be set if app_type is set to Relational_Databases_Other, Big_Data_Analytics_Other, Business_Applications_Other, Healthcare_Other, Virtualization_Other or Other. If the app_type attribute is set to anything other than one of these values, the attribute will be cleared. Was added in version 2.1.0.0.  # noqa: E501

        :param app_type_other: The app_type_other of this VolumeInstance.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                app_type_other is not None and len(app_type_other) > 32):
            raise ValueError("Invalid value for `app_type_other`, length must be less than or equal to `32`")  # noqa: E501

        self._app_type_other = app_type_other

    @property
    def type_l10n(self):
        """Gets the type_l10n of this VolumeInstance.  # noqa: E501

        Localized message string corresponding to type  # noqa: E501

        :return: The type_l10n of this VolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._type_l10n

    @type_l10n.setter
    def type_l10n(self, type_l10n):
        """Sets the type_l10n of this VolumeInstance.

        Localized message string corresponding to type  # noqa: E501

        :param type_l10n: The type_l10n of this VolumeInstance.  # noqa: E501
        :type: str
        """

        self._type_l10n = type_l10n

    @property
    def state_l10n(self):
        """Gets the state_l10n of this VolumeInstance.  # noqa: E501

        Localized message string corresponding to state  # noqa: E501

        :return: The state_l10n of this VolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._state_l10n

    @state_l10n.setter
    def state_l10n(self, state_l10n):
        """Sets the state_l10n of this VolumeInstance.

        Localized message string corresponding to state  # noqa: E501

        :param state_l10n: The state_l10n of this VolumeInstance.  # noqa: E501
        :type: str
        """

        self._state_l10n = state_l10n

    @property
    def node_affinity_l10n(self):
        """Gets the node_affinity_l10n of this VolumeInstance.  # noqa: E501

        Localized message string corresponding to node_affinity  # noqa: E501

        :return: The node_affinity_l10n of this VolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._node_affinity_l10n

    @node_affinity_l10n.setter
    def node_affinity_l10n(self, node_affinity_l10n):
        """Sets the node_affinity_l10n of this VolumeInstance.

        Localized message string corresponding to node_affinity  # noqa: E501

        :param node_affinity_l10n: The node_affinity_l10n of this VolumeInstance.  # noqa: E501
        :type: str
        """

        self._node_affinity_l10n = node_affinity_l10n

    @property
    def app_type_l10n(self):
        """Gets the app_type_l10n of this VolumeInstance.  # noqa: E501

        Localized message string corresponding to app_type Was added in version 2.1.0.0.  # noqa: E501

        :return: The app_type_l10n of this VolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._app_type_l10n

    @app_type_l10n.setter
    def app_type_l10n(self, app_type_l10n):
        """Sets the app_type_l10n of this VolumeInstance.

        Localized message string corresponding to app_type Was added in version 2.1.0.0.  # noqa: E501

        :param app_type_l10n: The app_type_l10n of this VolumeInstance.  # noqa: E501
        :type: str
        """

        self._app_type_l10n = app_type_l10n

    @property
    def appliance(self):
        """Gets the appliance of this VolumeInstance.  # noqa: E501

        This is the embeddable reference form of appliance_id attribute.  # noqa: E501

        :return: The appliance of this VolumeInstance.  # noqa: E501
        :rtype: ApplianceInstance
        """
        return self._appliance

    @appliance.setter
    def appliance(self, appliance):
        """Sets the appliance of this VolumeInstance.

        This is the embeddable reference form of appliance_id attribute.  # noqa: E501

        :param appliance: The appliance of this VolumeInstance.  # noqa: E501
        :type: ApplianceInstance
        """

        self._appliance = appliance

    @property
    def protection_policy(self):
        """Gets the protection_policy of this VolumeInstance.  # noqa: E501

        This is the embeddable reference form of protection_policy_id attribute.  # noqa: E501

        :return: The protection_policy of this VolumeInstance.  # noqa: E501
        :rtype: PolicyInstance
        """
        return self._protection_policy

    @protection_policy.setter
    def protection_policy(self, protection_policy):
        """Sets the protection_policy of this VolumeInstance.

        This is the embeddable reference form of protection_policy_id attribute.  # noqa: E501

        :param protection_policy: The protection_policy of this VolumeInstance.  # noqa: E501
        :type: PolicyInstance
        """

        self._protection_policy = protection_policy

    @property
    def migration_session(self):
        """Gets the migration_session of this VolumeInstance.  # noqa: E501

        This is the embeddable reference form of migration_session_id attribute.  # noqa: E501

        :return: The migration_session of this VolumeInstance.  # noqa: E501
        :rtype: MigrationSessionInstance
        """
        return self._migration_session

    @migration_session.setter
    def migration_session(self, migration_session):
        """Sets the migration_session of this VolumeInstance.

        This is the embeddable reference form of migration_session_id attribute.  # noqa: E501

        :param migration_session: The migration_session of this VolumeInstance.  # noqa: E501
        :type: MigrationSessionInstance
        """

        self._migration_session = migration_session

    @property
    def mapped_volumes(self):
        """Gets the mapped_volumes of this VolumeInstance.  # noqa: E501

        This is the inverse of the resource type host_volume_mapping association.  # noqa: E501

        :return: The mapped_volumes of this VolumeInstance.  # noqa: E501
        :rtype: list[HostVolumeMappingInstance]
        """
        return self._mapped_volumes

    @mapped_volumes.setter
    def mapped_volumes(self, mapped_volumes):
        """Sets the mapped_volumes of this VolumeInstance.

        This is the inverse of the resource type host_volume_mapping association.  # noqa: E501

        :param mapped_volumes: The mapped_volumes of this VolumeInstance.  # noqa: E501
        :type: list[HostVolumeMappingInstance]
        """

        self._mapped_volumes = mapped_volumes

    @property
    def volume_groups(self):
        """Gets the volume_groups of this VolumeInstance.  # noqa: E501

        List of the volume_groups that are associated with this volume.  # noqa: E501

        :return: The volume_groups of this VolumeInstance.  # noqa: E501
        :rtype: list[VolumeGroupInstance]
        """
        return self._volume_groups

    @volume_groups.setter
    def volume_groups(self, volume_groups):
        """Sets the volume_groups of this VolumeInstance.

        List of the volume_groups that are associated with this volume.  # noqa: E501

        :param volume_groups: The volume_groups of this VolumeInstance.  # noqa: E501
        :type: list[VolumeGroupInstance]
        """

        self._volume_groups = volume_groups

    @property
    def datastores(self):
        """Gets the datastores of this VolumeInstance.  # noqa: E501

        List of the datastores that are associated with this volume.  # noqa: E501

        :return: The datastores of this VolumeInstance.  # noqa: E501
        :rtype: list[DatastoreInstance]
        """
        return self._datastores

    @datastores.setter
    def datastores(self, datastores):
        """Sets the datastores of this VolumeInstance.

        List of the datastores that are associated with this volume.  # noqa: E501

        :param datastores: The datastores of this VolumeInstance.  # noqa: E501
        :type: list[DatastoreInstance]
        """

        self._datastores = datastores

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
        if issubclass(VolumeInstance, dict):
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
        if not isinstance(other, VolumeInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VolumeInstance):
            return True

        return self.to_dict() != other.to_dict()
