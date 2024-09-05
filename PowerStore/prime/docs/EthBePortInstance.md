# EthBePortInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the Ethernet Backend port. | [optional] 
**name** | **str** | Name of the Ethernet Backend port.  This property supports case-insensitive filtering. | [optional] 
**appliance_id** | **str** | Unique identifier of the appliance containing the port. | [optional] 
**node_id** | **str** | Unique identifier of the hardware instance of type &#39;Node&#39; containing the port. | [optional] 
**mac_address** | **str** | The MAC address of the Ethernet Backend port. | [optional] 
**is_link_up** | **bool** | Indicates whether the Ethernet Backend port&#39;s link is up. Values are: * true - Link is up. * false - Link is down.  | [optional] 
**speed** | [**EthBEPortSpeedEnum**](EthBEPortSpeedEnum.md) |  | [optional] 
**sfp_id** | **str** | Unique identifier of the hardware instance of type &#39;SFP&#39; (Small Form-factor Pluggable) inserted into the port.  | [optional] 
**port_index** | **int** | Index of the Ethernet Backend port in IO module. | [optional] 
**port_connector_type** | [**FrontEndPortConnectionTypeEnum**](FrontEndPortConnectionTypeEnum.md) |  | [optional] 
**hardware_parent_id** | **str** | Unique identifier of the parent hardware instance handling the port. | [optional] 
**expected_peer_id** | **str** | Unique identifier of the backend ethernet port which is expected to be connected to this one.  | [optional] 
**actual_peer_id** | **str** | Unique identifier of the backend ethernet port which is actually connected to this one.  | [optional] 
**protocols** | [**list[EthBEPortProtocolEnum]**](EthBEPortProtocolEnum.md) | Supported Protocols over Ethernet port. currently only NVMe is supported.  | [optional] 
**stale_state** | [**PortStaleStateEnum**](PortStaleStateEnum.md) |  | [optional] 
**speed_l10n** | **str** | Localized message string corresponding to speed Was added in version 3.0.0.0. | [optional] 
**port_connector_type_l10n** | **str** | Localized message string corresponding to port_connector_type Was added in version 3.0.0.0. | [optional] 
**protocols_l10n** | **list[str]** | Localized message array corresponding to protocols Was added in version 3.0.0.0. | [optional] 
**stale_state_l10n** | **str** | Localized message string corresponding to stale_state Was added in version 3.0.0.0. | [optional] 
**appliance** | [**ApplianceInstance**](ApplianceInstance.md) | This is the embeddable reference form of appliance_id attribute. | [optional] 
**node** | [**HardwareInstance**](HardwareInstance.md) | This is the embeddable reference form of node_id attribute. | [optional] 
**sfp** | [**HardwareInstance**](HardwareInstance.md) | This is the embeddable reference form of sfp_id attribute. | [optional] 
**hardware_parent** | [**HardwareInstance**](HardwareInstance.md) | This is the embeddable reference form of hardware_parent_id attribute. | [optional] 
**expected_peer** | [**EthBePortInstance**](EthBePortInstance.md) | This is the embeddable reference form of expected_peer_id attribute. | [optional] 
**actual_peer** | [**EthBePortInstance**](EthBePortInstance.md) | This is the embeddable reference form of actual_peer_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


