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


class FileInterfaceRouteCreate(object):
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
        'file_interface_id': 'str',
        'destination': 'str',
        'prefix_length': 'int',
        'gateway': 'str'
    }

    attribute_map = {
        'file_interface_id': 'file_interface_id',
        'destination': 'destination',
        'prefix_length': 'prefix_length',
        'gateway': 'gateway'
    }

    def __init__(self, file_interface_id=None, destination=None, prefix_length=None, gateway=None, _configuration=None):  # noqa: E501
        """FileInterfaceRouteCreate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._file_interface_id = None
        self._destination = None
        self._prefix_length = None
        self._gateway = None
        self.discriminator = None

        self.file_interface_id = file_interface_id
        self.destination = destination
        self.prefix_length = prefix_length
        if gateway is not None:
            self.gateway = gateway

    @property
    def file_interface_id(self):
        """Gets the file_interface_id of this FileInterfaceRouteCreate.  # noqa: E501

        Unique identifier of the associated file interface. name:{name} can be used instead of {id}. For example:'file_interface_id':'name:file_interface_name'  # noqa: E501

        :return: The file_interface_id of this FileInterfaceRouteCreate.  # noqa: E501
        :rtype: str
        """
        return self._file_interface_id

    @file_interface_id.setter
    def file_interface_id(self, file_interface_id):
        """Sets the file_interface_id of this FileInterfaceRouteCreate.

        Unique identifier of the associated file interface. name:{name} can be used instead of {id}. For example:'file_interface_id':'name:file_interface_name'  # noqa: E501

        :param file_interface_id: The file_interface_id of this FileInterfaceRouteCreate.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and file_interface_id is None:
            raise ValueError("Invalid value for `file_interface_id`, must not be `None`")  # noqa: E501

        self._file_interface_id = file_interface_id

    @property
    def destination(self):
        """Gets the destination of this FileInterfaceRouteCreate.  # noqa: E501

        IPv4 or IPv6 address of the target network node based on the specific route type. Values are: * For a default route, the route is specified in the gateway value for the related file interface. * For a host route, the destination value is a host IP address. For an IPV4 address the prefix_length must be 32, otherwise for an IPv6 address the prefix_length must be 128. * For a subnet route, the destination value is a subnet IP address and the appropriate prefix_length must be specified accordingly.   # noqa: E501

        :return: The destination of this FileInterfaceRouteCreate.  # noqa: E501
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this FileInterfaceRouteCreate.

        IPv4 or IPv6 address of the target network node based on the specific route type. Values are: * For a default route, the route is specified in the gateway value for the related file interface. * For a host route, the destination value is a host IP address. For an IPV4 address the prefix_length must be 32, otherwise for an IPv6 address the prefix_length must be 128. * For a subnet route, the destination value is a subnet IP address and the appropriate prefix_length must be specified accordingly.   # noqa: E501

        :param destination: The destination of this FileInterfaceRouteCreate.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and destination is None:
            raise ValueError("Invalid value for `destination`, must not be `None`")  # noqa: E501

        self._destination = destination

    @property
    def prefix_length(self):
        """Gets the prefix_length of this FileInterfaceRouteCreate.  # noqa: E501

        IPv4 or IPv6 prefix length for the route.  # noqa: E501

        :return: The prefix_length of this FileInterfaceRouteCreate.  # noqa: E501
        :rtype: int
        """
        return self._prefix_length

    @prefix_length.setter
    def prefix_length(self, prefix_length):
        """Sets the prefix_length of this FileInterfaceRouteCreate.

        IPv4 or IPv6 prefix length for the route.  # noqa: E501

        :param prefix_length: The prefix_length of this FileInterfaceRouteCreate.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and prefix_length is None:
            raise ValueError("Invalid value for `prefix_length`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                prefix_length is not None and prefix_length > 128):  # noqa: E501
            raise ValueError("Invalid value for `prefix_length`, must be a value less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                prefix_length is not None and prefix_length < 1):  # noqa: E501
            raise ValueError("Invalid value for `prefix_length`, must be a value greater than or equal to `1`")  # noqa: E501

        self._prefix_length = prefix_length

    @property
    def gateway(self):
        """Gets the gateway of this FileInterfaceRouteCreate.  # noqa: E501

        IP address of the gateway associated with the route.  # noqa: E501

        :return: The gateway of this FileInterfaceRouteCreate.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this FileInterfaceRouteCreate.

        IP address of the gateway associated with the route.  # noqa: E501

        :param gateway: The gateway of this FileInterfaceRouteCreate.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                gateway is not None and len(gateway) > 45):
            raise ValueError("Invalid value for `gateway`, length must be less than or equal to `45`")  # noqa: E501
        if (self._configuration.client_side_validation and
                gateway is not None and len(gateway) < 1):
            raise ValueError("Invalid value for `gateway`, length must be greater than or equal to `1`")  # noqa: E501

        self._gateway = gateway

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
        if issubclass(FileInterfaceRouteCreate, dict):
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
        if not isinstance(other, FileInterfaceRouteCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileInterfaceRouteCreate):
            return True

        return self.to_dict() != other.to_dict()
