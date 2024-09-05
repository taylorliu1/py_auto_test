# ImportVnxArrayInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the VNX storage system. | [optional] 
**name** | **str** | Name of the VNX storage system.  This property supports case-insensitive filtering. | [optional] 
**serial_number** | **str** | Serial number of the VNX storage system. | [optional] 
**management_address** | **str** | Management address for communicating with the VNX storage system. This is usually the address of Storage Processor A (SPA). The address can be an IPv4 address or FQDN (Fully Qualified Domain Name). | [optional] 
**alternate_management_address** | **str** | Alternate management address for communicating with the VNX storage system. This is usually the address of Storage Processor B (SPB). The address can be an IPv4 address or FQDN (Fully Qualified Domain Name). | [optional] 
**user_name** | **str** | User account name used to communicate with the VNX storage system. | [optional] 
**model** | **str** | Model name of the VNX storage system. | [optional] 
**is_faulted** | **bool** | Indicates whether the VNX storage system is faulted. | [optional] 
**last_updated_timestamp** | **datetime** | Timestamp at which the VNX storage system details were last updated. These details include information about the VNX storage system and its importable volumes and consistency groups. The timestamp is updated when the VNX storage system is created and when the importable storage resources are discovered using the discover action. | [optional] 
**software_version** | **str** | The software version of the block operating environment of the VNX storage system. | [optional] 
**supported_import_type** | [**SupportedImportTypeEnum**](SupportedImportTypeEnum.md) |  Was added in version 1.0.2. | [optional] 
**supported_import_type_l10n** | **str** | Localized message string corresponding to supported_import_type Was added in version 1.0.2. | [optional] 
**import_vnx_volumes** | [**list[ImportVnxVolumeInstance]**](ImportVnxVolumeInstance.md) | This is the inverse of the resource type import_vnx_volume association. | [optional] 
**import_vnx_consistency_groups** | [**list[ImportVnxConsistencyGroupInstance]**](ImportVnxConsistencyGroupInstance.md) | This is the inverse of the resource type import_vnx_consistency_group association. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


