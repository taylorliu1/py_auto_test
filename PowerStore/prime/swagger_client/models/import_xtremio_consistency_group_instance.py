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


class ImportXtremioConsistencyGroupInstance(object):
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
        'import_xtremio_id': 'str',
        'importable_criteria': 'CGImportableCriteriaEnum',
        'importable_criteria_l10n': 'str',
        'import_xtremio_volumes': 'list[ImportXtremioVolumeInstance]',
        'import_xtremio': 'ImportXtremioInstance'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'import_xtremio_id': 'import_xtremio_id',
        'importable_criteria': 'importable_criteria',
        'importable_criteria_l10n': 'importable_criteria_l10n',
        'import_xtremio_volumes': 'import_xtremio_volumes',
        'import_xtremio': 'import_xtremio'
    }

    def __init__(self, id=None, name=None, import_xtremio_id=None, importable_criteria=None, importable_criteria_l10n=None, import_xtremio_volumes=None, import_xtremio=None, _configuration=None):  # noqa: E501
        """ImportXtremioConsistencyGroupInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._import_xtremio_id = None
        self._importable_criteria = None
        self._importable_criteria_l10n = None
        self._import_xtremio_volumes = None
        self._import_xtremio = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if import_xtremio_id is not None:
            self.import_xtremio_id = import_xtremio_id
        if importable_criteria is not None:
            self.importable_criteria = importable_criteria
        if importable_criteria_l10n is not None:
            self.importable_criteria_l10n = importable_criteria_l10n
        if import_xtremio_volumes is not None:
            self.import_xtremio_volumes = import_xtremio_volumes
        if import_xtremio is not None:
            self.import_xtremio = import_xtremio

    @property
    def id(self):
        """Gets the id of this ImportXtremioConsistencyGroupInstance.  # noqa: E501

        Unique identifier of the XtremIO consistency group.  # noqa: E501

        :return: The id of this ImportXtremioConsistencyGroupInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImportXtremioConsistencyGroupInstance.

        Unique identifier of the XtremIO consistency group.  # noqa: E501

        :param id: The id of this ImportXtremioConsistencyGroupInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ImportXtremioConsistencyGroupInstance.  # noqa: E501

        Name of the consistency group.  This property supports case-insensitive filtering.  # noqa: E501

        :return: The name of this ImportXtremioConsistencyGroupInstance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImportXtremioConsistencyGroupInstance.

        Name of the consistency group.  This property supports case-insensitive filtering.  # noqa: E501

        :param name: The name of this ImportXtremioConsistencyGroupInstance.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def import_xtremio_id(self):
        """Gets the import_xtremio_id of this ImportXtremioConsistencyGroupInstance.  # noqa: E501

        Unique identifier of the XtremIO storage system where the consistency group resides.  # noqa: E501

        :return: The import_xtremio_id of this ImportXtremioConsistencyGroupInstance.  # noqa: E501
        :rtype: str
        """
        return self._import_xtremio_id

    @import_xtremio_id.setter
    def import_xtremio_id(self, import_xtremio_id):
        """Sets the import_xtremio_id of this ImportXtremioConsistencyGroupInstance.

        Unique identifier of the XtremIO storage system where the consistency group resides.  # noqa: E501

        :param import_xtremio_id: The import_xtremio_id of this ImportXtremioConsistencyGroupInstance.  # noqa: E501
        :type: str
        """

        self._import_xtremio_id = import_xtremio_id

    @property
    def importable_criteria(self):
        """Gets the importable_criteria of this ImportXtremioConsistencyGroupInstance.  # noqa: E501

        Consistency group import criteria. If the value is not Ready, the consistency group is not importable.  # noqa: E501

        :return: The importable_criteria of this ImportXtremioConsistencyGroupInstance.  # noqa: E501
        :rtype: CGImportableCriteriaEnum
        """
        return self._importable_criteria

    @importable_criteria.setter
    def importable_criteria(self, importable_criteria):
        """Sets the importable_criteria of this ImportXtremioConsistencyGroupInstance.

        Consistency group import criteria. If the value is not Ready, the consistency group is not importable.  # noqa: E501

        :param importable_criteria: The importable_criteria of this ImportXtremioConsistencyGroupInstance.  # noqa: E501
        :type: CGImportableCriteriaEnum
        """

        self._importable_criteria = importable_criteria

    @property
    def importable_criteria_l10n(self):
        """Gets the importable_criteria_l10n of this ImportXtremioConsistencyGroupInstance.  # noqa: E501

        Localized message string corresponding to importable_criteria Was added in version 1.0.2.  # noqa: E501

        :return: The importable_criteria_l10n of this ImportXtremioConsistencyGroupInstance.  # noqa: E501
        :rtype: str
        """
        return self._importable_criteria_l10n

    @importable_criteria_l10n.setter
    def importable_criteria_l10n(self, importable_criteria_l10n):
        """Sets the importable_criteria_l10n of this ImportXtremioConsistencyGroupInstance.

        Localized message string corresponding to importable_criteria Was added in version 1.0.2.  # noqa: E501

        :param importable_criteria_l10n: The importable_criteria_l10n of this ImportXtremioConsistencyGroupInstance.  # noqa: E501
        :type: str
        """

        self._importable_criteria_l10n = importable_criteria_l10n

    @property
    def import_xtremio_volumes(self):
        """Gets the import_xtremio_volumes of this ImportXtremioConsistencyGroupInstance.  # noqa: E501

        This is the inverse of the resource type import_xtremio_volume association.  # noqa: E501

        :return: The import_xtremio_volumes of this ImportXtremioConsistencyGroupInstance.  # noqa: E501
        :rtype: list[ImportXtremioVolumeInstance]
        """
        return self._import_xtremio_volumes

    @import_xtremio_volumes.setter
    def import_xtremio_volumes(self, import_xtremio_volumes):
        """Sets the import_xtremio_volumes of this ImportXtremioConsistencyGroupInstance.

        This is the inverse of the resource type import_xtremio_volume association.  # noqa: E501

        :param import_xtremio_volumes: The import_xtremio_volumes of this ImportXtremioConsistencyGroupInstance.  # noqa: E501
        :type: list[ImportXtremioVolumeInstance]
        """

        self._import_xtremio_volumes = import_xtremio_volumes

    @property
    def import_xtremio(self):
        """Gets the import_xtremio of this ImportXtremioConsistencyGroupInstance.  # noqa: E501

        This is the embeddable reference form of import_xtremio_id attribute.  # noqa: E501

        :return: The import_xtremio of this ImportXtremioConsistencyGroupInstance.  # noqa: E501
        :rtype: ImportXtremioInstance
        """
        return self._import_xtremio

    @import_xtremio.setter
    def import_xtremio(self, import_xtremio):
        """Sets the import_xtremio of this ImportXtremioConsistencyGroupInstance.

        This is the embeddable reference form of import_xtremio_id attribute.  # noqa: E501

        :param import_xtremio: The import_xtremio of this ImportXtremioConsistencyGroupInstance.  # noqa: E501
        :type: ImportXtremioInstance
        """

        self._import_xtremio = import_xtremio

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
        if issubclass(ImportXtremioConsistencyGroupInstance, dict):
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
        if not isinstance(other, ImportXtremioConsistencyGroupInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImportXtremioConsistencyGroupInstance):
            return True

        return self.to_dict() != other.to_dict()
