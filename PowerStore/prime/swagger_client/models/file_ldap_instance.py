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


class FileLdapInstance(object):
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
        'nas_server_id': 'str',
        'base_dn': 'str',
        'profile_dn': 'str',
        'addresses': 'list[str]',
        'port_number': 'int',
        'authentication_type': 'FileLDAPAuthenticationTypeEnum',
        'protocol': 'FileLDAPProtocolEnum',
        'is_verify_server_certificate': 'bool',
        'bind_dn': 'str',
        'is_smb_account_used': 'bool',
        'principal': 'str',
        'realm': 'str',
        'schema_type': 'FileLDAPSchemaTypeEnum',
        'is_config_file_uploaded': 'bool',
        'is_certificate_uploaded': 'bool',
        'is_destination_override_enabled': 'bool',
        'source_parameters': 'object',
        'authentication_type_l10n': 'str',
        'protocol_l10n': 'str',
        'schema_type_l10n': 'str',
        'nas_server': 'NasServerInstance'
    }

    attribute_map = {
        'id': 'id',
        'nas_server_id': 'nas_server_id',
        'base_dn': 'base_DN',
        'profile_dn': 'profile_DN',
        'addresses': 'addresses',
        'port_number': 'port_number',
        'authentication_type': 'authentication_type',
        'protocol': 'protocol',
        'is_verify_server_certificate': 'is_verify_server_certificate',
        'bind_dn': 'bind_DN',
        'is_smb_account_used': 'is_smb_account_used',
        'principal': 'principal',
        'realm': 'realm',
        'schema_type': 'schema_type',
        'is_config_file_uploaded': 'is_config_file_uploaded',
        'is_certificate_uploaded': 'is_certificate_uploaded',
        'is_destination_override_enabled': 'is_destination_override_enabled',
        'source_parameters': 'source_parameters',
        'authentication_type_l10n': 'authentication_type_l10n',
        'protocol_l10n': 'protocol_l10n',
        'schema_type_l10n': 'schema_type_l10n',
        'nas_server': 'nas_server'
    }

    def __init__(self, id=None, nas_server_id=None, base_dn=None, profile_dn=None, addresses=None, port_number=None, authentication_type=None, protocol=None, is_verify_server_certificate=None, bind_dn=None, is_smb_account_used=None, principal=None, realm=None, schema_type=None, is_config_file_uploaded=False, is_certificate_uploaded=False, is_destination_override_enabled=False, source_parameters=None, authentication_type_l10n=None, protocol_l10n=None, schema_type_l10n=None, nas_server=None, _configuration=None):  # noqa: E501
        """FileLdapInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._nas_server_id = None
        self._base_dn = None
        self._profile_dn = None
        self._addresses = None
        self._port_number = None
        self._authentication_type = None
        self._protocol = None
        self._is_verify_server_certificate = None
        self._bind_dn = None
        self._is_smb_account_used = None
        self._principal = None
        self._realm = None
        self._schema_type = None
        self._is_config_file_uploaded = None
        self._is_certificate_uploaded = None
        self._is_destination_override_enabled = None
        self._source_parameters = None
        self._authentication_type_l10n = None
        self._protocol_l10n = None
        self._schema_type_l10n = None
        self._nas_server = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if nas_server_id is not None:
            self.nas_server_id = nas_server_id
        if base_dn is not None:
            self.base_dn = base_dn
        if profile_dn is not None:
            self.profile_dn = profile_dn
        if addresses is not None:
            self.addresses = addresses
        if port_number is not None:
            self.port_number = port_number
        if authentication_type is not None:
            self.authentication_type = authentication_type
        if protocol is not None:
            self.protocol = protocol
        if is_verify_server_certificate is not None:
            self.is_verify_server_certificate = is_verify_server_certificate
        if bind_dn is not None:
            self.bind_dn = bind_dn
        if is_smb_account_used is not None:
            self.is_smb_account_used = is_smb_account_used
        if principal is not None:
            self.principal = principal
        if realm is not None:
            self.realm = realm
        if schema_type is not None:
            self.schema_type = schema_type
        if is_config_file_uploaded is not None:
            self.is_config_file_uploaded = is_config_file_uploaded
        if is_certificate_uploaded is not None:
            self.is_certificate_uploaded = is_certificate_uploaded
        if is_destination_override_enabled is not None:
            self.is_destination_override_enabled = is_destination_override_enabled
        if source_parameters is not None:
            self.source_parameters = source_parameters
        if authentication_type_l10n is not None:
            self.authentication_type_l10n = authentication_type_l10n
        if protocol_l10n is not None:
            self.protocol_l10n = protocol_l10n
        if schema_type_l10n is not None:
            self.schema_type_l10n = schema_type_l10n
        if nas_server is not None:
            self.nas_server = nas_server

    @property
    def id(self):
        """Gets the id of this FileLdapInstance.  # noqa: E501

        Unique identifier of the LDAP service object.  # noqa: E501

        :return: The id of this FileLdapInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FileLdapInstance.

        Unique identifier of the LDAP service object.  # noqa: E501

        :param id: The id of this FileLdapInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def nas_server_id(self):
        """Gets the nas_server_id of this FileLdapInstance.  # noqa: E501

        Unique identifier of the associated NAS Server instance that uses this LDAP object. Only one LDAP object per NAS Server is supported.   # noqa: E501

        :return: The nas_server_id of this FileLdapInstance.  # noqa: E501
        :rtype: str
        """
        return self._nas_server_id

    @nas_server_id.setter
    def nas_server_id(self, nas_server_id):
        """Sets the nas_server_id of this FileLdapInstance.

        Unique identifier of the associated NAS Server instance that uses this LDAP object. Only one LDAP object per NAS Server is supported.   # noqa: E501

        :param nas_server_id: The nas_server_id of this FileLdapInstance.  # noqa: E501
        :type: str
        """

        self._nas_server_id = nas_server_id

    @property
    def base_dn(self):
        """Gets the base_dn of this FileLdapInstance.  # noqa: E501

        Name of the LDAP base DN.  Base Distinguished Name (BDN) of the root of the LDAP directory tree. The appliance uses the DN to bind to the LDAP service and locate in the LDAP directory tree to begin a search for information.   The base DN can be expressed as a fully-qualified domain name or in X.509 format by using the attribute dc=. For example, if the fully-qualified domain name is mycompany.com, the base DN is expressed as dc=mycompany,dc=com.  # noqa: E501

        :return: The base_dn of this FileLdapInstance.  # noqa: E501
        :rtype: str
        """
        return self._base_dn

    @base_dn.setter
    def base_dn(self, base_dn):
        """Sets the base_dn of this FileLdapInstance.

        Name of the LDAP base DN.  Base Distinguished Name (BDN) of the root of the LDAP directory tree. The appliance uses the DN to bind to the LDAP service and locate in the LDAP directory tree to begin a search for information.   The base DN can be expressed as a fully-qualified domain name or in X.509 format by using the attribute dc=. For example, if the fully-qualified domain name is mycompany.com, the base DN is expressed as dc=mycompany,dc=com.  # noqa: E501

        :param base_dn: The base_dn of this FileLdapInstance.  # noqa: E501
        :type: str
        """

        self._base_dn = base_dn

    @property
    def profile_dn(self):
        """Gets the profile_dn of this FileLdapInstance.  # noqa: E501

        For an iPlanet LDAP server, specifies the DN of the entry with the configuration profile.  # noqa: E501

        :return: The profile_dn of this FileLdapInstance.  # noqa: E501
        :rtype: str
        """
        return self._profile_dn

    @profile_dn.setter
    def profile_dn(self, profile_dn):
        """Sets the profile_dn of this FileLdapInstance.

        For an iPlanet LDAP server, specifies the DN of the entry with the configuration profile.  # noqa: E501

        :param profile_dn: The profile_dn of this FileLdapInstance.  # noqa: E501
        :type: str
        """

        self._profile_dn = profile_dn

    @property
    def addresses(self):
        """Gets the addresses of this FileLdapInstance.  # noqa: E501

        The list of LDAP server IP addresses. The addresses may be IPv4 or IPv6.  # noqa: E501

        :return: The addresses of this FileLdapInstance.  # noqa: E501
        :rtype: list[str]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this FileLdapInstance.

        The list of LDAP server IP addresses. The addresses may be IPv4 or IPv6.  # noqa: E501

        :param addresses: The addresses of this FileLdapInstance.  # noqa: E501
        :type: list[str]
        """

        self._addresses = addresses

    @property
    def port_number(self):
        """Gets the port_number of this FileLdapInstance.  # noqa: E501

        The TCP/IP port used by the NAS Server to connect to the LDAP servers. The default port number for LDAP is 389 and LDAPS is 636.  # noqa: E501

        :return: The port_number of this FileLdapInstance.  # noqa: E501
        :rtype: int
        """
        return self._port_number

    @port_number.setter
    def port_number(self, port_number):
        """Sets the port_number of this FileLdapInstance.

        The TCP/IP port used by the NAS Server to connect to the LDAP servers. The default port number for LDAP is 389 and LDAPS is 636.  # noqa: E501

        :param port_number: The port_number of this FileLdapInstance.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                port_number is not None and port_number > 65535):  # noqa: E501
            raise ValueError("Invalid value for `port_number`, must be a value less than or equal to `65535`")  # noqa: E501
        if (self._configuration.client_side_validation and
                port_number is not None and port_number < 0):  # noqa: E501
            raise ValueError("Invalid value for `port_number`, must be a value greater than or equal to `0`")  # noqa: E501

        self._port_number = port_number

    @property
    def authentication_type(self):
        """Gets the authentication_type of this FileLdapInstance.  # noqa: E501


        :return: The authentication_type of this FileLdapInstance.  # noqa: E501
        :rtype: FileLDAPAuthenticationTypeEnum
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        """Sets the authentication_type of this FileLdapInstance.


        :param authentication_type: The authentication_type of this FileLdapInstance.  # noqa: E501
        :type: FileLDAPAuthenticationTypeEnum
        """

        self._authentication_type = authentication_type

    @property
    def protocol(self):
        """Gets the protocol of this FileLdapInstance.  # noqa: E501


        :return: The protocol of this FileLdapInstance.  # noqa: E501
        :rtype: FileLDAPProtocolEnum
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this FileLdapInstance.


        :param protocol: The protocol of this FileLdapInstance.  # noqa: E501
        :type: FileLDAPProtocolEnum
        """

        self._protocol = protocol

    @property
    def is_verify_server_certificate(self):
        """Gets the is_verify_server_certificate of this FileLdapInstance.  # noqa: E501

        Indicates whether a Certification Authority certificate is used to verify the LDAP server certificate for secure SSL connections. Values are:  * true - verifies LDAP server's certificate.  * false - doesn't verify LDAP server's certificate.   # noqa: E501

        :return: The is_verify_server_certificate of this FileLdapInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_verify_server_certificate

    @is_verify_server_certificate.setter
    def is_verify_server_certificate(self, is_verify_server_certificate):
        """Sets the is_verify_server_certificate of this FileLdapInstance.

        Indicates whether a Certification Authority certificate is used to verify the LDAP server certificate for secure SSL connections. Values are:  * true - verifies LDAP server's certificate.  * false - doesn't verify LDAP server's certificate.   # noqa: E501

        :param is_verify_server_certificate: The is_verify_server_certificate of this FileLdapInstance.  # noqa: E501
        :type: bool
        """

        self._is_verify_server_certificate = is_verify_server_certificate

    @property
    def bind_dn(self):
        """Gets the bind_dn of this FileLdapInstance.  # noqa: E501

        Bind Distinguished Name (DN) to be used when binding.  # noqa: E501

        :return: The bind_dn of this FileLdapInstance.  # noqa: E501
        :rtype: str
        """
        return self._bind_dn

    @bind_dn.setter
    def bind_dn(self, bind_dn):
        """Sets the bind_dn of this FileLdapInstance.

        Bind Distinguished Name (DN) to be used when binding.  # noqa: E501

        :param bind_dn: The bind_dn of this FileLdapInstance.  # noqa: E501
        :type: str
        """

        self._bind_dn = bind_dn

    @property
    def is_smb_account_used(self):
        """Gets the is_smb_account_used of this FileLdapInstance.  # noqa: E501

        Indicates whether SMB authentication is used to authenticate to the LDAP server. Values are:     * true - Indicates that the SMB settings are used for Kerberos authentication.     * false - Indicates that Kerberos uses its own settings.   # noqa: E501

        :return: The is_smb_account_used of this FileLdapInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_smb_account_used

    @is_smb_account_used.setter
    def is_smb_account_used(self, is_smb_account_used):
        """Sets the is_smb_account_used of this FileLdapInstance.

        Indicates whether SMB authentication is used to authenticate to the LDAP server. Values are:     * true - Indicates that the SMB settings are used for Kerberos authentication.     * false - Indicates that Kerberos uses its own settings.   # noqa: E501

        :param is_smb_account_used: The is_smb_account_used of this FileLdapInstance.  # noqa: E501
        :type: bool
        """

        self._is_smb_account_used = is_smb_account_used

    @property
    def principal(self):
        """Gets the principal of this FileLdapInstance.  # noqa: E501

        Specifies the principal name for Kerberos authentication.  # noqa: E501

        :return: The principal of this FileLdapInstance.  # noqa: E501
        :rtype: str
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this FileLdapInstance.

        Specifies the principal name for Kerberos authentication.  # noqa: E501

        :param principal: The principal of this FileLdapInstance.  # noqa: E501
        :type: str
        """

        self._principal = principal

    @property
    def realm(self):
        """Gets the realm of this FileLdapInstance.  # noqa: E501

        Specifies the realm name for Kerberos authentication.  # noqa: E501

        :return: The realm of this FileLdapInstance.  # noqa: E501
        :rtype: str
        """
        return self._realm

    @realm.setter
    def realm(self, realm):
        """Sets the realm of this FileLdapInstance.

        Specifies the realm name for Kerberos authentication.  # noqa: E501

        :param realm: The realm of this FileLdapInstance.  # noqa: E501
        :type: str
        """

        self._realm = realm

    @property
    def schema_type(self):
        """Gets the schema_type of this FileLdapInstance.  # noqa: E501


        :return: The schema_type of this FileLdapInstance.  # noqa: E501
        :rtype: FileLDAPSchemaTypeEnum
        """
        return self._schema_type

    @schema_type.setter
    def schema_type(self, schema_type):
        """Sets the schema_type of this FileLdapInstance.


        :param schema_type: The schema_type of this FileLdapInstance.  # noqa: E501
        :type: FileLDAPSchemaTypeEnum
        """

        self._schema_type = schema_type

    @property
    def is_config_file_uploaded(self):
        """Gets the is_config_file_uploaded of this FileLdapInstance.  # noqa: E501

        Indicates whether an LDAP configuration file has been uploaded.  # noqa: E501

        :return: The is_config_file_uploaded of this FileLdapInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_config_file_uploaded

    @is_config_file_uploaded.setter
    def is_config_file_uploaded(self, is_config_file_uploaded):
        """Sets the is_config_file_uploaded of this FileLdapInstance.

        Indicates whether an LDAP configuration file has been uploaded.  # noqa: E501

        :param is_config_file_uploaded: The is_config_file_uploaded of this FileLdapInstance.  # noqa: E501
        :type: bool
        """

        self._is_config_file_uploaded = is_config_file_uploaded

    @property
    def is_certificate_uploaded(self):
        """Gets the is_certificate_uploaded of this FileLdapInstance.  # noqa: E501

        Indicates whether an LDAP certificate file has been uploaded.  # noqa: E501

        :return: The is_certificate_uploaded of this FileLdapInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_certificate_uploaded

    @is_certificate_uploaded.setter
    def is_certificate_uploaded(self, is_certificate_uploaded):
        """Sets the is_certificate_uploaded of this FileLdapInstance.

        Indicates whether an LDAP certificate file has been uploaded.  # noqa: E501

        :param is_certificate_uploaded: The is_certificate_uploaded of this FileLdapInstance.  # noqa: E501
        :type: bool
        """

        self._is_certificate_uploaded = is_certificate_uploaded

    @property
    def is_destination_override_enabled(self):
        """Gets the is_destination_override_enabled of this FileLdapInstance.  # noqa: E501

        In order to modify any properties of this resource when the associated NAS server is a replication destination, the is_destination_override_enabled flag must be set to true. When true these properties may be modified: addresses Values are:   true - Enable locally set properties. Source property changes will propagate to the source_parameters of the resource.   false - Reset the properties to the ones from the source. Source property changes will propagate directly to this resource.  Was added in version 3.0.0.0.  # noqa: E501

        :return: The is_destination_override_enabled of this FileLdapInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_destination_override_enabled

    @is_destination_override_enabled.setter
    def is_destination_override_enabled(self, is_destination_override_enabled):
        """Sets the is_destination_override_enabled of this FileLdapInstance.

        In order to modify any properties of this resource when the associated NAS server is a replication destination, the is_destination_override_enabled flag must be set to true. When true these properties may be modified: addresses Values are:   true - Enable locally set properties. Source property changes will propagate to the source_parameters of the resource.   false - Reset the properties to the ones from the source. Source property changes will propagate directly to this resource.  Was added in version 3.0.0.0.  # noqa: E501

        :param is_destination_override_enabled: The is_destination_override_enabled of this FileLdapInstance.  # noqa: E501
        :type: bool
        """

        self._is_destination_override_enabled = is_destination_override_enabled

    @property
    def source_parameters(self):
        """Gets the source_parameters of this FileLdapInstance.  # noqa: E501

        Information about the corresponding source NAS Server's File LDAP settings. Only populated when is_destination_override_enabled flag is set to true. Was added in version 3.0.0.0.  Filtering on the fields of this embedded resource is not supported.  # noqa: E501

        :return: The source_parameters of this FileLdapInstance.  # noqa: E501
        :rtype: object
        """
        return self._source_parameters

    @source_parameters.setter
    def source_parameters(self, source_parameters):
        """Sets the source_parameters of this FileLdapInstance.

        Information about the corresponding source NAS Server's File LDAP settings. Only populated when is_destination_override_enabled flag is set to true. Was added in version 3.0.0.0.  Filtering on the fields of this embedded resource is not supported.  # noqa: E501

        :param source_parameters: The source_parameters of this FileLdapInstance.  # noqa: E501
        :type: object
        """

        self._source_parameters = source_parameters

    @property
    def authentication_type_l10n(self):
        """Gets the authentication_type_l10n of this FileLdapInstance.  # noqa: E501

        Localized message string corresponding to authentication_type  # noqa: E501

        :return: The authentication_type_l10n of this FileLdapInstance.  # noqa: E501
        :rtype: str
        """
        return self._authentication_type_l10n

    @authentication_type_l10n.setter
    def authentication_type_l10n(self, authentication_type_l10n):
        """Sets the authentication_type_l10n of this FileLdapInstance.

        Localized message string corresponding to authentication_type  # noqa: E501

        :param authentication_type_l10n: The authentication_type_l10n of this FileLdapInstance.  # noqa: E501
        :type: str
        """

        self._authentication_type_l10n = authentication_type_l10n

    @property
    def protocol_l10n(self):
        """Gets the protocol_l10n of this FileLdapInstance.  # noqa: E501

        Localized message string corresponding to protocol  # noqa: E501

        :return: The protocol_l10n of this FileLdapInstance.  # noqa: E501
        :rtype: str
        """
        return self._protocol_l10n

    @protocol_l10n.setter
    def protocol_l10n(self, protocol_l10n):
        """Sets the protocol_l10n of this FileLdapInstance.

        Localized message string corresponding to protocol  # noqa: E501

        :param protocol_l10n: The protocol_l10n of this FileLdapInstance.  # noqa: E501
        :type: str
        """

        self._protocol_l10n = protocol_l10n

    @property
    def schema_type_l10n(self):
        """Gets the schema_type_l10n of this FileLdapInstance.  # noqa: E501

        Localized message string corresponding to schema_type  # noqa: E501

        :return: The schema_type_l10n of this FileLdapInstance.  # noqa: E501
        :rtype: str
        """
        return self._schema_type_l10n

    @schema_type_l10n.setter
    def schema_type_l10n(self, schema_type_l10n):
        """Sets the schema_type_l10n of this FileLdapInstance.

        Localized message string corresponding to schema_type  # noqa: E501

        :param schema_type_l10n: The schema_type_l10n of this FileLdapInstance.  # noqa: E501
        :type: str
        """

        self._schema_type_l10n = schema_type_l10n

    @property
    def nas_server(self):
        """Gets the nas_server of this FileLdapInstance.  # noqa: E501

        This is the embeddable reference form of nas_server_id attribute.  # noqa: E501

        :return: The nas_server of this FileLdapInstance.  # noqa: E501
        :rtype: NasServerInstance
        """
        return self._nas_server

    @nas_server.setter
    def nas_server(self, nas_server):
        """Sets the nas_server of this FileLdapInstance.

        This is the embeddable reference form of nas_server_id attribute.  # noqa: E501

        :param nas_server: The nas_server of this FileLdapInstance.  # noqa: E501
        :type: NasServerInstance
        """

        self._nas_server = nas_server

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
        if issubclass(FileLdapInstance, dict):
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
        if not isinstance(other, FileLdapInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileLdapInstance):
            return True

        return self.to_dict() != other.to_dict()
