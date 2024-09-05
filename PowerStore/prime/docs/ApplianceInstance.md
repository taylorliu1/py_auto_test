# ApplianceInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the appliance. | [optional] 
**name** | **str** | Name of the appliance.  This property supports case-insensitive filtering. | [optional] 
**service_tag** | **str** | Dell Service Tag. | [optional] 
**express_service_code** | **str** | Express Service Code. | [optional] 
**model** | **str** | Model of the appliance. | [optional] 
**node_count** | **int** | The number of nodes deployed on an appliance. Was added in version 3.0.0.0. | [optional] [default to 2]
**drive_failure_tolerance_level** | [**DriveFailureToleranceLevelEnum**](DriveFailureToleranceLevelEnum.md) |  Was added in version 2.0.0.0. | [optional] 
**drive_failure_tolerance_level_l10n** | **str** | Localized message string corresponding to drive_failure_tolerance_level Was added in version 2.0.0.0. | [optional] 
**nodes** | [**list[NodeInstance]**](NodeInstance.md) | This is the inverse of the resource type node association. | [optional] 
**ip_pool_addresses** | [**list[IpPoolAddressInstance]**](IpPoolAddressInstance.md) | This is the inverse of the resource type ip_pool_address association. | [optional] 
**veth_ports** | [**list[VethPortInstance]**](VethPortInstance.md) | This is the inverse of the resource type veth_port association. | [optional] 
**virtual_volumes** | [**list[VirtualVolumeInstance]**](VirtualVolumeInstance.md) | This is the inverse of the resource type virtual_volume association. | [optional] 
**maintenance_windows** | [**list[MaintenanceWindowInstance]**](MaintenanceWindowInstance.md) | This is the inverse of the resource type maintenance_window association. | [optional] 
**fc_ports** | [**list[FcPortInstance]**](FcPortInstance.md) | This is the inverse of the resource type fc_port association. | [optional] 
**sas_ports** | [**list[SasPortInstance]**](SasPortInstance.md) | This is the inverse of the resource type sas_port association. | [optional] 
**eth_ports** | [**list[EthPortInstance]**](EthPortInstance.md) | This is the inverse of the resource type eth_port association. | [optional] 
**eth_be_ports** | [**list[EthBePortInstance]**](EthBePortInstance.md) | This is the inverse of the resource type eth_be_port association. | [optional] 
**software_installed** | [**list[SoftwareInstalledInstance]**](SoftwareInstalledInstance.md) | This is the inverse of the resource type software_installed association. | [optional] 
**hardware** | [**list[HardwareInstance]**](HardwareInstance.md) | This is the inverse of the resource type hardware association. | [optional] 
**volumes** | [**list[VolumeInstance]**](VolumeInstance.md) | This is the inverse of the resource type volume association. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


