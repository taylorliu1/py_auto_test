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


class VolumeGroupInstance(object):
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
        'creation_timestamp': 'datetime',
        'is_protectable': 'bool',
        'protection_policy_id': 'str',
        'migration_session_id': 'str',
        'is_write_order_consistent': 'bool',
        'placement_rule': 'VGPlacementRule',
        'type': 'VolumeTypeEnum',
        'is_replication_destination': 'bool',
        'protection_data': 'ProtectionDataInstance',
        'is_importing': 'bool',
        'location_history': 'list[LocationHistoryInstance]',
        'type_l10n': 'str',
        'protection_policy': 'PolicyInstance',
        'migration_session': 'MigrationSessionInstance',
        'volumes': 'list[VolumeInstance]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'creation_timestamp': 'creation_timestamp',
        'is_protectable': 'is_protectable',
        'protection_policy_id': 'protection_policy_id',
        'migration_session_id': 'migration_session_id',
        'is_write_order_consistent': 'is_write_order_consistent',
        'placement_rule': 'placement_rule',
        'type': 'type',
        'is_replication_destination': 'is_replication_destination',
        'protection_data': 'protection_data',
        'is_importing': 'is_importing',
        'location_history': 'location_history',
        'type_l10n': 'type_l10n',
        'protection_policy': 'protection_policy',
        'migration_session': 'migration_session',
        'volumes': 'volumes'
    }

    def __init__(self, id=None, name=None, description=None, creation_timestamp=None, is_protectable=None, protection_policy_id=None, migration_session_id=None, is_write_order_consistent=None, placement_rule=None, type=None, is_replication_destination=False, protection_data=None, is_importing=None, location_history=None, type_l10n=None, protection_policy=None, migration_session=None, volumes=None, _configuration=None):  # noqa: E501
        """VolumeGroupInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._description = None
        self._creation_timestamp = None
        self._is_protectable = None
        self._protection_policy_id = None
        self._migration_session_id = None
        self._is_write_order_consistent = None
        self._placement_rule = None
        self._type = None
        self._is_replication_destination = None
        self._protection_data = None
        self._is_importing = None
        self._location_history = None
        self._type_l10n = None
        self._protection_policy = None
        self._migration_session = None
        self._volumes = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if is_protectable is not None:
            self.is_protectable = is_protectable
        if protection_policy_id is not None:
            self.protection_policy_id = protection_policy_id
        if migration_session_id is not None:
            self.migration_session_id = migration_session_id
        if is_write_order_consistent is not None:
            self.is_write_order_consistent = is_write_order_consistent
        if placement_rule is not None:
            self.placement_rule = placement_rule
        if type is not None:
            self.type = type
        if is_replication_destination is not None:
            self.is_replication_destination = is_replication_destination
        if protection_data is not None:
            self.protection_data = protection_data
        if is_importing is not None:
            self.is_importing = is_importing
        if location_history is not None:
            self.location_history = location_history
        if type_l10n is not None:
            self.type_l10n = type_l10n
        if protection_policy is not None:
            self.protection_policy = protection_policy
        if migration_session is not None:
            self.migration_session = migration_session
        if volumes is not None:
            self.volumes = volumes

    @property
    def id(self):
        """Gets the id of this VolumeGroupInstance.  # noqa: E501

        Unique identifier of the volume group.  # noqa: E501

        :return: The id of this VolumeGroupInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VolumeGroupInstance.

        Unique identifier of the volume group.  # noqa: E501

        :param id: The id of this VolumeGroupInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this VolumeGroupInstance.  # noqa: E501

        Name of the volume group.  This property supports case-insensitive filtering.  # noqa: E501

        :return: The name of this VolumeGroupInstance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VolumeGroupInstance.

        Name of the volume group.  This property supports case-insensitive filtering.  # noqa: E501

        :param name: The name of this VolumeGroupInstance.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this VolumeGroupInstance.  # noqa: E501

        Description for the volume group.  # noqa: E501

        :return: The description of this VolumeGroupInstance.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VolumeGroupInstance.

        Description for the volume group.  # noqa: E501

        :param description: The description of this VolumeGroupInstance.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this VolumeGroupInstance.  # noqa: E501

        The time at which the volume group was created.  # noqa: E501

        :return: The creation_timestamp of this VolumeGroupInstance.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this VolumeGroupInstance.

        The time at which the volume group was created.  # noqa: E501

        :param creation_timestamp: The creation_timestamp of this VolumeGroupInstance.  # noqa: E501
        :type: datetime
        """

        self._creation_timestamp = creation_timestamp

    @property
    def is_protectable(self):
        """Gets the is_protectable of this VolumeGroupInstance.  # noqa: E501

        This is a derived field that is set internally. It enables/disables the following functionality: * Whether a protection_policy can be applied to the group. * Whether manual snapshots can be taken. * Whether clones of the group can be created.   # noqa: E501

        :return: The is_protectable of this VolumeGroupInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_protectable

    @is_protectable.setter
    def is_protectable(self, is_protectable):
        """Sets the is_protectable of this VolumeGroupInstance.

        This is a derived field that is set internally. It enables/disables the following functionality: * Whether a protection_policy can be applied to the group. * Whether manual snapshots can be taken. * Whether clones of the group can be created.   # noqa: E501

        :param is_protectable: The is_protectable of this VolumeGroupInstance.  # noqa: E501
        :type: bool
        """

        self._is_protectable = is_protectable

    @property
    def protection_policy_id(self):
        """Gets the protection_policy_id of this VolumeGroupInstance.  # noqa: E501

        Unique identifier of the protection policy assigned to the volume group. This attribute is only applicable to primary and clone volume groups.  # noqa: E501

        :return: The protection_policy_id of this VolumeGroupInstance.  # noqa: E501
        :rtype: str
        """
        return self._protection_policy_id

    @protection_policy_id.setter
    def protection_policy_id(self, protection_policy_id):
        """Sets the protection_policy_id of this VolumeGroupInstance.

        Unique identifier of the protection policy assigned to the volume group. This attribute is only applicable to primary and clone volume groups.  # noqa: E501

        :param protection_policy_id: The protection_policy_id of this VolumeGroupInstance.  # noqa: E501
        :type: str
        """

        self._protection_policy_id = protection_policy_id

    @property
    def migration_session_id(self):
        """Gets the migration_session_id of this VolumeGroupInstance.  # noqa: E501

        Unique identifier of the migration session assigned to the volume group when it is part of a migration activity.  # noqa: E501

        :return: The migration_session_id of this VolumeGroupInstance.  # noqa: E501
        :rtype: str
        """
        return self._migration_session_id

    @migration_session_id.setter
    def migration_session_id(self, migration_session_id):
        """Sets the migration_session_id of this VolumeGroupInstance.

        Unique identifier of the migration session assigned to the volume group when it is part of a migration activity.  # noqa: E501

        :param migration_session_id: The migration_session_id of this VolumeGroupInstance.  # noqa: E501
        :type: str
        """

        self._migration_session_id = migration_session_id

    @property
    def is_write_order_consistent(self):
        """Gets the is_write_order_consistent of this VolumeGroupInstance.  # noqa: E501

        For a primary or a clone volume group, this property determines whether snapshot sets of the group will be write order consistent.  For a snapshot set, this property indicates whether the snapshot set is write-order consistent.  # noqa: E501

        :return: The is_write_order_consistent of this VolumeGroupInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_write_order_consistent

    @is_write_order_consistent.setter
    def is_write_order_consistent(self, is_write_order_consistent):
        """Sets the is_write_order_consistent of this VolumeGroupInstance.

        For a primary or a clone volume group, this property determines whether snapshot sets of the group will be write order consistent.  For a snapshot set, this property indicates whether the snapshot set is write-order consistent.  # noqa: E501

        :param is_write_order_consistent: The is_write_order_consistent of this VolumeGroupInstance.  # noqa: E501
        :type: bool
        """

        self._is_write_order_consistent = is_write_order_consistent

    @property
    def placement_rule(self):
        """Gets the placement_rule of this VolumeGroupInstance.  # noqa: E501


        :return: The placement_rule of this VolumeGroupInstance.  # noqa: E501
        :rtype: VGPlacementRule
        """
        return self._placement_rule

    @placement_rule.setter
    def placement_rule(self, placement_rule):
        """Sets the placement_rule of this VolumeGroupInstance.


        :param placement_rule: The placement_rule of this VolumeGroupInstance.  # noqa: E501
        :type: VGPlacementRule
        """

        self._placement_rule = placement_rule

    @property
    def type(self):
        """Gets the type of this VolumeGroupInstance.  # noqa: E501


        :return: The type of this VolumeGroupInstance.  # noqa: E501
        :rtype: VolumeTypeEnum
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VolumeGroupInstance.


        :param type: The type of this VolumeGroupInstance.  # noqa: E501
        :type: VolumeTypeEnum
        """

        self._type = type

    @property
    def is_replication_destination(self):
        """Gets the is_replication_destination of this VolumeGroupInstance.  # noqa: E501

        Indicates whether this volume group is a replication destination. A replication destination will be created by the system when a replication session is created. When there is an active replication session, all the user operations are restricted including modification, deletion, host operation, snapshot, clone, etc. After the replication session is deleted, the replication destination will remain as it is until the end user changes it to be a non-replication destination. After the change, it becomes a primary volume group. If the end user keeps it as a replication destination, when the replication session is recreated, the replication destination could potentially be reused in the new session to avoid a time-consuming full sync. This property is only valid for primary and clone volume groups.  # noqa: E501

        :return: The is_replication_destination of this VolumeGroupInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_replication_destination

    @is_replication_destination.setter
    def is_replication_destination(self, is_replication_destination):
        """Sets the is_replication_destination of this VolumeGroupInstance.

        Indicates whether this volume group is a replication destination. A replication destination will be created by the system when a replication session is created. When there is an active replication session, all the user operations are restricted including modification, deletion, host operation, snapshot, clone, etc. After the replication session is deleted, the replication destination will remain as it is until the end user changes it to be a non-replication destination. After the change, it becomes a primary volume group. If the end user keeps it as a replication destination, when the replication session is recreated, the replication destination could potentially be reused in the new session to avoid a time-consuming full sync. This property is only valid for primary and clone volume groups.  # noqa: E501

        :param is_replication_destination: The is_replication_destination of this VolumeGroupInstance.  # noqa: E501
        :type: bool
        """

        self._is_replication_destination = is_replication_destination

    @property
    def protection_data(self):
        """Gets the protection_data of this VolumeGroupInstance.  # noqa: E501


        :return: The protection_data of this VolumeGroupInstance.  # noqa: E501
        :rtype: ProtectionDataInstance
        """
        return self._protection_data

    @protection_data.setter
    def protection_data(self, protection_data):
        """Sets the protection_data of this VolumeGroupInstance.


        :param protection_data: The protection_data of this VolumeGroupInstance.  # noqa: E501
        :type: ProtectionDataInstance
        """

        self._protection_data = protection_data

    @property
    def is_importing(self):
        """Gets the is_importing of this VolumeGroupInstance.  # noqa: E501

        Indicates whether the volume group is being imported.  # noqa: E501

        :return: The is_importing of this VolumeGroupInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_importing

    @is_importing.setter
    def is_importing(self, is_importing):
        """Sets the is_importing of this VolumeGroupInstance.

        Indicates whether the volume group is being imported.  # noqa: E501

        :param is_importing: The is_importing of this VolumeGroupInstance.  # noqa: E501
        :type: bool
        """

        self._is_importing = is_importing

    @property
    def location_history(self):
        """Gets the location_history of this VolumeGroupInstance.  # noqa: E501

        A list of locations. The list of locations includes the move to the current appliance.  Filtering on the fields of this embedded resource is not supported.  # noqa: E501

        :return: The location_history of this VolumeGroupInstance.  # noqa: E501
        :rtype: list[LocationHistoryInstance]
        """
        return self._location_history

    @location_history.setter
    def location_history(self, location_history):
        """Sets the location_history of this VolumeGroupInstance.

        A list of locations. The list of locations includes the move to the current appliance.  Filtering on the fields of this embedded resource is not supported.  # noqa: E501

        :param location_history: The location_history of this VolumeGroupInstance.  # noqa: E501
        :type: list[LocationHistoryInstance]
        """

        self._location_history = location_history

    @property
    def type_l10n(self):
        """Gets the type_l10n of this VolumeGroupInstance.  # noqa: E501

        Localized message string corresponding to type  # noqa: E501

        :return: The type_l10n of this VolumeGroupInstance.  # noqa: E501
        :rtype: str
        """
        return self._type_l10n

    @type_l10n.setter
    def type_l10n(self, type_l10n):
        """Sets the type_l10n of this VolumeGroupInstance.

        Localized message string corresponding to type  # noqa: E501

        :param type_l10n: The type_l10n of this VolumeGroupInstance.  # noqa: E501
        :type: str
        """

        self._type_l10n = type_l10n

    @property
    def protection_policy(self):
        """Gets the protection_policy of this VolumeGroupInstance.  # noqa: E501

        This is the embeddable reference form of protection_policy_id attribute.  # noqa: E501

        :return: The protection_policy of this VolumeGroupInstance.  # noqa: E501
        :rtype: PolicyInstance
        """
        return self._protection_policy

    @protection_policy.setter
    def protection_policy(self, protection_policy):
        """Sets the protection_policy of this VolumeGroupInstance.

        This is the embeddable reference form of protection_policy_id attribute.  # noqa: E501

        :param protection_policy: The protection_policy of this VolumeGroupInstance.  # noqa: E501
        :type: PolicyInstance
        """

        self._protection_policy = protection_policy

    @property
    def migration_session(self):
        """Gets the migration_session of this VolumeGroupInstance.  # noqa: E501

        This is the embeddable reference form of migration_session_id attribute.  # noqa: E501

        :return: The migration_session of this VolumeGroupInstance.  # noqa: E501
        :rtype: MigrationSessionInstance
        """
        return self._migration_session

    @migration_session.setter
    def migration_session(self, migration_session):
        """Sets the migration_session of this VolumeGroupInstance.

        This is the embeddable reference form of migration_session_id attribute.  # noqa: E501

        :param migration_session: The migration_session of this VolumeGroupInstance.  # noqa: E501
        :type: MigrationSessionInstance
        """

        self._migration_session = migration_session

    @property
    def volumes(self):
        """Gets the volumes of this VolumeGroupInstance.  # noqa: E501

        List of the volumes that are associated with this volume_group.  # noqa: E501

        :return: The volumes of this VolumeGroupInstance.  # noqa: E501
        :rtype: list[VolumeInstance]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this VolumeGroupInstance.

        List of the volumes that are associated with this volume_group.  # noqa: E501

        :param volumes: The volumes of this VolumeGroupInstance.  # noqa: E501
        :type: list[VolumeInstance]
        """

        self._volumes = volumes

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
        if issubclass(VolumeGroupInstance, dict):
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
        if not isinstance(other, VolumeGroupInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VolumeGroupInstance):
            return True

        return self.to_dict() != other.to_dict()
