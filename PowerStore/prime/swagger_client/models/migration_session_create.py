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


class MigrationSessionCreate(object):
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
        'resource_type': 'MigrationResourceTypeEnum',
        'family_id': 'str',
        'destination_appliance_id': 'str',
        'automatic_cutover': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'resource_type': 'resource_type',
        'family_id': 'family_id',
        'destination_appliance_id': 'destination_appliance_id',
        'automatic_cutover': 'automatic_cutover'
    }

    def __init__(self, name=None, resource_type=None, family_id=None, destination_appliance_id=None, automatic_cutover=False, _configuration=None):  # noqa: E501
        """MigrationSessionCreate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._resource_type = None
        self._family_id = None
        self._destination_appliance_id = None
        self._automatic_cutover = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.resource_type = resource_type
        self.family_id = family_id
        self.destination_appliance_id = destination_appliance_id
        if automatic_cutover is not None:
            self.automatic_cutover = automatic_cutover

    @property
    def name(self):
        """Gets the name of this MigrationSessionCreate.  # noqa: E501

        User-specified friendly name of the migration session instance. The name can contain a maximum of 32 Unicode characters. It cannot contain unprintable characters, special HTTP characters, or whitespace.  # noqa: E501

        :return: The name of this MigrationSessionCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MigrationSessionCreate.

        User-specified friendly name of the migration session instance. The name can contain a maximum of 32 Unicode characters. It cannot contain unprintable characters, special HTTP characters, or whitespace.  # noqa: E501

        :param name: The name of this MigrationSessionCreate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def resource_type(self):
        """Gets the resource_type of this MigrationSessionCreate.  # noqa: E501


        :return: The resource_type of this MigrationSessionCreate.  # noqa: E501
        :rtype: MigrationResourceTypeEnum
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this MigrationSessionCreate.


        :param resource_type: The resource_type of this MigrationSessionCreate.  # noqa: E501
        :type: MigrationResourceTypeEnum
        """
        if self._configuration.client_side_validation and resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501

        self._resource_type = resource_type

    @property
    def family_id(self):
        """Gets the family_id of this MigrationSessionCreate.  # noqa: E501

        Family identifier designating the storage resource or resources to migrate. For volume or virtual_volume migrations, the family is moved together because they share data among the primary object, snapshots, and clones. For volume_group migration, the family of each volume in the group is moved because it is a grouping of volumes.  # noqa: E501

        :return: The family_id of this MigrationSessionCreate.  # noqa: E501
        :rtype: str
        """
        return self._family_id

    @family_id.setter
    def family_id(self, family_id):
        """Sets the family_id of this MigrationSessionCreate.

        Family identifier designating the storage resource or resources to migrate. For volume or virtual_volume migrations, the family is moved together because they share data among the primary object, snapshots, and clones. For volume_group migration, the family of each volume in the group is moved because it is a grouping of volumes.  # noqa: E501

        :param family_id: The family_id of this MigrationSessionCreate.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and family_id is None:
            raise ValueError("Invalid value for `family_id`, must not be `None`")  # noqa: E501

        self._family_id = family_id

    @property
    def destination_appliance_id(self):
        """Gets the destination_appliance_id of this MigrationSessionCreate.  # noqa: E501

        Unique identifier of the destination appliance instance. name:{name} can be used instead of {id}. For example:'appliance_id':'name:appliance_name'  # noqa: E501

        :return: The destination_appliance_id of this MigrationSessionCreate.  # noqa: E501
        :rtype: str
        """
        return self._destination_appliance_id

    @destination_appliance_id.setter
    def destination_appliance_id(self, destination_appliance_id):
        """Sets the destination_appliance_id of this MigrationSessionCreate.

        Unique identifier of the destination appliance instance. name:{name} can be used instead of {id}. For example:'appliance_id':'name:appliance_name'  # noqa: E501

        :param destination_appliance_id: The destination_appliance_id of this MigrationSessionCreate.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and destination_appliance_id is None:
            raise ValueError("Invalid value for `destination_appliance_id`, must not be `None`")  # noqa: E501

        self._destination_appliance_id = destination_appliance_id

    @property
    def automatic_cutover(self):
        """Gets the automatic_cutover of this MigrationSessionCreate.  # noqa: E501

        Indicates whether the migration session cutover is manual or automatic. Default for virtual_volume resource type migrations is automatic, otherwise the default is manual.  # noqa: E501

        :return: The automatic_cutover of this MigrationSessionCreate.  # noqa: E501
        :rtype: bool
        """
        return self._automatic_cutover

    @automatic_cutover.setter
    def automatic_cutover(self, automatic_cutover):
        """Sets the automatic_cutover of this MigrationSessionCreate.

        Indicates whether the migration session cutover is manual or automatic. Default for virtual_volume resource type migrations is automatic, otherwise the default is manual.  # noqa: E501

        :param automatic_cutover: The automatic_cutover of this MigrationSessionCreate.  # noqa: E501
        :type: bool
        """

        self._automatic_cutover = automatic_cutover

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
        if issubclass(MigrationSessionCreate, dict):
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
        if not isinstance(other, MigrationSessionCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MigrationSessionCreate):
            return True

        return self.to_dict() != other.to_dict()
