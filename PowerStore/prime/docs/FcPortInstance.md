# FcPortInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the port. | [optional] 
**name** | **str** | Name of the port.  This property supports case-insensitive filtering. | [optional] 
**appliance_id** | **str** | Unique identifier of the appliance containing the port. | [optional] 
**node_id** | **str** | Unique identifier of the hardware instance of type &#39;Node&#39; containing the port. | [optional] 
**wwn** | **str** | World Wide Name (WWN) of the port. | [optional] 
**wwn_nvme** | **str** | World Wide Name (WWN) of NVME port. Was added in version 2.0.0.0. | [optional] 
**wwn_node** | **str** | World Wide Name (WWN) of the Node of the port. Was added in version 3.0.0.0. | [optional] 
**is_link_up** | **bool** | Indicates whether the port&#39;s link is up. Values are: * true - Link is up. * false - Link is down.  | [optional] 
**is_in_use** | **bool** | Indicates whether the port is in use. Values are: * true - Is in use. * false - Is not in use.  Was added in version 3.0.0.0. | [optional] 
**supported_speeds** | [**list[FcPortSpeedEnum]**](FcPortSpeedEnum.md) | List of supported transmission speeds for the port. | [optional] 
**current_speed** | [**FcPortSpeedEnum**](FcPortSpeedEnum.md) |  | [optional] 
**requested_speed** | [**FcPortSpeedEnum**](FcPortSpeedEnum.md) |  | [optional] 
**sfp_id** | **str** | Unique identifier of the hardware instance of type &#39;SFP&#39; (Small Form-factor Pluggable) inserted into the port.  | [optional] 
**io_module_id** | **str** | Unique identifier of the hardware instance of type &#39;IO_Module&#39; handling the port. Was deprecated in version 2.0.0.0. | [optional] 
**hardware_parent_id** | **str** | Unique identifier of the parent hardware instance handling the port. @added(Foothills) Was added in version 2.0.0.0. | [optional] 
**port_index** | **int** | Index of the port in the IO module. | [optional] 
**port_connector_type** | [**FrontEndPortConnectionTypeEnum**](FrontEndPortConnectionTypeEnum.md) |  | [optional] 
**partner_id** | **str** | Unique identifier of the partner port. | [optional] 
**protocols** | [**list[FcPortProtocolEnum]**](FcPortProtocolEnum.md) | List of supported protocols for the port. Was added in version 2.0.0.0. | [optional] 
**stale_state** | [**PortStaleStateEnum**](PortStaleStateEnum.md) | Indicator of the stale state of the port. Was added in version 2.0.0.0. | [optional] 
**scsi_mode** | [**FcPortScsiModeEnum**](FcPortScsiModeEnum.md) |  Was added in version 3.0.0.0. | [optional] 
**supported_speeds_l10n** | **list[str]** | Localized message array corresponding to supported_speeds | [optional] 
**current_speed_l10n** | **str** | Localized message string corresponding to current_speed | [optional] 
**requested_speed_l10n** | **str** | Localized message string corresponding to requested_speed | [optional] 
**port_connector_type_l10n** | **str** | Localized message string corresponding to port_connector_type | [optional] 
**protocols_l10n** | **list[str]** | Localized message array corresponding to protocols Was added in version 2.0.0.0. | [optional] 
**stale_state_l10n** | **str** | Localized message string corresponding to stale_state Was added in version 2.0.0.0. | [optional] 
**scsi_mode_l10n** | **str** | Localized message string corresponding to scsi_mode Was added in version 3.0.0.0. | [optional] 
**appliance** | [**ApplianceInstance**](ApplianceInstance.md) | This is the embeddable reference form of appliance_id attribute. | [optional] 
**node** | [**HardwareInstance**](HardwareInstance.md) | This is the embeddable reference form of node_id attribute. | [optional] 
**sfp** | [**HardwareInstance**](HardwareInstance.md) | This is the embeddable reference form of sfp_id attribute. | [optional] 
**io_module** | [**HardwareInstance**](HardwareInstance.md) | This is the embeddable reference form of io_module_id attribute. | [optional] 
**hardware_parent** | [**HardwareInstance**](HardwareInstance.md) | This is the embeddable reference form of hardware_parent_id attribute. | [optional] 
**partner** | [**FcPortInstance**](FcPortInstance.md) | This is the embeddable reference form of partner_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


