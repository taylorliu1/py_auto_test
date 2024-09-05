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


class ImportVnxArrayInstance(object):
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
        'serial_number': 'str',
        'management_address': 'str',
        'alternate_management_address': 'str',
        'user_name': 'str',
        'model': 'str',
        'is_faulted': 'bool',
        'last_updated_timestamp': 'datetime',
        'software_version': 'str',
        'supported_import_type': 'SupportedImportTypeEnum',
        'supported_import_type_l10n': 'str',
        'import_vnx_volumes': 'list[ImportVnxVolumeInstance]',
        'import_vnx_consistency_groups': 'list[ImportVnxConsistencyGroupInstance]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'serial_number': 'serial_number',
        'management_address': 'management_address',
        'alternate_management_address': 'alternate_management_address',
        'user_name': 'user_name',
        'model': 'model',
        'is_faulted': 'is_faulted',
        'last_updated_timestamp': 'last_updated_timestamp',
        'software_version': 'software_version',
        'supported_import_type': 'supported_import_type',
        'supported_import_type_l10n': 'supported_import_type_l10n',
        'import_vnx_volumes': 'import_vnx_volumes',
        'import_vnx_consistency_groups': 'import_vnx_consistency_groups'
    }

    def __init__(self, id=None, name=None, serial_number=None, management_address=None, alternate_management_address=None, user_name=None, model=None, is_faulted=None, last_updated_timestamp=None, software_version=None, supported_import_type=None, supported_import_type_l10n=None, import_vnx_volumes=None, import_vnx_consistency_groups=None, _configuration=None):  # noqa: E501
        """ImportVnxArrayInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._serial_number = None
        self._management_address = None
        self._alternate_management_address = None
        self._user_name = None
        self._model = None
        self._is_faulted = None
        self._last_updated_timestamp = None
        self._software_version = None
        self._supported_import_type = None
        self._supported_import_type_l10n = None
        self._import_vnx_volumes = None
        self._import_vnx_consistency_groups = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if serial_number is not None:
            self.serial_number = serial_number
        if management_address is not None:
            self.management_address = management_address
        if alternate_management_address is not None:
            self.alternate_management_address = alternate_management_address
        if user_name is not None:
            self.user_name = user_name
        if model is not None:
            self.model = model
        if is_faulted is not None:
            self.is_faulted = is_faulted
        if last_updated_timestamp is not None:
            self.last_updated_timestamp = last_updated_timestamp
        if software_version is not None:
            self.software_version = software_version
        if supported_import_type is not None:
            self.supported_import_type = supported_import_type
        if supported_import_type_l10n is not None:
            self.supported_import_type_l10n = supported_import_type_l10n
        if import_vnx_volumes is not None:
            self.import_vnx_volumes = import_vnx_volumes
        if import_vnx_consistency_groups is not None:
            self.import_vnx_consistency_groups = import_vnx_consistency_groups

    @property
    def id(self):
        """Gets the id of this ImportVnxArrayInstance.  # noqa: E501

        Unique identifier of the VNX storage system.  # noqa: E501

        :return: The id of this ImportVnxArrayInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImportVnxArrayInstance.

        Unique identifier of the VNX storage system.  # noqa: E501

        :param id: The id of this ImportVnxArrayInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ImportVnxArrayInstance.  # noqa: E501

        Name of the VNX storage system.  This property supports case-insensitive filtering.  # noqa: E501

        :return: The name of this ImportVnxArrayInstance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImportVnxArrayInstance.

        Name of the VNX storage system.  This property supports case-insensitive filtering.  # noqa: E501

        :param name: The name of this ImportVnxArrayInstance.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def serial_number(self):
        """Gets the serial_number of this ImportVnxArrayInstance.  # noqa: E501

        Serial number of the VNX storage system.  # noqa: E501

        :return: The serial_number of this ImportVnxArrayInstance.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this ImportVnxArrayInstance.

        Serial number of the VNX storage system.  # noqa: E501

        :param serial_number: The serial_number of this ImportVnxArrayInstance.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def management_address(self):
        """Gets the management_address of this ImportVnxArrayInstance.  # noqa: E501

        Management address for communicating with the VNX storage system. This is usually the address of Storage Processor A (SPA). The address can be an IPv4 address or FQDN (Fully Qualified Domain Name).  # noqa: E501

        :return: The management_address of this ImportVnxArrayInstance.  # noqa: E501
        :rtype: str
        """
        return self._management_address

    @management_address.setter
    def management_address(self, management_address):
        """Sets the management_address of this ImportVnxArrayInstance.

        Management address for communicating with the VNX storage system. This is usually the address of Storage Processor A (SPA). The address can be an IPv4 address or FQDN (Fully Qualified Domain Name).  # noqa: E501

        :param management_address: The management_address of this ImportVnxArrayInstance.  # noqa: E501
        :type: str
        """

        self._management_address = management_address

    @property
    def alternate_management_address(self):
        """Gets the alternate_management_address of this ImportVnxArrayInstance.  # noqa: E501

        Alternate management address for communicating with the VNX storage system. This is usually the address of Storage Processor B (SPB). The address can be an IPv4 address or FQDN (Fully Qualified Domain Name).  # noqa: E501

        :return: The alternate_management_address of this ImportVnxArrayInstance.  # noqa: E501
        :rtype: str
        """
        return self._alternate_management_address

    @alternate_management_address.setter
    def alternate_management_address(self, alternate_management_address):
        """Sets the alternate_management_address of this ImportVnxArrayInstance.

        Alternate management address for communicating with the VNX storage system. This is usually the address of Storage Processor B (SPB). The address can be an IPv4 address or FQDN (Fully Qualified Domain Name).  # noqa: E501

        :param alternate_management_address: The alternate_management_address of this ImportVnxArrayInstance.  # noqa: E501
        :type: str
        """

        self._alternate_management_address = alternate_management_address

    @property
    def user_name(self):
        """Gets the user_name of this ImportVnxArrayInstance.  # noqa: E501

        User account name used to communicate with the VNX storage system.  # noqa: E501

        :return: The user_name of this ImportVnxArrayInstance.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ImportVnxArrayInstance.

        User account name used to communicate with the VNX storage system.  # noqa: E501

        :param user_name: The user_name of this ImportVnxArrayInstance.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def model(self):
        """Gets the model of this ImportVnxArrayInstance.  # noqa: E501

        Model name of the VNX storage system.  # noqa: E501

        :return: The model of this ImportVnxArrayInstance.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ImportVnxArrayInstance.

        Model name of the VNX storage system.  # noqa: E501

        :param model: The model of this ImportVnxArrayInstance.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def is_faulted(self):
        """Gets the is_faulted of this ImportVnxArrayInstance.  # noqa: E501

        Indicates whether the VNX storage system is faulted.  # noqa: E501

        :return: The is_faulted of this ImportVnxArrayInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_faulted

    @is_faulted.setter
    def is_faulted(self, is_faulted):
        """Sets the is_faulted of this ImportVnxArrayInstance.

        Indicates whether the VNX storage system is faulted.  # noqa: E501

        :param is_faulted: The is_faulted of this ImportVnxArrayInstance.  # noqa: E501
        :type: bool
        """

        self._is_faulted = is_faulted

    @property
    def last_updated_timestamp(self):
        """Gets the last_updated_timestamp of this ImportVnxArrayInstance.  # noqa: E501

        Timestamp at which the VNX storage system details were last updated. These details include information about the VNX storage system and its importable volumes and consistency groups. The timestamp is updated when the VNX storage system is created and when the importable storage resources are discovered using the discover action.  # noqa: E501

        :return: The last_updated_timestamp of this ImportVnxArrayInstance.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated_timestamp

    @last_updated_timestamp.setter
    def last_updated_timestamp(self, last_updated_timestamp):
        """Sets the last_updated_timestamp of this ImportVnxArrayInstance.

        Timestamp at which the VNX storage system details were last updated. These details include information about the VNX storage system and its importable volumes and consistency groups. The timestamp is updated when the VNX storage system is created and when the importable storage resources are discovered using the discover action.  # noqa: E501

        :param last_updated_timestamp: The last_updated_timestamp of this ImportVnxArrayInstance.  # noqa: E501
        :type: datetime
        """

        self._last_updated_timestamp = last_updated_timestamp

    @property
    def software_version(self):
        """Gets the software_version of this ImportVnxArrayInstance.  # noqa: E501

        The software version of the block operating environment of the VNX storage system.  # noqa: E501

        :return: The software_version of this ImportVnxArrayInstance.  # noqa: E501
        :rtype: str
        """
        return self._software_version

    @software_version.setter
    def software_version(self, software_version):
        """Sets the software_version of this ImportVnxArrayInstance.

        The software version of the block operating environment of the VNX storage system.  # noqa: E501

        :param software_version: The software_version of this ImportVnxArrayInstance.  # noqa: E501
        :type: str
        """

        self._software_version = software_version

    @property
    def supported_import_type(self):
        """Gets the supported_import_type of this ImportVnxArrayInstance.  # noqa: E501

         Was added in version 1.0.2.  # noqa: E501

        :return: The supported_import_type of this ImportVnxArrayInstance.  # noqa: E501
        :rtype: SupportedImportTypeEnum
        """
        return self._supported_import_type

    @supported_import_type.setter
    def supported_import_type(self, supported_import_type):
        """Sets the supported_import_type of this ImportVnxArrayInstance.

         Was added in version 1.0.2.  # noqa: E501

        :param supported_import_type: The supported_import_type of this ImportVnxArrayInstance.  # noqa: E501
        :type: SupportedImportTypeEnum
        """

        self._supported_import_type = supported_import_type

    @property
    def supported_import_type_l10n(self):
        """Gets the supported_import_type_l10n of this ImportVnxArrayInstance.  # noqa: E501

        Localized message string corresponding to supported_import_type Was added in version 1.0.2.  # noqa: E501

        :return: The supported_import_type_l10n of this ImportVnxArrayInstance.  # noqa: E501
        :rtype: str
        """
        return self._supported_import_type_l10n

    @supported_import_type_l10n.setter
    def supported_import_type_l10n(self, supported_import_type_l10n):
        """Sets the supported_import_type_l10n of this ImportVnxArrayInstance.

        Localized message string corresponding to supported_import_type Was added in version 1.0.2.  # noqa: E501

        :param supported_import_type_l10n: The supported_import_type_l10n of this ImportVnxArrayInstance.  # noqa: E501
        :type: str
        """

        self._supported_import_type_l10n = supported_import_type_l10n

    @property
    def import_vnx_volumes(self):
        """Gets the import_vnx_volumes of this ImportVnxArrayInstance.  # noqa: E501

        This is the inverse of the resource type import_vnx_volume association.  # noqa: E501

        :return: The import_vnx_volumes of this ImportVnxArrayInstance.  # noqa: E501
        :rtype: list[ImportVnxVolumeInstance]
        """
        return self._import_vnx_volumes

    @import_vnx_volumes.setter
    def import_vnx_volumes(self, import_vnx_volumes):
        """Sets the import_vnx_volumes of this ImportVnxArrayInstance.

        This is the inverse of the resource type import_vnx_volume association.  # noqa: E501

        :param import_vnx_volumes: The import_vnx_volumes of this ImportVnxArrayInstance.  # noqa: E501
        :type: list[ImportVnxVolumeInstance]
        """

        self._import_vnx_volumes = import_vnx_volumes

    @property
    def import_vnx_consistency_groups(self):
        """Gets the import_vnx_consistency_groups of this ImportVnxArrayInstance.  # noqa: E501

        This is the inverse of the resource type import_vnx_consistency_group association.  # noqa: E501

        :return: The import_vnx_consistency_groups of this ImportVnxArrayInstance.  # noqa: E501
        :rtype: list[ImportVnxConsistencyGroupInstance]
        """
        return self._import_vnx_consistency_groups

    @import_vnx_consistency_groups.setter
    def import_vnx_consistency_groups(self, import_vnx_consistency_groups):
        """Sets the import_vnx_consistency_groups of this ImportVnxArrayInstance.

        This is the inverse of the resource type import_vnx_consistency_group association.  # noqa: E501

        :param import_vnx_consistency_groups: The import_vnx_consistency_groups of this ImportVnxArrayInstance.  # noqa: E501
        :type: list[ImportVnxConsistencyGroupInstance]
        """

        self._import_vnx_consistency_groups = import_vnx_consistency_groups

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
        if issubclass(ImportVnxArrayInstance, dict):
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
        if not isinstance(other, ImportVnxArrayInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImportVnxArrayInstance):
            return True

        return self.to_dict() != other.to_dict()
