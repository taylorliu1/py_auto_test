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


class ImportUnityVolumeInstance(object):
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
        'wwn': 'str',
        'name': 'str',
        'size': 'int',
        'import_unity_id': 'str',
        'import_unity_consistency_group_id': 'str',
        'health': 'UnityHealthEnum',
        'type': 'UnityVolumeTypeEnum',
        'migration_state': 'UnityVolumeMigrationStateEnum',
        'is_replication_destination': 'bool',
        'is_thin_clone': 'bool',
        'importable_criteria': 'VolumeImportableCriteriaEnum',
        'host_volume_ids': 'list[str]',
        'health_l10n': 'str',
        'type_l10n': 'str',
        'migration_state_l10n': 'str',
        'importable_criteria_l10n': 'str',
        'import_unity': 'ImportUnityInstance',
        'import_unity_consistency_group': 'ImportUnityConsistencyGroupInstance'
    }

    attribute_map = {
        'id': 'id',
        'wwn': 'wwn',
        'name': 'name',
        'size': 'size',
        'import_unity_id': 'import_unity_id',
        'import_unity_consistency_group_id': 'import_unity_consistency_group_id',
        'health': 'health',
        'type': 'type',
        'migration_state': 'migration_state',
        'is_replication_destination': 'is_replication_destination',
        'is_thin_clone': 'is_thin_clone',
        'importable_criteria': 'importable_criteria',
        'host_volume_ids': 'host_volume_ids',
        'health_l10n': 'health_l10n',
        'type_l10n': 'type_l10n',
        'migration_state_l10n': 'migration_state_l10n',
        'importable_criteria_l10n': 'importable_criteria_l10n',
        'import_unity': 'import_unity',
        'import_unity_consistency_group': 'import_unity_consistency_group'
    }

    def __init__(self, id=None, wwn=None, name=None, size=None, import_unity_id=None, import_unity_consistency_group_id=None, health=None, type=None, migration_state=None, is_replication_destination=None, is_thin_clone=None, importable_criteria=None, host_volume_ids=None, health_l10n=None, type_l10n=None, migration_state_l10n=None, importable_criteria_l10n=None, import_unity=None, import_unity_consistency_group=None, _configuration=None):  # noqa: E501
        """ImportUnityVolumeInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._wwn = None
        self._name = None
        self._size = None
        self._import_unity_id = None
        self._import_unity_consistency_group_id = None
        self._health = None
        self._type = None
        self._migration_state = None
        self._is_replication_destination = None
        self._is_thin_clone = None
        self._importable_criteria = None
        self._host_volume_ids = None
        self._health_l10n = None
        self._type_l10n = None
        self._migration_state_l10n = None
        self._importable_criteria_l10n = None
        self._import_unity = None
        self._import_unity_consistency_group = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if wwn is not None:
            self.wwn = wwn
        if name is not None:
            self.name = name
        if size is not None:
            self.size = size
        if import_unity_id is not None:
            self.import_unity_id = import_unity_id
        if import_unity_consistency_group_id is not None:
            self.import_unity_consistency_group_id = import_unity_consistency_group_id
        if health is not None:
            self.health = health
        if type is not None:
            self.type = type
        if migration_state is not None:
            self.migration_state = migration_state
        if is_replication_destination is not None:
            self.is_replication_destination = is_replication_destination
        if is_thin_clone is not None:
            self.is_thin_clone = is_thin_clone
        if importable_criteria is not None:
            self.importable_criteria = importable_criteria
        if host_volume_ids is not None:
            self.host_volume_ids = host_volume_ids
        if health_l10n is not None:
            self.health_l10n = health_l10n
        if type_l10n is not None:
            self.type_l10n = type_l10n
        if migration_state_l10n is not None:
            self.migration_state_l10n = migration_state_l10n
        if importable_criteria_l10n is not None:
            self.importable_criteria_l10n = importable_criteria_l10n
        if import_unity is not None:
            self.import_unity = import_unity
        if import_unity_consistency_group is not None:
            self.import_unity_consistency_group = import_unity_consistency_group

    @property
    def id(self):
        """Gets the id of this ImportUnityVolumeInstance.  # noqa: E501

        Unique identifier of the Unity volume.  # noqa: E501

        :return: The id of this ImportUnityVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImportUnityVolumeInstance.

        Unique identifier of the Unity volume.  # noqa: E501

        :param id: The id of this ImportUnityVolumeInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def wwn(self):
        """Gets the wwn of this ImportUnityVolumeInstance.  # noqa: E501

        World Wide Name (WWN) of the Unity volume.  # noqa: E501

        :return: The wwn of this ImportUnityVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._wwn

    @wwn.setter
    def wwn(self, wwn):
        """Sets the wwn of this ImportUnityVolumeInstance.

        World Wide Name (WWN) of the Unity volume.  # noqa: E501

        :param wwn: The wwn of this ImportUnityVolumeInstance.  # noqa: E501
        :type: str
        """

        self._wwn = wwn

    @property
    def name(self):
        """Gets the name of this ImportUnityVolumeInstance.  # noqa: E501

        Name of the Unity volume.  This property supports case-insensitive filtering.  # noqa: E501

        :return: The name of this ImportUnityVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImportUnityVolumeInstance.

        Name of the Unity volume.  This property supports case-insensitive filtering.  # noqa: E501

        :param name: The name of this ImportUnityVolumeInstance.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def size(self):
        """Gets the size of this ImportUnityVolumeInstance.  # noqa: E501

        Size of the Unity volume, in bytes.  # noqa: E501

        :return: The size of this ImportUnityVolumeInstance.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ImportUnityVolumeInstance.

        Size of the Unity volume, in bytes.  # noqa: E501

        :param size: The size of this ImportUnityVolumeInstance.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                size is not None and size > -9223372036854775616):  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value less than or equal to `-9223372036854775616`")  # noqa: E501
        if (self._configuration.client_side_validation and
                size is not None and size < 0):  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._size = size

    @property
    def import_unity_id(self):
        """Gets the import_unity_id of this ImportUnityVolumeInstance.  # noqa: E501

        Unique identifier of the Unity storage system to which the Unity volume belongs.  # noqa: E501

        :return: The import_unity_id of this ImportUnityVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._import_unity_id

    @import_unity_id.setter
    def import_unity_id(self, import_unity_id):
        """Sets the import_unity_id of this ImportUnityVolumeInstance.

        Unique identifier of the Unity storage system to which the Unity volume belongs.  # noqa: E501

        :param import_unity_id: The import_unity_id of this ImportUnityVolumeInstance.  # noqa: E501
        :type: str
        """

        self._import_unity_id = import_unity_id

    @property
    def import_unity_consistency_group_id(self):
        """Gets the import_unity_consistency_group_id of this ImportUnityVolumeInstance.  # noqa: E501

        Unique identifier of the consistency group to which the Unity volume belongs. This value is null if the volume does not belong to a consistency group.  # noqa: E501

        :return: The import_unity_consistency_group_id of this ImportUnityVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._import_unity_consistency_group_id

    @import_unity_consistency_group_id.setter
    def import_unity_consistency_group_id(self, import_unity_consistency_group_id):
        """Sets the import_unity_consistency_group_id of this ImportUnityVolumeInstance.

        Unique identifier of the consistency group to which the Unity volume belongs. This value is null if the volume does not belong to a consistency group.  # noqa: E501

        :param import_unity_consistency_group_id: The import_unity_consistency_group_id of this ImportUnityVolumeInstance.  # noqa: E501
        :type: str
        """

        self._import_unity_consistency_group_id = import_unity_consistency_group_id

    @property
    def health(self):
        """Gets the health of this ImportUnityVolumeInstance.  # noqa: E501


        :return: The health of this ImportUnityVolumeInstance.  # noqa: E501
        :rtype: UnityHealthEnum
        """
        return self._health

    @health.setter
    def health(self, health):
        """Sets the health of this ImportUnityVolumeInstance.


        :param health: The health of this ImportUnityVolumeInstance.  # noqa: E501
        :type: UnityHealthEnum
        """

        self._health = health

    @property
    def type(self):
        """Gets the type of this ImportUnityVolumeInstance.  # noqa: E501


        :return: The type of this ImportUnityVolumeInstance.  # noqa: E501
        :rtype: UnityVolumeTypeEnum
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ImportUnityVolumeInstance.


        :param type: The type of this ImportUnityVolumeInstance.  # noqa: E501
        :type: UnityVolumeTypeEnum
        """

        self._type = type

    @property
    def migration_state(self):
        """Gets the migration_state of this ImportUnityVolumeInstance.  # noqa: E501


        :return: The migration_state of this ImportUnityVolumeInstance.  # noqa: E501
        :rtype: UnityVolumeMigrationStateEnum
        """
        return self._migration_state

    @migration_state.setter
    def migration_state(self, migration_state):
        """Sets the migration_state of this ImportUnityVolumeInstance.


        :param migration_state: The migration_state of this ImportUnityVolumeInstance.  # noqa: E501
        :type: UnityVolumeMigrationStateEnum
        """

        self._migration_state = migration_state

    @property
    def is_replication_destination(self):
        """Gets the is_replication_destination of this ImportUnityVolumeInstance.  # noqa: E501

        Indicates whether the Unity volume is a replication destination.  # noqa: E501

        :return: The is_replication_destination of this ImportUnityVolumeInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_replication_destination

    @is_replication_destination.setter
    def is_replication_destination(self, is_replication_destination):
        """Sets the is_replication_destination of this ImportUnityVolumeInstance.

        Indicates whether the Unity volume is a replication destination.  # noqa: E501

        :param is_replication_destination: The is_replication_destination of this ImportUnityVolumeInstance.  # noqa: E501
        :type: bool
        """

        self._is_replication_destination = is_replication_destination

    @property
    def is_thin_clone(self):
        """Gets the is_thin_clone of this ImportUnityVolumeInstance.  # noqa: E501

        Indicates whether the Unity volume is a thin clone.   # noqa: E501

        :return: The is_thin_clone of this ImportUnityVolumeInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_thin_clone

    @is_thin_clone.setter
    def is_thin_clone(self, is_thin_clone):
        """Sets the is_thin_clone of this ImportUnityVolumeInstance.

        Indicates whether the Unity volume is a thin clone.   # noqa: E501

        :param is_thin_clone: The is_thin_clone of this ImportUnityVolumeInstance.  # noqa: E501
        :type: bool
        """

        self._is_thin_clone = is_thin_clone

    @property
    def importable_criteria(self):
        """Gets the importable_criteria of this ImportUnityVolumeInstance.  # noqa: E501

        Volume import criteria. If the value is not Ready, the volume is not importable and the value specifies the reason it is not importable.  # noqa: E501

        :return: The importable_criteria of this ImportUnityVolumeInstance.  # noqa: E501
        :rtype: VolumeImportableCriteriaEnum
        """
        return self._importable_criteria

    @importable_criteria.setter
    def importable_criteria(self, importable_criteria):
        """Sets the importable_criteria of this ImportUnityVolumeInstance.

        Volume import criteria. If the value is not Ready, the volume is not importable and the value specifies the reason it is not importable.  # noqa: E501

        :param importable_criteria: The importable_criteria of this ImportUnityVolumeInstance.  # noqa: E501
        :type: VolumeImportableCriteriaEnum
        """

        self._importable_criteria = importable_criteria

    @property
    def host_volume_ids(self):
        """Gets the host_volume_ids of this ImportUnityVolumeInstance.  # noqa: E501

        List of host volume identifiers that correspond to Unity volumes.  # noqa: E501

        :return: The host_volume_ids of this ImportUnityVolumeInstance.  # noqa: E501
        :rtype: list[str]
        """
        return self._host_volume_ids

    @host_volume_ids.setter
    def host_volume_ids(self, host_volume_ids):
        """Sets the host_volume_ids of this ImportUnityVolumeInstance.

        List of host volume identifiers that correspond to Unity volumes.  # noqa: E501

        :param host_volume_ids: The host_volume_ids of this ImportUnityVolumeInstance.  # noqa: E501
        :type: list[str]
        """

        self._host_volume_ids = host_volume_ids

    @property
    def health_l10n(self):
        """Gets the health_l10n of this ImportUnityVolumeInstance.  # noqa: E501

        Localized message string corresponding to health  # noqa: E501

        :return: The health_l10n of this ImportUnityVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._health_l10n

    @health_l10n.setter
    def health_l10n(self, health_l10n):
        """Sets the health_l10n of this ImportUnityVolumeInstance.

        Localized message string corresponding to health  # noqa: E501

        :param health_l10n: The health_l10n of this ImportUnityVolumeInstance.  # noqa: E501
        :type: str
        """

        self._health_l10n = health_l10n

    @property
    def type_l10n(self):
        """Gets the type_l10n of this ImportUnityVolumeInstance.  # noqa: E501

        Localized message string corresponding to type  # noqa: E501

        :return: The type_l10n of this ImportUnityVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._type_l10n

    @type_l10n.setter
    def type_l10n(self, type_l10n):
        """Sets the type_l10n of this ImportUnityVolumeInstance.

        Localized message string corresponding to type  # noqa: E501

        :param type_l10n: The type_l10n of this ImportUnityVolumeInstance.  # noqa: E501
        :type: str
        """

        self._type_l10n = type_l10n

    @property
    def migration_state_l10n(self):
        """Gets the migration_state_l10n of this ImportUnityVolumeInstance.  # noqa: E501

        Localized message string corresponding to migration_state  # noqa: E501

        :return: The migration_state_l10n of this ImportUnityVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._migration_state_l10n

    @migration_state_l10n.setter
    def migration_state_l10n(self, migration_state_l10n):
        """Sets the migration_state_l10n of this ImportUnityVolumeInstance.

        Localized message string corresponding to migration_state  # noqa: E501

        :param migration_state_l10n: The migration_state_l10n of this ImportUnityVolumeInstance.  # noqa: E501
        :type: str
        """

        self._migration_state_l10n = migration_state_l10n

    @property
    def importable_criteria_l10n(self):
        """Gets the importable_criteria_l10n of this ImportUnityVolumeInstance.  # noqa: E501

        Localized message string corresponding to importable_criteria  # noqa: E501

        :return: The importable_criteria_l10n of this ImportUnityVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._importable_criteria_l10n

    @importable_criteria_l10n.setter
    def importable_criteria_l10n(self, importable_criteria_l10n):
        """Sets the importable_criteria_l10n of this ImportUnityVolumeInstance.

        Localized message string corresponding to importable_criteria  # noqa: E501

        :param importable_criteria_l10n: The importable_criteria_l10n of this ImportUnityVolumeInstance.  # noqa: E501
        :type: str
        """

        self._importable_criteria_l10n = importable_criteria_l10n

    @property
    def import_unity(self):
        """Gets the import_unity of this ImportUnityVolumeInstance.  # noqa: E501

        This is the embeddable reference form of import_unity_id attribute.  # noqa: E501

        :return: The import_unity of this ImportUnityVolumeInstance.  # noqa: E501
        :rtype: ImportUnityInstance
        """
        return self._import_unity

    @import_unity.setter
    def import_unity(self, import_unity):
        """Sets the import_unity of this ImportUnityVolumeInstance.

        This is the embeddable reference form of import_unity_id attribute.  # noqa: E501

        :param import_unity: The import_unity of this ImportUnityVolumeInstance.  # noqa: E501
        :type: ImportUnityInstance
        """

        self._import_unity = import_unity

    @property
    def import_unity_consistency_group(self):
        """Gets the import_unity_consistency_group of this ImportUnityVolumeInstance.  # noqa: E501

        This is the embeddable reference form of import_unity_consistency_group_id attribute.  # noqa: E501

        :return: The import_unity_consistency_group of this ImportUnityVolumeInstance.  # noqa: E501
        :rtype: ImportUnityConsistencyGroupInstance
        """
        return self._import_unity_consistency_group

    @import_unity_consistency_group.setter
    def import_unity_consistency_group(self, import_unity_consistency_group):
        """Sets the import_unity_consistency_group of this ImportUnityVolumeInstance.

        This is the embeddable reference form of import_unity_consistency_group_id attribute.  # noqa: E501

        :param import_unity_consistency_group: The import_unity_consistency_group of this ImportUnityVolumeInstance.  # noqa: E501
        :type: ImportUnityConsistencyGroupInstance
        """

        self._import_unity_consistency_group = import_unity_consistency_group

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
        if issubclass(ImportUnityVolumeInstance, dict):
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
        if not isinstance(other, ImportUnityVolumeInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImportUnityVolumeInstance):
            return True

        return self.to_dict() != other.to_dict()
