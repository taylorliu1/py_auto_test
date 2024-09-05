# FileImportNasServerInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the NAS Server for the file import connection. | [optional] 
**name** | **str** | Name of the NAS Server for the file import connection.  This property supports case-insensitive filtering. | [optional] 
**protocol_type** | [**FileImportNasServerProtocolTypeEnum**](FileImportNasServerProtocolTypeEnum.md) |  | [optional] 
**importable_criteria** | [**FileImportNasServerImportableCriteriaEnum**](FileImportNasServerImportableCriteriaEnum.md) |  | [optional] 
**remote_system_id** | **str** | Unique identifier of the remote system where the NAS Server exists. | [optional] 
**smb_server** | [**FileImportSmbConfiguration**](FileImportSmbConfiguration.md) |  | [optional] 
**file_systems** | [**FileImportSourceFilesystem**](FileImportSourceFilesystem.md) |  | [optional] 
**file_interfaces** | [**FileImportSourceNetworkInterface**](FileImportSourceNetworkInterface.md) |  | [optional] 
**non_importable_reasons** | **str** | Non importable reason of the source NAS Server. | [optional] 
**protocol_type_l10n** | **str** | Localized message string corresponding to protocol_type Was added in version 3.0.0.0. | [optional] 
**importable_criteria_l10n** | **str** | Localized message string corresponding to importable_criteria Was added in version 3.0.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


