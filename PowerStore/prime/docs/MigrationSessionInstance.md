# MigrationSessionInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the migration session instance. | [optional] 
**name** | **str** | User-specified friendly name of the migration session instance.  This property supports case-insensitive filtering. | [optional] 
**resource_type** | [**MigrationResourceTypeEnum**](MigrationResourceTypeEnum.md) |  | [optional] 
**source_appliance_id** | **str** | Unique identifier of the source appliance instance. | [optional] 
**family_id** | **str** | Family identifier designating the storage resource or resources being migrated. For volume or virtual_volume migrations, the family is moved together because they share data among the primary object, snapshots, and clones. For volume_group migration, the family of each volume in the group is moved because it is a grouping of volumes. | [optional] 
**destination_appliance_id** | **str** | Unique identifier of the destination appliance instance. | [optional] 
**state** | [**MigrationSessionStateEnum**](MigrationSessionStateEnum.md) |  | [optional] 
**created_timestamp** | **datetime** | Time when the migration session was created. | [optional] 
**last_sync_timestamp** | **datetime** | Time of the last successful sync operation. | [optional] 
**current_transfer_rate** | **int** | Transfer rate of the current sync operation in bytes/sec. | [optional] 
**progress_percentage** | **int** | Progress percentage of the current sync operation. | [optional] 
**estimated_completion_timestamp** | **datetime** | Estimated completion time of the current sync operation. | [optional] 
**resource_type_l10n** | **str** | Localized message string corresponding to resource_type | [optional] 
**state_l10n** | **str** | Localized message string corresponding to state | [optional] 
**virtual_volumes** | [**list[VirtualVolumeInstance]**](VirtualVolumeInstance.md) | This is the inverse of the resource type virtual_volume association. | [optional] 
**volumes** | [**list[VolumeInstance]**](VolumeInstance.md) | This is the inverse of the resource type volume association. | [optional] 
**volume_groups** | [**list[VolumeGroupInstance]**](VolumeGroupInstance.md) | This is the inverse of the resource type volume_group association. | [optional] 
**replication_sessions** | [**list[ReplicationSessionInstance]**](ReplicationSessionInstance.md) | This is the inverse of the resource type replication_session association. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


