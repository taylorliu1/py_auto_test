# FileImportSessionInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the file import session. | [optional] 
**name** | **str** | User-specified name of the file import session.  This property supports case-insensitive filtering. | [optional] 
**description** | **str** | User-specified description of the file import session. | [optional] 
**remote_system_id** | **str** | Unique identifer of the storage system that contains the source NAS Server to be imported. | [optional] 
**source_resource_id** | **str** | Unique identifier of the source NAS server which is being imported by the file import session. | [optional] 
**destination_resource_id** | **str** | Unique identifier of the destination NAS server or filesystem created as part of the import process. | [optional] 
**destination_resource_type** | [**FileImportDestinationResourceTypeEnum**](FileImportDestinationResourceTypeEnum.md) |  | [optional] 
**import_file_interface_id** | **str** | Unique identifier of the destination file interface used for importing data from the source system. | [optional] 
**nas_server_id** | **str** | Unique identifier of the destination NAS server to which the destination filesystem will be added. | [optional] 
**last_update_timestamp** | **datetime** | The Date and time when the import session has been updated. This date is sepcified in ISO 8601 format with time expressed in UTC. | [optional] 
**scheduled_timestamp** | **datetime** | Indicates the Date and time at which the file import session is scheduled to run. The date is specified in ISO 8601 format with the time expressed in UTC format. | [optional] 
**state** | [**FileImportSessionStateEnum**](FileImportSessionStateEnum.md) |  | [optional] 
**current_operation** | [**FileImportSessionCurrentOperationEnum**](FileImportSessionCurrentOperationEnum.md) |  | [optional] 
**current_operation_progress_percentage** | **int** | When the import is in the &#39;Initial_Copy_In_Progress&#39; or &#39;Incremental_Copy_In_Progress&#39; state, this value indicates the completion percent for the import. Before the import is in the copy state, this value is 0. After the cutover or if there is a failure, this value is null. | [optional] 
**estimated_completion_timestamp** | **int** | When the import is in the &#39;Initial_Copy_In_Progress&#39; or &#39;Incremental_Copy_In_Progress&#39; state, this value indicates the estimated time at which the data copy will complete. Before the import is in the copy state, the value is null. | [optional] 
**protection_policy_id** | **str** | Unique identifier of the local protection policy in the PowerStore storage system that will be applied on an imported destination NAS server or filesystem after commit. Only snapshot policies are supported in an import. Once the import completes, you can add a replication policy. | [optional] 
**source_smb_admin_username** | **str** | User name for authentication to SMB Server on the source NAS Server with administrator previlege. | [optional] 
**source_dhsm_username** | **str** | The username for authentication to DHSM Server on the source NAS Server required for importing FLR filesystems. | [optional] 
**error** | **str** | File Import Session error. | [optional] 
**destination_resource_type_l10n** | **str** | Localized message string corresponding to destination_resource_type Was added in version 3.0.0.0. | [optional] 
**state_l10n** | **str** | Localized message string corresponding to state Was added in version 3.0.0.0. | [optional] 
**current_operation_l10n** | **str** | Localized message string corresponding to current_operation Was added in version 3.0.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


