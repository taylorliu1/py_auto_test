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


class ImportStorageCenterVolumeInstance(object):
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
        'size': 'int',
        'wwn': 'str',
        'health': 'SCStatusEnum',
        'is_active': 'bool',
        'import_storage_center_id': 'str',
        'migration_state': 'MigrationStateEnum',
        'is_read_only': 'bool',
        'importable_criteria': 'VolumeImportableCriteriaEnum',
        'host_volume_ids': 'list[str]',
        'import_storage_center_consistency_group_id': 'str',
        'import_storage_center_consistency_group_names': 'list[str]',
        'health_l10n': 'str',
        'migration_state_l10n': 'str',
        'importable_criteria_l10n': 'str',
        'import_storage_center': 'ImportStorageCenterInstance',
        'import_storage_center_consistency_group': 'ImportStorageCenterConsistencyGroupInstance'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'size': 'size',
        'wwn': 'wwn',
        'health': 'health',
        'is_active': 'is_active',
        'import_storage_center_id': 'import_storage_center_id',
        'migration_state': 'migration_state',
        'is_read_only': 'is_read_only',
        'importable_criteria': 'importable_criteria',
        'host_volume_ids': 'host_volume_ids',
        'import_storage_center_consistency_group_id': 'import_storage_center_consistency_group_id',
        'import_storage_center_consistency_group_names': 'import_storage_center_consistency_group_names',
        'health_l10n': 'health_l10n',
        'migration_state_l10n': 'migration_state_l10n',
        'importable_criteria_l10n': 'importable_criteria_l10n',
        'import_storage_center': 'import_storage_center',
        'import_storage_center_consistency_group': 'import_storage_center_consistency_group'
    }

    def __init__(self, id=None, name=None, size=None, wwn=None, health=None, is_active=None, import_storage_center_id=None, migration_state=None, is_read_only=None, importable_criteria=None, host_volume_ids=None, import_storage_center_consistency_group_id=None, import_storage_center_consistency_group_names=None, health_l10n=None, migration_state_l10n=None, importable_criteria_l10n=None, import_storage_center=None, import_storage_center_consistency_group=None, _configuration=None):  # noqa: E501
        """ImportStorageCenterVolumeInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._size = None
        self._wwn = None
        self._health = None
        self._is_active = None
        self._import_storage_center_id = None
        self._migration_state = None
        self._is_read_only = None
        self._importable_criteria = None
        self._host_volume_ids = None
        self._import_storage_center_consistency_group_id = None
        self._import_storage_center_consistency_group_names = None
        self._health_l10n = None
        self._migration_state_l10n = None
        self._importable_criteria_l10n = None
        self._import_storage_center = None
        self._import_storage_center_consistency_group = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if size is not None:
            self.size = size
        if wwn is not None:
            self.wwn = wwn
        if health is not None:
            self.health = health
        if is_active is not None:
            self.is_active = is_active
        if import_storage_center_id is not None:
            self.import_storage_center_id = import_storage_center_id
        if migration_state is not None:
            self.migration_state = migration_state
        if is_read_only is not None:
            self.is_read_only = is_read_only
        if importable_criteria is not None:
            self.importable_criteria = importable_criteria
        if host_volume_ids is not None:
            self.host_volume_ids = host_volume_ids
        if import_storage_center_consistency_group_id is not None:
            self.import_storage_center_consistency_group_id = import_storage_center_consistency_group_id
        if import_storage_center_consistency_group_names is not None:
            self.import_storage_center_consistency_group_names = import_storage_center_consistency_group_names
        if health_l10n is not None:
            self.health_l10n = health_l10n
        if migration_state_l10n is not None:
            self.migration_state_l10n = migration_state_l10n
        if importable_criteria_l10n is not None:
            self.importable_criteria_l10n = importable_criteria_l10n
        if import_storage_center is not None:
            self.import_storage_center = import_storage_center
        if import_storage_center_consistency_group is not None:
            self.import_storage_center_consistency_group = import_storage_center_consistency_group

    @property
    def id(self):
        """Gets the id of this ImportStorageCenterVolumeInstance.  # noqa: E501

        Unique identifier of the SC volume.  # noqa: E501

        :return: The id of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImportStorageCenterVolumeInstance.

        Unique identifier of the SC volume.  # noqa: E501

        :param id: The id of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ImportStorageCenterVolumeInstance.  # noqa: E501

        Name of the SC volume.  This property supports case-insensitive filtering.  # noqa: E501

        :return: The name of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImportStorageCenterVolumeInstance.

        Name of the SC volume.  This property supports case-insensitive filtering.  # noqa: E501

        :param name: The name of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def size(self):
        """Gets the size of this ImportStorageCenterVolumeInstance.  # noqa: E501

        Size of the SC volume, in bytes.  # noqa: E501

        :return: The size of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ImportStorageCenterVolumeInstance.

        Size of the SC volume, in bytes.  # noqa: E501

        :param size: The size of this ImportStorageCenterVolumeInstance.  # noqa: E501
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
    def wwn(self):
        """Gets the wwn of this ImportStorageCenterVolumeInstance.  # noqa: E501

        Device identifier presented to the server to which the volume is mapped.  # noqa: E501

        :return: The wwn of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._wwn

    @wwn.setter
    def wwn(self, wwn):
        """Sets the wwn of this ImportStorageCenterVolumeInstance.

        Device identifier presented to the server to which the volume is mapped.  # noqa: E501

        :param wwn: The wwn of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :type: str
        """

        self._wwn = wwn

    @property
    def health(self):
        """Gets the health of this ImportStorageCenterVolumeInstance.  # noqa: E501


        :return: The health of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :rtype: SCStatusEnum
        """
        return self._health

    @health.setter
    def health(self, health):
        """Sets the health of this ImportStorageCenterVolumeInstance.


        :param health: The health of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :type: SCStatusEnum
        """

        self._health = health

    @property
    def is_active(self):
        """Gets the is_active of this ImportStorageCenterVolumeInstance.  # noqa: E501

        Indicates whether the SC volume is active on any controller. Only volumes that are active are importable.  # noqa: E501

        :return: The is_active of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this ImportStorageCenterVolumeInstance.

        Indicates whether the SC volume is active on any controller. Only volumes that are active are importable.  # noqa: E501

        :param is_active: The is_active of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def import_storage_center_id(self):
        """Gets the import_storage_center_id of this ImportStorageCenterVolumeInstance.  # noqa: E501

        Unique identifier of the SC array where the volume resides.  # noqa: E501

        :return: The import_storage_center_id of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._import_storage_center_id

    @import_storage_center_id.setter
    def import_storage_center_id(self, import_storage_center_id):
        """Sets the import_storage_center_id of this ImportStorageCenterVolumeInstance.

        Unique identifier of the SC array where the volume resides.  # noqa: E501

        :param import_storage_center_id: The import_storage_center_id of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :type: str
        """

        self._import_storage_center_id = import_storage_center_id

    @property
    def migration_state(self):
        """Gets the migration_state of this ImportStorageCenterVolumeInstance.  # noqa: E501


        :return: The migration_state of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :rtype: MigrationStateEnum
        """
        return self._migration_state

    @migration_state.setter
    def migration_state(self, migration_state):
        """Sets the migration_state of this ImportStorageCenterVolumeInstance.


        :param migration_state: The migration_state of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :type: MigrationStateEnum
        """

        self._migration_state = migration_state

    @property
    def is_read_only(self):
        """Gets the is_read_only of this ImportStorageCenterVolumeInstance.  # noqa: E501

        Indicates whether the volume is read-only.  # noqa: E501

        :return: The is_read_only of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_read_only

    @is_read_only.setter
    def is_read_only(self, is_read_only):
        """Sets the is_read_only of this ImportStorageCenterVolumeInstance.

        Indicates whether the volume is read-only.  # noqa: E501

        :param is_read_only: The is_read_only of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :type: bool
        """

        self._is_read_only = is_read_only

    @property
    def importable_criteria(self):
        """Gets the importable_criteria of this ImportStorageCenterVolumeInstance.  # noqa: E501

        Volume import criteria. If the value is not Ready, the volume is not importable.  # noqa: E501

        :return: The importable_criteria of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :rtype: VolumeImportableCriteriaEnum
        """
        return self._importable_criteria

    @importable_criteria.setter
    def importable_criteria(self, importable_criteria):
        """Sets the importable_criteria of this ImportStorageCenterVolumeInstance.

        Volume import criteria. If the value is not Ready, the volume is not importable.  # noqa: E501

        :param importable_criteria: The importable_criteria of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :type: VolumeImportableCriteriaEnum
        """

        self._importable_criteria = importable_criteria

    @property
    def host_volume_ids(self):
        """Gets the host_volume_ids of this ImportStorageCenterVolumeInstance.  # noqa: E501

        List of host volume identifiers that correspond to SC volumes.  # noqa: E501

        :return: The host_volume_ids of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :rtype: list[str]
        """
        return self._host_volume_ids

    @host_volume_ids.setter
    def host_volume_ids(self, host_volume_ids):
        """Sets the host_volume_ids of this ImportStorageCenterVolumeInstance.

        List of host volume identifiers that correspond to SC volumes.  # noqa: E501

        :param host_volume_ids: The host_volume_ids of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :type: list[str]
        """

        self._host_volume_ids = host_volume_ids

    @property
    def import_storage_center_consistency_group_id(self):
        """Gets the import_storage_center_consistency_group_id of this ImportStorageCenterVolumeInstance.  # noqa: E501

        Unique identifier of an SC consistency group, if the volume is part of one consistency group only. If the volume is part of multiple consistency groups, the attribute is empty.  # noqa: E501

        :return: The import_storage_center_consistency_group_id of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._import_storage_center_consistency_group_id

    @import_storage_center_consistency_group_id.setter
    def import_storage_center_consistency_group_id(self, import_storage_center_consistency_group_id):
        """Sets the import_storage_center_consistency_group_id of this ImportStorageCenterVolumeInstance.

        Unique identifier of an SC consistency group, if the volume is part of one consistency group only. If the volume is part of multiple consistency groups, the attribute is empty.  # noqa: E501

        :param import_storage_center_consistency_group_id: The import_storage_center_consistency_group_id of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :type: str
        """

        self._import_storage_center_consistency_group_id = import_storage_center_consistency_group_id

    @property
    def import_storage_center_consistency_group_names(self):
        """Gets the import_storage_center_consistency_group_names of this ImportStorageCenterVolumeInstance.  # noqa: E501

        Names of the consistency groups of which the volume is a member, if this volume is in multiple consistency groups.  # noqa: E501

        :return: The import_storage_center_consistency_group_names of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :rtype: list[str]
        """
        return self._import_storage_center_consistency_group_names

    @import_storage_center_consistency_group_names.setter
    def import_storage_center_consistency_group_names(self, import_storage_center_consistency_group_names):
        """Sets the import_storage_center_consistency_group_names of this ImportStorageCenterVolumeInstance.

        Names of the consistency groups of which the volume is a member, if this volume is in multiple consistency groups.  # noqa: E501

        :param import_storage_center_consistency_group_names: The import_storage_center_consistency_group_names of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :type: list[str]
        """

        self._import_storage_center_consistency_group_names = import_storage_center_consistency_group_names

    @property
    def health_l10n(self):
        """Gets the health_l10n of this ImportStorageCenterVolumeInstance.  # noqa: E501

        Localized message string corresponding to health  # noqa: E501

        :return: The health_l10n of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._health_l10n

    @health_l10n.setter
    def health_l10n(self, health_l10n):
        """Sets the health_l10n of this ImportStorageCenterVolumeInstance.

        Localized message string corresponding to health  # noqa: E501

        :param health_l10n: The health_l10n of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :type: str
        """

        self._health_l10n = health_l10n

    @property
    def migration_state_l10n(self):
        """Gets the migration_state_l10n of this ImportStorageCenterVolumeInstance.  # noqa: E501

        Localized message string corresponding to migration_state  # noqa: E501

        :return: The migration_state_l10n of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._migration_state_l10n

    @migration_state_l10n.setter
    def migration_state_l10n(self, migration_state_l10n):
        """Sets the migration_state_l10n of this ImportStorageCenterVolumeInstance.

        Localized message string corresponding to migration_state  # noqa: E501

        :param migration_state_l10n: The migration_state_l10n of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :type: str
        """

        self._migration_state_l10n = migration_state_l10n

    @property
    def importable_criteria_l10n(self):
        """Gets the importable_criteria_l10n of this ImportStorageCenterVolumeInstance.  # noqa: E501

        Localized message string corresponding to importable_criteria  # noqa: E501

        :return: The importable_criteria_l10n of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._importable_criteria_l10n

    @importable_criteria_l10n.setter
    def importable_criteria_l10n(self, importable_criteria_l10n):
        """Sets the importable_criteria_l10n of this ImportStorageCenterVolumeInstance.

        Localized message string corresponding to importable_criteria  # noqa: E501

        :param importable_criteria_l10n: The importable_criteria_l10n of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :type: str
        """

        self._importable_criteria_l10n = importable_criteria_l10n

    @property
    def import_storage_center(self):
        """Gets the import_storage_center of this ImportStorageCenterVolumeInstance.  # noqa: E501

        This is the embeddable reference form of import_storage_center_id attribute.  # noqa: E501

        :return: The import_storage_center of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :rtype: ImportStorageCenterInstance
        """
        return self._import_storage_center

    @import_storage_center.setter
    def import_storage_center(self, import_storage_center):
        """Sets the import_storage_center of this ImportStorageCenterVolumeInstance.

        This is the embeddable reference form of import_storage_center_id attribute.  # noqa: E501

        :param import_storage_center: The import_storage_center of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :type: ImportStorageCenterInstance
        """

        self._import_storage_center = import_storage_center

    @property
    def import_storage_center_consistency_group(self):
        """Gets the import_storage_center_consistency_group of this ImportStorageCenterVolumeInstance.  # noqa: E501

        This is the embeddable reference form of import_storage_center_consistency_group_id attribute.  # noqa: E501

        :return: The import_storage_center_consistency_group of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :rtype: ImportStorageCenterConsistencyGroupInstance
        """
        return self._import_storage_center_consistency_group

    @import_storage_center_consistency_group.setter
    def import_storage_center_consistency_group(self, import_storage_center_consistency_group):
        """Sets the import_storage_center_consistency_group of this ImportStorageCenterVolumeInstance.

        This is the embeddable reference form of import_storage_center_consistency_group_id attribute.  # noqa: E501

        :param import_storage_center_consistency_group: The import_storage_center_consistency_group of this ImportStorageCenterVolumeInstance.  # noqa: E501
        :type: ImportStorageCenterConsistencyGroupInstance
        """

        self._import_storage_center_consistency_group = import_storage_center_consistency_group

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
        if issubclass(ImportStorageCenterVolumeInstance, dict):
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
        if not isinstance(other, ImportStorageCenterVolumeInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImportStorageCenterVolumeInstance):
            return True

        return self.to_dict() != other.to_dict()
