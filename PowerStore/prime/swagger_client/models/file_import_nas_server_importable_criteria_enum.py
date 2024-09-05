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


class FileImportNasServerImportableCriteriaEnum(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    READY = "Ready"
    IN_PROGRESS = "In_Progress"
    MULTIPLE_CIFS_SERVERS = "Multiple_CIFS_Servers"
    PROTOCOL_TYPE_CHANGED = "Protocol_Type_Changed"
    FAILED_PRECHECK = "Failed_Precheck"
    NO_PRODUCTION_FILE_INTERFACES = "No_Production_File_Interfaces"
    NO_FILE_INTERFACES = "No_File_Interfaces"
    NO_IMPORT_FILE_INTERFACES = "No_Import_File_Interfaces"
    DESTINATION_NAS_SERVER_LIMIT_EXCEEDED = "Destination_NAS_Server_Limit_Exceeded"
    DESTINATION_FILE_INTERFACES_LIMIT_EXCEEDED = "Destination_File_Interfaces_Limit_Exceeded"
    UNSUPPORTED_PROTOCOL_TYPE = "Unsupported_Protocol_Type"
    CONFIGURATION_CHANGE_DETECTED = "Configuration_Change_Detected"
    VALIDATION_FAILED = "Validation_Failed"
    NO_SUITABLE_IMPORT_FILE_INTERFACE = "No_Suitable_Import_File_Interface"
    IMPORTED = "Imported"
    SINGLE_ACTIVE_FILE_INTERFACE = "Single_Active_File_Interface"

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self, _configuration=None):  # noqa: E501
        """FileImportNasServerImportableCriteriaEnum - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration
        self.discriminator = None

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
        if issubclass(FileImportNasServerImportableCriteriaEnum, dict):
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
        if not isinstance(other, FileImportNasServerImportableCriteriaEnum):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileImportNasServerImportableCriteriaEnum):
            return True

        return self.to_dict() != other.to_dict()
