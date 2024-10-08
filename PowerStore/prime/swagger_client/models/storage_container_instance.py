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


class StorageContainerInstance(object):
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
        'quota': 'int',
        'storage_protocol': 'StorageContainerStorageProtocolEnum',
        'storage_protocol_l10n': 'str',
        'virtual_volumes': 'list[VirtualVolumeInstance]',
        'replication_groups': 'list[ReplicationGroupInstance]',
        'datastores': 'list[DatastoreInstance]',
        'destinations': 'list[StorageContainerDestinationInstance]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'quota': 'quota',
        'storage_protocol': 'storage_protocol',
        'storage_protocol_l10n': 'storage_protocol_l10n',
        'virtual_volumes': 'virtual_volumes',
        'replication_groups': 'replication_groups',
        'datastores': 'datastores',
        'destinations': 'destinations'
    }

    def __init__(self, id=None, name=None, quota=None, storage_protocol=None, storage_protocol_l10n=None, virtual_volumes=None, replication_groups=None, datastores=None, destinations=None, _configuration=None):  # noqa: E501
        """StorageContainerInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._quota = None
        self._storage_protocol = None
        self._storage_protocol_l10n = None
        self._virtual_volumes = None
        self._replication_groups = None
        self._datastores = None
        self._destinations = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if quota is not None:
            self.quota = quota
        if storage_protocol is not None:
            self.storage_protocol = storage_protocol
        if storage_protocol_l10n is not None:
            self.storage_protocol_l10n = storage_protocol_l10n
        if virtual_volumes is not None:
            self.virtual_volumes = virtual_volumes
        if replication_groups is not None:
            self.replication_groups = replication_groups
        if datastores is not None:
            self.datastores = datastores
        if destinations is not None:
            self.destinations = destinations

    @property
    def id(self):
        """Gets the id of this StorageContainerInstance.  # noqa: E501

        The unique id of the storage container.  # noqa: E501

        :return: The id of this StorageContainerInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StorageContainerInstance.

        The unique id of the storage container.  # noqa: E501

        :param id: The id of this StorageContainerInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this StorageContainerInstance.  # noqa: E501

        Name for the storage container.  This should be unique across all storage containers in the cluster. Name can be from 1 to 64 UTF-8 characters, and not more than 127 bytes.  This property supports case-insensitive filtering.  # noqa: E501

        :return: The name of this StorageContainerInstance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StorageContainerInstance.

        Name for the storage container.  This should be unique across all storage containers in the cluster. Name can be from 1 to 64 UTF-8 characters, and not more than 127 bytes.  This property supports case-insensitive filtering.  # noqa: E501

        :param name: The name of this StorageContainerInstance.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 64):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def quota(self):
        """Gets the quota of this StorageContainerInstance.  # noqa: E501

        The total number of bytes that can be provisioned/reserved against this storage container.  A value of 0 means there is no limit.  It is possible to set the quota to a value that overprovisions the amount of space available in the system.  # noqa: E501

        :return: The quota of this StorageContainerInstance.  # noqa: E501
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this StorageContainerInstance.

        The total number of bytes that can be provisioned/reserved against this storage container.  A value of 0 means there is no limit.  It is possible to set the quota to a value that overprovisions the amount of space available in the system.  # noqa: E501

        :param quota: The quota of this StorageContainerInstance.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                quota is not None and quota > -9223372036854775616):  # noqa: E501
            raise ValueError("Invalid value for `quota`, must be a value less than or equal to `-9223372036854775616`")  # noqa: E501
        if (self._configuration.client_side_validation and
                quota is not None and quota < 0):  # noqa: E501
            raise ValueError("Invalid value for `quota`, must be a value greater than or equal to `0`")  # noqa: E501

        self._quota = quota

    @property
    def storage_protocol(self):
        """Gets the storage_protocol of this StorageContainerInstance.  # noqa: E501

         Was added in version 3.0.0.0.  # noqa: E501

        :return: The storage_protocol of this StorageContainerInstance.  # noqa: E501
        :rtype: StorageContainerStorageProtocolEnum
        """
        return self._storage_protocol

    @storage_protocol.setter
    def storage_protocol(self, storage_protocol):
        """Sets the storage_protocol of this StorageContainerInstance.

         Was added in version 3.0.0.0.  # noqa: E501

        :param storage_protocol: The storage_protocol of this StorageContainerInstance.  # noqa: E501
        :type: StorageContainerStorageProtocolEnum
        """

        self._storage_protocol = storage_protocol

    @property
    def storage_protocol_l10n(self):
        """Gets the storage_protocol_l10n of this StorageContainerInstance.  # noqa: E501

        Localized message string corresponding to storage_protocol Was added in version 3.0.0.0.  # noqa: E501

        :return: The storage_protocol_l10n of this StorageContainerInstance.  # noqa: E501
        :rtype: str
        """
        return self._storage_protocol_l10n

    @storage_protocol_l10n.setter
    def storage_protocol_l10n(self, storage_protocol_l10n):
        """Sets the storage_protocol_l10n of this StorageContainerInstance.

        Localized message string corresponding to storage_protocol Was added in version 3.0.0.0.  # noqa: E501

        :param storage_protocol_l10n: The storage_protocol_l10n of this StorageContainerInstance.  # noqa: E501
        :type: str
        """

        self._storage_protocol_l10n = storage_protocol_l10n

    @property
    def virtual_volumes(self):
        """Gets the virtual_volumes of this StorageContainerInstance.  # noqa: E501

        This is the inverse of the resource type virtual_volume association.  # noqa: E501

        :return: The virtual_volumes of this StorageContainerInstance.  # noqa: E501
        :rtype: list[VirtualVolumeInstance]
        """
        return self._virtual_volumes

    @virtual_volumes.setter
    def virtual_volumes(self, virtual_volumes):
        """Sets the virtual_volumes of this StorageContainerInstance.

        This is the inverse of the resource type virtual_volume association.  # noqa: E501

        :param virtual_volumes: The virtual_volumes of this StorageContainerInstance.  # noqa: E501
        :type: list[VirtualVolumeInstance]
        """

        self._virtual_volumes = virtual_volumes

    @property
    def replication_groups(self):
        """Gets the replication_groups of this StorageContainerInstance.  # noqa: E501

        This is the inverse of the resource type replication_group association.  # noqa: E501

        :return: The replication_groups of this StorageContainerInstance.  # noqa: E501
        :rtype: list[ReplicationGroupInstance]
        """
        return self._replication_groups

    @replication_groups.setter
    def replication_groups(self, replication_groups):
        """Sets the replication_groups of this StorageContainerInstance.

        This is the inverse of the resource type replication_group association.  # noqa: E501

        :param replication_groups: The replication_groups of this StorageContainerInstance.  # noqa: E501
        :type: list[ReplicationGroupInstance]
        """

        self._replication_groups = replication_groups

    @property
    def datastores(self):
        """Gets the datastores of this StorageContainerInstance.  # noqa: E501

        This is the inverse of the resource type datastore association.  # noqa: E501

        :return: The datastores of this StorageContainerInstance.  # noqa: E501
        :rtype: list[DatastoreInstance]
        """
        return self._datastores

    @datastores.setter
    def datastores(self, datastores):
        """Sets the datastores of this StorageContainerInstance.

        This is the inverse of the resource type datastore association.  # noqa: E501

        :param datastores: The datastores of this StorageContainerInstance.  # noqa: E501
        :type: list[DatastoreInstance]
        """

        self._datastores = datastores

    @property
    def destinations(self):
        """Gets the destinations of this StorageContainerInstance.  # noqa: E501

        This is the inverse of the resource type storage_container_destination association.  # noqa: E501

        :return: The destinations of this StorageContainerInstance.  # noqa: E501
        :rtype: list[StorageContainerDestinationInstance]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """Sets the destinations of this StorageContainerInstance.

        This is the inverse of the resource type storage_container_destination association.  # noqa: E501

        :param destinations: The destinations of this StorageContainerInstance.  # noqa: E501
        :type: list[StorageContainerDestinationInstance]
        """

        self._destinations = destinations

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
        if issubclass(StorageContainerInstance, dict):
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
        if not isinstance(other, StorageContainerInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageContainerInstance):
            return True

        return self.to_dict() != other.to_dict()
