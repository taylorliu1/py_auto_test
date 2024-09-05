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


class HostAttach(object):
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
        'volume_id': 'str',
        'logical_unit_number': 'int'
    }

    attribute_map = {
        'volume_id': 'volume_id',
        'logical_unit_number': 'logical_unit_number'
    }

    def __init__(self, volume_id=None, logical_unit_number=None, _configuration=None):  # noqa: E501
        """HostAttach - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._volume_id = None
        self._logical_unit_number = None
        self.discriminator = None

        self.volume_id = volume_id
        if logical_unit_number is not None:
            self.logical_unit_number = logical_unit_number

    @property
    def volume_id(self):
        """Gets the volume_id of this HostAttach.  # noqa: E501

        Volume to attach. name:{name} can be used instead of {id}. For example:'volume_id':'name:volume_name'  # noqa: E501

        :return: The volume_id of this HostAttach.  # noqa: E501
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this HostAttach.

        Volume to attach. name:{name} can be used instead of {id}. For example:'volume_id':'name:volume_name'  # noqa: E501

        :param volume_id: The volume_id of this HostAttach.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and volume_id is None:
            raise ValueError("Invalid value for `volume_id`, must not be `None`")  # noqa: E501

        self._volume_id = volume_id

    @property
    def logical_unit_number(self):
        """Gets the logical_unit_number of this HostAttach.  # noqa: E501

        Logical unit number for the volume, if desired.  # noqa: E501

        :return: The logical_unit_number of this HostAttach.  # noqa: E501
        :rtype: int
        """
        return self._logical_unit_number

    @logical_unit_number.setter
    def logical_unit_number(self, logical_unit_number):
        """Sets the logical_unit_number of this HostAttach.

        Logical unit number for the volume, if desired.  # noqa: E501

        :param logical_unit_number: The logical_unit_number of this HostAttach.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                logical_unit_number is not None and logical_unit_number > 16383):  # noqa: E501
            raise ValueError("Invalid value for `logical_unit_number`, must be a value less than or equal to `16383`")  # noqa: E501
        if (self._configuration.client_side_validation and
                logical_unit_number is not None and logical_unit_number < 0):  # noqa: E501
            raise ValueError("Invalid value for `logical_unit_number`, must be a value greater than or equal to `0`")  # noqa: E501

        self._logical_unit_number = logical_unit_number

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
        if issubclass(HostAttach, dict):
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
        if not isinstance(other, HostAttach):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HostAttach):
            return True

        return self.to_dict() != other.to_dict()
