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


class NasServerDelete(object):
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
        'is_skip_domain_unjoin': 'bool',
        'domain_user_name': 'str',
        'domain_password': 'str'
    }

    attribute_map = {
        'is_skip_domain_unjoin': 'is_skip_domain_unjoin',
        'domain_user_name': 'domain_user_name',
        'domain_password': 'domain_password'
    }

    def __init__(self, is_skip_domain_unjoin=False, domain_user_name=None, domain_password=None, _configuration=None):  # noqa: E501
        """NasServerDelete - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._is_skip_domain_unjoin = None
        self._domain_user_name = None
        self._domain_password = None
        self.discriminator = None

        if is_skip_domain_unjoin is not None:
            self.is_skip_domain_unjoin = is_skip_domain_unjoin
        if domain_user_name is not None:
            self.domain_user_name = domain_user_name
        if domain_password is not None:
            self.domain_password = domain_password

    @property
    def is_skip_domain_unjoin(self):
        """Gets the is_skip_domain_unjoin of this NasServerDelete.  # noqa: E501

        Indicates whether to keep the associated SMB servers joined to the Active Directory when the NAS server is deleted. Values are:\\n - true - Keep the associated SMB servers joined to the Active Directory when the NAS server is deleted. - false - (Default) Try to unjoin the associated SMB servers from the Active Directory before deleting the NAS server.  # noqa: E501

        :return: The is_skip_domain_unjoin of this NasServerDelete.  # noqa: E501
        :rtype: bool
        """
        return self._is_skip_domain_unjoin

    @is_skip_domain_unjoin.setter
    def is_skip_domain_unjoin(self, is_skip_domain_unjoin):
        """Sets the is_skip_domain_unjoin of this NasServerDelete.

        Indicates whether to keep the associated SMB servers joined to the Active Directory when the NAS server is deleted. Values are:\\n - true - Keep the associated SMB servers joined to the Active Directory when the NAS server is deleted. - false - (Default) Try to unjoin the associated SMB servers from the Active Directory before deleting the NAS server.  # noqa: E501

        :param is_skip_domain_unjoin: The is_skip_domain_unjoin of this NasServerDelete.  # noqa: E501
        :type: bool
        """

        self._is_skip_domain_unjoin = is_skip_domain_unjoin

    @property
    def domain_user_name(self):
        """Gets the domain_user_name of this NasServerDelete.  # noqa: E501

        Administrator login used to unjoin the associated SMB servers from the Active Directory (AD) domain before deleting the NAS server. This parameter is required when the skipDomainUnjoin parameter is false or not set, and the NAS server has SMB servers joined to an AD domain.  # noqa: E501

        :return: The domain_user_name of this NasServerDelete.  # noqa: E501
        :rtype: str
        """
        return self._domain_user_name

    @domain_user_name.setter
    def domain_user_name(self, domain_user_name):
        """Sets the domain_user_name of this NasServerDelete.

        Administrator login used to unjoin the associated SMB servers from the Active Directory (AD) domain before deleting the NAS server. This parameter is required when the skipDomainUnjoin parameter is false or not set, and the NAS server has SMB servers joined to an AD domain.  # noqa: E501

        :param domain_user_name: The domain_user_name of this NasServerDelete.  # noqa: E501
        :type: str
        """

        self._domain_user_name = domain_user_name

    @property
    def domain_password(self):
        """Gets the domain_password of this NasServerDelete.  # noqa: E501

        Administrator password used to unjoin the associated SMB servers from the Active Directory (AD) domain before deleting the NAS server. This parameter is required when the skipDomainUnjoin parameter is false or not set, and the NAS server has SMB servers joined to an AD domain.  # noqa: E501

        :return: The domain_password of this NasServerDelete.  # noqa: E501
        :rtype: str
        """
        return self._domain_password

    @domain_password.setter
    def domain_password(self, domain_password):
        """Sets the domain_password of this NasServerDelete.

        Administrator password used to unjoin the associated SMB servers from the Active Directory (AD) domain before deleting the NAS server. This parameter is required when the skipDomainUnjoin parameter is false or not set, and the NAS server has SMB servers joined to an AD domain.  # noqa: E501

        :param domain_password: The domain_password of this NasServerDelete.  # noqa: E501
        :type: str
        """

        self._domain_password = domain_password

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
        if issubclass(NasServerDelete, dict):
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
        if not isinstance(other, NasServerDelete):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NasServerDelete):
            return True

        return self.to_dict() != other.to_dict()
