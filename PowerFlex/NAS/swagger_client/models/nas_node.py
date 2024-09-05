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

class NASNode(object):
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
        'platform_management_ip': 'str',
        'platform_id': 'str',
        'node_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'platform_management_ip': 'platform_management_ip',
        'platform_id': 'platform_id',
        'node_name': 'node_name'
    }

    def __init__(self, id=None, platform_management_ip=None, platform_id=None, node_name=None):  # noqa: E501
        """NASNode - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._platform_management_ip = None
        self._platform_id = None
        self._node_name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if platform_management_ip is not None:
            self.platform_management_ip = platform_management_ip
        if platform_id is not None:
            self.platform_id = platform_id
        if node_name is not None:
            self.node_name = node_name

    @property
    def id(self):
        """Gets the id of this NASNode.  # noqa: E501

        Unique identifier of the NAS Server.  # noqa: E501

        :return: The id of this NASNode.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NASNode.

        Unique identifier of the NAS Server.  # noqa: E501

        :param id: The id of this NASNode.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def platform_management_ip(self):
        """Gets the platform_management_ip of this NASNode.  # noqa: E501

        IP-address of NAS node  # noqa: E501

        :return: The platform_management_ip of this NASNode.  # noqa: E501
        :rtype: str
        """
        return self._platform_management_ip

    @platform_management_ip.setter
    def platform_management_ip(self, platform_management_ip):
        """Sets the platform_management_ip of this NASNode.

        IP-address of NAS node  # noqa: E501

        :param platform_management_ip: The platform_management_ip of this NASNode.  # noqa: E501
        :type: str
        """

        self._platform_management_ip = platform_management_ip

    @property
    def platform_id(self):
        """Gets the platform_id of this NASNode.  # noqa: E501

        Platform node ID where NAS node is hosted  # noqa: E501

        :return: The platform_id of this NASNode.  # noqa: E501
        :rtype: str
        """
        return self._platform_id

    @platform_id.setter
    def platform_id(self, platform_id):
        """Sets the platform_id of this NASNode.

        Platform node ID where NAS node is hosted  # noqa: E501

        :param platform_id: The platform_id of this NASNode.  # noqa: E501
        :type: str
        """

        self._platform_id = platform_id

    @property
    def node_name(self):
        """Gets the node_name of this NASNode.  # noqa: E501

        Name of the NAS node.  # noqa: E501

        :return: The node_name of this NASNode.  # noqa: E501
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this NASNode.

        Name of the NAS node.  # noqa: E501

        :param node_name: The node_name of this NASNode.  # noqa: E501
        :type: str
        """

        self._node_name = node_name

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
        if issubclass(NASNode, dict):
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
        if not isinstance(other, NASNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
