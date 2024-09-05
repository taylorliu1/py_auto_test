# ImportStorageCenterInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the SC array that is a source storage system for import. | [optional] 
**name** | **str** | Name of the SC array.  This property supports case-insensitive filtering. | [optional] 
**management_address** | **str** | Management address to use for communicating with the SC array. The address can be an IPv4 address or FQDN (Fully Qualified Domain Name). | [optional] 
**user_name** | **str** | User account name used to communicate with the SC array. | [optional] 
**model** | **str** | Model name of the SC array. | [optional] 
**serial_number** | **int** | Serial number of the SC array. | [optional] 
**api_version** | **str** | API version of the SC OS (SCOS). | [optional] 
**status** | [**SCStatusEnum**](SCStatusEnum.md) |  | [optional] 
**last_update_time** | **datetime** | Timestamp at which the SC array details were last updated. This includes the information about the array and its importable volumes and consistency groups. The timestamp is updated when the SC array is created and when the importable storage resources are discovered using the discover_importable_resources action. | [optional] 
**supported_import_type** | [**SupportedImportTypeEnum**](SupportedImportTypeEnum.md) |  Was added in version 1.0.2. | [optional] 
**status_l10n** | **str** | Localized message string corresponding to status | [optional] 
**supported_import_type_l10n** | **str** | Localized message string corresponding to supported_import_type Was added in version 1.0.2. | [optional] 
**import_storage_center_volumes** | [**list[ImportStorageCenterVolumeInstance]**](ImportStorageCenterVolumeInstance.md) | This is the inverse of the resource type import_storage_center_volume association. | [optional] 
**import_storage_center_consistency_groups** | [**list[ImportStorageCenterConsistencyGroupInstance]**](ImportStorageCenterConsistencyGroupInstance.md) | This is the inverse of the resource type import_storage_center_consistency_group association. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


