# PhysicalSwitchConnectionInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Physical switch address in IPv4 or IPv6 or DNS hostname format. | [optional] 
**port** | **int** | Port used for connection to switch. | [optional] 
**connect_method** | [**PhysicalSwitchConnectMethodEnum**](PhysicalSwitchConnectMethodEnum.md) |  | [optional] 
**username** | **str** | Username to connect a physical switch for SSH connection method. | [optional] 
**physical_switch_id** | **str** | Id of physical switch to which connection belongs. | [optional] 
**connect_method_l10n** | **str** | Localized message string corresponding to connect_method | [optional] 
**physical_switch** | [**PhysicalSwitchInstance**](PhysicalSwitchInstance.md) | This is the embeddable reference form of physical_switch_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


