# PhysicalSwitchConnectionModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Physical switch address in IPv4 or IPv6 or DNS hostname format. | 
**port** | **int** | Port used for connection to switch. | [optional] 
**connect_method** | [**PhysicalSwitchConnectMethodEnum**](PhysicalSwitchConnectMethodEnum.md) |  | 
**username** | **str** | Username to connect a physical switch for SSH connection method. | [optional] 
**ssh_password** | **str** | SSH password to connect a physical switch if SSH connect method is specified. | [optional] 
**snmp_community_string** | **str** | SNMPv2 community string, if SNMPv2c connect method is specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


