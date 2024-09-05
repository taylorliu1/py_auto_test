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


class HardwareInstance(object):
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
        'type': 'HardwareTypeEnum',
        'lifecycle_state': 'HardwareLifecycleStateEnum',
        'parent_id': 'str',
        'appliance_id': 'str',
        'slot': 'int',
        'part_number': 'str',
        'serial_number': 'str',
        'status_led_state': 'HardwareStatusLEDStateEnum',
        'is_marked': 'bool',
        'extra_details': 'HardwareExtraDetailsInstance',
        'stale_state': 'HardwareStaleStateEnum',
        'type_l10n': 'str',
        'lifecycle_state_l10n': 'str',
        'status_led_state_l10n': 'str',
        'stale_state_l10n': 'str',
        'node_fc_ports': 'list[FcPortInstance]',
        'sfp_fc_ports': 'list[FcPortInstance]',
        'io_module_fc_ports': 'list[FcPortInstance]',
        'hardware_parent_fc_ports': 'list[FcPortInstance]',
        'node_sas_ports': 'list[SasPortInstance]',
        'sfp_sas_ports': 'list[SasPortInstance]',
        'io_module_sas_ports': 'list[SasPortInstance]',
        'hardware_parent_sas_ports': 'list[SasPortInstance]',
        'node_eth_ports': 'list[EthPortInstance]',
        'sfp_eth_ports': 'list[EthPortInstance]',
        'io_module_eth_ports': 'list[EthPortInstance]',
        'hardware_parent_eth_ports': 'list[EthPortInstance]',
        'node_eth_be_ports': 'list[EthBePortInstance]',
        'sfp_eth_be_ports': 'list[EthBePortInstance]',
        'hardware_parent_eth_be_ports': 'list[EthBePortInstance]',
        'parent': 'HardwareInstance',
        'children': 'list[HardwareInstance]',
        'appliance': 'ApplianceInstance'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'lifecycle_state': 'lifecycle_state',
        'parent_id': 'parent_id',
        'appliance_id': 'appliance_id',
        'slot': 'slot',
        'part_number': 'part_number',
        'serial_number': 'serial_number',
        'status_led_state': 'status_led_state',
        'is_marked': 'is_marked',
        'extra_details': 'extra_details',
        'stale_state': 'stale_state',
        'type_l10n': 'type_l10n',
        'lifecycle_state_l10n': 'lifecycle_state_l10n',
        'status_led_state_l10n': 'status_led_state_l10n',
        'stale_state_l10n': 'stale_state_l10n',
        'node_fc_ports': 'node_fc_ports',
        'sfp_fc_ports': 'sfp_fc_ports',
        'io_module_fc_ports': 'io_module_fc_ports',
        'hardware_parent_fc_ports': 'hardware_parent_fc_ports',
        'node_sas_ports': 'node_sas_ports',
        'sfp_sas_ports': 'sfp_sas_ports',
        'io_module_sas_ports': 'io_module_sas_ports',
        'hardware_parent_sas_ports': 'hardware_parent_sas_ports',
        'node_eth_ports': 'node_eth_ports',
        'sfp_eth_ports': 'sfp_eth_ports',
        'io_module_eth_ports': 'io_module_eth_ports',
        'hardware_parent_eth_ports': 'hardware_parent_eth_ports',
        'node_eth_be_ports': 'node_eth_be_ports',
        'sfp_eth_be_ports': 'sfp_eth_be_ports',
        'hardware_parent_eth_be_ports': 'hardware_parent_eth_be_ports',
        'parent': 'parent',
        'children': 'children',
        'appliance': 'appliance'
    }

    def __init__(self, id=None, name=None, type=None, lifecycle_state=None, parent_id=None, appliance_id=None, slot=None, part_number=None, serial_number=None, status_led_state=None, is_marked=None, extra_details=None, stale_state=None, type_l10n=None, lifecycle_state_l10n=None, status_led_state_l10n=None, stale_state_l10n=None, node_fc_ports=None, sfp_fc_ports=None, io_module_fc_ports=None, hardware_parent_fc_ports=None, node_sas_ports=None, sfp_sas_ports=None, io_module_sas_ports=None, hardware_parent_sas_ports=None, node_eth_ports=None, sfp_eth_ports=None, io_module_eth_ports=None, hardware_parent_eth_ports=None, node_eth_be_ports=None, sfp_eth_be_ports=None, hardware_parent_eth_be_ports=None, parent=None, children=None, appliance=None, _configuration=None):  # noqa: E501
        """HardwareInstance - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._type = None
        self._lifecycle_state = None
        self._parent_id = None
        self._appliance_id = None
        self._slot = None
        self._part_number = None
        self._serial_number = None
        self._status_led_state = None
        self._is_marked = None
        self._extra_details = None
        self._stale_state = None
        self._type_l10n = None
        self._lifecycle_state_l10n = None
        self._status_led_state_l10n = None
        self._stale_state_l10n = None
        self._node_fc_ports = None
        self._sfp_fc_ports = None
        self._io_module_fc_ports = None
        self._hardware_parent_fc_ports = None
        self._node_sas_ports = None
        self._sfp_sas_ports = None
        self._io_module_sas_ports = None
        self._hardware_parent_sas_ports = None
        self._node_eth_ports = None
        self._sfp_eth_ports = None
        self._io_module_eth_ports = None
        self._hardware_parent_eth_ports = None
        self._node_eth_be_ports = None
        self._sfp_eth_be_ports = None
        self._hardware_parent_eth_be_ports = None
        self._parent = None
        self._children = None
        self._appliance = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if lifecycle_state is not None:
            self.lifecycle_state = lifecycle_state
        if parent_id is not None:
            self.parent_id = parent_id
        if appliance_id is not None:
            self.appliance_id = appliance_id
        if slot is not None:
            self.slot = slot
        if part_number is not None:
            self.part_number = part_number
        if serial_number is not None:
            self.serial_number = serial_number
        if status_led_state is not None:
            self.status_led_state = status_led_state
        if is_marked is not None:
            self.is_marked = is_marked
        if extra_details is not None:
            self.extra_details = extra_details
        if stale_state is not None:
            self.stale_state = stale_state
        if type_l10n is not None:
            self.type_l10n = type_l10n
        if lifecycle_state_l10n is not None:
            self.lifecycle_state_l10n = lifecycle_state_l10n
        if status_led_state_l10n is not None:
            self.status_led_state_l10n = status_led_state_l10n
        if stale_state_l10n is not None:
            self.stale_state_l10n = stale_state_l10n
        if node_fc_ports is not None:
            self.node_fc_ports = node_fc_ports
        if sfp_fc_ports is not None:
            self.sfp_fc_ports = sfp_fc_ports
        if io_module_fc_ports is not None:
            self.io_module_fc_ports = io_module_fc_ports
        if hardware_parent_fc_ports is not None:
            self.hardware_parent_fc_ports = hardware_parent_fc_ports
        if node_sas_ports is not None:
            self.node_sas_ports = node_sas_ports
        if sfp_sas_ports is not None:
            self.sfp_sas_ports = sfp_sas_ports
        if io_module_sas_ports is not None:
            self.io_module_sas_ports = io_module_sas_ports
        if hardware_parent_sas_ports is not None:
            self.hardware_parent_sas_ports = hardware_parent_sas_ports
        if node_eth_ports is not None:
            self.node_eth_ports = node_eth_ports
        if sfp_eth_ports is not None:
            self.sfp_eth_ports = sfp_eth_ports
        if io_module_eth_ports is not None:
            self.io_module_eth_ports = io_module_eth_ports
        if hardware_parent_eth_ports is not None:
            self.hardware_parent_eth_ports = hardware_parent_eth_ports
        if node_eth_be_ports is not None:
            self.node_eth_be_ports = node_eth_be_ports
        if sfp_eth_be_ports is not None:
            self.sfp_eth_be_ports = sfp_eth_be_ports
        if hardware_parent_eth_be_ports is not None:
            self.hardware_parent_eth_be_ports = hardware_parent_eth_be_ports
        if parent is not None:
            self.parent = parent
        if children is not None:
            self.children = children
        if appliance is not None:
            self.appliance = appliance

    @property
    def id(self):
        """Gets the id of this HardwareInstance.  # noqa: E501

        The unique id of the component.  # noqa: E501

        :return: The id of this HardwareInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HardwareInstance.

        The unique id of the component.  # noqa: E501

        :param id: The id of this HardwareInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this HardwareInstance.  # noqa: E501

        The name of the component.  This property supports case-insensitive filtering.  # noqa: E501

        :return: The name of this HardwareInstance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HardwareInstance.

        The name of the component.  This property supports case-insensitive filtering.  # noqa: E501

        :param name: The name of this HardwareInstance.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this HardwareInstance.  # noqa: E501

        Hardware component type.  # noqa: E501

        :return: The type of this HardwareInstance.  # noqa: E501
        :rtype: HardwareTypeEnum
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HardwareInstance.

        Hardware component type.  # noqa: E501

        :param type: The type of this HardwareInstance.  # noqa: E501
        :type: HardwareTypeEnum
        """

        self._type = type

    @property
    def lifecycle_state(self):
        """Gets the lifecycle_state of this HardwareInstance.  # noqa: E501

        Life cycle state of the component.  # noqa: E501

        :return: The lifecycle_state of this HardwareInstance.  # noqa: E501
        :rtype: HardwareLifecycleStateEnum
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """Sets the lifecycle_state of this HardwareInstance.

        Life cycle state of the component.  # noqa: E501

        :param lifecycle_state: The lifecycle_state of this HardwareInstance.  # noqa: E501
        :type: HardwareLifecycleStateEnum
        """

        self._lifecycle_state = lifecycle_state

    @property
    def parent_id(self):
        """Gets the parent_id of this HardwareInstance.  # noqa: E501

        The id of the component's parent, or null if this component is at the top of the parent hierarchy.  # noqa: E501

        :return: The parent_id of this HardwareInstance.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this HardwareInstance.

        The id of the component's parent, or null if this component is at the top of the parent hierarchy.  # noqa: E501

        :param parent_id: The parent_id of this HardwareInstance.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def appliance_id(self):
        """Gets the appliance_id of this HardwareInstance.  # noqa: E501

        The id of the component's associated appliance.  # noqa: E501

        :return: The appliance_id of this HardwareInstance.  # noqa: E501
        :rtype: str
        """
        return self._appliance_id

    @appliance_id.setter
    def appliance_id(self, appliance_id):
        """Sets the appliance_id of this HardwareInstance.

        The id of the component's associated appliance.  # noqa: E501

        :param appliance_id: The appliance_id of this HardwareInstance.  # noqa: E501
        :type: str
        """

        self._appliance_id = appliance_id

    @property
    def slot(self):
        """Gets the slot of this HardwareInstance.  # noqa: E501

        The slot or location of the component.  # noqa: E501

        :return: The slot of this HardwareInstance.  # noqa: E501
        :rtype: int
        """
        return self._slot

    @slot.setter
    def slot(self, slot):
        """Sets the slot of this HardwareInstance.

        The slot or location of the component.  # noqa: E501

        :param slot: The slot of this HardwareInstance.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                slot is not None and slot > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `slot`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self._configuration.client_side_validation and
                slot is not None and slot < 0):  # noqa: E501
            raise ValueError("Invalid value for `slot`, must be a value greater than or equal to `0`")  # noqa: E501

        self._slot = slot

    @property
    def part_number(self):
        """Gets the part_number of this HardwareInstance.  # noqa: E501

        The part number of the component.  # noqa: E501

        :return: The part_number of this HardwareInstance.  # noqa: E501
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this HardwareInstance.

        The part number of the component.  # noqa: E501

        :param part_number: The part_number of this HardwareInstance.  # noqa: E501
        :type: str
        """

        self._part_number = part_number

    @property
    def serial_number(self):
        """Gets the serial_number of this HardwareInstance.  # noqa: E501

        The serial number of the component.  # noqa: E501

        :return: The serial_number of this HardwareInstance.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this HardwareInstance.

        The serial number of the component.  # noqa: E501

        :param serial_number: The serial_number of this HardwareInstance.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def status_led_state(self):
        """Gets the status_led_state of this HardwareInstance.  # noqa: E501

        Indicator of the state of the component status LED.  # noqa: E501

        :return: The status_led_state of this HardwareInstance.  # noqa: E501
        :rtype: HardwareStatusLEDStateEnum
        """
        return self._status_led_state

    @status_led_state.setter
    def status_led_state(self, status_led_state):
        """Sets the status_led_state of this HardwareInstance.

        Indicator of the state of the component status LED.  # noqa: E501

        :param status_led_state: The status_led_state of this HardwareInstance.  # noqa: E501
        :type: HardwareStatusLEDStateEnum
        """

        self._status_led_state = status_led_state

    @property
    def is_marked(self):
        """Gets the is_marked of this HardwareInstance.  # noqa: E501

        Indicator of whether a component is location marked or not.  # noqa: E501

        :return: The is_marked of this HardwareInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_marked

    @is_marked.setter
    def is_marked(self, is_marked):
        """Sets the is_marked of this HardwareInstance.

        Indicator of whether a component is location marked or not.  # noqa: E501

        :param is_marked: The is_marked of this HardwareInstance.  # noqa: E501
        :type: bool
        """

        self._is_marked = is_marked

    @property
    def extra_details(self):
        """Gets the extra_details of this HardwareInstance.  # noqa: E501

        Additional hardware details. Contents are specific to each component type.  # noqa: E501

        :return: The extra_details of this HardwareInstance.  # noqa: E501
        :rtype: HardwareExtraDetailsInstance
        """
        return self._extra_details

    @extra_details.setter
    def extra_details(self, extra_details):
        """Sets the extra_details of this HardwareInstance.

        Additional hardware details. Contents are specific to each component type.  # noqa: E501

        :param extra_details: The extra_details of this HardwareInstance.  # noqa: E501
        :type: HardwareExtraDetailsInstance
        """

        self._extra_details = extra_details

    @property
    def stale_state(self):
        """Gets the stale_state of this HardwareInstance.  # noqa: E501

        Indicator of the stale state of component. Was added in version 2.0.0.0.  # noqa: E501

        :return: The stale_state of this HardwareInstance.  # noqa: E501
        :rtype: HardwareStaleStateEnum
        """
        return self._stale_state

    @stale_state.setter
    def stale_state(self, stale_state):
        """Sets the stale_state of this HardwareInstance.

        Indicator of the stale state of component. Was added in version 2.0.0.0.  # noqa: E501

        :param stale_state: The stale_state of this HardwareInstance.  # noqa: E501
        :type: HardwareStaleStateEnum
        """

        self._stale_state = stale_state

    @property
    def type_l10n(self):
        """Gets the type_l10n of this HardwareInstance.  # noqa: E501

        Localized message string corresponding to type  # noqa: E501

        :return: The type_l10n of this HardwareInstance.  # noqa: E501
        :rtype: str
        """
        return self._type_l10n

    @type_l10n.setter
    def type_l10n(self, type_l10n):
        """Sets the type_l10n of this HardwareInstance.

        Localized message string corresponding to type  # noqa: E501

        :param type_l10n: The type_l10n of this HardwareInstance.  # noqa: E501
        :type: str
        """

        self._type_l10n = type_l10n

    @property
    def lifecycle_state_l10n(self):
        """Gets the lifecycle_state_l10n of this HardwareInstance.  # noqa: E501

        Localized message string corresponding to lifecycle_state  # noqa: E501

        :return: The lifecycle_state_l10n of this HardwareInstance.  # noqa: E501
        :rtype: str
        """
        return self._lifecycle_state_l10n

    @lifecycle_state_l10n.setter
    def lifecycle_state_l10n(self, lifecycle_state_l10n):
        """Sets the lifecycle_state_l10n of this HardwareInstance.

        Localized message string corresponding to lifecycle_state  # noqa: E501

        :param lifecycle_state_l10n: The lifecycle_state_l10n of this HardwareInstance.  # noqa: E501
        :type: str
        """

        self._lifecycle_state_l10n = lifecycle_state_l10n

    @property
    def status_led_state_l10n(self):
        """Gets the status_led_state_l10n of this HardwareInstance.  # noqa: E501

        Localized message string corresponding to status_led_state  # noqa: E501

        :return: The status_led_state_l10n of this HardwareInstance.  # noqa: E501
        :rtype: str
        """
        return self._status_led_state_l10n

    @status_led_state_l10n.setter
    def status_led_state_l10n(self, status_led_state_l10n):
        """Sets the status_led_state_l10n of this HardwareInstance.

        Localized message string corresponding to status_led_state  # noqa: E501

        :param status_led_state_l10n: The status_led_state_l10n of this HardwareInstance.  # noqa: E501
        :type: str
        """

        self._status_led_state_l10n = status_led_state_l10n

    @property
    def stale_state_l10n(self):
        """Gets the stale_state_l10n of this HardwareInstance.  # noqa: E501

        Localized message string corresponding to stale_state Was added in version 2.0.0.0.  # noqa: E501

        :return: The stale_state_l10n of this HardwareInstance.  # noqa: E501
        :rtype: str
        """
        return self._stale_state_l10n

    @stale_state_l10n.setter
    def stale_state_l10n(self, stale_state_l10n):
        """Sets the stale_state_l10n of this HardwareInstance.

        Localized message string corresponding to stale_state Was added in version 2.0.0.0.  # noqa: E501

        :param stale_state_l10n: The stale_state_l10n of this HardwareInstance.  # noqa: E501
        :type: str
        """

        self._stale_state_l10n = stale_state_l10n

    @property
    def node_fc_ports(self):
        """Gets the node_fc_ports of this HardwareInstance.  # noqa: E501

        This is the inverse of the resource type fc_port association.  # noqa: E501

        :return: The node_fc_ports of this HardwareInstance.  # noqa: E501
        :rtype: list[FcPortInstance]
        """
        return self._node_fc_ports

    @node_fc_ports.setter
    def node_fc_ports(self, node_fc_ports):
        """Sets the node_fc_ports of this HardwareInstance.

        This is the inverse of the resource type fc_port association.  # noqa: E501

        :param node_fc_ports: The node_fc_ports of this HardwareInstance.  # noqa: E501
        :type: list[FcPortInstance]
        """

        self._node_fc_ports = node_fc_ports

    @property
    def sfp_fc_ports(self):
        """Gets the sfp_fc_ports of this HardwareInstance.  # noqa: E501

        This is the inverse of the resource type fc_port association.  # noqa: E501

        :return: The sfp_fc_ports of this HardwareInstance.  # noqa: E501
        :rtype: list[FcPortInstance]
        """
        return self._sfp_fc_ports

    @sfp_fc_ports.setter
    def sfp_fc_ports(self, sfp_fc_ports):
        """Sets the sfp_fc_ports of this HardwareInstance.

        This is the inverse of the resource type fc_port association.  # noqa: E501

        :param sfp_fc_ports: The sfp_fc_ports of this HardwareInstance.  # noqa: E501
        :type: list[FcPortInstance]
        """

        self._sfp_fc_ports = sfp_fc_ports

    @property
    def io_module_fc_ports(self):
        """Gets the io_module_fc_ports of this HardwareInstance.  # noqa: E501

        This is the inverse of the resource type fc_port association.  # noqa: E501

        :return: The io_module_fc_ports of this HardwareInstance.  # noqa: E501
        :rtype: list[FcPortInstance]
        """
        return self._io_module_fc_ports

    @io_module_fc_ports.setter
    def io_module_fc_ports(self, io_module_fc_ports):
        """Sets the io_module_fc_ports of this HardwareInstance.

        This is the inverse of the resource type fc_port association.  # noqa: E501

        :param io_module_fc_ports: The io_module_fc_ports of this HardwareInstance.  # noqa: E501
        :type: list[FcPortInstance]
        """

        self._io_module_fc_ports = io_module_fc_ports

    @property
    def hardware_parent_fc_ports(self):
        """Gets the hardware_parent_fc_ports of this HardwareInstance.  # noqa: E501

        This is the inverse of the resource type fc_port association.  # noqa: E501

        :return: The hardware_parent_fc_ports of this HardwareInstance.  # noqa: E501
        :rtype: list[FcPortInstance]
        """
        return self._hardware_parent_fc_ports

    @hardware_parent_fc_ports.setter
    def hardware_parent_fc_ports(self, hardware_parent_fc_ports):
        """Sets the hardware_parent_fc_ports of this HardwareInstance.

        This is the inverse of the resource type fc_port association.  # noqa: E501

        :param hardware_parent_fc_ports: The hardware_parent_fc_ports of this HardwareInstance.  # noqa: E501
        :type: list[FcPortInstance]
        """

        self._hardware_parent_fc_ports = hardware_parent_fc_ports

    @property
    def node_sas_ports(self):
        """Gets the node_sas_ports of this HardwareInstance.  # noqa: E501

        This is the inverse of the resource type sas_port association.  # noqa: E501

        :return: The node_sas_ports of this HardwareInstance.  # noqa: E501
        :rtype: list[SasPortInstance]
        """
        return self._node_sas_ports

    @node_sas_ports.setter
    def node_sas_ports(self, node_sas_ports):
        """Sets the node_sas_ports of this HardwareInstance.

        This is the inverse of the resource type sas_port association.  # noqa: E501

        :param node_sas_ports: The node_sas_ports of this HardwareInstance.  # noqa: E501
        :type: list[SasPortInstance]
        """

        self._node_sas_ports = node_sas_ports

    @property
    def sfp_sas_ports(self):
        """Gets the sfp_sas_ports of this HardwareInstance.  # noqa: E501

        This is the inverse of the resource type sas_port association.  # noqa: E501

        :return: The sfp_sas_ports of this HardwareInstance.  # noqa: E501
        :rtype: list[SasPortInstance]
        """
        return self._sfp_sas_ports

    @sfp_sas_ports.setter
    def sfp_sas_ports(self, sfp_sas_ports):
        """Sets the sfp_sas_ports of this HardwareInstance.

        This is the inverse of the resource type sas_port association.  # noqa: E501

        :param sfp_sas_ports: The sfp_sas_ports of this HardwareInstance.  # noqa: E501
        :type: list[SasPortInstance]
        """

        self._sfp_sas_ports = sfp_sas_ports

    @property
    def io_module_sas_ports(self):
        """Gets the io_module_sas_ports of this HardwareInstance.  # noqa: E501

        This is the inverse of the resource type sas_port association.  # noqa: E501

        :return: The io_module_sas_ports of this HardwareInstance.  # noqa: E501
        :rtype: list[SasPortInstance]
        """
        return self._io_module_sas_ports

    @io_module_sas_ports.setter
    def io_module_sas_ports(self, io_module_sas_ports):
        """Sets the io_module_sas_ports of this HardwareInstance.

        This is the inverse of the resource type sas_port association.  # noqa: E501

        :param io_module_sas_ports: The io_module_sas_ports of this HardwareInstance.  # noqa: E501
        :type: list[SasPortInstance]
        """

        self._io_module_sas_ports = io_module_sas_ports

    @property
    def hardware_parent_sas_ports(self):
        """Gets the hardware_parent_sas_ports of this HardwareInstance.  # noqa: E501

        This is the inverse of the resource type sas_port association.  # noqa: E501

        :return: The hardware_parent_sas_ports of this HardwareInstance.  # noqa: E501
        :rtype: list[SasPortInstance]
        """
        return self._hardware_parent_sas_ports

    @hardware_parent_sas_ports.setter
    def hardware_parent_sas_ports(self, hardware_parent_sas_ports):
        """Sets the hardware_parent_sas_ports of this HardwareInstance.

        This is the inverse of the resource type sas_port association.  # noqa: E501

        :param hardware_parent_sas_ports: The hardware_parent_sas_ports of this HardwareInstance.  # noqa: E501
        :type: list[SasPortInstance]
        """

        self._hardware_parent_sas_ports = hardware_parent_sas_ports

    @property
    def node_eth_ports(self):
        """Gets the node_eth_ports of this HardwareInstance.  # noqa: E501

        This is the inverse of the resource type eth_port association.  # noqa: E501

        :return: The node_eth_ports of this HardwareInstance.  # noqa: E501
        :rtype: list[EthPortInstance]
        """
        return self._node_eth_ports

    @node_eth_ports.setter
    def node_eth_ports(self, node_eth_ports):
        """Sets the node_eth_ports of this HardwareInstance.

        This is the inverse of the resource type eth_port association.  # noqa: E501

        :param node_eth_ports: The node_eth_ports of this HardwareInstance.  # noqa: E501
        :type: list[EthPortInstance]
        """

        self._node_eth_ports = node_eth_ports

    @property
    def sfp_eth_ports(self):
        """Gets the sfp_eth_ports of this HardwareInstance.  # noqa: E501

        This is the inverse of the resource type eth_port association.  # noqa: E501

        :return: The sfp_eth_ports of this HardwareInstance.  # noqa: E501
        :rtype: list[EthPortInstance]
        """
        return self._sfp_eth_ports

    @sfp_eth_ports.setter
    def sfp_eth_ports(self, sfp_eth_ports):
        """Sets the sfp_eth_ports of this HardwareInstance.

        This is the inverse of the resource type eth_port association.  # noqa: E501

        :param sfp_eth_ports: The sfp_eth_ports of this HardwareInstance.  # noqa: E501
        :type: list[EthPortInstance]
        """

        self._sfp_eth_ports = sfp_eth_ports

    @property
    def io_module_eth_ports(self):
        """Gets the io_module_eth_ports of this HardwareInstance.  # noqa: E501

        This is the inverse of the resource type eth_port association.  # noqa: E501

        :return: The io_module_eth_ports of this HardwareInstance.  # noqa: E501
        :rtype: list[EthPortInstance]
        """
        return self._io_module_eth_ports

    @io_module_eth_ports.setter
    def io_module_eth_ports(self, io_module_eth_ports):
        """Sets the io_module_eth_ports of this HardwareInstance.

        This is the inverse of the resource type eth_port association.  # noqa: E501

        :param io_module_eth_ports: The io_module_eth_ports of this HardwareInstance.  # noqa: E501
        :type: list[EthPortInstance]
        """

        self._io_module_eth_ports = io_module_eth_ports

    @property
    def hardware_parent_eth_ports(self):
        """Gets the hardware_parent_eth_ports of this HardwareInstance.  # noqa: E501

        This is the inverse of the resource type eth_port association.  # noqa: E501

        :return: The hardware_parent_eth_ports of this HardwareInstance.  # noqa: E501
        :rtype: list[EthPortInstance]
        """
        return self._hardware_parent_eth_ports

    @hardware_parent_eth_ports.setter
    def hardware_parent_eth_ports(self, hardware_parent_eth_ports):
        """Sets the hardware_parent_eth_ports of this HardwareInstance.

        This is the inverse of the resource type eth_port association.  # noqa: E501

        :param hardware_parent_eth_ports: The hardware_parent_eth_ports of this HardwareInstance.  # noqa: E501
        :type: list[EthPortInstance]
        """

        self._hardware_parent_eth_ports = hardware_parent_eth_ports

    @property
    def node_eth_be_ports(self):
        """Gets the node_eth_be_ports of this HardwareInstance.  # noqa: E501

        This is the inverse of the resource type eth_be_port association.  # noqa: E501

        :return: The node_eth_be_ports of this HardwareInstance.  # noqa: E501
        :rtype: list[EthBePortInstance]
        """
        return self._node_eth_be_ports

    @node_eth_be_ports.setter
    def node_eth_be_ports(self, node_eth_be_ports):
        """Sets the node_eth_be_ports of this HardwareInstance.

        This is the inverse of the resource type eth_be_port association.  # noqa: E501

        :param node_eth_be_ports: The node_eth_be_ports of this HardwareInstance.  # noqa: E501
        :type: list[EthBePortInstance]
        """

        self._node_eth_be_ports = node_eth_be_ports

    @property
    def sfp_eth_be_ports(self):
        """Gets the sfp_eth_be_ports of this HardwareInstance.  # noqa: E501

        This is the inverse of the resource type eth_be_port association.  # noqa: E501

        :return: The sfp_eth_be_ports of this HardwareInstance.  # noqa: E501
        :rtype: list[EthBePortInstance]
        """
        return self._sfp_eth_be_ports

    @sfp_eth_be_ports.setter
    def sfp_eth_be_ports(self, sfp_eth_be_ports):
        """Sets the sfp_eth_be_ports of this HardwareInstance.

        This is the inverse of the resource type eth_be_port association.  # noqa: E501

        :param sfp_eth_be_ports: The sfp_eth_be_ports of this HardwareInstance.  # noqa: E501
        :type: list[EthBePortInstance]
        """

        self._sfp_eth_be_ports = sfp_eth_be_ports

    @property
    def hardware_parent_eth_be_ports(self):
        """Gets the hardware_parent_eth_be_ports of this HardwareInstance.  # noqa: E501

        This is the inverse of the resource type eth_be_port association.  # noqa: E501

        :return: The hardware_parent_eth_be_ports of this HardwareInstance.  # noqa: E501
        :rtype: list[EthBePortInstance]
        """
        return self._hardware_parent_eth_be_ports

    @hardware_parent_eth_be_ports.setter
    def hardware_parent_eth_be_ports(self, hardware_parent_eth_be_ports):
        """Sets the hardware_parent_eth_be_ports of this HardwareInstance.

        This is the inverse of the resource type eth_be_port association.  # noqa: E501

        :param hardware_parent_eth_be_ports: The hardware_parent_eth_be_ports of this HardwareInstance.  # noqa: E501
        :type: list[EthBePortInstance]
        """

        self._hardware_parent_eth_be_ports = hardware_parent_eth_be_ports

    @property
    def parent(self):
        """Gets the parent of this HardwareInstance.  # noqa: E501

        This is the embeddable reference form of parent_id attribute.  # noqa: E501

        :return: The parent of this HardwareInstance.  # noqa: E501
        :rtype: HardwareInstance
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this HardwareInstance.

        This is the embeddable reference form of parent_id attribute.  # noqa: E501

        :param parent: The parent of this HardwareInstance.  # noqa: E501
        :type: HardwareInstance
        """

        self._parent = parent

    @property
    def children(self):
        """Gets the children of this HardwareInstance.  # noqa: E501

        This is the inverse of the resource type hardware association.  # noqa: E501

        :return: The children of this HardwareInstance.  # noqa: E501
        :rtype: list[HardwareInstance]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this HardwareInstance.

        This is the inverse of the resource type hardware association.  # noqa: E501

        :param children: The children of this HardwareInstance.  # noqa: E501
        :type: list[HardwareInstance]
        """

        self._children = children

    @property
    def appliance(self):
        """Gets the appliance of this HardwareInstance.  # noqa: E501

        This is the embeddable reference form of appliance_id attribute.  # noqa: E501

        :return: The appliance of this HardwareInstance.  # noqa: E501
        :rtype: ApplianceInstance
        """
        return self._appliance

    @appliance.setter
    def appliance(self, appliance):
        """Sets the appliance of this HardwareInstance.

        This is the embeddable reference form of appliance_id attribute.  # noqa: E501

        :param appliance: The appliance of this HardwareInstance.  # noqa: E501
        :type: ApplianceInstance
        """

        self._appliance = appliance

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
        if issubclass(HardwareInstance, dict):
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
        if not isinstance(other, HardwareInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HardwareInstance):
            return True

        return self.to_dict() != other.to_dict()
