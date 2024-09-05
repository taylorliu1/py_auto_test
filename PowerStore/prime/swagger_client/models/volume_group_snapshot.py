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


class VolumeGroupSnapshot(object):
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
        'description': 'str',
        'expiration_timestamp': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'expiration_timestamp': 'expiration_timestamp'
    }

    def __init__(self, name=None, description=None, expiration_timestamp=None, _configuration=None):  # noqa: E501
        """VolumeGroupSnapshot - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._description = None
        self._expiration_timestamp = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if expiration_timestamp is not None:
            self.expiration_timestamp = expiration_timestamp

    @property
    def name(self):
        """Gets the name of this VolumeGroupSnapshot.  # noqa: E501

        Unique name of the snapshot set to be created.  # noqa: E501

        :return: The name of this VolumeGroupSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VolumeGroupSnapshot.

        Unique name of the snapshot set to be created.  # noqa: E501

        :param name: The name of this VolumeGroupSnapshot.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 128):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this VolumeGroupSnapshot.  # noqa: E501

        Optional description for the snapshot set. If description is not specified, the description for the snapshot set will not be set.  # noqa: E501

        :return: The description of this VolumeGroupSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VolumeGroupSnapshot.

        Optional description for the snapshot set. If description is not specified, the description for the snapshot set will not be set.  # noqa: E501

        :param description: The description of this VolumeGroupSnapshot.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def expiration_timestamp(self):
        """Gets the expiration_timestamp of this VolumeGroupSnapshot.  # noqa: E501

        Time after which the snapshot set can be auto-purged. Time must be specified in Zulu time zone. Expiration time cannot be prior to current time. Use a maximum timestamp value to set an expiration to never expire. Valid format is yyyy-MM-dd'T'HH:mm:ssZ or yyyy-MM-dd'T'HH:mm:ss.SSSZ. By default, expiration time will not be set. Was added in version 2.0.0.0.  # noqa: E501

        :return: The expiration_timestamp of this VolumeGroupSnapshot.  # noqa: E501
        :rtype: str
        """
        return self._expiration_timestamp

    @expiration_timestamp.setter
    def expiration_timestamp(self, expiration_timestamp):
        """Sets the expiration_timestamp of this VolumeGroupSnapshot.

        Time after which the snapshot set can be auto-purged. Time must be specified in Zulu time zone. Expiration time cannot be prior to current time. Use a maximum timestamp value to set an expiration to never expire. Valid format is yyyy-MM-dd'T'HH:mm:ssZ or yyyy-MM-dd'T'HH:mm:ss.SSSZ. By default, expiration time will not be set. Was added in version 2.0.0.0.  # noqa: E501

        :param expiration_timestamp: The expiration_timestamp of this VolumeGroupSnapshot.  # noqa: E501
        :type: str
        """

        self._expiration_timestamp = expiration_timestamp

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
        if issubclass(VolumeGroupSnapshot, dict):
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
        if not isinstance(other, VolumeGroupSnapshot):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VolumeGroupSnapshot):
            return True

        return self.to_dict() != other.to_dict()
