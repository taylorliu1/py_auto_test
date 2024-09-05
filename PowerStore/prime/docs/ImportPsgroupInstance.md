# ImportPsgroupInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the PS Group. | [optional] 
**name** | **str** | Name of the PS Group.  This property supports case-insensitive filtering. | [optional] 
**serial_number** | **str** | Serial number of the PS Group. | [optional] 
**management_address** | **str** | Management address of the PS Group. This can be an IPv4 address or FQDN (Fully Qualified Domain Name). | [optional] 
**description** | **str** | Description of the PS Group. | [optional] 
**user_name** | **str** | Name used to log in to the PS Group. | [optional] 
**group_address** | **str** | IP address of the PS Group, which is used for data path communication. If a management address is not configured, this address is also used for management operations. | [optional] 
**last_update_time** | **datetime** | Time when the PS Group was last updated. | [optional] 
**supported_import_type** | [**SupportedImportTypeEnum**](SupportedImportTypeEnum.md) |  Was added in version 1.0.2. | [optional] 
**supported_import_type_l10n** | **str** | Localized message string corresponding to supported_import_type Was added in version 1.0.2. | [optional] 
**import_psgroup_volumes** | [**list[ImportPsgroupVolumeInstance]**](ImportPsgroupVolumeInstance.md) | This is the inverse of the resource type import_psgroup_volume association. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


