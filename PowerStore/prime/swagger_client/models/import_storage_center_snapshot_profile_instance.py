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


class ImportStorageCenterSnapshotProfileInstance(object):
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
        'type': 'ScSnapshotProfileTypeEnum',
        'description': 'str',
        'rules': 'list[ScProfileRuleInstance]',
        'type_l10n': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'rules': 'rules',
        'type_l10n': 'type_l10n'
    }

    def __init__(self, id=None, name=None, type=None, description=None, rules=None, type_l10n=None, _configuration=None):  # noqa: E501
        """ImportStorageCenterSnapshotProfileInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._type = None
        self._description = None
        self._rules = None
        self._type_l10n = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if rules is not None:
            self.rules = rules
        if type_l10n is not None:
            self.type_l10n = type_l10n

    @property
    def id(self):
        """Gets the id of this ImportStorageCenterSnapshotProfileInstance.  # noqa: E501

        Unique identifier of the snapshot profile.  # noqa: E501

        :return: The id of this ImportStorageCenterSnapshotProfileInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImportStorageCenterSnapshotProfileInstance.

        Unique identifier of the snapshot profile.  # noqa: E501

        :param id: The id of this ImportStorageCenterSnapshotProfileInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ImportStorageCenterSnapshotProfileInstance.  # noqa: E501

        Name of the snapshot profile.  # noqa: E501

        :return: The name of this ImportStorageCenterSnapshotProfileInstance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImportStorageCenterSnapshotProfileInstance.

        Name of the snapshot profile.  # noqa: E501

        :param name: The name of this ImportStorageCenterSnapshotProfileInstance.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this ImportStorageCenterSnapshotProfileInstance.  # noqa: E501

        Type of the snapshot profile.  # noqa: E501

        :return: The type of this ImportStorageCenterSnapshotProfileInstance.  # noqa: E501
        :rtype: ScSnapshotProfileTypeEnum
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ImportStorageCenterSnapshotProfileInstance.

        Type of the snapshot profile.  # noqa: E501

        :param type: The type of this ImportStorageCenterSnapshotProfileInstance.  # noqa: E501
        :type: ScSnapshotProfileTypeEnum
        """

        self._type = type

    @property
    def description(self):
        """Gets the description of this ImportStorageCenterSnapshotProfileInstance.  # noqa: E501

        Description of the snapshot profile.  # noqa: E501

        :return: The description of this ImportStorageCenterSnapshotProfileInstance.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ImportStorageCenterSnapshotProfileInstance.

        Description of the snapshot profile.  # noqa: E501

        :param description: The description of this ImportStorageCenterSnapshotProfileInstance.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def rules(self):
        """Gets the rules of this ImportStorageCenterSnapshotProfileInstance.  # noqa: E501


        :return: The rules of this ImportStorageCenterSnapshotProfileInstance.  # noqa: E501
        :rtype: list[ScProfileRuleInstance]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this ImportStorageCenterSnapshotProfileInstance.


        :param rules: The rules of this ImportStorageCenterSnapshotProfileInstance.  # noqa: E501
        :type: list[ScProfileRuleInstance]
        """

        self._rules = rules

    @property
    def type_l10n(self):
        """Gets the type_l10n of this ImportStorageCenterSnapshotProfileInstance.  # noqa: E501

        Localized message string corresponding to type  # noqa: E501

        :return: The type_l10n of this ImportStorageCenterSnapshotProfileInstance.  # noqa: E501
        :rtype: str
        """
        return self._type_l10n

    @type_l10n.setter
    def type_l10n(self, type_l10n):
        """Sets the type_l10n of this ImportStorageCenterSnapshotProfileInstance.

        Localized message string corresponding to type  # noqa: E501

        :param type_l10n: The type_l10n of this ImportStorageCenterSnapshotProfileInstance.  # noqa: E501
        :type: str
        """

        self._type_l10n = type_l10n

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
        if issubclass(ImportStorageCenterSnapshotProfileInstance, dict):
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
        if not isinstance(other, ImportStorageCenterSnapshotProfileInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImportStorageCenterSnapshotProfileInstance):
            return True

        return self.to_dict() != other.to_dict()
