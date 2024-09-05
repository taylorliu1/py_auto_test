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


class ImportUnityInstance(object):
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
        'management_address': 'str',
        'model': 'str',
        'software_version': 'str',
        'api_version': 'str',
        'health': 'UnityHealthEnum',
        'user_name': 'str',
        'serial_number': 'str',
        'last_updated_timestamp': 'datetime',
        'supported_import_type': 'SupportedImportTypeEnum',
        'health_l10n': 'str',
        'supported_import_type_l10n': 'str',
        'import_unity_volumes': 'list[ImportUnityVolumeInstance]',
        'import_unity_consistency_groups': 'list[ImportUnityConsistencyGroupInstance]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'management_address': 'management_address',
        'model': 'model',
        'software_version': 'software_version',
        'api_version': 'api_version',
        'health': 'health',
        'user_name': 'user_name',
        'serial_number': 'serial_number',
        'last_updated_timestamp': 'last_updated_timestamp',
        'supported_import_type': 'supported_import_type',
        'health_l10n': 'health_l10n',
        'supported_import_type_l10n': 'supported_import_type_l10n',
        'import_unity_volumes': 'import_unity_volumes',
        'import_unity_consistency_groups': 'import_unity_consistency_groups'
    }

    def __init__(self, id=None, name=None, management_address=None, model=None, software_version=None, api_version=None, health=None, user_name=None, serial_number=None, last_updated_timestamp=None, supported_import_type=None, health_l10n=None, supported_import_type_l10n=None, import_unity_volumes=None, import_unity_consistency_groups=None, _configuration=None):  # noqa: E501
        """ImportUnityInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._management_address = None
        self._model = None
        self._software_version = None
        self._api_version = None
        self._health = None
        self._user_name = None
        self._serial_number = None
        self._last_updated_timestamp = None
        self._supported_import_type = None
        self._health_l10n = None
        self._supported_import_type_l10n = None
        self._import_unity_volumes = None
        self._import_unity_consistency_groups = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if management_address is not None:
            self.management_address = management_address
        if model is not None:
            self.model = model
        if software_version is not None:
            self.software_version = software_version
        if api_version is not None:
            self.api_version = api_version
        if health is not None:
            self.health = health
        if user_name is not None:
            self.user_name = user_name
        if serial_number is not None:
            self.serial_number = serial_number
        if last_updated_timestamp is not None:
            self.last_updated_timestamp = last_updated_timestamp
        if supported_import_type is not None:
            self.supported_import_type = supported_import_type
        if health_l10n is not None:
            self.health_l10n = health_l10n
        if supported_import_type_l10n is not None:
            self.supported_import_type_l10n = supported_import_type_l10n
        if import_unity_volumes is not None:
            self.import_unity_volumes = import_unity_volumes
        if import_unity_consistency_groups is not None:
            self.import_unity_consistency_groups = import_unity_consistency_groups

    @property
    def id(self):
        """Gets the id of this ImportUnityInstance.  # noqa: E501

        Unique identifier of the Unity storage system that is a source storage system for import. This is the serial number of the storage system.  # noqa: E501

        :return: The id of this ImportUnityInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImportUnityInstance.

        Unique identifier of the Unity storage system that is a source storage system for import. This is the serial number of the storage system.  # noqa: E501

        :param id: The id of this ImportUnityInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ImportUnityInstance.  # noqa: E501

        Name of the Unity storage system.  This property supports case-insensitive filtering.  # noqa: E501

        :return: The name of this ImportUnityInstance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImportUnityInstance.

        Name of the Unity storage system.  This property supports case-insensitive filtering.  # noqa: E501

        :param name: The name of this ImportUnityInstance.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def management_address(self):
        """Gets the management_address of this ImportUnityInstance.  # noqa: E501

        Management address to use for communicating with the Unity storage system. The address can be an IPv4 address or FQDN (Fully Qualified Domain Name).  # noqa: E501

        :return: The management_address of this ImportUnityInstance.  # noqa: E501
        :rtype: str
        """
        return self._management_address

    @management_address.setter
    def management_address(self, management_address):
        """Sets the management_address of this ImportUnityInstance.

        Management address to use for communicating with the Unity storage system. The address can be an IPv4 address or FQDN (Fully Qualified Domain Name).  # noqa: E501

        :param management_address: The management_address of this ImportUnityInstance.  # noqa: E501
        :type: str
        """

        self._management_address = management_address

    @property
    def model(self):
        """Gets the model of this ImportUnityInstance.  # noqa: E501

        Model name of the Unity storage system.  # noqa: E501

        :return: The model of this ImportUnityInstance.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ImportUnityInstance.

        Model name of the Unity storage system.  # noqa: E501

        :param model: The model of this ImportUnityInstance.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def software_version(self):
        """Gets the software_version of this ImportUnityInstance.  # noqa: E501

        Software version of the Unity storage system.  # noqa: E501

        :return: The software_version of this ImportUnityInstance.  # noqa: E501
        :rtype: str
        """
        return self._software_version

    @software_version.setter
    def software_version(self, software_version):
        """Sets the software_version of this ImportUnityInstance.

        Software version of the Unity storage system.  # noqa: E501

        :param software_version: The software_version of this ImportUnityInstance.  # noqa: E501
        :type: str
        """

        self._software_version = software_version

    @property
    def api_version(self):
        """Gets the api_version of this ImportUnityInstance.  # noqa: E501

        Version of the API that the Unity storage system supports.  # noqa: E501

        :return: The api_version of this ImportUnityInstance.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this ImportUnityInstance.

        Version of the API that the Unity storage system supports.  # noqa: E501

        :param api_version: The api_version of this ImportUnityInstance.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def health(self):
        """Gets the health of this ImportUnityInstance.  # noqa: E501


        :return: The health of this ImportUnityInstance.  # noqa: E501
        :rtype: UnityHealthEnum
        """
        return self._health

    @health.setter
    def health(self, health):
        """Sets the health of this ImportUnityInstance.


        :param health: The health of this ImportUnityInstance.  # noqa: E501
        :type: UnityHealthEnum
        """

        self._health = health

    @property
    def user_name(self):
        """Gets the user_name of this ImportUnityInstance.  # noqa: E501

        User account name used to communicate with the Unity storage system.  # noqa: E501

        :return: The user_name of this ImportUnityInstance.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ImportUnityInstance.

        User account name used to communicate with the Unity storage system.  # noqa: E501

        :param user_name: The user_name of this ImportUnityInstance.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def serial_number(self):
        """Gets the serial_number of this ImportUnityInstance.  # noqa: E501

        Serial number of the system  # noqa: E501

        :return: The serial_number of this ImportUnityInstance.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this ImportUnityInstance.

        Serial number of the system  # noqa: E501

        :param serial_number: The serial_number of this ImportUnityInstance.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def last_updated_timestamp(self):
        """Gets the last_updated_timestamp of this ImportUnityInstance.  # noqa: E501

        Date and time when the Unity storage system details were last updated. These details include the Unity storage system and information about its importable volumes and consistency groups. The timestamp is updated when the Unity storage system is created and whenever the importable volumes and consistency groups are discovered.  # noqa: E501

        :return: The last_updated_timestamp of this ImportUnityInstance.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated_timestamp

    @last_updated_timestamp.setter
    def last_updated_timestamp(self, last_updated_timestamp):
        """Sets the last_updated_timestamp of this ImportUnityInstance.

        Date and time when the Unity storage system details were last updated. These details include the Unity storage system and information about its importable volumes and consistency groups. The timestamp is updated when the Unity storage system is created and whenever the importable volumes and consistency groups are discovered.  # noqa: E501

        :param last_updated_timestamp: The last_updated_timestamp of this ImportUnityInstance.  # noqa: E501
        :type: datetime
        """

        self._last_updated_timestamp = last_updated_timestamp

    @property
    def supported_import_type(self):
        """Gets the supported_import_type of this ImportUnityInstance.  # noqa: E501

         Was added in version 1.0.2.  # noqa: E501

        :return: The supported_import_type of this ImportUnityInstance.  # noqa: E501
        :rtype: SupportedImportTypeEnum
        """
        return self._supported_import_type

    @supported_import_type.setter
    def supported_import_type(self, supported_import_type):
        """Sets the supported_import_type of this ImportUnityInstance.

         Was added in version 1.0.2.  # noqa: E501

        :param supported_import_type: The supported_import_type of this ImportUnityInstance.  # noqa: E501
        :type: SupportedImportTypeEnum
        """

        self._supported_import_type = supported_import_type

    @property
    def health_l10n(self):
        """Gets the health_l10n of this ImportUnityInstance.  # noqa: E501

        Localized message string corresponding to health  # noqa: E501

        :return: The health_l10n of this ImportUnityInstance.  # noqa: E501
        :rtype: str
        """
        return self._health_l10n

    @health_l10n.setter
    def health_l10n(self, health_l10n):
        """Sets the health_l10n of this ImportUnityInstance.

        Localized message string corresponding to health  # noqa: E501

        :param health_l10n: The health_l10n of this ImportUnityInstance.  # noqa: E501
        :type: str
        """

        self._health_l10n = health_l10n

    @property
    def supported_import_type_l10n(self):
        """Gets the supported_import_type_l10n of this ImportUnityInstance.  # noqa: E501

        Localized message string corresponding to supported_import_type Was added in version 1.0.2.  # noqa: E501

        :return: The supported_import_type_l10n of this ImportUnityInstance.  # noqa: E501
        :rtype: str
        """
        return self._supported_import_type_l10n

    @supported_import_type_l10n.setter
    def supported_import_type_l10n(self, supported_import_type_l10n):
        """Sets the supported_import_type_l10n of this ImportUnityInstance.

        Localized message string corresponding to supported_import_type Was added in version 1.0.2.  # noqa: E501

        :param supported_import_type_l10n: The supported_import_type_l10n of this ImportUnityInstance.  # noqa: E501
        :type: str
        """

        self._supported_import_type_l10n = supported_import_type_l10n

    @property
    def import_unity_volumes(self):
        """Gets the import_unity_volumes of this ImportUnityInstance.  # noqa: E501

        This is the inverse of the resource type import_unity_volume association.  # noqa: E501

        :return: The import_unity_volumes of this ImportUnityInstance.  # noqa: E501
        :rtype: list[ImportUnityVolumeInstance]
        """
        return self._import_unity_volumes

    @import_unity_volumes.setter
    def import_unity_volumes(self, import_unity_volumes):
        """Sets the import_unity_volumes of this ImportUnityInstance.

        This is the inverse of the resource type import_unity_volume association.  # noqa: E501

        :param import_unity_volumes: The import_unity_volumes of this ImportUnityInstance.  # noqa: E501
        :type: list[ImportUnityVolumeInstance]
        """

        self._import_unity_volumes = import_unity_volumes

    @property
    def import_unity_consistency_groups(self):
        """Gets the import_unity_consistency_groups of this ImportUnityInstance.  # noqa: E501

        This is the inverse of the resource type import_unity_consistency_group association.  # noqa: E501

        :return: The import_unity_consistency_groups of this ImportUnityInstance.  # noqa: E501
        :rtype: list[ImportUnityConsistencyGroupInstance]
        """
        return self._import_unity_consistency_groups

    @import_unity_consistency_groups.setter
    def import_unity_consistency_groups(self, import_unity_consistency_groups):
        """Sets the import_unity_consistency_groups of this ImportUnityInstance.

        This is the inverse of the resource type import_unity_consistency_group association.  # noqa: E501

        :param import_unity_consistency_groups: The import_unity_consistency_groups of this ImportUnityInstance.  # noqa: E501
        :type: list[ImportUnityConsistencyGroupInstance]
        """

        self._import_unity_consistency_groups = import_unity_consistency_groups

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
        if issubclass(ImportUnityInstance, dict):
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
        if not isinstance(other, ImportUnityInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImportUnityInstance):
            return True

        return self.to_dict() != other.to_dict()
