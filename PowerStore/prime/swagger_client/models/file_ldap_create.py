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


class FileLdapCreate(object):
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
        'nas_server_id': 'str',
        'authentication_type': 'FileLDAPAuthenticationTypeEnum',
        'base_dn': 'str',
        'addresses': 'list[str]',
        'port_number': 'int',
        'protocol': 'FileLDAPProtocolEnum',
        'is_verify_server_certificate': 'bool',
        'profile_dn': 'str',
        'bind_dn': 'str',
        'bind_password': 'str',
        'is_smb_account_used': 'bool',
        'principal': 'str',
        'realm': 'str',
        'password': 'str'
    }

    attribute_map = {
        'nas_server_id': 'nas_server_id',
        'authentication_type': 'authentication_type',
        'base_dn': 'base_DN',
        'addresses': 'addresses',
        'port_number': 'port_number',
        'protocol': 'protocol',
        'is_verify_server_certificate': 'is_verify_server_certificate',
        'profile_dn': 'profile_DN',
        'bind_dn': 'bind_DN',
        'bind_password': 'bind_password',
        'is_smb_account_used': 'is_smb_account_used',
        'principal': 'principal',
        'realm': 'realm',
        'password': 'password'
    }

    def __init__(self, nas_server_id=None, authentication_type=None, base_dn=None, addresses=None, port_number=None, protocol=None, is_verify_server_certificate=None, profile_dn=None, bind_dn=None, bind_password=None, is_smb_account_used=None, principal=None, realm=None, password=None, _configuration=None):  # noqa: E501
        """FileLdapCreate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._nas_server_id = None
        self._authentication_type = None
        self._base_dn = None
        self._addresses = None
        self._port_number = None
        self._protocol = None
        self._is_verify_server_certificate = None
        self._profile_dn = None
        self._bind_dn = None
        self._bind_password = None
        self._is_smb_account_used = None
        self._principal = None
        self._realm = None
        self._password = None
        self.discriminator = None

        self.nas_server_id = nas_server_id
        self.authentication_type = authentication_type
        self.base_dn = base_dn
        self.addresses = addresses
        self.port_number = port_number
        if protocol is not None:
            self.protocol = protocol
        if is_verify_server_certificate is not None:
            self.is_verify_server_certificate = is_verify_server_certificate
        if profile_dn is not None:
            self.profile_dn = profile_dn
        if bind_dn is not None:
            self.bind_dn = bind_dn
        if bind_password is not None:
            self.bind_password = bind_password
        if is_smb_account_used is not None:
            self.is_smb_account_used = is_smb_account_used
        if principal is not None:
            self.principal = principal
        if realm is not None:
            self.realm = realm
        if password is not None:
            self.password = password

    @property
    def nas_server_id(self):
        """Gets the nas_server_id of this FileLdapCreate.  # noqa: E501

        Unique identifier of the associated NAS Server instance that will use this LDAP object. Only one LDAP object per NAS Server is supported. name:{name} can be used instead of {id}. For example:'nas_server_id':'name:nas_server_name'  # noqa: E501

        :return: The nas_server_id of this FileLdapCreate.  # noqa: E501
        :rtype: str
        """
        return self._nas_server_id

    @nas_server_id.setter
    def nas_server_id(self, nas_server_id):
        """Sets the nas_server_id of this FileLdapCreate.

        Unique identifier of the associated NAS Server instance that will use this LDAP object. Only one LDAP object per NAS Server is supported. name:{name} can be used instead of {id}. For example:'nas_server_id':'name:nas_server_name'  # noqa: E501

        :param nas_server_id: The nas_server_id of this FileLdapCreate.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and nas_server_id is None:
            raise ValueError("Invalid value for `nas_server_id`, must not be `None`")  # noqa: E501

        self._nas_server_id = nas_server_id

    @property
    def authentication_type(self):
        """Gets the authentication_type of this FileLdapCreate.  # noqa: E501


        :return: The authentication_type of this FileLdapCreate.  # noqa: E501
        :rtype: FileLDAPAuthenticationTypeEnum
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        """Sets the authentication_type of this FileLdapCreate.


        :param authentication_type: The authentication_type of this FileLdapCreate.  # noqa: E501
        :type: FileLDAPAuthenticationTypeEnum
        """
        if self._configuration.client_side_validation and authentication_type is None:
            raise ValueError("Invalid value for `authentication_type`, must not be `None`")  # noqa: E501

        self._authentication_type = authentication_type

    @property
    def base_dn(self):
        """Gets the base_dn of this FileLdapCreate.  # noqa: E501

        Name of the LDAP base DN.  Base Distinguished Name (BDN) of the root of the LDAP directory tree. The appliance uses the DN to bind to the LDAP service and locate in the LDAP directory tree to begin a search for information.   The base DN can be expressed as a fully-qualified domain name or in X.509 format by using the attribute dc=. For example, if the fully-qualified domain name is mycompany.com, the base DN is expressed as dc=mycompany,dc=com.  # noqa: E501

        :return: The base_dn of this FileLdapCreate.  # noqa: E501
        :rtype: str
        """
        return self._base_dn

    @base_dn.setter
    def base_dn(self, base_dn):
        """Sets the base_dn of this FileLdapCreate.

        Name of the LDAP base DN.  Base Distinguished Name (BDN) of the root of the LDAP directory tree. The appliance uses the DN to bind to the LDAP service and locate in the LDAP directory tree to begin a search for information.   The base DN can be expressed as a fully-qualified domain name or in X.509 format by using the attribute dc=. For example, if the fully-qualified domain name is mycompany.com, the base DN is expressed as dc=mycompany,dc=com.  # noqa: E501

        :param base_dn: The base_dn of this FileLdapCreate.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and base_dn is None:
            raise ValueError("Invalid value for `base_dn`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                base_dn is not None and len(base_dn) > 255):
            raise ValueError("Invalid value for `base_dn`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                base_dn is not None and len(base_dn) < 3):
            raise ValueError("Invalid value for `base_dn`, length must be greater than or equal to `3`")  # noqa: E501

        self._base_dn = base_dn

    @property
    def addresses(self):
        """Gets the addresses of this FileLdapCreate.  # noqa: E501

        The list of LDAP server IP addresses. The addresses may be IPv4 or IPv6.  # noqa: E501

        :return: The addresses of this FileLdapCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this FileLdapCreate.

        The list of LDAP server IP addresses. The addresses may be IPv4 or IPv6.  # noqa: E501

        :param addresses: The addresses of this FileLdapCreate.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and addresses is None:
            raise ValueError("Invalid value for `addresses`, must not be `None`")  # noqa: E501

        self._addresses = addresses

    @property
    def port_number(self):
        """Gets the port_number of this FileLdapCreate.  # noqa: E501

        The TCP/IP port used by the NAS Server to connect to the LDAP servers. The default port number for LDAP is 389 and LDAPS is 636.  # noqa: E501

        :return: The port_number of this FileLdapCreate.  # noqa: E501
        :rtype: int
        """
        return self._port_number

    @port_number.setter
    def port_number(self, port_number):
        """Sets the port_number of this FileLdapCreate.

        The TCP/IP port used by the NAS Server to connect to the LDAP servers. The default port number for LDAP is 389 and LDAPS is 636.  # noqa: E501

        :param port_number: The port_number of this FileLdapCreate.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and port_number is None:
            raise ValueError("Invalid value for `port_number`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                port_number is not None and port_number > 65535):  # noqa: E501
            raise ValueError("Invalid value for `port_number`, must be a value less than or equal to `65535`")  # noqa: E501
        if (self._configuration.client_side_validation and
                port_number is not None and port_number < 1):  # noqa: E501
            raise ValueError("Invalid value for `port_number`, must be a value greater than or equal to `1`")  # noqa: E501

        self._port_number = port_number

    @property
    def protocol(self):
        """Gets the protocol of this FileLdapCreate.  # noqa: E501


        :return: The protocol of this FileLdapCreate.  # noqa: E501
        :rtype: FileLDAPProtocolEnum
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this FileLdapCreate.


        :param protocol: The protocol of this FileLdapCreate.  # noqa: E501
        :type: FileLDAPProtocolEnum
        """

        self._protocol = protocol

    @property
    def is_verify_server_certificate(self):
        """Gets the is_verify_server_certificate of this FileLdapCreate.  # noqa: E501

        Indicates whether Certification Authority certificate is used to verify the LDAP server certificate for secure SSL connections. Values are:  * true - verifies LDAP server's certificate.  * false - doesn't verify LDAP server's certificate.   # noqa: E501

        :return: The is_verify_server_certificate of this FileLdapCreate.  # noqa: E501
        :rtype: bool
        """
        return self._is_verify_server_certificate

    @is_verify_server_certificate.setter
    def is_verify_server_certificate(self, is_verify_server_certificate):
        """Sets the is_verify_server_certificate of this FileLdapCreate.

        Indicates whether Certification Authority certificate is used to verify the LDAP server certificate for secure SSL connections. Values are:  * true - verifies LDAP server's certificate.  * false - doesn't verify LDAP server's certificate.   # noqa: E501

        :param is_verify_server_certificate: The is_verify_server_certificate of this FileLdapCreate.  # noqa: E501
        :type: bool
        """

        self._is_verify_server_certificate = is_verify_server_certificate

    @property
    def profile_dn(self):
        """Gets the profile_dn of this FileLdapCreate.  # noqa: E501

        For an iPlanet LDAP server, specifies the DN of the entry with the configuration profile.  # noqa: E501

        :return: The profile_dn of this FileLdapCreate.  # noqa: E501
        :rtype: str
        """
        return self._profile_dn

    @profile_dn.setter
    def profile_dn(self, profile_dn):
        """Sets the profile_dn of this FileLdapCreate.

        For an iPlanet LDAP server, specifies the DN of the entry with the configuration profile.  # noqa: E501

        :param profile_dn: The profile_dn of this FileLdapCreate.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                profile_dn is not None and len(profile_dn) > 255):
            raise ValueError("Invalid value for `profile_dn`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                profile_dn is not None and len(profile_dn) < 0):
            raise ValueError("Invalid value for `profile_dn`, length must be greater than or equal to `0`")  # noqa: E501

        self._profile_dn = profile_dn

    @property
    def bind_dn(self):
        """Gets the bind_dn of this FileLdapCreate.  # noqa: E501

        Bind Distinguished Name (DN) to be used when binding.  # noqa: E501

        :return: The bind_dn of this FileLdapCreate.  # noqa: E501
        :rtype: str
        """
        return self._bind_dn

    @bind_dn.setter
    def bind_dn(self, bind_dn):
        """Sets the bind_dn of this FileLdapCreate.

        Bind Distinguished Name (DN) to be used when binding.  # noqa: E501

        :param bind_dn: The bind_dn of this FileLdapCreate.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                bind_dn is not None and len(bind_dn) > 1023):
            raise ValueError("Invalid value for `bind_dn`, length must be less than or equal to `1023`")  # noqa: E501
        if (self._configuration.client_side_validation and
                bind_dn is not None and len(bind_dn) < 0):
            raise ValueError("Invalid value for `bind_dn`, length must be greater than or equal to `0`")  # noqa: E501

        self._bind_dn = bind_dn

    @property
    def bind_password(self):
        """Gets the bind_password of this FileLdapCreate.  # noqa: E501

        The associated password to be used when binding to the server.  # noqa: E501

        :return: The bind_password of this FileLdapCreate.  # noqa: E501
        :rtype: str
        """
        return self._bind_password

    @bind_password.setter
    def bind_password(self, bind_password):
        """Sets the bind_password of this FileLdapCreate.

        The associated password to be used when binding to the server.  # noqa: E501

        :param bind_password: The bind_password of this FileLdapCreate.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                bind_password is not None and len(bind_password) > 1023):
            raise ValueError("Invalid value for `bind_password`, length must be less than or equal to `1023`")  # noqa: E501
        if (self._configuration.client_side_validation and
                bind_password is not None and len(bind_password) < 0):
            raise ValueError("Invalid value for `bind_password`, length must be greater than or equal to `0`")  # noqa: E501

        self._bind_password = bind_password

    @property
    def is_smb_account_used(self):
        """Gets the is_smb_account_used of this FileLdapCreate.  # noqa: E501

        Indicates whether SMB authentication is used to authenticate to the LDAP server. Values are:     * true - Indicates that the SMB settings are used for Kerberos authentication.     * false - Indicates that Kerberos uses its own settings.   # noqa: E501

        :return: The is_smb_account_used of this FileLdapCreate.  # noqa: E501
        :rtype: bool
        """
        return self._is_smb_account_used

    @is_smb_account_used.setter
    def is_smb_account_used(self, is_smb_account_used):
        """Sets the is_smb_account_used of this FileLdapCreate.

        Indicates whether SMB authentication is used to authenticate to the LDAP server. Values are:     * true - Indicates that the SMB settings are used for Kerberos authentication.     * false - Indicates that Kerberos uses its own settings.   # noqa: E501

        :param is_smb_account_used: The is_smb_account_used of this FileLdapCreate.  # noqa: E501
        :type: bool
        """

        self._is_smb_account_used = is_smb_account_used

    @property
    def principal(self):
        """Gets the principal of this FileLdapCreate.  # noqa: E501

        Specifies the principal name for Kerberos authentication.  # noqa: E501

        :return: The principal of this FileLdapCreate.  # noqa: E501
        :rtype: str
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this FileLdapCreate.

        Specifies the principal name for Kerberos authentication.  # noqa: E501

        :param principal: The principal of this FileLdapCreate.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                principal is not None and len(principal) > 1023):
            raise ValueError("Invalid value for `principal`, length must be less than or equal to `1023`")  # noqa: E501
        if (self._configuration.client_side_validation and
                principal is not None and len(principal) < 0):
            raise ValueError("Invalid value for `principal`, length must be greater than or equal to `0`")  # noqa: E501

        self._principal = principal

    @property
    def realm(self):
        """Gets the realm of this FileLdapCreate.  # noqa: E501

        Specifies the realm name for Kerberos authentication.  # noqa: E501

        :return: The realm of this FileLdapCreate.  # noqa: E501
        :rtype: str
        """
        return self._realm

    @realm.setter
    def realm(self, realm):
        """Sets the realm of this FileLdapCreate.

        Specifies the realm name for Kerberos authentication.  # noqa: E501

        :param realm: The realm of this FileLdapCreate.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                realm is not None and len(realm) > 255):
            raise ValueError("Invalid value for `realm`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                realm is not None and len(realm) < 0):
            raise ValueError("Invalid value for `realm`, length must be greater than or equal to `0`")  # noqa: E501

        self._realm = realm

    @property
    def password(self):
        """Gets the password of this FileLdapCreate.  # noqa: E501

        The associated password for Kerberos authentication.  # noqa: E501

        :return: The password of this FileLdapCreate.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this FileLdapCreate.

        The associated password for Kerberos authentication.  # noqa: E501

        :param password: The password of this FileLdapCreate.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                password is not None and len(password) > 1023):
            raise ValueError("Invalid value for `password`, length must be less than or equal to `1023`")  # noqa: E501
        if (self._configuration.client_side_validation and
                password is not None and len(password) < 0):
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `0`")  # noqa: E501

        self._password = password

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
        if issubclass(FileLdapCreate, dict):
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
        if not isinstance(other, FileLdapCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileLdapCreate):
            return True

        return self.to_dict() != other.to_dict()
