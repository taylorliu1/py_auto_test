# ImportVmaxInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the import_vmax resource instance, and of the corresponding remote_system instance. | [optional] 
**symmetrix_id** | **str** | Unique identifier of the VMAX storage system that is a storage system for import. | [optional] 
**management_address** | **str** | Management address to use for communicating with the VMAX storage system. The address can be an IPv4 address, IPv6 address, or FQDN (Fully Qualified Domain Name). | [optional] 
**model** | **str** | Model represent the model of VMAX storage system. | [optional] 
**unisphere_api_version** | **str** | Version of the Unisphere that manages the VMAX storage system. | [optional] 
**is_embedded** | **bool** | The Unisphere is running as embedded or standalone. | [optional] 
**ucode_version** | **str** | Ucode version will be present in this format 5977.1131.1131 for the VMAX storage system. | [optional] 
**supported_import_type** | [**SupportedImportTypeEnum**](SupportedImportTypeEnum.md) |  | [optional] 
**user_name** | **str** | User account name used to communicate with the VMAX storage system. | [optional] 
**last_updated_timestamp** | **datetime** | Date and time when the VMAX storage system details were last updated. These details include the VMAX storage system and information about its importable storage groups. The timestamp is updated when the VMAX storage system is created and whenever the importable storage groups is discovered. | [optional] 
**port** | **int** | Management port of PowerMax/VMAX remote system.  | [optional] 
**supported_import_type_l10n** | **str** | Localized message string corresponding to supported_import_type Was added in version 3.0.0.0. | [optional] 
**import_vmax_volumes** | [**list[ImportVmaxVolumeInstance]**](ImportVmaxVolumeInstance.md) | This is the inverse of the resource type import_vmax_volume association. | [optional] 
**import_vmax_storage_group** | [**list[ImportVmaxStorageGroupInstance]**](ImportVmaxStorageGroupInstance.md) | This is the inverse of the resource type import_vmax_storage_group association. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


