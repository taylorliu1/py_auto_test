# ImportSessionInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the import session. | [optional] 
**type** | [**ImportSessionTypeEnum**](ImportSessionTypeEnum.md) |  Was added in version 1.0.2. | [optional] 
**name** | **str** | User-specified name of the import session.  This property supports case-insensitive filtering. | [optional] 
**global_storage_discovery_address** | **str** | Global storage discovery iSCSI ip address that will be used for import workflow. The address can be an IPv4 address or FQDN (Fully Qualified Domain Name). Was added in version 3.0.0.0. | [optional] 
**description** | **str** | User-specified description of the import session. | [optional] 
**remote_system_id** | **str** | Unique identifier of the storage system that contains the source volume or consistency group to be imported. | [optional] 
**source_resource_id** | **str** | Unique identifier of the volume or consistency group to be imported. | [optional] 
**destination_resource_id** | **str** | Unique identifier of the destination volume or volume group created as part of the import process. | [optional] 
**destination_resource_type** | [**ImportDestinationResourceTypeEnum**](ImportDestinationResourceTypeEnum.md) |  | [optional] 
**parent_session_id** | **str** | For a volume that is part of a consistency group import, this value is the session identifier of the import session. For an individual volume import, this value is null. | [optional] 
**state** | [**ImportSessionStateEnum**](ImportSessionStateEnum.md) |  | [optional] 
**estimated_completion_timestamp** | **datetime** | When the import is in the Copy_In_Progress state, this value indicates the estimated time at which the data copy will complete. Before the import is in the Copy_In_Progress state, the value is null. | [optional] 
**progress_percentage** | **int** | When the import is in the Copy_In_Progress state, this value indicates the completion percent for the import. Before the import is in the Copy_In_Progress state, this value is 0. After the cutover or if there is a failure, this value is null. | [optional] 
**average_transfer_rate** | **int** | Average transfer rate of a data import operation in bytes/sec over the whole copy period. Before and after the import is in the Copy_In_Progress state, this value is null. | [optional] 
**current_transfer_rate** | **int** | Current transfer rate of a data import operation in bytes/sec. Before and after the import is in the Copy_In_Progress state, this value is null. | [optional] 
**protection_policy_id** | **str** | Unique identifier of the local protection policy in the PowerStore storage system that will be applied on an imported destination volume or consistency group after cutover. Only snapshot policies are supported in an import. Once the import completes, you can add a replication policy. | [optional] 
**volume_group_id** | **str** | Unique identifier of the volume group to which the destination volume will be added, if any. | [optional] 
**automatic_cutover** | **bool** | Indicates whether the import session cutover is manual (true) or automatic (false). | [optional] [default to False]
**scheduled_timestamp** | **datetime** | Date and time at which the import session is scheduled to run. The date is specified in ISO 8601 format with the time expressed in UTC format. | [optional] 
**error** | [**ErrorInstance**](ErrorInstance.md) |  | [optional] 
**last_update_timestamp** | **datetime** | Date and time when was the import was last updated. This value is updated each time the import job updates. | [optional] 
**type_l10n** | **str** | Localized message string corresponding to type Was added in version 1.0.2. | [optional] 
**destination_resource_type_l10n** | **str** | Localized message string corresponding to destination_resource_type | [optional] 
**state_l10n** | **str** | Localized message string corresponding to state | [optional] 
**remote_system** | [**RemoteSystemInstance**](RemoteSystemInstance.md) | This is the embeddable reference form of remote_system_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


