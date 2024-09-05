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


class StorageContainerDestinationInstance(object):
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
        'storage_container_id': 'str',
        'remote_system_id': 'str',
        'remote_storage_container_id': 'str',
        'storage_container': 'StorageContainerInstance',
        'remote_system': 'RemoteSystemInstance'
    }

    attribute_map = {
        'id': 'id',
        'storage_container_id': 'storage_container_id',
        'remote_system_id': 'remote_system_id',
        'remote_storage_container_id': 'remote_storage_container_id',
        'storage_container': 'storage_container',
        'remote_system': 'remote_system'
    }

    def __init__(self, id=None, storage_container_id=None, remote_system_id=None, remote_storage_container_id=None, storage_container=None, remote_system=None, _configuration=None):  # noqa: E501
        """StorageContainerDestinationInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._storage_container_id = None
        self._remote_system_id = None
        self._remote_storage_container_id = None
        self._storage_container = None
        self._remote_system = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if storage_container_id is not None:
            self.storage_container_id = storage_container_id
        if remote_system_id is not None:
            self.remote_system_id = remote_system_id
        if remote_storage_container_id is not None:
            self.remote_storage_container_id = remote_storage_container_id
        if storage_container is not None:
            self.storage_container = storage_container
        if remote_system is not None:
            self.remote_system = remote_system

    @property
    def id(self):
        """Gets the id of this StorageContainerDestinationInstance.  # noqa: E501

        The unique id of the storage container destination.  # noqa: E501

        :return: The id of this StorageContainerDestinationInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StorageContainerDestinationInstance.

        The unique id of the storage container destination.  # noqa: E501

        :param id: The id of this StorageContainerDestinationInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def storage_container_id(self):
        """Gets the storage_container_id of this StorageContainerDestinationInstance.  # noqa: E501

        The unique id of the local storage container.  # noqa: E501

        :return: The storage_container_id of this StorageContainerDestinationInstance.  # noqa: E501
        :rtype: str
        """
        return self._storage_container_id

    @storage_container_id.setter
    def storage_container_id(self, storage_container_id):
        """Sets the storage_container_id of this StorageContainerDestinationInstance.

        The unique id of the local storage container.  # noqa: E501

        :param storage_container_id: The storage_container_id of this StorageContainerDestinationInstance.  # noqa: E501
        :type: str
        """

        self._storage_container_id = storage_container_id

    @property
    def remote_system_id(self):
        """Gets the remote_system_id of this StorageContainerDestinationInstance.  # noqa: E501

        The unique id of the remote system.  # noqa: E501

        :return: The remote_system_id of this StorageContainerDestinationInstance.  # noqa: E501
        :rtype: str
        """
        return self._remote_system_id

    @remote_system_id.setter
    def remote_system_id(self, remote_system_id):
        """Sets the remote_system_id of this StorageContainerDestinationInstance.

        The unique id of the remote system.  # noqa: E501

        :param remote_system_id: The remote_system_id of this StorageContainerDestinationInstance.  # noqa: E501
        :type: str
        """

        self._remote_system_id = remote_system_id

    @property
    def remote_storage_container_id(self):
        """Gets the remote_storage_container_id of this StorageContainerDestinationInstance.  # noqa: E501

        The unique id of the destination storage container on the remote system.  # noqa: E501

        :return: The remote_storage_container_id of this StorageContainerDestinationInstance.  # noqa: E501
        :rtype: str
        """
        return self._remote_storage_container_id

    @remote_storage_container_id.setter
    def remote_storage_container_id(self, remote_storage_container_id):
        """Sets the remote_storage_container_id of this StorageContainerDestinationInstance.

        The unique id of the destination storage container on the remote system.  # noqa: E501

        :param remote_storage_container_id: The remote_storage_container_id of this StorageContainerDestinationInstance.  # noqa: E501
        :type: str
        """

        self._remote_storage_container_id = remote_storage_container_id

    @property
    def storage_container(self):
        """Gets the storage_container of this StorageContainerDestinationInstance.  # noqa: E501

        This is the embeddable reference form of storage_container_id attribute.  # noqa: E501

        :return: The storage_container of this StorageContainerDestinationInstance.  # noqa: E501
        :rtype: StorageContainerInstance
        """
        return self._storage_container

    @storage_container.setter
    def storage_container(self, storage_container):
        """Sets the storage_container of this StorageContainerDestinationInstance.

        This is the embeddable reference form of storage_container_id attribute.  # noqa: E501

        :param storage_container: The storage_container of this StorageContainerDestinationInstance.  # noqa: E501
        :type: StorageContainerInstance
        """

        self._storage_container = storage_container

    @property
    def remote_system(self):
        """Gets the remote_system of this StorageContainerDestinationInstance.  # noqa: E501

        This is the embeddable reference form of remote_system_id attribute.  # noqa: E501

        :return: The remote_system of this StorageContainerDestinationInstance.  # noqa: E501
        :rtype: RemoteSystemInstance
        """
        return self._remote_system

    @remote_system.setter
    def remote_system(self, remote_system):
        """Sets the remote_system of this StorageContainerDestinationInstance.

        This is the embeddable reference form of remote_system_id attribute.  # noqa: E501

        :param remote_system: The remote_system of this StorageContainerDestinationInstance.  # noqa: E501
        :type: RemoteSystemInstance
        """

        self._remote_system = remote_system

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
        if issubclass(StorageContainerDestinationInstance, dict):
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
        if not isinstance(other, StorageContainerDestinationInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageContainerDestinationInstance):
            return True

        return self.to_dict() != other.to_dict()
