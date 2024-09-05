# SasPortInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the SAS port. | [optional] 
**name** | **str** | Name of the SAS port.  This property supports case-insensitive filtering. | [optional] 
**appliance_id** | **str** | Unique identifier of the appliance containing the port. | [optional] 
**node_id** | **str** | Unique identifier of the hardware instance of type &#39;Node&#39; containing the port. | [optional] 
**is_link_up** | **bool** | Indicates whether the SAS port&#39;s link is up. Values are: * true - Link is up. * false - Link is down.  | [optional] 
**is_in_use** | **bool** | Indicates whether the port is in use. Values are: * true - Is in use. * false - Is not in use.  Was added in version 3.0.0.0. | [optional] 
**speed** | [**SasPortSpeedEnum**](SasPortSpeedEnum.md) |  | [optional] 
**sfp_id** | **str** | Unique identifier of the hardware instance of type &#39;SFP&#39; (Small Form-factor Pluggable) inserted into the port.  | [optional] 
**io_module_id** | **str** | Unique identifier of the hardware instance of type &#39;IO_Module&#39; handling the port. Was deprecated in version 2.0.0.0. | [optional] 
**hardware_parent_id** | **str** | Unique identifier of the parent hardware instance handling the port. Was added in version 2.0.0.0. | [optional] 
**port_index** | **int** | Index of the SAS port in IO module. | [optional] 
**partner_id** | **str** | Unique identifier of the SAS partner port. | [optional] 
**stale_state** | [**PortStaleStateEnum**](PortStaleStateEnum.md) | Indicator of the stale state of the port. Was added in version 2.0.0.0. | [optional] 
**speed_l10n** | **str** | Localized message string corresponding to speed | [optional] 
**stale_state_l10n** | **str** | Localized message string corresponding to stale_state Was added in version 2.0.0.0. | [optional] 
**appliance** | [**ApplianceInstance**](ApplianceInstance.md) | This is the embeddable reference form of appliance_id attribute. | [optional] 
**node** | [**HardwareInstance**](HardwareInstance.md) | This is the embeddable reference form of node_id attribute. | [optional] 
**sfp** | [**HardwareInstance**](HardwareInstance.md) | This is the embeddable reference form of sfp_id attribute. | [optional] 
**io_module** | [**HardwareInstance**](HardwareInstance.md) | This is the embeddable reference form of io_module_id attribute. | [optional] 
**hardware_parent** | [**HardwareInstance**](HardwareInstance.md) | This is the embeddable reference form of hardware_parent_id attribute. | [optional] 
**partner** | [**SasPortInstance**](SasPortInstance.md) | This is the embeddable reference form of partner_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


