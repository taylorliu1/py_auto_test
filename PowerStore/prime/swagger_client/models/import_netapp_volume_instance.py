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


class ImportNetappVolumeInstance(object):
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
        'state': 'NetAppVolumeStateEnum',
        'container_state': 'NetAppContainerStateEnum',
        'is_read_only': 'bool',
        'is_replication_destination': 'bool',
        'importable_criteria': 'VolumeImportableCriteriaEnum',
        'import_netapp_id': 'str',
        'state_l10n': 'str',
        'container_state_l10n': 'str',
        'importable_criteria_l10n': 'str',
        'import_netapp': 'ImportNetappInstance'
    }

    attribute_map = {
        'id': 'id',
        'wwn': 'wwn',
        'name': 'name',
        'size': 'size',
        'state': 'state',
        'container_state': 'container_state',
        'is_read_only': 'is_read_only',
        'is_replication_destination': 'is_replication_destination',
        'importable_criteria': 'importable_criteria',
        'import_netapp_id': 'import_netapp_id',
        'state_l10n': 'state_l10n',
        'container_state_l10n': 'container_state_l10n',
        'importable_criteria_l10n': 'importable_criteria_l10n',
        'import_netapp': 'import_netapp'
    }

    def __init__(self, id=None, wwn=None, name=None, size=None, state=None, container_state=None, is_read_only=None, is_replication_destination=None, importable_criteria=None, import_netapp_id=None, state_l10n=None, container_state_l10n=None, importable_criteria_l10n=None, import_netapp=None, _configuration=None):  # noqa: E501
        """ImportNetappVolumeInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._wwn = None
        self._name = None
        self._size = None
        self._state = None
        self._container_state = None
        self._is_read_only = None
        self._is_replication_destination = None
        self._importable_criteria = None
        self._import_netapp_id = None
        self._state_l10n = None
        self._container_state_l10n = None
        self._importable_criteria_l10n = None
        self._import_netapp = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if wwn is not None:
            self.wwn = wwn
        if name is not None:
            self.name = name
        if size is not None:
            self.size = size
        if state is not None:
            self.state = state
        if container_state is not None:
            self.container_state = container_state
        if is_read_only is not None:
            self.is_read_only = is_read_only
        if is_replication_destination is not None:
            self.is_replication_destination = is_replication_destination
        if importable_criteria is not None:
            self.importable_criteria = importable_criteria
        if import_netapp_id is not None:
            self.import_netapp_id = import_netapp_id
        if state_l10n is not None:
            self.state_l10n = state_l10n
        if container_state_l10n is not None:
            self.container_state_l10n = container_state_l10n
        if importable_criteria_l10n is not None:
            self.importable_criteria_l10n = importable_criteria_l10n
        if import_netapp is not None:
            self.import_netapp = import_netapp

    @property
    def id(self):
        """Gets the id of this ImportNetappVolumeInstance.  # noqa: E501

        Unique identifier of the NetApp volume.  # noqa: E501

        :return: The id of this ImportNetappVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImportNetappVolumeInstance.

        Unique identifier of the NetApp volume.  # noqa: E501

        :param id: The id of this ImportNetappVolumeInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def wwn(self):
        """Gets the wwn of this ImportNetappVolumeInstance.  # noqa: E501

        World Wide Name (WWN) of the NetApp volume.  # noqa: E501

        :return: The wwn of this ImportNetappVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._wwn

    @wwn.setter
    def wwn(self, wwn):
        """Sets the wwn of this ImportNetappVolumeInstance.

        World Wide Name (WWN) of the NetApp volume.  # noqa: E501

        :param wwn: The wwn of this ImportNetappVolumeInstance.  # noqa: E501
        :type: str
        """

        self._wwn = wwn

    @property
    def name(self):
        """Gets the name of this ImportNetappVolumeInstance.  # noqa: E501

        Name of the NetApp volume.  This property supports case-insensitive filtering.  # noqa: E501

        :return: The name of this ImportNetappVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImportNetappVolumeInstance.

        Name of the NetApp volume.  This property supports case-insensitive filtering.  # noqa: E501

        :param name: The name of this ImportNetappVolumeInstance.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def size(self):
        """Gets the size of this ImportNetappVolumeInstance.  # noqa: E501

        Size of the NetApp volume, in bytes.  # noqa: E501

        :return: The size of this ImportNetappVolumeInstance.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ImportNetappVolumeInstance.

        Size of the NetApp volume, in bytes.  # noqa: E501

        :param size: The size of this ImportNetappVolumeInstance.  # noqa: E501
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
    def state(self):
        """Gets the state of this ImportNetappVolumeInstance.  # noqa: E501


        :return: The state of this ImportNetappVolumeInstance.  # noqa: E501
        :rtype: NetAppVolumeStateEnum
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ImportNetappVolumeInstance.


        :param state: The state of this ImportNetappVolumeInstance.  # noqa: E501
        :type: NetAppVolumeStateEnum
        """

        self._state = state

    @property
    def container_state(self):
        """Gets the container_state of this ImportNetappVolumeInstance.  # noqa: E501


        :return: The container_state of this ImportNetappVolumeInstance.  # noqa: E501
        :rtype: NetAppContainerStateEnum
        """
        return self._container_state

    @container_state.setter
    def container_state(self, container_state):
        """Sets the container_state of this ImportNetappVolumeInstance.


        :param container_state: The container_state of this ImportNetappVolumeInstance.  # noqa: E501
        :type: NetAppContainerStateEnum
        """

        self._container_state = container_state

    @property
    def is_read_only(self):
        """Gets the is_read_only of this ImportNetappVolumeInstance.  # noqa: E501

        Indicates whether the NetApp volume is a read only volume.  # noqa: E501

        :return: The is_read_only of this ImportNetappVolumeInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_read_only

    @is_read_only.setter
    def is_read_only(self, is_read_only):
        """Sets the is_read_only of this ImportNetappVolumeInstance.

        Indicates whether the NetApp volume is a read only volume.  # noqa: E501

        :param is_read_only: The is_read_only of this ImportNetappVolumeInstance.  # noqa: E501
        :type: bool
        """

        self._is_read_only = is_read_only

    @property
    def is_replication_destination(self):
        """Gets the is_replication_destination of this ImportNetappVolumeInstance.  # noqa: E501

        Indicates whether the NetApp volume is a replication destination.  # noqa: E501

        :return: The is_replication_destination of this ImportNetappVolumeInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_replication_destination

    @is_replication_destination.setter
    def is_replication_destination(self, is_replication_destination):
        """Sets the is_replication_destination of this ImportNetappVolumeInstance.

        Indicates whether the NetApp volume is a replication destination.  # noqa: E501

        :param is_replication_destination: The is_replication_destination of this ImportNetappVolumeInstance.  # noqa: E501
        :type: bool
        """

        self._is_replication_destination = is_replication_destination

    @property
    def importable_criteria(self):
        """Gets the importable_criteria of this ImportNetappVolumeInstance.  # noqa: E501

        Indicates the reason when the volume is not importable. If the value is not Ready_For_Agentless_Import, the volume is not importable.  # noqa: E501

        :return: The importable_criteria of this ImportNetappVolumeInstance.  # noqa: E501
        :rtype: VolumeImportableCriteriaEnum
        """
        return self._importable_criteria

    @importable_criteria.setter
    def importable_criteria(self, importable_criteria):
        """Sets the importable_criteria of this ImportNetappVolumeInstance.

        Indicates the reason when the volume is not importable. If the value is not Ready_For_Agentless_Import, the volume is not importable.  # noqa: E501

        :param importable_criteria: The importable_criteria of this ImportNetappVolumeInstance.  # noqa: E501
        :type: VolumeImportableCriteriaEnum
        """

        self._importable_criteria = importable_criteria

    @property
    def import_netapp_id(self):
        """Gets the import_netapp_id of this ImportNetappVolumeInstance.  # noqa: E501

        Unique identifier of the NetApp storage system to which the NetApp volume belongs.  # noqa: E501

        :return: The import_netapp_id of this ImportNetappVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._import_netapp_id

    @import_netapp_id.setter
    def import_netapp_id(self, import_netapp_id):
        """Sets the import_netapp_id of this ImportNetappVolumeInstance.

        Unique identifier of the NetApp storage system to which the NetApp volume belongs.  # noqa: E501

        :param import_netapp_id: The import_netapp_id of this ImportNetappVolumeInstance.  # noqa: E501
        :type: str
        """

        self._import_netapp_id = import_netapp_id

    @property
    def state_l10n(self):
        """Gets the state_l10n of this ImportNetappVolumeInstance.  # noqa: E501

        Localized message string corresponding to state Was added in version 3.0.0.0.  # noqa: E501

        :return: The state_l10n of this ImportNetappVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._state_l10n

    @state_l10n.setter
    def state_l10n(self, state_l10n):
        """Sets the state_l10n of this ImportNetappVolumeInstance.

        Localized message string corresponding to state Was added in version 3.0.0.0.  # noqa: E501

        :param state_l10n: The state_l10n of this ImportNetappVolumeInstance.  # noqa: E501
        :type: str
        """

        self._state_l10n = state_l10n

    @property
    def container_state_l10n(self):
        """Gets the container_state_l10n of this ImportNetappVolumeInstance.  # noqa: E501

        Localized message string corresponding to container_state Was added in version 3.0.0.0.  # noqa: E501

        :return: The container_state_l10n of this ImportNetappVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._container_state_l10n

    @container_state_l10n.setter
    def container_state_l10n(self, container_state_l10n):
        """Sets the container_state_l10n of this ImportNetappVolumeInstance.

        Localized message string corresponding to container_state Was added in version 3.0.0.0.  # noqa: E501

        :param container_state_l10n: The container_state_l10n of this ImportNetappVolumeInstance.  # noqa: E501
        :type: str
        """

        self._container_state_l10n = container_state_l10n

    @property
    def importable_criteria_l10n(self):
        """Gets the importable_criteria_l10n of this ImportNetappVolumeInstance.  # noqa: E501

        Localized message string corresponding to importable_criteria Was added in version 3.0.0.0.  # noqa: E501

        :return: The importable_criteria_l10n of this ImportNetappVolumeInstance.  # noqa: E501
        :rtype: str
        """
        return self._importable_criteria_l10n

    @importable_criteria_l10n.setter
    def importable_criteria_l10n(self, importable_criteria_l10n):
        """Sets the importable_criteria_l10n of this ImportNetappVolumeInstance.

        Localized message string corresponding to importable_criteria Was added in version 3.0.0.0.  # noqa: E501

        :param importable_criteria_l10n: The importable_criteria_l10n of this ImportNetappVolumeInstance.  # noqa: E501
        :type: str
        """

        self._importable_criteria_l10n = importable_criteria_l10n

    @property
    def import_netapp(self):
        """Gets the import_netapp of this ImportNetappVolumeInstance.  # noqa: E501

        This is the embeddable reference form of import_netapp_id attribute.  # noqa: E501

        :return: The import_netapp of this ImportNetappVolumeInstance.  # noqa: E501
        :rtype: ImportNetappInstance
        """
        return self._import_netapp

    @import_netapp.setter
    def import_netapp(self, import_netapp):
        """Sets the import_netapp of this ImportNetappVolumeInstance.

        This is the embeddable reference form of import_netapp_id attribute.  # noqa: E501

        :param import_netapp: The import_netapp of this ImportNetappVolumeInstance.  # noqa: E501
        :type: ImportNetappInstance
        """

        self._import_netapp = import_netapp

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
        if issubclass(ImportNetappVolumeInstance, dict):
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
        if not isinstance(other, ImportNetappVolumeInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImportNetappVolumeInstance):
            return True

        return self.to_dict() != other.to_dict()
