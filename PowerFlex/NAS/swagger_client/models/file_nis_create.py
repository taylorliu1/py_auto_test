# coding: utf-8

"""
    PowerFlex NAS Management REST API

    NAS Storage Management REST API definition.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FileNisCreate(object):
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
        'nas_server_id': 'str',
        'domain': 'str',
        'ip_addresses': 'list[str]'
    }

    attribute_map = {
        'nas_server_id': 'nas_server_id',
        'domain': 'domain',
        'ip_addresses': 'ip_addresses'
    }

    def __init__(self, nas_server_id=None, domain=None, ip_addresses=None):  # noqa: E501
        """FileNisCreate - a model defined in Swagger"""  # noqa: E501
        self._nas_server_id = None
        self._domain = None
        self._ip_addresses = None
        self.discriminator = None
        self.nas_server_id = nas_server_id
        self.domain = domain
        self.ip_addresses = ip_addresses

    @property
    def nas_server_id(self):
        """Gets the nas_server_id of this FileNisCreate.  # noqa: E501

        Unique identifier of the associated NAS Server instance that uses this NIS Service object.  Only one NIS Service per NAS Server is supported.  # noqa: E501

        :return: The nas_server_id of this FileNisCreate.  # noqa: E501
        :rtype: str
        """
        return self._nas_server_id

    @nas_server_id.setter
    def nas_server_id(self, nas_server_id):
        """Sets the nas_server_id of this FileNisCreate.

        Unique identifier of the associated NAS Server instance that uses this NIS Service object.  Only one NIS Service per NAS Server is supported.  # noqa: E501

        :param nas_server_id: The nas_server_id of this FileNisCreate.  # noqa: E501
        :type: str
        """
        if nas_server_id is None:
            raise ValueError("Invalid value for `nas_server_id`, must not be `None`")  # noqa: E501

        self._nas_server_id = nas_server_id

    @property
    def domain(self):
        """Gets the domain of this FileNisCreate.  # noqa: E501

        Name of the NIS domain.  # noqa: E501

        :return: The domain of this FileNisCreate.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this FileNisCreate.

        Name of the NIS domain.  # noqa: E501

        :param domain: The domain of this FileNisCreate.  # noqa: E501
        :type: str
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def ip_addresses(self):
        """Gets the ip_addresses of this FileNisCreate.  # noqa: E501

        The list of NIS server IP addresses.  # noqa: E501

        :return: The ip_addresses of this FileNisCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """Sets the ip_addresses of this FileNisCreate.

        The list of NIS server IP addresses.  # noqa: E501

        :param ip_addresses: The ip_addresses of this FileNisCreate.  # noqa: E501
        :type: list[str]
        """
        if ip_addresses is None:
            raise ValueError("Invalid value for `ip_addresses`, must not be `None`")  # noqa: E501

        self._ip_addresses = ip_addresses

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
        if issubclass(FileNisCreate, dict):
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
        if not isinstance(other, FileNisCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
