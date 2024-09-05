# ImportXtremioInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the XtremIO storage system that is a source storage system for import. | [optional] 
**name** | **str** | Name of the XtremIO storage system.  This property supports case-insensitive filtering. | [optional] 
**management_address** | **str** | Management address to use for communicating with the XtremIO storage system. The address can be an IPv4 address or FQDN (Fully Qualified Domain Name). | [optional] 
**serial_number** | **str** | Serial number of the XtremIO storage system. | [optional] 
**cluster_guid** | **str** | Cluster GUID of the XtremIO storage system. | [optional] 
**platform** | [**XtremIOPlatformEnum**](XtremIOPlatformEnum.md) |  | [optional] 
**software_version** | **str** | Software version of the XtremIO storage system. | [optional] 
**xms_version** | **str** | Version of the XMS instance that manages the XtremIO storage system. | [optional] 
**supported_import_type** | [**SupportedImportTypeEnum**](SupportedImportTypeEnum.md) |  | [optional] 
**state** | [**XtremIOStateEnum**](XtremIOStateEnum.md) |  | [optional] 
**severity** | [**XtremIOObjectSeverityEnum**](XtremIOObjectSeverityEnum.md) |  | [optional] 
**user_name** | **str** | User account name used to communicate with the XtremIO storage system. | [optional] 
**last_updated_timestamp** | **datetime** | Date and time when the XtremIO storage system details were last updated. These details include the XtremIO storage system and information about its importable volumes and consistency groups. The timestamp is updated when the XtremIO storage system is created and whenever the importable volumes and consistency groups are discovered. | [optional] 
**platform_l10n** | **str** | Localized message string corresponding to platform Was added in version 1.0.2. | [optional] 
**supported_import_type_l10n** | **str** | Localized message string corresponding to supported_import_type Was added in version 1.0.2. | [optional] 
**state_l10n** | **str** | Localized message string corresponding to state Was added in version 1.0.2. | [optional] 
**severity_l10n** | **str** | Localized message string corresponding to severity Was added in version 1.0.2. | [optional] 
**import_xtremio_volumes** | [**list[ImportXtremioVolumeInstance]**](ImportXtremioVolumeInstance.md) | This is the inverse of the resource type import_xtremio_volume association. | [optional] 
**import_xtremio_consistency_groups** | [**list[ImportXtremioConsistencyGroupInstance]**](ImportXtremioConsistencyGroupInstance.md) | This is the inverse of the resource type import_xtremio_consistency_group association. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


