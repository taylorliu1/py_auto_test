# HardwareInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of the component. | [optional] 
**name** | **str** | The name of the component.  This property supports case-insensitive filtering. | [optional] 
**type** | [**HardwareTypeEnum**](HardwareTypeEnum.md) | Hardware component type. | [optional] 
**lifecycle_state** | [**HardwareLifecycleStateEnum**](HardwareLifecycleStateEnum.md) | Life cycle state of the component. | [optional] 
**parent_id** | **str** | The id of the component&#39;s parent, or null if this component is at the top of the parent hierarchy. | [optional] 
**appliance_id** | **str** | The id of the component&#39;s associated appliance. | [optional] 
**slot** | **int** | The slot or location of the component. | [optional] 
**part_number** | **str** | The part number of the component. | [optional] 
**serial_number** | **str** | The serial number of the component. | [optional] 
**status_led_state** | [**HardwareStatusLEDStateEnum**](HardwareStatusLEDStateEnum.md) | Indicator of the state of the component status LED. | [optional] 
**is_marked** | **bool** | Indicator of whether a component is location marked or not. | [optional] 
**extra_details** | [**HardwareExtraDetailsInstance**](HardwareExtraDetailsInstance.md) | Additional hardware details. Contents are specific to each component type. | [optional] 
**stale_state** | [**HardwareStaleStateEnum**](HardwareStaleStateEnum.md) | Indicator of the stale state of component. Was added in version 2.0.0.0. | [optional] 
**type_l10n** | **str** | Localized message string corresponding to type | [optional] 
**lifecycle_state_l10n** | **str** | Localized message string corresponding to lifecycle_state | [optional] 
**status_led_state_l10n** | **str** | Localized message string corresponding to status_led_state | [optional] 
**stale_state_l10n** | **str** | Localized message string corresponding to stale_state Was added in version 2.0.0.0. | [optional] 
**node_fc_ports** | [**list[FcPortInstance]**](FcPortInstance.md) | This is the inverse of the resource type fc_port association. | [optional] 
**sfp_fc_ports** | [**list[FcPortInstance]**](FcPortInstance.md) | This is the inverse of the resource type fc_port association. | [optional] 
**io_module_fc_ports** | [**list[FcPortInstance]**](FcPortInstance.md) | This is the inverse of the resource type fc_port association. | [optional] 
**hardware_parent_fc_ports** | [**list[FcPortInstance]**](FcPortInstance.md) | This is the inverse of the resource type fc_port association. | [optional] 
**node_sas_ports** | [**list[SasPortInstance]**](SasPortInstance.md) | This is the inverse of the resource type sas_port association. | [optional] 
**sfp_sas_ports** | [**list[SasPortInstance]**](SasPortInstance.md) | This is the inverse of the resource type sas_port association. | [optional] 
**io_module_sas_ports** | [**list[SasPortInstance]**](SasPortInstance.md) | This is the inverse of the resource type sas_port association. | [optional] 
**hardware_parent_sas_ports** | [**list[SasPortInstance]**](SasPortInstance.md) | This is the inverse of the resource type sas_port association. | [optional] 
**node_eth_ports** | [**list[EthPortInstance]**](EthPortInstance.md) | This is the inverse of the resource type eth_port association. | [optional] 
**sfp_eth_ports** | [**list[EthPortInstance]**](EthPortInstance.md) | This is the inverse of the resource type eth_port association. | [optional] 
**io_module_eth_ports** | [**list[EthPortInstance]**](EthPortInstance.md) | This is the inverse of the resource type eth_port association. | [optional] 
**hardware_parent_eth_ports** | [**list[EthPortInstance]**](EthPortInstance.md) | This is the inverse of the resource type eth_port association. | [optional] 
**node_eth_be_ports** | [**list[EthBePortInstance]**](EthBePortInstance.md) | This is the inverse of the resource type eth_be_port association. | [optional] 
**sfp_eth_be_ports** | [**list[EthBePortInstance]**](EthBePortInstance.md) | This is the inverse of the resource type eth_be_port association. | [optional] 
**hardware_parent_eth_be_ports** | [**list[EthBePortInstance]**](EthBePortInstance.md) | This is the inverse of the resource type eth_be_port association. | [optional] 
**parent** | [**HardwareInstance**](HardwareInstance.md) | This is the embeddable reference form of parent_id attribute. | [optional] 
**children** | [**list[HardwareInstance]**](HardwareInstance.md) | This is the inverse of the resource type hardware association. | [optional] 
**appliance** | [**ApplianceInstance**](ApplianceInstance.md) | This is the embeddable reference form of appliance_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


