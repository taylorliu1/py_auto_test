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


class RemoteSyslogServerInstance(object):
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
        'remote_server_address': 'str',
        'port': 'int',
        'protocol_type': 'ProtocolTypeEnum',
        'encryption': 'EncryptionTypeEnum',
        'audit_types': 'list[AuditEventTypeEnum]',
        'is_enabled': 'bool',
        'status': 'RemoteSyslogServerStatusEnum',
        'protocol_type_l10n': 'str',
        'encryption_l10n': 'str',
        'audit_types_l10n': 'list[str]',
        'status_l10n': 'str'
    }

    attribute_map = {
        'id': 'id',
        'remote_server_address': 'remote_server_address',
        'port': 'port',
        'protocol_type': 'protocol_type',
        'encryption': 'encryption',
        'audit_types': 'audit_types',
        'is_enabled': 'is_enabled',
        'status': 'status',
        'protocol_type_l10n': 'protocol_type_l10n',
        'encryption_l10n': 'encryption_l10n',
        'audit_types_l10n': 'audit_types_l10n',
        'status_l10n': 'status_l10n'
    }

    def __init__(self, id=None, remote_server_address=None, port=None, protocol_type=None, encryption=None, audit_types=None, is_enabled=None, status=None, protocol_type_l10n=None, encryption_l10n=None, audit_types_l10n=None, status_l10n=None, _configuration=None):  # noqa: E501
        """RemoteSyslogServerInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._remote_server_address = None
        self._port = None
        self._protocol_type = None
        self._encryption = None
        self._audit_types = None
        self._is_enabled = None
        self._status = None
        self._protocol_type_l10n = None
        self._encryption_l10n = None
        self._audit_types_l10n = None
        self._status_l10n = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if remote_server_address is not None:
            self.remote_server_address = remote_server_address
        if port is not None:
            self.port = port
        if protocol_type is not None:
            self.protocol_type = protocol_type
        if encryption is not None:
            self.encryption = encryption
        if audit_types is not None:
            self.audit_types = audit_types
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if status is not None:
            self.status = status
        if protocol_type_l10n is not None:
            self.protocol_type_l10n = protocol_type_l10n
        if encryption_l10n is not None:
            self.encryption_l10n = encryption_l10n
        if audit_types_l10n is not None:
            self.audit_types_l10n = audit_types_l10n
        if status_l10n is not None:
            self.status_l10n = status_l10n

    @property
    def id(self):
        """Gets the id of this RemoteSyslogServerInstance.  # noqa: E501

        Unique remote syslog server identifier.  # noqa: E501

        :return: The id of this RemoteSyslogServerInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RemoteSyslogServerInstance.

        Unique remote syslog server identifier.  # noqa: E501

        :param id: The id of this RemoteSyslogServerInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def remote_server_address(self):
        """Gets the remote_server_address of this RemoteSyslogServerInstance.  # noqa: E501

        IPv4 or IPv6 address, or DNS name of the log server.  # noqa: E501

        :return: The remote_server_address of this RemoteSyslogServerInstance.  # noqa: E501
        :rtype: str
        """
        return self._remote_server_address

    @remote_server_address.setter
    def remote_server_address(self, remote_server_address):
        """Sets the remote_server_address of this RemoteSyslogServerInstance.

        IPv4 or IPv6 address, or DNS name of the log server.  # noqa: E501

        :param remote_server_address: The remote_server_address of this RemoteSyslogServerInstance.  # noqa: E501
        :type: str
        """

        self._remote_server_address = remote_server_address

    @property
    def port(self):
        """Gets the port of this RemoteSyslogServerInstance.  # noqa: E501

        Port used for connection to the remote server.  # noqa: E501

        :return: The port of this RemoteSyslogServerInstance.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this RemoteSyslogServerInstance.

        Port used for connection to the remote server.  # noqa: E501

        :param port: The port of this RemoteSyslogServerInstance.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                port is not None and port > 65535):  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value less than or equal to `65535`")  # noqa: E501
        if (self._configuration.client_side_validation and
                port is not None and port < 0):  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value greater than or equal to `0`")  # noqa: E501

        self._port = port

    @property
    def protocol_type(self):
        """Gets the protocol_type of this RemoteSyslogServerInstance.  # noqa: E501


        :return: The protocol_type of this RemoteSyslogServerInstance.  # noqa: E501
        :rtype: ProtocolTypeEnum
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        """Sets the protocol_type of this RemoteSyslogServerInstance.


        :param protocol_type: The protocol_type of this RemoteSyslogServerInstance.  # noqa: E501
        :type: ProtocolTypeEnum
        """

        self._protocol_type = protocol_type

    @property
    def encryption(self):
        """Gets the encryption of this RemoteSyslogServerInstance.  # noqa: E501


        :return: The encryption of this RemoteSyslogServerInstance.  # noqa: E501
        :rtype: EncryptionTypeEnum
        """
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        """Sets the encryption of this RemoteSyslogServerInstance.


        :param encryption: The encryption of this RemoteSyslogServerInstance.  # noqa: E501
        :type: EncryptionTypeEnum
        """

        self._encryption = encryption

    @property
    def audit_types(self):
        """Gets the audit_types of this RemoteSyslogServerInstance.  # noqa: E501

        Audit type selections. If empty, all types will be sent to the remote log server. Otherwise, only audit events of the specified type(s) will be sent.  # noqa: E501

        :return: The audit_types of this RemoteSyslogServerInstance.  # noqa: E501
        :rtype: list[AuditEventTypeEnum]
        """
        return self._audit_types

    @audit_types.setter
    def audit_types(self, audit_types):
        """Sets the audit_types of this RemoteSyslogServerInstance.

        Audit type selections. If empty, all types will be sent to the remote log server. Otherwise, only audit events of the specified type(s) will be sent.  # noqa: E501

        :param audit_types: The audit_types of this RemoteSyslogServerInstance.  # noqa: E501
        :type: list[AuditEventTypeEnum]
        """

        self._audit_types = audit_types

    @property
    def is_enabled(self):
        """Gets the is_enabled of this RemoteSyslogServerInstance.  # noqa: E501

        If true, then this instance will receive audit messages.  # noqa: E501

        :return: The is_enabled of this RemoteSyslogServerInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this RemoteSyslogServerInstance.

        If true, then this instance will receive audit messages.  # noqa: E501

        :param is_enabled: The is_enabled of this RemoteSyslogServerInstance.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def status(self):
        """Gets the status of this RemoteSyslogServerInstance.  # noqa: E501


        :return: The status of this RemoteSyslogServerInstance.  # noqa: E501
        :rtype: RemoteSyslogServerStatusEnum
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RemoteSyslogServerInstance.


        :param status: The status of this RemoteSyslogServerInstance.  # noqa: E501
        :type: RemoteSyslogServerStatusEnum
        """

        self._status = status

    @property
    def protocol_type_l10n(self):
        """Gets the protocol_type_l10n of this RemoteSyslogServerInstance.  # noqa: E501

        Localized message string corresponding to protocol_type Was added in version 2.0.0.0.  # noqa: E501

        :return: The protocol_type_l10n of this RemoteSyslogServerInstance.  # noqa: E501
        :rtype: str
        """
        return self._protocol_type_l10n

    @protocol_type_l10n.setter
    def protocol_type_l10n(self, protocol_type_l10n):
        """Sets the protocol_type_l10n of this RemoteSyslogServerInstance.

        Localized message string corresponding to protocol_type Was added in version 2.0.0.0.  # noqa: E501

        :param protocol_type_l10n: The protocol_type_l10n of this RemoteSyslogServerInstance.  # noqa: E501
        :type: str
        """

        self._protocol_type_l10n = protocol_type_l10n

    @property
    def encryption_l10n(self):
        """Gets the encryption_l10n of this RemoteSyslogServerInstance.  # noqa: E501

        Localized message string corresponding to encryption Was added in version 2.0.0.0.  # noqa: E501

        :return: The encryption_l10n of this RemoteSyslogServerInstance.  # noqa: E501
        :rtype: str
        """
        return self._encryption_l10n

    @encryption_l10n.setter
    def encryption_l10n(self, encryption_l10n):
        """Sets the encryption_l10n of this RemoteSyslogServerInstance.

        Localized message string corresponding to encryption Was added in version 2.0.0.0.  # noqa: E501

        :param encryption_l10n: The encryption_l10n of this RemoteSyslogServerInstance.  # noqa: E501
        :type: str
        """

        self._encryption_l10n = encryption_l10n

    @property
    def audit_types_l10n(self):
        """Gets the audit_types_l10n of this RemoteSyslogServerInstance.  # noqa: E501

        Localized message array corresponding to audit_types Was added in version 2.0.0.0.  # noqa: E501

        :return: The audit_types_l10n of this RemoteSyslogServerInstance.  # noqa: E501
        :rtype: list[str]
        """
        return self._audit_types_l10n

    @audit_types_l10n.setter
    def audit_types_l10n(self, audit_types_l10n):
        """Sets the audit_types_l10n of this RemoteSyslogServerInstance.

        Localized message array corresponding to audit_types Was added in version 2.0.0.0.  # noqa: E501

        :param audit_types_l10n: The audit_types_l10n of this RemoteSyslogServerInstance.  # noqa: E501
        :type: list[str]
        """

        self._audit_types_l10n = audit_types_l10n

    @property
    def status_l10n(self):
        """Gets the status_l10n of this RemoteSyslogServerInstance.  # noqa: E501

        Localized message string corresponding to status Was added in version 2.0.0.0.  # noqa: E501

        :return: The status_l10n of this RemoteSyslogServerInstance.  # noqa: E501
        :rtype: str
        """
        return self._status_l10n

    @status_l10n.setter
    def status_l10n(self, status_l10n):
        """Sets the status_l10n of this RemoteSyslogServerInstance.

        Localized message string corresponding to status Was added in version 2.0.0.0.  # noqa: E501

        :param status_l10n: The status_l10n of this RemoteSyslogServerInstance.  # noqa: E501
        :type: str
        """

        self._status_l10n = status_l10n

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
        if issubclass(RemoteSyslogServerInstance, dict):
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
        if not isinstance(other, RemoteSyslogServerInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RemoteSyslogServerInstance):
            return True

        return self.to_dict() != other.to_dict()
