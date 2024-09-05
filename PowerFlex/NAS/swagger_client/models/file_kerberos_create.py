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

class FileKerberosCreate(object):
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
        'realm': 'str',
        'kdc_addresses': 'list[str]',
        'port_number': 'int'
    }

    attribute_map = {
        'nas_server_id': 'nas_server_id',
        'realm': 'realm',
        'kdc_addresses': 'kdc_addresses',
        'port_number': 'port_number'
    }

    def __init__(self, nas_server_id=None, realm=None, kdc_addresses=None, port_number=88):  # noqa: E501
        """FileKerberosCreate - a model defined in Swagger"""  # noqa: E501
        self._nas_server_id = None
        self._realm = None
        self._kdc_addresses = None
        self._port_number = None
        self.discriminator = None
        self.nas_server_id = nas_server_id
        self.realm = realm
        self.kdc_addresses = kdc_addresses
        if port_number is not None:
            self.port_number = port_number

    @property
    def nas_server_id(self):
        """Gets the nas_server_id of this FileKerberosCreate.  # noqa: E501

        Unique identifier of the associated NAS Server instance that uses this Kerberos object. Only one Kerberos object per NAS Server is supported.  # noqa: E501

        :return: The nas_server_id of this FileKerberosCreate.  # noqa: E501
        :rtype: str
        """
        return self._nas_server_id

    @nas_server_id.setter
    def nas_server_id(self, nas_server_id):
        """Sets the nas_server_id of this FileKerberosCreate.

        Unique identifier of the associated NAS Server instance that uses this Kerberos object. Only one Kerberos object per NAS Server is supported.  # noqa: E501

        :param nas_server_id: The nas_server_id of this FileKerberosCreate.  # noqa: E501
        :type: str
        """
        if nas_server_id is None:
            raise ValueError("Invalid value for `nas_server_id`, must not be `None`")  # noqa: E501

        self._nas_server_id = nas_server_id

    @property
    def realm(self):
        """Gets the realm of this FileKerberosCreate.  # noqa: E501

        Realm name of the Kerberos Service.  # noqa: E501

        :return: The realm of this FileKerberosCreate.  # noqa: E501
        :rtype: str
        """
        return self._realm

    @realm.setter
    def realm(self, realm):
        """Sets the realm of this FileKerberosCreate.

        Realm name of the Kerberos Service.  # noqa: E501

        :param realm: The realm of this FileKerberosCreate.  # noqa: E501
        :type: str
        """
        if realm is None:
            raise ValueError("Invalid value for `realm`, must not be `None`")  # noqa: E501

        self._realm = realm

    @property
    def kdc_addresses(self):
        """Gets the kdc_addresses of this FileKerberosCreate.  # noqa: E501

        Fully Qualified domain names of the Kerberos Key Distribution Center (KDC) servers. IPv4 and IPv6 addresses are not supported.  # noqa: E501

        :return: The kdc_addresses of this FileKerberosCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._kdc_addresses

    @kdc_addresses.setter
    def kdc_addresses(self, kdc_addresses):
        """Sets the kdc_addresses of this FileKerberosCreate.

        Fully Qualified domain names of the Kerberos Key Distribution Center (KDC) servers. IPv4 and IPv6 addresses are not supported.  # noqa: E501

        :param kdc_addresses: The kdc_addresses of this FileKerberosCreate.  # noqa: E501
        :type: list[str]
        """
        if kdc_addresses is None:
            raise ValueError("Invalid value for `kdc_addresses`, must not be `None`")  # noqa: E501

        self._kdc_addresses = kdc_addresses

    @property
    def port_number(self):
        """Gets the port_number of this FileKerberosCreate.  # noqa: E501

        KDC servers TCP port.  # noqa: E501

        :return: The port_number of this FileKerberosCreate.  # noqa: E501
        :rtype: int
        """
        return self._port_number

    @port_number.setter
    def port_number(self, port_number):
        """Sets the port_number of this FileKerberosCreate.

        KDC servers TCP port.  # noqa: E501

        :param port_number: The port_number of this FileKerberosCreate.  # noqa: E501
        :type: int
        """

        self._port_number = port_number

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
        if issubclass(FileKerberosCreate, dict):
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
        if not isinstance(other, FileKerberosCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
