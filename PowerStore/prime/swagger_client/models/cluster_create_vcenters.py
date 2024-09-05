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


class ClusterCreateVcenters(object):
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
        'address': 'str',
        'username': 'str',
        'password': 'str',
        'is_verify_server_cert': 'bool',
        'data_center_id': 'str',
        'data_center_name': 'str',
        'data_center_create': 'bool',
        'esx_cluster_name': 'str',
        'vasa_provider_credentials': 'ClusterCreateVasaProviderCredentials'
    }

    attribute_map = {
        'address': 'address',
        'username': 'username',
        'password': 'password',
        'is_verify_server_cert': 'is_verify_server_cert',
        'data_center_id': 'data_center_id',
        'data_center_name': 'data_center_name',
        'data_center_create': 'data_center_create',
        'esx_cluster_name': 'esx_cluster_name',
        'vasa_provider_credentials': 'vasa_provider_credentials'
    }

    def __init__(self, address=None, username=None, password=None, is_verify_server_cert=None, data_center_id=None, data_center_name=None, data_center_create=False, esx_cluster_name='name', vasa_provider_credentials=None, _configuration=None):  # noqa: E501
        """ClusterCreateVcenters - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._address = None
        self._username = None
        self._password = None
        self._is_verify_server_cert = None
        self._data_center_id = None
        self._data_center_name = None
        self._data_center_create = None
        self._esx_cluster_name = None
        self._vasa_provider_credentials = None
        self.discriminator = None

        self.address = address
        self.username = username
        self.password = password
        self.is_verify_server_cert = is_verify_server_cert
        if data_center_id is not None:
            self.data_center_id = data_center_id
        if data_center_name is not None:
            self.data_center_name = data_center_name
        if data_center_create is not None:
            self.data_center_create = data_center_create
        if esx_cluster_name is not None:
            self.esx_cluster_name = esx_cluster_name
        self.vasa_provider_credentials = vasa_provider_credentials

    @property
    def address(self):
        """Gets the address of this ClusterCreateVcenters.  # noqa: E501

        IP address of vCenter in IPv4 or IPv6 or hostname format.  # noqa: E501

        :return: The address of this ClusterCreateVcenters.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ClusterCreateVcenters.

        IP address of vCenter in IPv4 or IPv6 or hostname format.  # noqa: E501

        :param address: The address of this ClusterCreateVcenters.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def username(self):
        """Gets the username of this ClusterCreateVcenters.  # noqa: E501

        User name to login to vCenter.  # noqa: E501

        :return: The username of this ClusterCreateVcenters.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ClusterCreateVcenters.

        User name to login to vCenter.  # noqa: E501

        :param username: The username of this ClusterCreateVcenters.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def password(self):
        """Gets the password of this ClusterCreateVcenters.  # noqa: E501

        Password to login to vCenter.  # noqa: E501

        :return: The password of this ClusterCreateVcenters.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ClusterCreateVcenters.

        Password to login to vCenter.  # noqa: E501

        :param password: The password of this ClusterCreateVcenters.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def is_verify_server_cert(self):
        """Gets the is_verify_server_cert of this ClusterCreateVcenters.  # noqa: E501

        Whether or not the connection will be secured with the vCenter SSL certificate.  # noqa: E501

        :return: The is_verify_server_cert of this ClusterCreateVcenters.  # noqa: E501
        :rtype: bool
        """
        return self._is_verify_server_cert

    @is_verify_server_cert.setter
    def is_verify_server_cert(self, is_verify_server_cert):
        """Sets the is_verify_server_cert of this ClusterCreateVcenters.

        Whether or not the connection will be secured with the vCenter SSL certificate.  # noqa: E501

        :param is_verify_server_cert: The is_verify_server_cert of this ClusterCreateVcenters.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_verify_server_cert is None:
            raise ValueError("Invalid value for `is_verify_server_cert`, must not be `None`")  # noqa: E501

        self._is_verify_server_cert = is_verify_server_cert

    @property
    def data_center_id(self):
        """Gets the data_center_id of this ClusterCreateVcenters.  # noqa: E501

        VMWare ID of the datacenter. This should be specified when creating PowerStoreX cluster to join an existing datacenter. data_center_name may not also be specified with this. Was added in version 3.0.0.0.  # noqa: E501

        :return: The data_center_id of this ClusterCreateVcenters.  # noqa: E501
        :rtype: str
        """
        return self._data_center_id

    @data_center_id.setter
    def data_center_id(self, data_center_id):
        """Sets the data_center_id of this ClusterCreateVcenters.

        VMWare ID of the datacenter. This should be specified when creating PowerStoreX cluster to join an existing datacenter. data_center_name may not also be specified with this. Was added in version 3.0.0.0.  # noqa: E501

        :param data_center_id: The data_center_id of this ClusterCreateVcenters.  # noqa: E501
        :type: str
        """

        self._data_center_id = data_center_id

    @property
    def data_center_name(self):
        """Gets the data_center_name of this ClusterCreateVcenters.  # noqa: E501

        Name of the data center. This should be specified when creating PowerStoreX cluster in order to create and join a new datacenter in vCenter. data_center_id may not also be specified with this. When data_center_create is false, then an existing datacenter will be used if the name matches, otherwise a new one will be created.  # noqa: E501

        :return: The data_center_name of this ClusterCreateVcenters.  # noqa: E501
        :rtype: str
        """
        return self._data_center_name

    @data_center_name.setter
    def data_center_name(self, data_center_name):
        """Sets the data_center_name of this ClusterCreateVcenters.

        Name of the data center. This should be specified when creating PowerStoreX cluster in order to create and join a new datacenter in vCenter. data_center_id may not also be specified with this. When data_center_create is false, then an existing datacenter will be used if the name matches, otherwise a new one will be created.  # noqa: E501

        :param data_center_name: The data_center_name of this ClusterCreateVcenters.  # noqa: E501
        :type: str
        """

        self._data_center_name = data_center_name

    @property
    def data_center_create(self):
        """Gets the data_center_create of this ClusterCreateVcenters.  # noqa: E501

        Along with data_center_name, indicates an intent to either create or use existing data center by name. Was added in version 3.0.0.0. Was deprecated in version 3.0.0.0.  # noqa: E501

        :return: The data_center_create of this ClusterCreateVcenters.  # noqa: E501
        :rtype: bool
        """
        return self._data_center_create

    @data_center_create.setter
    def data_center_create(self, data_center_create):
        """Sets the data_center_create of this ClusterCreateVcenters.

        Along with data_center_name, indicates an intent to either create or use existing data center by name. Was added in version 3.0.0.0. Was deprecated in version 3.0.0.0.  # noqa: E501

        :param data_center_create: The data_center_create of this ClusterCreateVcenters.  # noqa: E501
        :type: bool
        """

        self._data_center_create = data_center_create

    @property
    def esx_cluster_name(self):
        """Gets the esx_cluster_name of this ClusterCreateVcenters.  # noqa: E501

        ESXi cluster name. The default name is \"Cluster-\" followed by the PowerStore cluster name. This should be specified when creating PowerStore X cluster.  # noqa: E501

        :return: The esx_cluster_name of this ClusterCreateVcenters.  # noqa: E501
        :rtype: str
        """
        return self._esx_cluster_name

    @esx_cluster_name.setter
    def esx_cluster_name(self, esx_cluster_name):
        """Sets the esx_cluster_name of this ClusterCreateVcenters.

        ESXi cluster name. The default name is \"Cluster-\" followed by the PowerStore cluster name. This should be specified when creating PowerStore X cluster.  # noqa: E501

        :param esx_cluster_name: The esx_cluster_name of this ClusterCreateVcenters.  # noqa: E501
        :type: str
        """

        self._esx_cluster_name = esx_cluster_name

    @property
    def vasa_provider_credentials(self):
        """Gets the vasa_provider_credentials of this ClusterCreateVcenters.  # noqa: E501


        :return: The vasa_provider_credentials of this ClusterCreateVcenters.  # noqa: E501
        :rtype: ClusterCreateVasaProviderCredentials
        """
        return self._vasa_provider_credentials

    @vasa_provider_credentials.setter
    def vasa_provider_credentials(self, vasa_provider_credentials):
        """Sets the vasa_provider_credentials of this ClusterCreateVcenters.


        :param vasa_provider_credentials: The vasa_provider_credentials of this ClusterCreateVcenters.  # noqa: E501
        :type: ClusterCreateVasaProviderCredentials
        """
        if self._configuration.client_side_validation and vasa_provider_credentials is None:
            raise ValueError("Invalid value for `vasa_provider_credentials`, must not be `None`")  # noqa: E501

        self._vasa_provider_credentials = vasa_provider_credentials

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
        if issubclass(ClusterCreateVcenters, dict):
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
        if not isinstance(other, ClusterCreateVcenters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterCreateVcenters):
            return True

        return self.to_dict() != other.to_dict()
