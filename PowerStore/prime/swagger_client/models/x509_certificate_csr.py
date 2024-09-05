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


class X509CertificateCsr(object):
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
        'type': 'X509CertificateUsageTypeEnum',
        'service': 'X509CertificateServiceEnum',
        'scope': 'str',
        'common_name': 'str',
        'dns_name': 'list[str]',
        'ip_addresses': 'list[str]',
        'organizational_unit': 'str',
        'organization': 'str',
        'locality': 'str',
        'state': 'str',
        'country': 'str',
        'key_length': 'int'
    }

    attribute_map = {
        'type': 'type',
        'service': 'service',
        'scope': 'scope',
        'common_name': 'common_name',
        'dns_name': 'dns_name',
        'ip_addresses': 'ip_addresses',
        'organizational_unit': 'organizational_unit',
        'organization': 'organization',
        'locality': 'locality',
        'state': 'state',
        'country': 'country',
        'key_length': 'key_length'
    }

    def __init__(self, type=None, service=None, scope=None, common_name=None, dns_name=None, ip_addresses=None, organizational_unit=None, organization=None, locality=None, state=None, country=None, key_length=None, _configuration=None):  # noqa: E501
        """X509CertificateCsr - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type = None
        self._service = None
        self._scope = None
        self._common_name = None
        self._dns_name = None
        self._ip_addresses = None
        self._organizational_unit = None
        self._organization = None
        self._locality = None
        self._state = None
        self._country = None
        self._key_length = None
        self.discriminator = None

        self.type = type
        self.service = service
        if scope is not None:
            self.scope = scope
        if common_name is not None:
            self.common_name = common_name
        if dns_name is not None:
            self.dns_name = dns_name
        if ip_addresses is not None:
            self.ip_addresses = ip_addresses
        if organizational_unit is not None:
            self.organizational_unit = organizational_unit
        if organization is not None:
            self.organization = organization
        if locality is not None:
            self.locality = locality
        if state is not None:
            self.state = state
        if country is not None:
            self.country = country
        self.key_length = key_length

    @property
    def type(self):
        """Gets the type of this X509CertificateCsr.  # noqa: E501


        :return: The type of this X509CertificateCsr.  # noqa: E501
        :rtype: X509CertificateUsageTypeEnum
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this X509CertificateCsr.


        :param type: The type of this X509CertificateCsr.  # noqa: E501
        :type: X509CertificateUsageTypeEnum
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def service(self):
        """Gets the service of this X509CertificateCsr.  # noqa: E501


        :return: The service of this X509CertificateCsr.  # noqa: E501
        :rtype: X509CertificateServiceEnum
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this X509CertificateCsr.


        :param service: The service of this X509CertificateCsr.  # noqa: E501
        :type: X509CertificateServiceEnum
        """
        if self._configuration.client_side_validation and service is None:
            raise ValueError("Invalid value for `service`, must not be `None`")  # noqa: E501

        self._service = service

    @property
    def scope(self):
        """Gets the scope of this X509CertificateCsr.  # noqa: E501

        Scope defines a subset of certificates belonging to one Service. Scope here defines what Certificate Signing Request (CSR) can be generated. The scope for CSR Generation only includes: - Certificate with Service Management_HTTP and Type of Server, Scope value can only be External - Certificate with Service VASA_HTTP and Type of Server, Scope value can be null(unused and optional) - Certificate with Service KMIP_HTTP and Type of Client, Scope value can be null(unused and optional) - Certificate with Service Syslog_HTTP and Type of Client, Scope value can be null(unused and optional)   # noqa: E501

        :return: The scope of this X509CertificateCsr.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this X509CertificateCsr.

        Scope defines a subset of certificates belonging to one Service. Scope here defines what Certificate Signing Request (CSR) can be generated. The scope for CSR Generation only includes: - Certificate with Service Management_HTTP and Type of Server, Scope value can only be External - Certificate with Service VASA_HTTP and Type of Server, Scope value can be null(unused and optional) - Certificate with Service KMIP_HTTP and Type of Client, Scope value can be null(unused and optional) - Certificate with Service Syslog_HTTP and Type of Client, Scope value can be null(unused and optional)   # noqa: E501

        :param scope: The scope of this X509CertificateCsr.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def common_name(self):
        """Gets the common_name of this X509CertificateCsr.  # noqa: E501

        Part of distinguished name. e.g., www.dell.common.  # noqa: E501

        :return: The common_name of this X509CertificateCsr.  # noqa: E501
        :rtype: str
        """
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        """Sets the common_name of this X509CertificateCsr.

        Part of distinguished name. e.g., www.dell.common.  # noqa: E501

        :param common_name: The common_name of this X509CertificateCsr.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                common_name is not None and len(common_name) > 64):
            raise ValueError("Invalid value for `common_name`, length must be less than or equal to `64`")  # noqa: E501
        if (self._configuration.client_side_validation and
                common_name is not None and len(common_name) < 0):
            raise ValueError("Invalid value for `common_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._common_name = common_name

    @property
    def dns_name(self):
        """Gets the dns_name of this X509CertificateCsr.  # noqa: E501

        DNS names in the certificate extensions  # noqa: E501

        :return: The dns_name of this X509CertificateCsr.  # noqa: E501
        :rtype: list[str]
        """
        return self._dns_name

    @dns_name.setter
    def dns_name(self, dns_name):
        """Sets the dns_name of this X509CertificateCsr.

        DNS names in the certificate extensions  # noqa: E501

        :param dns_name: The dns_name of this X509CertificateCsr.  # noqa: E501
        :type: list[str]
        """

        self._dns_name = dns_name

    @property
    def ip_addresses(self):
        """Gets the ip_addresses of this X509CertificateCsr.  # noqa: E501

        IP addresses in the certificate extensions  # noqa: E501

        :return: The ip_addresses of this X509CertificateCsr.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """Sets the ip_addresses of this X509CertificateCsr.

        IP addresses in the certificate extensions  # noqa: E501

        :param ip_addresses: The ip_addresses of this X509CertificateCsr.  # noqa: E501
        :type: list[str]
        """

        self._ip_addresses = ip_addresses

    @property
    def organizational_unit(self):
        """Gets the organizational_unit of this X509CertificateCsr.  # noqa: E501

        Part of distinguished name. e.g., Security Department.  # noqa: E501

        :return: The organizational_unit of this X509CertificateCsr.  # noqa: E501
        :rtype: str
        """
        return self._organizational_unit

    @organizational_unit.setter
    def organizational_unit(self, organizational_unit):
        """Sets the organizational_unit of this X509CertificateCsr.

        Part of distinguished name. e.g., Security Department.  # noqa: E501

        :param organizational_unit: The organizational_unit of this X509CertificateCsr.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                organizational_unit is not None and len(organizational_unit) > 64):
            raise ValueError("Invalid value for `organizational_unit`, length must be less than or equal to `64`")  # noqa: E501
        if (self._configuration.client_side_validation and
                organizational_unit is not None and len(organizational_unit) < 0):
            raise ValueError("Invalid value for `organizational_unit`, length must be greater than or equal to `0`")  # noqa: E501

        self._organizational_unit = organizational_unit

    @property
    def organization(self):
        """Gets the organization of this X509CertificateCsr.  # noqa: E501

        Part of distinguished name. e.g., Dell-EMC.  # noqa: E501

        :return: The organization of this X509CertificateCsr.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this X509CertificateCsr.

        Part of distinguished name. e.g., Dell-EMC.  # noqa: E501

        :param organization: The organization of this X509CertificateCsr.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                organization is not None and len(organization) > 64):
            raise ValueError("Invalid value for `organization`, length must be less than or equal to `64`")  # noqa: E501
        if (self._configuration.client_side_validation and
                organization is not None and len(organization) < 0):
            raise ValueError("Invalid value for `organization`, length must be greater than or equal to `0`")  # noqa: E501

        self._organization = organization

    @property
    def locality(self):
        """Gets the locality of this X509CertificateCsr.  # noqa: E501

        Part of distinguished name. e.g., Hopkinton.  # noqa: E501

        :return: The locality of this X509CertificateCsr.  # noqa: E501
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """Sets the locality of this X509CertificateCsr.

        Part of distinguished name. e.g., Hopkinton.  # noqa: E501

        :param locality: The locality of this X509CertificateCsr.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                locality is not None and len(locality) > 128):
            raise ValueError("Invalid value for `locality`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                locality is not None and len(locality) < 0):
            raise ValueError("Invalid value for `locality`, length must be greater than or equal to `0`")  # noqa: E501

        self._locality = locality

    @property
    def state(self):
        """Gets the state of this X509CertificateCsr.  # noqa: E501

        Part of distinguished name. e.g., Massachusetts.  # noqa: E501

        :return: The state of this X509CertificateCsr.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this X509CertificateCsr.

        Part of distinguished name. e.g., Massachusetts.  # noqa: E501

        :param state: The state of this X509CertificateCsr.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                state is not None and len(state) > 128):
            raise ValueError("Invalid value for `state`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                state is not None and len(state) < 0):
            raise ValueError("Invalid value for `state`, length must be greater than or equal to `0`")  # noqa: E501

        self._state = state

    @property
    def country(self):
        """Gets the country of this X509CertificateCsr.  # noqa: E501

        Part of distinguished name. e.g., US.  # noqa: E501

        :return: The country of this X509CertificateCsr.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this X509CertificateCsr.

        Part of distinguished name. e.g., US.  # noqa: E501

        :param country: The country of this X509CertificateCsr.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                country is not None and len(country) > 2):
            raise ValueError("Invalid value for `country`, length must be less than or equal to `2`")  # noqa: E501
        if (self._configuration.client_side_validation and
                country is not None and len(country) < 2):
            raise ValueError("Invalid value for `country`, length must be greater than or equal to `2`")  # noqa: E501

        self._country = country

    @property
    def key_length(self):
        """Gets the key_length of this X509CertificateCsr.  # noqa: E501

        Private key length. It can only be 2048 or 4096.  # noqa: E501

        :return: The key_length of this X509CertificateCsr.  # noqa: E501
        :rtype: int
        """
        return self._key_length

    @key_length.setter
    def key_length(self, key_length):
        """Sets the key_length of this X509CertificateCsr.

        Private key length. It can only be 2048 or 4096.  # noqa: E501

        :param key_length: The key_length of this X509CertificateCsr.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and key_length is None:
            raise ValueError("Invalid value for `key_length`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                key_length is not None and key_length > 4096):  # noqa: E501
            raise ValueError("Invalid value for `key_length`, must be a value less than or equal to `4096`")  # noqa: E501
        if (self._configuration.client_side_validation and
                key_length is not None and key_length < 2048):  # noqa: E501
            raise ValueError("Invalid value for `key_length`, must be a value greater than or equal to `2048`")  # noqa: E501

        self._key_length = key_length

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
        if issubclass(X509CertificateCsr, dict):
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
        if not isinstance(other, X509CertificateCsr):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, X509CertificateCsr):
            return True

        return self.to_dict() != other.to_dict()
