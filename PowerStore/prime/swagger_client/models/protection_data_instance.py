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


class ProtectionDataInstance(object):
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
        'created_by_rule_id': 'str',
        'created_by_rule_name': 'str',
        'creator_type': 'StorageCreatorTypeEnum',
        'expiration_timestamp': 'datetime',
        'source_timestamp': 'datetime',
        'family_id': 'str',
        'source_id': 'str',
        'parent_id': 'str',
        'copy_signature': 'str',
        'is_app_consistent': 'bool',
        'creator_type_l10n': 'str'
    }

    attribute_map = {
        'created_by_rule_id': 'created_by_rule_id',
        'created_by_rule_name': 'created_by_rule_name',
        'creator_type': 'creator_type',
        'expiration_timestamp': 'expiration_timestamp',
        'source_timestamp': 'source_timestamp',
        'family_id': 'family_id',
        'source_id': 'source_id',
        'parent_id': 'parent_id',
        'copy_signature': 'copy_signature',
        'is_app_consistent': 'is_app_consistent',
        'creator_type_l10n': 'creator_type_l10n'
    }

    def __init__(self, created_by_rule_id=None, created_by_rule_name=None, creator_type=None, expiration_timestamp=None, source_timestamp=None, family_id=None, source_id=None, parent_id=None, copy_signature=None, is_app_consistent=False, creator_type_l10n=None, _configuration=None):  # noqa: E501
        """ProtectionDataInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created_by_rule_id = None
        self._created_by_rule_name = None
        self._creator_type = None
        self._expiration_timestamp = None
        self._source_timestamp = None
        self._family_id = None
        self._source_id = None
        self._parent_id = None
        self._copy_signature = None
        self._is_app_consistent = None
        self._creator_type_l10n = None
        self.discriminator = None

        if created_by_rule_id is not None:
            self.created_by_rule_id = created_by_rule_id
        if created_by_rule_name is not None:
            self.created_by_rule_name = created_by_rule_name
        if creator_type is not None:
            self.creator_type = creator_type
        if expiration_timestamp is not None:
            self.expiration_timestamp = expiration_timestamp
        if source_timestamp is not None:
            self.source_timestamp = source_timestamp
        if family_id is not None:
            self.family_id = family_id
        if source_id is not None:
            self.source_id = source_id
        if parent_id is not None:
            self.parent_id = parent_id
        if copy_signature is not None:
            self.copy_signature = copy_signature
        if is_app_consistent is not None:
            self.is_app_consistent = is_app_consistent
        if creator_type_l10n is not None:
            self.creator_type_l10n = creator_type_l10n

    @property
    def created_by_rule_id(self):
        """Gets the created_by_rule_id of this ProtectionDataInstance.  # noqa: E501

        Unique identifier of the snapshot rule that created the snapshot.  # noqa: E501

        :return: The created_by_rule_id of this ProtectionDataInstance.  # noqa: E501
        :rtype: str
        """
        return self._created_by_rule_id

    @created_by_rule_id.setter
    def created_by_rule_id(self, created_by_rule_id):
        """Sets the created_by_rule_id of this ProtectionDataInstance.

        Unique identifier of the snapshot rule that created the snapshot.  # noqa: E501

        :param created_by_rule_id: The created_by_rule_id of this ProtectionDataInstance.  # noqa: E501
        :type: str
        """

        self._created_by_rule_id = created_by_rule_id

    @property
    def created_by_rule_name(self):
        """Gets the created_by_rule_name of this ProtectionDataInstance.  # noqa: E501

        The name of the rule that created the snapshot. This value will not change if the name of the rule changes after creating the snapshot.  # noqa: E501

        :return: The created_by_rule_name of this ProtectionDataInstance.  # noqa: E501
        :rtype: str
        """
        return self._created_by_rule_name

    @created_by_rule_name.setter
    def created_by_rule_name(self, created_by_rule_name):
        """Sets the created_by_rule_name of this ProtectionDataInstance.

        The name of the rule that created the snapshot. This value will not change if the name of the rule changes after creating the snapshot.  # noqa: E501

        :param created_by_rule_name: The created_by_rule_name of this ProtectionDataInstance.  # noqa: E501
        :type: str
        """

        self._created_by_rule_name = created_by_rule_name

    @property
    def creator_type(self):
        """Gets the creator_type of this ProtectionDataInstance.  # noqa: E501

        StorageCreatorTypeEnum  # noqa: E501

        :return: The creator_type of this ProtectionDataInstance.  # noqa: E501
        :rtype: StorageCreatorTypeEnum
        """
        return self._creator_type

    @creator_type.setter
    def creator_type(self, creator_type):
        """Sets the creator_type of this ProtectionDataInstance.

        StorageCreatorTypeEnum  # noqa: E501

        :param creator_type: The creator_type of this ProtectionDataInstance.  # noqa: E501
        :type: StorageCreatorTypeEnum
        """

        self._creator_type = creator_type

    @property
    def expiration_timestamp(self):
        """Gets the expiration_timestamp of this ProtectionDataInstance.  # noqa: E501

        Date when the snapshot can be automatically purged.  # noqa: E501

        :return: The expiration_timestamp of this ProtectionDataInstance.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_timestamp

    @expiration_timestamp.setter
    def expiration_timestamp(self, expiration_timestamp):
        """Sets the expiration_timestamp of this ProtectionDataInstance.

        Date when the snapshot can be automatically purged.  # noqa: E501

        :param expiration_timestamp: The expiration_timestamp of this ProtectionDataInstance.  # noqa: E501
        :type: datetime
        """

        self._expiration_timestamp = expiration_timestamp

    @property
    def source_timestamp(self):
        """Gets the source_timestamp of this ProtectionDataInstance.  # noqa: E501

        The time at which the resource was sourced from the resource identified by source_id.  # noqa: E501

        :return: The source_timestamp of this ProtectionDataInstance.  # noqa: E501
        :rtype: datetime
        """
        return self._source_timestamp

    @source_timestamp.setter
    def source_timestamp(self, source_timestamp):
        """Sets the source_timestamp of this ProtectionDataInstance.

        The time at which the resource was sourced from the resource identified by source_id.  # noqa: E501

        :param source_timestamp: The source_timestamp of this ProtectionDataInstance.  # noqa: E501
        :type: datetime
        """

        self._source_timestamp = source_timestamp

    @property
    def family_id(self):
        """Gets the family_id of this ProtectionDataInstance.  # noqa: E501

        Family identifier of the resource. This is the identifier of the primary object at the root of the family tree. For a primary resource this will be the same as the unique identifier of the object. For snapshots and clone resources it will be set to the source object's family identifier.  # noqa: E501

        :return: The family_id of this ProtectionDataInstance.  # noqa: E501
        :rtype: str
        """
        return self._family_id

    @family_id.setter
    def family_id(self, family_id):
        """Sets the family_id of this ProtectionDataInstance.

        Family identifier of the resource. This is the identifier of the primary object at the root of the family tree. For a primary resource this will be the same as the unique identifier of the object. For snapshots and clone resources it will be set to the source object's family identifier.  # noqa: E501

        :param family_id: The family_id of this ProtectionDataInstance.  # noqa: E501
        :type: str
        """

        self._family_id = family_id

    @property
    def source_id(self):
        """Gets the source_id of this ProtectionDataInstance.  # noqa: E501

        Unique identifier of the resource from which the content has been sourced. Data is sourced from another resource when a snapshot or clone is created, or when a refresh or restore occurs.  # noqa: E501

        :return: The source_id of this ProtectionDataInstance.  # noqa: E501
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this ProtectionDataInstance.

        Unique identifier of the resource from which the content has been sourced. Data is sourced from another resource when a snapshot or clone is created, or when a refresh or restore occurs.  # noqa: E501

        :param source_id: The source_id of this ProtectionDataInstance.  # noqa: E501
        :type: str
        """

        self._source_id = source_id

    @property
    def parent_id(self):
        """Gets the parent_id of this ProtectionDataInstance.  # noqa: E501

        Unique identifier of the resource from which a snapshot or clone resource is created. The parent_id is set when a resource is created and will only change if its parent resource is deleted. When a resource is deleted, its children get reparented to the parent of the deleted resource. If the deleted parent is of type Primary, the parent_id of the child resources will be set to null.  # noqa: E501

        :return: The parent_id of this ProtectionDataInstance.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this ProtectionDataInstance.

        Unique identifier of the resource from which a snapshot or clone resource is created. The parent_id is set when a resource is created and will only change if its parent resource is deleted. When a resource is deleted, its children get reparented to the parent of the deleted resource. If the deleted parent is of type Primary, the parent_id of the child resources will be set to null.  # noqa: E501

        :param parent_id: The parent_id of this ProtectionDataInstance.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def copy_signature(self):
        """Gets the copy_signature of this ProtectionDataInstance.  # noqa: E501

        Used for tracking replicated copies of a snapshot set.  # noqa: E501

        :return: The copy_signature of this ProtectionDataInstance.  # noqa: E501
        :rtype: str
        """
        return self._copy_signature

    @copy_signature.setter
    def copy_signature(self, copy_signature):
        """Sets the copy_signature of this ProtectionDataInstance.

        Used for tracking replicated copies of a snapshot set.  # noqa: E501

        :param copy_signature: The copy_signature of this ProtectionDataInstance.  # noqa: E501
        :type: str
        """

        self._copy_signature = copy_signature

    @property
    def is_app_consistent(self):
        """Gets the is_app_consistent of this ProtectionDataInstance.  # noqa: E501

        A boolean flag that indicates whether the snapshot is application consistent. Only App Sync can create application consistent snapshots.  # noqa: E501

        :return: The is_app_consistent of this ProtectionDataInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_app_consistent

    @is_app_consistent.setter
    def is_app_consistent(self, is_app_consistent):
        """Sets the is_app_consistent of this ProtectionDataInstance.

        A boolean flag that indicates whether the snapshot is application consistent. Only App Sync can create application consistent snapshots.  # noqa: E501

        :param is_app_consistent: The is_app_consistent of this ProtectionDataInstance.  # noqa: E501
        :type: bool
        """

        self._is_app_consistent = is_app_consistent

    @property
    def creator_type_l10n(self):
        """Gets the creator_type_l10n of this ProtectionDataInstance.  # noqa: E501

        Localized message string corresponding to creator_type  # noqa: E501

        :return: The creator_type_l10n of this ProtectionDataInstance.  # noqa: E501
        :rtype: str
        """
        return self._creator_type_l10n

    @creator_type_l10n.setter
    def creator_type_l10n(self, creator_type_l10n):
        """Sets the creator_type_l10n of this ProtectionDataInstance.

        Localized message string corresponding to creator_type  # noqa: E501

        :param creator_type_l10n: The creator_type_l10n of this ProtectionDataInstance.  # noqa: E501
        :type: str
        """

        self._creator_type_l10n = creator_type_l10n

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
        if issubclass(ProtectionDataInstance, dict):
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
        if not isinstance(other, ProtectionDataInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProtectionDataInstance):
            return True

        return self.to_dict() != other.to_dict()
