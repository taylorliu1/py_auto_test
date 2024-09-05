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


class FileNisInstance(object):
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
        'nas_server_id': 'str',
        'domain': 'str',
        'ip_addresses': 'list[str]',
        'is_destination_override_enabled': 'bool',
        'source_parameters': 'object',
        'nas_server': 'NasServerInstance'
    }

    attribute_map = {
        'id': 'id',
        'nas_server_id': 'nas_server_id',
        'domain': 'domain',
        'ip_addresses': 'ip_addresses',
        'is_destination_override_enabled': 'is_destination_override_enabled',
        'source_parameters': 'source_parameters',
        'nas_server': 'nas_server'
    }

    def __init__(self, id=None, nas_server_id=None, domain=None, ip_addresses=None, is_destination_override_enabled=False, source_parameters=None, nas_server=None, _configuration=None):  # noqa: E501
        """FileNisInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._nas_server_id = None
        self._domain = None
        self._ip_addresses = None
        self._is_destination_override_enabled = None
        self._source_parameters = None
        self._nas_server = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if nas_server_id is not None:
            self.nas_server_id = nas_server_id
        if domain is not None:
            self.domain = domain
        if ip_addresses is not None:
            self.ip_addresses = ip_addresses
        if is_destination_override_enabled is not None:
            self.is_destination_override_enabled = is_destination_override_enabled
        if source_parameters is not None:
            self.source_parameters = source_parameters
        if nas_server is not None:
            self.nas_server = nas_server

    @property
    def id(self):
        """Gets the id of this FileNisInstance.  # noqa: E501

        Unique identifier of the NIS Service.  # noqa: E501

        :return: The id of this FileNisInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FileNisInstance.

        Unique identifier of the NIS Service.  # noqa: E501

        :param id: The id of this FileNisInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def nas_server_id(self):
        """Gets the nas_server_id of this FileNisInstance.  # noqa: E501

        Unique identifier of the associated NAS Server instance that uses this NIS Service object. Only one NIS Service per NAS Server is supported.  # noqa: E501

        :return: The nas_server_id of this FileNisInstance.  # noqa: E501
        :rtype: str
        """
        return self._nas_server_id

    @nas_server_id.setter
    def nas_server_id(self, nas_server_id):
        """Sets the nas_server_id of this FileNisInstance.

        Unique identifier of the associated NAS Server instance that uses this NIS Service object. Only one NIS Service per NAS Server is supported.  # noqa: E501

        :param nas_server_id: The nas_server_id of this FileNisInstance.  # noqa: E501
        :type: str
        """

        self._nas_server_id = nas_server_id

    @property
    def domain(self):
        """Gets the domain of this FileNisInstance.  # noqa: E501

        Name of the NIS domain.  # noqa: E501

        :return: The domain of this FileNisInstance.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this FileNisInstance.

        Name of the NIS domain.  # noqa: E501

        :param domain: The domain of this FileNisInstance.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def ip_addresses(self):
        """Gets the ip_addresses of this FileNisInstance.  # noqa: E501

        The list of NIS server IP addresses.  # noqa: E501

        :return: The ip_addresses of this FileNisInstance.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """Sets the ip_addresses of this FileNisInstance.

        The list of NIS server IP addresses.  # noqa: E501

        :param ip_addresses: The ip_addresses of this FileNisInstance.  # noqa: E501
        :type: list[str]
        """

        self._ip_addresses = ip_addresses

    @property
    def is_destination_override_enabled(self):
        """Gets the is_destination_override_enabled of this FileNisInstance.  # noqa: E501

        Used in replication context when the user wants to override the settings on the destination. Was added in version 3.0.0.0.  # noqa: E501

        :return: The is_destination_override_enabled of this FileNisInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_destination_override_enabled

    @is_destination_override_enabled.setter
    def is_destination_override_enabled(self, is_destination_override_enabled):
        """Sets the is_destination_override_enabled of this FileNisInstance.

        Used in replication context when the user wants to override the settings on the destination. Was added in version 3.0.0.0.  # noqa: E501

        :param is_destination_override_enabled: The is_destination_override_enabled of this FileNisInstance.  # noqa: E501
        :type: bool
        """

        self._is_destination_override_enabled = is_destination_override_enabled

    @property
    def source_parameters(self):
        """Gets the source_parameters of this FileNisInstance.  # noqa: E501

        Information about the corresponding source NAS Server's File NIS settings. Only populated when is_destination_override_enabled flag is set to true. Was added in version 3.0.0.0.  Filtering on the fields of this embedded resource is not supported.  # noqa: E501

        :return: The source_parameters of this FileNisInstance.  # noqa: E501
        :rtype: object
        """
        return self._source_parameters

    @source_parameters.setter
    def source_parameters(self, source_parameters):
        """Sets the source_parameters of this FileNisInstance.

        Information about the corresponding source NAS Server's File NIS settings. Only populated when is_destination_override_enabled flag is set to true. Was added in version 3.0.0.0.  Filtering on the fields of this embedded resource is not supported.  # noqa: E501

        :param source_parameters: The source_parameters of this FileNisInstance.  # noqa: E501
        :type: object
        """

        self._source_parameters = source_parameters

    @property
    def nas_server(self):
        """Gets the nas_server of this FileNisInstance.  # noqa: E501

        This is the embeddable reference form of nas_server_id attribute.  # noqa: E501

        :return: The nas_server of this FileNisInstance.  # noqa: E501
        :rtype: NasServerInstance
        """
        return self._nas_server

    @nas_server.setter
    def nas_server(self, nas_server):
        """Sets the nas_server of this FileNisInstance.

        This is the embeddable reference form of nas_server_id attribute.  # noqa: E501

        :param nas_server: The nas_server of this FileNisInstance.  # noqa: E501
        :type: NasServerInstance
        """

        self._nas_server = nas_server

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
        if issubclass(FileNisInstance, dict):
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
        if not isinstance(other, FileNisInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileNisInstance):
            return True

        return self.to_dict() != other.to_dict()
