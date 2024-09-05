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


class ClusterCreateCluster(object):
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
        'name': 'str',
        'ignore_network_warnings': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'ignore_network_warnings': 'ignore_network_warnings'
    }

    def __init__(self, name=None, ignore_network_warnings=False, _configuration=None):  # noqa: E501
        """ClusterCreateCluster - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._ignore_network_warnings = None
        self.discriminator = None

        self.name = name
        if ignore_network_warnings is not None:
            self.ignore_network_warnings = ignore_network_warnings

    @property
    def name(self):
        """Gets the name of this ClusterCreateCluster.  # noqa: E501

        The name of the cluster. The name can be up to 64 UTF-8 characters and cannot be an empty string.  # noqa: E501

        :return: The name of this ClusterCreateCluster.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterCreateCluster.

        The name of the cluster. The name can be up to 64 UTF-8 characters and cannot be an empty string.  # noqa: E501

        :param name: The name of this ClusterCreateCluster.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 64):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `64`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def ignore_network_warnings(self):
        """Gets the ignore_network_warnings of this ClusterCreateCluster.  # noqa: E501

        Set to true to ignore network warnings about unreachable external network services discovered while cluster creation. This can be useful for configuring a system before delivery into the intended deployment environment. The default is false, and these warnings will cause cluster creation to fail.  # noqa: E501

        :return: The ignore_network_warnings of this ClusterCreateCluster.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_network_warnings

    @ignore_network_warnings.setter
    def ignore_network_warnings(self, ignore_network_warnings):
        """Sets the ignore_network_warnings of this ClusterCreateCluster.

        Set to true to ignore network warnings about unreachable external network services discovered while cluster creation. This can be useful for configuring a system before delivery into the intended deployment environment. The default is false, and these warnings will cause cluster creation to fail.  # noqa: E501

        :param ignore_network_warnings: The ignore_network_warnings of this ClusterCreateCluster.  # noqa: E501
        :type: bool
        """

        self._ignore_network_warnings = ignore_network_warnings

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
        if issubclass(ClusterCreateCluster, dict):
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
        if not isinstance(other, ClusterCreateCluster):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterCreateCluster):
            return True

        return self.to_dict() != other.to_dict()
