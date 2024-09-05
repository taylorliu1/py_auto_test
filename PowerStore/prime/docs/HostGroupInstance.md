# HostGroupInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The host group unique identifier. | [optional] 
**name** | **str** | The host group name.  This property supports case-insensitive filtering. | [optional] 
**description** | **str** | A description for the host group. | [optional] 
**host_connectivity** | [**HostConnectivityEnum**](HostConnectivityEnum.md) |  Was added in version 3.0.0.0. | [optional] 
**host_connectivity_l10n** | **str** | Localized message string corresponding to host_connectivity Was added in version 3.0.0.0. | [optional] 
**hosts** | [**list[HostInstance]**](HostInstance.md) | This is the inverse of the resource type host association. | [optional] 
**mapped_host_groups** | [**list[HostVolumeMappingInstance]**](HostVolumeMappingInstance.md) | This is the inverse of the resource type host_volume_mapping association. | [optional] 
**host_virtual_volume_mappings** | [**list[HostVirtualVolumeMappingInstance]**](HostVirtualVolumeMappingInstance.md) | This is the inverse of the resource type host_virtual_volume_mapping association. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


