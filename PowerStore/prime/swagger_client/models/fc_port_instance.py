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


class FcPortInstance(object):
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
        'appliance_id': 'str',
        'node_id': 'str',
        'wwn': 'str',
        'wwn_nvme': 'str',
        'wwn_node': 'str',
        'is_link_up': 'bool',
        'is_in_use': 'bool',
        'supported_speeds': 'list[FcPortSpeedEnum]',
        'current_speed': 'FcPortSpeedEnum',
        'requested_speed': 'FcPortSpeedEnum',
        'sfp_id': 'str',
        'io_module_id': 'str',
        'hardware_parent_id': 'str',
        'port_index': 'int',
        'port_connector_type': 'FrontEndPortConnectionTypeEnum',
        'partner_id': 'str',
        'protocols': 'list[FcPortProtocolEnum]',
        'stale_state': 'PortStaleStateEnum',
        'scsi_mode': 'FcPortScsiModeEnum',
        'supported_speeds_l10n': 'list[str]',
        'current_speed_l10n': 'str',
        'requested_speed_l10n': 'str',
        'port_connector_type_l10n': 'str',
        'protocols_l10n': 'list[str]',
        'stale_state_l10n': 'str',
        'scsi_mode_l10n': 'str',
        'appliance': 'ApplianceInstance',
        'node': 'HardwareInstance',
        'sfp': 'HardwareInstance',
        'io_module': 'HardwareInstance',
        'hardware_parent': 'HardwareInstance',
        'partner': 'FcPortInstance'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'appliance_id': 'appliance_id',
        'node_id': 'node_id',
        'wwn': 'wwn',
        'wwn_nvme': 'wwn_nvme',
        'wwn_node': 'wwn_node',
        'is_link_up': 'is_link_up',
        'is_in_use': 'is_in_use',
        'supported_speeds': 'supported_speeds',
        'current_speed': 'current_speed',
        'requested_speed': 'requested_speed',
        'sfp_id': 'sfp_id',
        'io_module_id': 'io_module_id',
        'hardware_parent_id': 'hardware_parent_id',
        'port_index': 'port_index',
        'port_connector_type': 'port_connector_type',
        'partner_id': 'partner_id',
        'protocols': 'protocols',
        'stale_state': 'stale_state',
        'scsi_mode': 'scsi_mode',
        'supported_speeds_l10n': 'supported_speeds_l10n',
        'current_speed_l10n': 'current_speed_l10n',
        'requested_speed_l10n': 'requested_speed_l10n',
        'port_connector_type_l10n': 'port_connector_type_l10n',
        'protocols_l10n': 'protocols_l10n',
        'stale_state_l10n': 'stale_state_l10n',
        'scsi_mode_l10n': 'scsi_mode_l10n',
        'appliance': 'appliance',
        'node': 'node',
        'sfp': 'sfp',
        'io_module': 'io_module',
        'hardware_parent': 'hardware_parent',
        'partner': 'partner'
    }

    def __init__(self, id=None, name=None, appliance_id=None, node_id=None, wwn=None, wwn_nvme=None, wwn_node=None, is_link_up=None, is_in_use=None, supported_speeds=None, current_speed=None, requested_speed=None, sfp_id=None, io_module_id=None, hardware_parent_id=None, port_index=None, port_connector_type=None, partner_id=None, protocols=None, stale_state=None, scsi_mode=None, supported_speeds_l10n=None, current_speed_l10n=None, requested_speed_l10n=None, port_connector_type_l10n=None, protocols_l10n=None, stale_state_l10n=None, scsi_mode_l10n=None, appliance=None, node=None, sfp=None, io_module=None, hardware_parent=None, partner=None, _configuration=None):  # noqa: E501
        """FcPortInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._appliance_id = None
        self._node_id = None
        self._wwn = None
        self._wwn_nvme = None
        self._wwn_node = None
        self._is_link_up = None
        self._is_in_use = None
        self._supported_speeds = None
        self._current_speed = None
        self._requested_speed = None
        self._sfp_id = None
        self._io_module_id = None
        self._hardware_parent_id = None
        self._port_index = None
        self._port_connector_type = None
        self._partner_id = None
        self._protocols = None
        self._stale_state = None
        self._scsi_mode = None
        self._supported_speeds_l10n = None
        self._current_speed_l10n = None
        self._requested_speed_l10n = None
        self._port_connector_type_l10n = None
        self._protocols_l10n = None
        self._stale_state_l10n = None
        self._scsi_mode_l10n = None
        self._appliance = None
        self._node = None
        self._sfp = None
        self._io_module = None
        self._hardware_parent = None
        self._partner = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if appliance_id is not None:
            self.appliance_id = appliance_id
        if node_id is not None:
            self.node_id = node_id
        if wwn is not None:
            self.wwn = wwn
        if wwn_nvme is not None:
            self.wwn_nvme = wwn_nvme
        if wwn_node is not None:
            self.wwn_node = wwn_node
        if is_link_up is not None:
            self.is_link_up = is_link_up
        if is_in_use is not None:
            self.is_in_use = is_in_use
        if supported_speeds is not None:
            self.supported_speeds = supported_speeds
        if current_speed is not None:
            self.current_speed = current_speed
        if requested_speed is not None:
            self.requested_speed = requested_speed
        if sfp_id is not None:
            self.sfp_id = sfp_id
        if io_module_id is not None:
            self.io_module_id = io_module_id
        if hardware_parent_id is not None:
            self.hardware_parent_id = hardware_parent_id
        if port_index is not None:
            self.port_index = port_index
        if port_connector_type is not None:
            self.port_connector_type = port_connector_type
        if partner_id is not None:
            self.partner_id = partner_id
        if protocols is not None:
            self.protocols = protocols
        if stale_state is not None:
            self.stale_state = stale_state
        if scsi_mode is not None:
            self.scsi_mode = scsi_mode
        if supported_speeds_l10n is not None:
            self.supported_speeds_l10n = supported_speeds_l10n
        if current_speed_l10n is not None:
            self.current_speed_l10n = current_speed_l10n
        if requested_speed_l10n is not None:
            self.requested_speed_l10n = requested_speed_l10n
        if port_connector_type_l10n is not None:
            self.port_connector_type_l10n = port_connector_type_l10n
        if protocols_l10n is not None:
            self.protocols_l10n = protocols_l10n
        if stale_state_l10n is not None:
            self.stale_state_l10n = stale_state_l10n
        if scsi_mode_l10n is not None:
            self.scsi_mode_l10n = scsi_mode_l10n
        if appliance is not None:
            self.appliance = appliance
        if node is not None:
            self.node = node
        if sfp is not None:
            self.sfp = sfp
        if io_module is not None:
            self.io_module = io_module
        if hardware_parent is not None:
            self.hardware_parent = hardware_parent
        if partner is not None:
            self.partner = partner

    @property
    def id(self):
        """Gets the id of this FcPortInstance.  # noqa: E501

        Unique identifier of the port.  # noqa: E501

        :return: The id of this FcPortInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FcPortInstance.

        Unique identifier of the port.  # noqa: E501

        :param id: The id of this FcPortInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this FcPortInstance.  # noqa: E501

        Name of the port.  This property supports case-insensitive filtering.  # noqa: E501

        :return: The name of this FcPortInstance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FcPortInstance.

        Name of the port.  This property supports case-insensitive filtering.  # noqa: E501

        :param name: The name of this FcPortInstance.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def appliance_id(self):
        """Gets the appliance_id of this FcPortInstance.  # noqa: E501

        Unique identifier of the appliance containing the port.  # noqa: E501

        :return: The appliance_id of this FcPortInstance.  # noqa: E501
        :rtype: str
        """
        return self._appliance_id

    @appliance_id.setter
    def appliance_id(self, appliance_id):
        """Sets the appliance_id of this FcPortInstance.

        Unique identifier of the appliance containing the port.  # noqa: E501

        :param appliance_id: The appliance_id of this FcPortInstance.  # noqa: E501
        :type: str
        """

        self._appliance_id = appliance_id

    @property
    def node_id(self):
        """Gets the node_id of this FcPortInstance.  # noqa: E501

        Unique identifier of the hardware instance of type 'Node' containing the port.  # noqa: E501

        :return: The node_id of this FcPortInstance.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this FcPortInstance.

        Unique identifier of the hardware instance of type 'Node' containing the port.  # noqa: E501

        :param node_id: The node_id of this FcPortInstance.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def wwn(self):
        """Gets the wwn of this FcPortInstance.  # noqa: E501

        World Wide Name (WWN) of the port.  # noqa: E501

        :return: The wwn of this FcPortInstance.  # noqa: E501
        :rtype: str
        """
        return self._wwn

    @wwn.setter
    def wwn(self, wwn):
        """Sets the wwn of this FcPortInstance.

        World Wide Name (WWN) of the port.  # noqa: E501

        :param wwn: The wwn of this FcPortInstance.  # noqa: E501
        :type: str
        """

        self._wwn = wwn

    @property
    def wwn_nvme(self):
        """Gets the wwn_nvme of this FcPortInstance.  # noqa: E501

        World Wide Name (WWN) of NVME port. Was added in version 2.0.0.0.  # noqa: E501

        :return: The wwn_nvme of this FcPortInstance.  # noqa: E501
        :rtype: str
        """
        return self._wwn_nvme

    @wwn_nvme.setter
    def wwn_nvme(self, wwn_nvme):
        """Sets the wwn_nvme of this FcPortInstance.

        World Wide Name (WWN) of NVME port. Was added in version 2.0.0.0.  # noqa: E501

        :param wwn_nvme: The wwn_nvme of this FcPortInstance.  # noqa: E501
        :type: str
        """

        self._wwn_nvme = wwn_nvme

    @property
    def wwn_node(self):
        """Gets the wwn_node of this FcPortInstance.  # noqa: E501

        World Wide Name (WWN) of the Node of the port. Was added in version 3.0.0.0.  # noqa: E501

        :return: The wwn_node of this FcPortInstance.  # noqa: E501
        :rtype: str
        """
        return self._wwn_node

    @wwn_node.setter
    def wwn_node(self, wwn_node):
        """Sets the wwn_node of this FcPortInstance.

        World Wide Name (WWN) of the Node of the port. Was added in version 3.0.0.0.  # noqa: E501

        :param wwn_node: The wwn_node of this FcPortInstance.  # noqa: E501
        :type: str
        """

        self._wwn_node = wwn_node

    @property
    def is_link_up(self):
        """Gets the is_link_up of this FcPortInstance.  # noqa: E501

        Indicates whether the port's link is up. Values are: * true - Link is up. * false - Link is down.   # noqa: E501

        :return: The is_link_up of this FcPortInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_link_up

    @is_link_up.setter
    def is_link_up(self, is_link_up):
        """Sets the is_link_up of this FcPortInstance.

        Indicates whether the port's link is up. Values are: * true - Link is up. * false - Link is down.   # noqa: E501

        :param is_link_up: The is_link_up of this FcPortInstance.  # noqa: E501
        :type: bool
        """

        self._is_link_up = is_link_up

    @property
    def is_in_use(self):
        """Gets the is_in_use of this FcPortInstance.  # noqa: E501

        Indicates whether the port is in use. Values are: * true - Is in use. * false - Is not in use.  Was added in version 3.0.0.0.  # noqa: E501

        :return: The is_in_use of this FcPortInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_in_use

    @is_in_use.setter
    def is_in_use(self, is_in_use):
        """Sets the is_in_use of this FcPortInstance.

        Indicates whether the port is in use. Values are: * true - Is in use. * false - Is not in use.  Was added in version 3.0.0.0.  # noqa: E501

        :param is_in_use: The is_in_use of this FcPortInstance.  # noqa: E501
        :type: bool
        """

        self._is_in_use = is_in_use

    @property
    def supported_speeds(self):
        """Gets the supported_speeds of this FcPortInstance.  # noqa: E501

        List of supported transmission speeds for the port.  # noqa: E501

        :return: The supported_speeds of this FcPortInstance.  # noqa: E501
        :rtype: list[FcPortSpeedEnum]
        """
        return self._supported_speeds

    @supported_speeds.setter
    def supported_speeds(self, supported_speeds):
        """Sets the supported_speeds of this FcPortInstance.

        List of supported transmission speeds for the port.  # noqa: E501

        :param supported_speeds: The supported_speeds of this FcPortInstance.  # noqa: E501
        :type: list[FcPortSpeedEnum]
        """

        self._supported_speeds = supported_speeds

    @property
    def current_speed(self):
        """Gets the current_speed of this FcPortInstance.  # noqa: E501


        :return: The current_speed of this FcPortInstance.  # noqa: E501
        :rtype: FcPortSpeedEnum
        """
        return self._current_speed

    @current_speed.setter
    def current_speed(self, current_speed):
        """Sets the current_speed of this FcPortInstance.


        :param current_speed: The current_speed of this FcPortInstance.  # noqa: E501
        :type: FcPortSpeedEnum
        """

        self._current_speed = current_speed

    @property
    def requested_speed(self):
        """Gets the requested_speed of this FcPortInstance.  # noqa: E501


        :return: The requested_speed of this FcPortInstance.  # noqa: E501
        :rtype: FcPortSpeedEnum
        """
        return self._requested_speed

    @requested_speed.setter
    def requested_speed(self, requested_speed):
        """Sets the requested_speed of this FcPortInstance.


        :param requested_speed: The requested_speed of this FcPortInstance.  # noqa: E501
        :type: FcPortSpeedEnum
        """

        self._requested_speed = requested_speed

    @property
    def sfp_id(self):
        """Gets the sfp_id of this FcPortInstance.  # noqa: E501

        Unique identifier of the hardware instance of type 'SFP' (Small Form-factor Pluggable) inserted into the port.   # noqa: E501

        :return: The sfp_id of this FcPortInstance.  # noqa: E501
        :rtype: str
        """
        return self._sfp_id

    @sfp_id.setter
    def sfp_id(self, sfp_id):
        """Sets the sfp_id of this FcPortInstance.

        Unique identifier of the hardware instance of type 'SFP' (Small Form-factor Pluggable) inserted into the port.   # noqa: E501

        :param sfp_id: The sfp_id of this FcPortInstance.  # noqa: E501
        :type: str
        """

        self._sfp_id = sfp_id

    @property
    def io_module_id(self):
        """Gets the io_module_id of this FcPortInstance.  # noqa: E501

        Unique identifier of the hardware instance of type 'IO_Module' handling the port. Was deprecated in version 2.0.0.0.  # noqa: E501

        :return: The io_module_id of this FcPortInstance.  # noqa: E501
        :rtype: str
        """
        return self._io_module_id

    @io_module_id.setter
    def io_module_id(self, io_module_id):
        """Sets the io_module_id of this FcPortInstance.

        Unique identifier of the hardware instance of type 'IO_Module' handling the port. Was deprecated in version 2.0.0.0.  # noqa: E501

        :param io_module_id: The io_module_id of this FcPortInstance.  # noqa: E501
        :type: str
        """

        self._io_module_id = io_module_id

    @property
    def hardware_parent_id(self):
        """Gets the hardware_parent_id of this FcPortInstance.  # noqa: E501

        Unique identifier of the parent hardware instance handling the port. @added(Foothills) Was added in version 2.0.0.0.  # noqa: E501

        :return: The hardware_parent_id of this FcPortInstance.  # noqa: E501
        :rtype: str
        """
        return self._hardware_parent_id

    @hardware_parent_id.setter
    def hardware_parent_id(self, hardware_parent_id):
        """Sets the hardware_parent_id of this FcPortInstance.

        Unique identifier of the parent hardware instance handling the port. @added(Foothills) Was added in version 2.0.0.0.  # noqa: E501

        :param hardware_parent_id: The hardware_parent_id of this FcPortInstance.  # noqa: E501
        :type: str
        """

        self._hardware_parent_id = hardware_parent_id

    @property
    def port_index(self):
        """Gets the port_index of this FcPortInstance.  # noqa: E501

        Index of the port in the IO module.  # noqa: E501

        :return: The port_index of this FcPortInstance.  # noqa: E501
        :rtype: int
        """
        return self._port_index

    @port_index.setter
    def port_index(self, port_index):
        """Sets the port_index of this FcPortInstance.

        Index of the port in the IO module.  # noqa: E501

        :param port_index: The port_index of this FcPortInstance.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                port_index is not None and port_index > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `port_index`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self._configuration.client_side_validation and
                port_index is not None and port_index < 0):  # noqa: E501
            raise ValueError("Invalid value for `port_index`, must be a value greater than or equal to `0`")  # noqa: E501

        self._port_index = port_index

    @property
    def port_connector_type(self):
        """Gets the port_connector_type of this FcPortInstance.  # noqa: E501


        :return: The port_connector_type of this FcPortInstance.  # noqa: E501
        :rtype: FrontEndPortConnectionTypeEnum
        """
        return self._port_connector_type

    @port_connector_type.setter
    def port_connector_type(self, port_connector_type):
        """Sets the port_connector_type of this FcPortInstance.


        :param port_connector_type: The port_connector_type of this FcPortInstance.  # noqa: E501
        :type: FrontEndPortConnectionTypeEnum
        """

        self._port_connector_type = port_connector_type

    @property
    def partner_id(self):
        """Gets the partner_id of this FcPortInstance.  # noqa: E501

        Unique identifier of the partner port.  # noqa: E501

        :return: The partner_id of this FcPortInstance.  # noqa: E501
        :rtype: str
        """
        return self._partner_id

    @partner_id.setter
    def partner_id(self, partner_id):
        """Sets the partner_id of this FcPortInstance.

        Unique identifier of the partner port.  # noqa: E501

        :param partner_id: The partner_id of this FcPortInstance.  # noqa: E501
        :type: str
        """

        self._partner_id = partner_id

    @property
    def protocols(self):
        """Gets the protocols of this FcPortInstance.  # noqa: E501

        List of supported protocols for the port. Was added in version 2.0.0.0.  # noqa: E501

        :return: The protocols of this FcPortInstance.  # noqa: E501
        :rtype: list[FcPortProtocolEnum]
        """
        return self._protocols

    @protocols.setter
    def protocols(self, protocols):
        """Sets the protocols of this FcPortInstance.

        List of supported protocols for the port. Was added in version 2.0.0.0.  # noqa: E501

        :param protocols: The protocols of this FcPortInstance.  # noqa: E501
        :type: list[FcPortProtocolEnum]
        """

        self._protocols = protocols

    @property
    def stale_state(self):
        """Gets the stale_state of this FcPortInstance.  # noqa: E501

        Indicator of the stale state of the port. Was added in version 2.0.0.0.  # noqa: E501

        :return: The stale_state of this FcPortInstance.  # noqa: E501
        :rtype: PortStaleStateEnum
        """
        return self._stale_state

    @stale_state.setter
    def stale_state(self, stale_state):
        """Sets the stale_state of this FcPortInstance.

        Indicator of the stale state of the port. Was added in version 2.0.0.0.  # noqa: E501

        :param stale_state: The stale_state of this FcPortInstance.  # noqa: E501
        :type: PortStaleStateEnum
        """

        self._stale_state = stale_state

    @property
    def scsi_mode(self):
        """Gets the scsi_mode of this FcPortInstance.  # noqa: E501

         Was added in version 3.0.0.0.  # noqa: E501

        :return: The scsi_mode of this FcPortInstance.  # noqa: E501
        :rtype: FcPortScsiModeEnum
        """
        return self._scsi_mode

    @scsi_mode.setter
    def scsi_mode(self, scsi_mode):
        """Sets the scsi_mode of this FcPortInstance.

         Was added in version 3.0.0.0.  # noqa: E501

        :param scsi_mode: The scsi_mode of this FcPortInstance.  # noqa: E501
        :type: FcPortScsiModeEnum
        """

        self._scsi_mode = scsi_mode

    @property
    def supported_speeds_l10n(self):
        """Gets the supported_speeds_l10n of this FcPortInstance.  # noqa: E501

        Localized message array corresponding to supported_speeds  # noqa: E501

        :return: The supported_speeds_l10n of this FcPortInstance.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_speeds_l10n

    @supported_speeds_l10n.setter
    def supported_speeds_l10n(self, supported_speeds_l10n):
        """Sets the supported_speeds_l10n of this FcPortInstance.

        Localized message array corresponding to supported_speeds  # noqa: E501

        :param supported_speeds_l10n: The supported_speeds_l10n of this FcPortInstance.  # noqa: E501
        :type: list[str]
        """

        self._supported_speeds_l10n = supported_speeds_l10n

    @property
    def current_speed_l10n(self):
        """Gets the current_speed_l10n of this FcPortInstance.  # noqa: E501

        Localized message string corresponding to current_speed  # noqa: E501

        :return: The current_speed_l10n of this FcPortInstance.  # noqa: E501
        :rtype: str
        """
        return self._current_speed_l10n

    @current_speed_l10n.setter
    def current_speed_l10n(self, current_speed_l10n):
        """Sets the current_speed_l10n of this FcPortInstance.

        Localized message string corresponding to current_speed  # noqa: E501

        :param current_speed_l10n: The current_speed_l10n of this FcPortInstance.  # noqa: E501
        :type: str
        """

        self._current_speed_l10n = current_speed_l10n

    @property
    def requested_speed_l10n(self):
        """Gets the requested_speed_l10n of this FcPortInstance.  # noqa: E501

        Localized message string corresponding to requested_speed  # noqa: E501

        :return: The requested_speed_l10n of this FcPortInstance.  # noqa: E501
        :rtype: str
        """
        return self._requested_speed_l10n

    @requested_speed_l10n.setter
    def requested_speed_l10n(self, requested_speed_l10n):
        """Sets the requested_speed_l10n of this FcPortInstance.

        Localized message string corresponding to requested_speed  # noqa: E501

        :param requested_speed_l10n: The requested_speed_l10n of this FcPortInstance.  # noqa: E501
        :type: str
        """

        self._requested_speed_l10n = requested_speed_l10n

    @property
    def port_connector_type_l10n(self):
        """Gets the port_connector_type_l10n of this FcPortInstance.  # noqa: E501

        Localized message string corresponding to port_connector_type  # noqa: E501

        :return: The port_connector_type_l10n of this FcPortInstance.  # noqa: E501
        :rtype: str
        """
        return self._port_connector_type_l10n

    @port_connector_type_l10n.setter
    def port_connector_type_l10n(self, port_connector_type_l10n):
        """Sets the port_connector_type_l10n of this FcPortInstance.

        Localized message string corresponding to port_connector_type  # noqa: E501

        :param port_connector_type_l10n: The port_connector_type_l10n of this FcPortInstance.  # noqa: E501
        :type: str
        """

        self._port_connector_type_l10n = port_connector_type_l10n

    @property
    def protocols_l10n(self):
        """Gets the protocols_l10n of this FcPortInstance.  # noqa: E501

        Localized message array corresponding to protocols Was added in version 2.0.0.0.  # noqa: E501

        :return: The protocols_l10n of this FcPortInstance.  # noqa: E501
        :rtype: list[str]
        """
        return self._protocols_l10n

    @protocols_l10n.setter
    def protocols_l10n(self, protocols_l10n):
        """Sets the protocols_l10n of this FcPortInstance.

        Localized message array corresponding to protocols Was added in version 2.0.0.0.  # noqa: E501

        :param protocols_l10n: The protocols_l10n of this FcPortInstance.  # noqa: E501
        :type: list[str]
        """

        self._protocols_l10n = protocols_l10n

    @property
    def stale_state_l10n(self):
        """Gets the stale_state_l10n of this FcPortInstance.  # noqa: E501

        Localized message string corresponding to stale_state Was added in version 2.0.0.0.  # noqa: E501

        :return: The stale_state_l10n of this FcPortInstance.  # noqa: E501
        :rtype: str
        """
        return self._stale_state_l10n

    @stale_state_l10n.setter
    def stale_state_l10n(self, stale_state_l10n):
        """Sets the stale_state_l10n of this FcPortInstance.

        Localized message string corresponding to stale_state Was added in version 2.0.0.0.  # noqa: E501

        :param stale_state_l10n: The stale_state_l10n of this FcPortInstance.  # noqa: E501
        :type: str
        """

        self._stale_state_l10n = stale_state_l10n

    @property
    def scsi_mode_l10n(self):
        """Gets the scsi_mode_l10n of this FcPortInstance.  # noqa: E501

        Localized message string corresponding to scsi_mode Was added in version 3.0.0.0.  # noqa: E501

        :return: The scsi_mode_l10n of this FcPortInstance.  # noqa: E501
        :rtype: str
        """
        return self._scsi_mode_l10n

    @scsi_mode_l10n.setter
    def scsi_mode_l10n(self, scsi_mode_l10n):
        """Sets the scsi_mode_l10n of this FcPortInstance.

        Localized message string corresponding to scsi_mode Was added in version 3.0.0.0.  # noqa: E501

        :param scsi_mode_l10n: The scsi_mode_l10n of this FcPortInstance.  # noqa: E501
        :type: str
        """

        self._scsi_mode_l10n = scsi_mode_l10n

    @property
    def appliance(self):
        """Gets the appliance of this FcPortInstance.  # noqa: E501

        This is the embeddable reference form of appliance_id attribute.  # noqa: E501

        :return: The appliance of this FcPortInstance.  # noqa: E501
        :rtype: ApplianceInstance
        """
        return self._appliance

    @appliance.setter
    def appliance(self, appliance):
        """Sets the appliance of this FcPortInstance.

        This is the embeddable reference form of appliance_id attribute.  # noqa: E501

        :param appliance: The appliance of this FcPortInstance.  # noqa: E501
        :type: ApplianceInstance
        """

        self._appliance = appliance

    @property
    def node(self):
        """Gets the node of this FcPortInstance.  # noqa: E501

        This is the embeddable reference form of node_id attribute.  # noqa: E501

        :return: The node of this FcPortInstance.  # noqa: E501
        :rtype: HardwareInstance
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this FcPortInstance.

        This is the embeddable reference form of node_id attribute.  # noqa: E501

        :param node: The node of this FcPortInstance.  # noqa: E501
        :type: HardwareInstance
        """

        self._node = node

    @property
    def sfp(self):
        """Gets the sfp of this FcPortInstance.  # noqa: E501

        This is the embeddable reference form of sfp_id attribute.  # noqa: E501

        :return: The sfp of this FcPortInstance.  # noqa: E501
        :rtype: HardwareInstance
        """
        return self._sfp

    @sfp.setter
    def sfp(self, sfp):
        """Sets the sfp of this FcPortInstance.

        This is the embeddable reference form of sfp_id attribute.  # noqa: E501

        :param sfp: The sfp of this FcPortInstance.  # noqa: E501
        :type: HardwareInstance
        """

        self._sfp = sfp

    @property
    def io_module(self):
        """Gets the io_module of this FcPortInstance.  # noqa: E501

        This is the embeddable reference form of io_module_id attribute.  # noqa: E501

        :return: The io_module of this FcPortInstance.  # noqa: E501
        :rtype: HardwareInstance
        """
        return self._io_module

    @io_module.setter
    def io_module(self, io_module):
        """Sets the io_module of this FcPortInstance.

        This is the embeddable reference form of io_module_id attribute.  # noqa: E501

        :param io_module: The io_module of this FcPortInstance.  # noqa: E501
        :type: HardwareInstance
        """

        self._io_module = io_module

    @property
    def hardware_parent(self):
        """Gets the hardware_parent of this FcPortInstance.  # noqa: E501

        This is the embeddable reference form of hardware_parent_id attribute.  # noqa: E501

        :return: The hardware_parent of this FcPortInstance.  # noqa: E501
        :rtype: HardwareInstance
        """
        return self._hardware_parent

    @hardware_parent.setter
    def hardware_parent(self, hardware_parent):
        """Sets the hardware_parent of this FcPortInstance.

        This is the embeddable reference form of hardware_parent_id attribute.  # noqa: E501

        :param hardware_parent: The hardware_parent of this FcPortInstance.  # noqa: E501
        :type: HardwareInstance
        """

        self._hardware_parent = hardware_parent

    @property
    def partner(self):
        """Gets the partner of this FcPortInstance.  # noqa: E501

        This is the embeddable reference form of partner_id attribute.  # noqa: E501

        :return: The partner of this FcPortInstance.  # noqa: E501
        :rtype: FcPortInstance
        """
        return self._partner

    @partner.setter
    def partner(self, partner):
        """Sets the partner of this FcPortInstance.

        This is the embeddable reference form of partner_id attribute.  # noqa: E501

        :param partner: The partner of this FcPortInstance.  # noqa: E501
        :type: FcPortInstance
        """

        self._partner = partner

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
        if issubclass(FcPortInstance, dict):
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
        if not isinstance(other, FcPortInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FcPortInstance):
            return True

        return self.to_dict() != other.to_dict()
