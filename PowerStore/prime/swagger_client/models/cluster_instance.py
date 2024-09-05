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


class ClusterInstance(object):
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
        'global_id': 'str',
        'name': 'str',
        'management_address': 'str',
        'storage_discovery_address': 'str',
        'master_appliance_id': 'str',
        'primary_appliance_id': 'str',
        'appliance_count': 'int',
        'physical_mtu': 'int',
        'is_encryption_enabled': 'bool',
        'compatibility_level': 'int',
        'state': 'ClusterStateEnum',
        'state_l10n': 'str',
        'system_time': 'datetime',
        'nvm_subsystem_nqn': 'str'
    }

    attribute_map = {
        'id': 'id',
        'global_id': 'global_id',
        'name': 'name',
        'management_address': 'management_address',
        'storage_discovery_address': 'storage_discovery_address',
        'master_appliance_id': 'master_appliance_id',
        'primary_appliance_id': 'primary_appliance_id',
        'appliance_count': 'appliance_count',
        'physical_mtu': 'physical_mtu',
        'is_encryption_enabled': 'is_encryption_enabled',
        'compatibility_level': 'compatibility_level',
        'state': 'state',
        'state_l10n': 'state_l10n',
        'system_time': 'system_time',
        'nvm_subsystem_nqn': 'nvm_subsystem_nqn'
    }

    def __init__(self, id=None, global_id=None, name=None, management_address=None, storage_discovery_address=None, master_appliance_id=None, primary_appliance_id=None, appliance_count=None, physical_mtu=None, is_encryption_enabled=None, compatibility_level=None, state=None, state_l10n=None, system_time=None, nvm_subsystem_nqn=None, _configuration=None):  # noqa: E501
        """ClusterInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._global_id = None
        self._name = None
        self._management_address = None
        self._storage_discovery_address = None
        self._master_appliance_id = None
        self._primary_appliance_id = None
        self._appliance_count = None
        self._physical_mtu = None
        self._is_encryption_enabled = None
        self._compatibility_level = None
        self._state = None
        self._state_l10n = None
        self._system_time = None
        self._nvm_subsystem_nqn = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if global_id is not None:
            self.global_id = global_id
        if name is not None:
            self.name = name
        if management_address is not None:
            self.management_address = management_address
        if storage_discovery_address is not None:
            self.storage_discovery_address = storage_discovery_address
        if master_appliance_id is not None:
            self.master_appliance_id = master_appliance_id
        if primary_appliance_id is not None:
            self.primary_appliance_id = primary_appliance_id
        if appliance_count is not None:
            self.appliance_count = appliance_count
        if physical_mtu is not None:
            self.physical_mtu = physical_mtu
        if is_encryption_enabled is not None:
            self.is_encryption_enabled = is_encryption_enabled
        if compatibility_level is not None:
            self.compatibility_level = compatibility_level
        if state is not None:
            self.state = state
        if state_l10n is not None:
            self.state_l10n = state_l10n
        if system_time is not None:
            self.system_time = system_time
        if nvm_subsystem_nqn is not None:
            self.nvm_subsystem_nqn = nvm_subsystem_nqn

    @property
    def id(self):
        """Gets the id of this ClusterInstance.  # noqa: E501

        The unique identifier of the cluster.  # noqa: E501

        :return: The id of this ClusterInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClusterInstance.

        The unique identifier of the cluster.  # noqa: E501

        :param id: The id of this ClusterInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def global_id(self):
        """Gets the global_id of this ClusterInstance.  # noqa: E501

        The global unique identifier of the cluster.  # noqa: E501

        :return: The global_id of this ClusterInstance.  # noqa: E501
        :rtype: str
        """
        return self._global_id

    @global_id.setter
    def global_id(self, global_id):
        """Sets the global_id of this ClusterInstance.

        The global unique identifier of the cluster.  # noqa: E501

        :param global_id: The global_id of this ClusterInstance.  # noqa: E501
        :type: str
        """

        self._global_id = global_id

    @property
    def name(self):
        """Gets the name of this ClusterInstance.  # noqa: E501

        The name of the cluster.  # noqa: E501

        :return: The name of this ClusterInstance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterInstance.

        The name of the cluster.  # noqa: E501

        :param name: The name of this ClusterInstance.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def management_address(self):
        """Gets the management_address of this ClusterInstance.  # noqa: E501

        The floating management IP address for the cluster in IPv4 or IPv6 format.  # noqa: E501

        :return: The management_address of this ClusterInstance.  # noqa: E501
        :rtype: str
        """
        return self._management_address

    @management_address.setter
    def management_address(self, management_address):
        """Sets the management_address of this ClusterInstance.

        The floating management IP address for the cluster in IPv4 or IPv6 format.  # noqa: E501

        :param management_address: The management_address of this ClusterInstance.  # noqa: E501
        :type: str
        """

        self._management_address = management_address

    @property
    def storage_discovery_address(self):
        """Gets the storage_discovery_address of this ClusterInstance.  # noqa: E501

        The floating storage discovery IP address for the cluster in IPv4 or IPv6 format. If multiple storage discovery addresses are configured, this property will be set to \"null\". In this case the required storage network should be used to retrieve the discovery address.  # noqa: E501

        :return: The storage_discovery_address of this ClusterInstance.  # noqa: E501
        :rtype: str
        """
        return self._storage_discovery_address

    @storage_discovery_address.setter
    def storage_discovery_address(self, storage_discovery_address):
        """Sets the storage_discovery_address of this ClusterInstance.

        The floating storage discovery IP address for the cluster in IPv4 or IPv6 format. If multiple storage discovery addresses are configured, this property will be set to \"null\". In this case the required storage network should be used to retrieve the discovery address.  # noqa: E501

        :param storage_discovery_address: The storage_discovery_address of this ClusterInstance.  # noqa: E501
        :type: str
        """

        self._storage_discovery_address = storage_discovery_address

    @property
    def master_appliance_id(self):
        """Gets the master_appliance_id of this ClusterInstance.  # noqa: E501

        The unique identifier of the appliance acting as primary. Was deprecated in version 2.0.0.0.  # noqa: E501

        :return: The master_appliance_id of this ClusterInstance.  # noqa: E501
        :rtype: str
        """
        return self._master_appliance_id

    @master_appliance_id.setter
    def master_appliance_id(self, master_appliance_id):
        """Sets the master_appliance_id of this ClusterInstance.

        The unique identifier of the appliance acting as primary. Was deprecated in version 2.0.0.0.  # noqa: E501

        :param master_appliance_id: The master_appliance_id of this ClusterInstance.  # noqa: E501
        :type: str
        """

        self._master_appliance_id = master_appliance_id

    @property
    def primary_appliance_id(self):
        """Gets the primary_appliance_id of this ClusterInstance.  # noqa: E501

        The unique identifier of the appliance acting as primary. Was added in version 2.0.0.0.  # noqa: E501

        :return: The primary_appliance_id of this ClusterInstance.  # noqa: E501
        :rtype: str
        """
        return self._primary_appliance_id

    @primary_appliance_id.setter
    def primary_appliance_id(self, primary_appliance_id):
        """Sets the primary_appliance_id of this ClusterInstance.

        The unique identifier of the appliance acting as primary. Was added in version 2.0.0.0.  # noqa: E501

        :param primary_appliance_id: The primary_appliance_id of this ClusterInstance.  # noqa: E501
        :type: str
        """

        self._primary_appliance_id = primary_appliance_id

    @property
    def appliance_count(self):
        """Gets the appliance_count of this ClusterInstance.  # noqa: E501

        Number of appliances configured in this cluster.  # noqa: E501

        :return: The appliance_count of this ClusterInstance.  # noqa: E501
        :rtype: int
        """
        return self._appliance_count

    @appliance_count.setter
    def appliance_count(self, appliance_count):
        """Sets the appliance_count of this ClusterInstance.

        Number of appliances configured in this cluster.  # noqa: E501

        :param appliance_count: The appliance_count of this ClusterInstance.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                appliance_count is not None and appliance_count > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `appliance_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self._configuration.client_side_validation and
                appliance_count is not None and appliance_count < 0):  # noqa: E501
            raise ValueError("Invalid value for `appliance_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._appliance_count = appliance_count

    @property
    def physical_mtu(self):
        """Gets the physical_mtu of this ClusterInstance.  # noqa: E501

        The physical ethernet port (eth_port resource) MTU setting is global for all ports in the cluster. This is the default MTU setting for IP traffic, and the upper limit on network-specific MTU settings (network resource), where this can be overridden for some specific kinds of traffic (management, data, and vMotion).  # noqa: E501

        :return: The physical_mtu of this ClusterInstance.  # noqa: E501
        :rtype: int
        """
        return self._physical_mtu

    @physical_mtu.setter
    def physical_mtu(self, physical_mtu):
        """Sets the physical_mtu of this ClusterInstance.

        The physical ethernet port (eth_port resource) MTU setting is global for all ports in the cluster. This is the default MTU setting for IP traffic, and the upper limit on network-specific MTU settings (network resource), where this can be overridden for some specific kinds of traffic (management, data, and vMotion).  # noqa: E501

        :param physical_mtu: The physical_mtu of this ClusterInstance.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                physical_mtu is not None and physical_mtu > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `physical_mtu`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self._configuration.client_side_validation and
                physical_mtu is not None and physical_mtu < 0):  # noqa: E501
            raise ValueError("Invalid value for `physical_mtu`, must be a value greater than or equal to `0`")  # noqa: E501

        self._physical_mtu = physical_mtu

    @property
    def is_encryption_enabled(self):
        """Gets the is_encryption_enabled of this ClusterInstance.  # noqa: E501

        Whether or not Data at Rest Encryption is enabled on the cluster.  # noqa: E501

        :return: The is_encryption_enabled of this ClusterInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_encryption_enabled

    @is_encryption_enabled.setter
    def is_encryption_enabled(self, is_encryption_enabled):
        """Sets the is_encryption_enabled of this ClusterInstance.

        Whether or not Data at Rest Encryption is enabled on the cluster.  # noqa: E501

        :param is_encryption_enabled: The is_encryption_enabled of this ClusterInstance.  # noqa: E501
        :type: bool
        """

        self._is_encryption_enabled = is_encryption_enabled

    @property
    def compatibility_level(self):
        """Gets the compatibility_level of this ClusterInstance.  # noqa: E501

        The behavioral version of the software version API, and it is used to ensure the compatibility across potentially different software versions.  # noqa: E501

        :return: The compatibility_level of this ClusterInstance.  # noqa: E501
        :rtype: int
        """
        return self._compatibility_level

    @compatibility_level.setter
    def compatibility_level(self, compatibility_level):
        """Sets the compatibility_level of this ClusterInstance.

        The behavioral version of the software version API, and it is used to ensure the compatibility across potentially different software versions.  # noqa: E501

        :param compatibility_level: The compatibility_level of this ClusterInstance.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                compatibility_level is not None and compatibility_level > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `compatibility_level`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self._configuration.client_side_validation and
                compatibility_level is not None and compatibility_level < 0):  # noqa: E501
            raise ValueError("Invalid value for `compatibility_level`, must be a value greater than or equal to `0`")  # noqa: E501

        self._compatibility_level = compatibility_level

    @property
    def state(self):
        """Gets the state of this ClusterInstance.  # noqa: E501


        :return: The state of this ClusterInstance.  # noqa: E501
        :rtype: ClusterStateEnum
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ClusterInstance.


        :param state: The state of this ClusterInstance.  # noqa: E501
        :type: ClusterStateEnum
        """

        self._state = state

    @property
    def state_l10n(self):
        """Gets the state_l10n of this ClusterInstance.  # noqa: E501

        Localized string corresponding to state.  # noqa: E501

        :return: The state_l10n of this ClusterInstance.  # noqa: E501
        :rtype: str
        """
        return self._state_l10n

    @state_l10n.setter
    def state_l10n(self, state_l10n):
        """Sets the state_l10n of this ClusterInstance.

        Localized string corresponding to state.  # noqa: E501

        :param state_l10n: The state_l10n of this ClusterInstance.  # noqa: E501
        :type: str
        """

        self._state_l10n = state_l10n

    @property
    def system_time(self):
        """Gets the system_time of this ClusterInstance.  # noqa: E501

        Current clock time for the system. System time and all the system reported times are in UTC (GMT+0:00) format. The system time is controlled via NTP. It cannot be set directly. Was added in version 2.0.0.0.  # noqa: E501

        :return: The system_time of this ClusterInstance.  # noqa: E501
        :rtype: datetime
        """
        return self._system_time

    @system_time.setter
    def system_time(self, system_time):
        """Sets the system_time of this ClusterInstance.

        Current clock time for the system. System time and all the system reported times are in UTC (GMT+0:00) format. The system time is controlled via NTP. It cannot be set directly. Was added in version 2.0.0.0.  # noqa: E501

        :param system_time: The system_time of this ClusterInstance.  # noqa: E501
        :type: datetime
        """

        self._system_time = system_time

    @property
    def nvm_subsystem_nqn(self):
        """Gets the nvm_subsystem_nqn of this ClusterInstance.  # noqa: E501

        NVMe Subsystem NQN for cluster. It cannot be set directly. Was added in version 3.0.0.0.  # noqa: E501

        :return: The nvm_subsystem_nqn of this ClusterInstance.  # noqa: E501
        :rtype: str
        """
        return self._nvm_subsystem_nqn

    @nvm_subsystem_nqn.setter
    def nvm_subsystem_nqn(self, nvm_subsystem_nqn):
        """Sets the nvm_subsystem_nqn of this ClusterInstance.

        NVMe Subsystem NQN for cluster. It cannot be set directly. Was added in version 3.0.0.0.  # noqa: E501

        :param nvm_subsystem_nqn: The nvm_subsystem_nqn of this ClusterInstance.  # noqa: E501
        :type: str
        """

        self._nvm_subsystem_nqn = nvm_subsystem_nqn

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
        if issubclass(ClusterInstance, dict):
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
        if not isinstance(other, ClusterInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterInstance):
            return True

        return self.to_dict() != other.to_dict()
