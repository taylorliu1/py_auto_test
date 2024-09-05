# EthPortInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Ethernet port instance identifier. | [optional] 
**name** | **str** | Ethernet port name.  This property supports case-insensitive filtering. | [optional] 
**appliance_id** | **str** | The id of the appliance containing the port. | [optional] 
**node_id** | **str** | Unique identifier of the hardware instance of type &#39;Node&#39; containing the port. | [optional] 
**bond_id** | **str** | Unique identifier of the bond containing the port, or null if the port is not in a bond. | [optional] 
**mac_address** | **str** | Ethernet port current MAC address. | [optional] 
**permanent_mac_address** | **str** | Ethernet port permanent MAC address assigned at the moment of the manufacture. Was added in version 3.0.0.0. | [optional] 
**is_link_up** | **bool** | Indicates whether the Ethernet port&#39;s link is up. Values are: * true - Link is up. * false - Link is down.  | [optional] 
**is_in_use** | **bool** | Indicates whether the port is in use. Values are: * true - Is in use. * false - Is not in use.  Was added in version 3.0.0.0. | [optional] 
**supported_speeds** | [**list[EthPortSpeedEnum]**](EthPortSpeedEnum.md) | The list of supported transmission speeds for Ethernet port. | [optional] 
**current_speed** | [**EthPortSpeedEnum**](EthPortSpeedEnum.md) |  | [optional] 
**requested_speed** | [**EthPortSpeedEnum**](EthPortSpeedEnum.md) |  | [optional] 
**current_mtu** | **int** | The Maximum transmission unit (MTU) packet size that the Ethernet port can transmit. The fabric MTU can be set to any value in the range [1500-9000]. The network MTU can be set to any value in the range [1280-9000]. The network MTU must be less than or equal to the current fabric MTU.  | [optional] 
**sfp_id** | **str** | Unique identifier of the hardware instance of type &#39;SFP&#39; (Small Form-factor Pluggable) inserted into the port.  | [optional] 
**io_module_id** | **str** | Unique identifier of the hardware instance of type &#39;IO_Module&#39; handling the port. Was deprecated in version 2.0.0.0. | [optional] 
**hardware_parent_id** | **str** | Unique identifier of the parent hardware instance handling the port. Was added in version 2.0.0.0. | [optional] 
**port_index** | **int** | The index of the Ethernet port in IO module. | [optional] 
**port_connector_type** | [**FrontEndPortConnectionTypeEnum**](FrontEndPortConnectionTypeEnum.md) |  | [optional] 
**partner_id** | **str** | Unique identifier of the partner port instance. | [optional] 
**is_hypervisor_managed** | **bool** | Indicates whether the port is managed by a hypervisor. | [optional] 
**hypervisor_port_name** | **str** | Hypervisor front-end port name capabilities.  This property supports case-insensitive filtering. | [optional] 
**hypervisor_vswitch_name** | **str** | Name of the virtual switch associated with the hypervisor port.  This property supports case-insensitive filtering. | [optional] 
**hypervisor_port_id** | **int** | Unique identifier of the virtual switch port associated with the hypervisor port. | [optional] 
**hypervisor_vswitch_id** | **str** | Unique identifier of the virtual switch associated with the hypervisor port. | [optional] 
**stale_state** | [**PortStaleStateEnum**](PortStaleStateEnum.md) | Indicator of the stale state of the port. Was added in version 2.0.0.0. | [optional] 
**supported_speeds_l10n** | **list[str]** | Localized message array corresponding to supported_speeds | [optional] 
**current_speed_l10n** | **str** | Localized message string corresponding to current_speed | [optional] 
**requested_speed_l10n** | **str** | Localized message string corresponding to requested_speed | [optional] 
**port_connector_type_l10n** | **str** | Localized message string corresponding to port_connector_type | [optional] 
**stale_state_l10n** | **str** | Localized message string corresponding to stale_state Was added in version 2.0.0.0. | [optional] 
**ip_ports** | [**list[IpPortInstance]**](IpPortInstance.md) | This is the inverse of the resource type ip_port association. | [optional] 
**appliance** | [**ApplianceInstance**](ApplianceInstance.md) | This is the embeddable reference form of appliance_id attribute. | [optional] 
**node** | [**HardwareInstance**](HardwareInstance.md) | This is the embeddable reference form of node_id attribute. | [optional] 
**bond** | [**BondInstance**](BondInstance.md) | This is the embeddable reference form of bond_id attribute. | [optional] 
**sfp** | [**HardwareInstance**](HardwareInstance.md) | This is the embeddable reference form of sfp_id attribute. | [optional] 
**io_module** | [**HardwareInstance**](HardwareInstance.md) | This is the embeddable reference form of io_module_id attribute. | [optional] 
**hardware_parent** | [**HardwareInstance**](HardwareInstance.md) | This is the embeddable reference form of hardware_parent_id attribute. | [optional] 
**partner** | [**EthPortInstance**](EthPortInstance.md) | This is the embeddable reference form of partner_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


