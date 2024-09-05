# ReplicationGroupInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the Replication Group instance. | [optional] 
**storage_container_id** | **str** | The storage container where the replication group resides. | [optional] 
**name** | **str** | Name of the Replication Group.  This property supports case-insensitive filtering. | [optional] 
**description** | **str** | Description of the Replication Group. | [optional] 
**creator_type** | [**StorageCreatorTypeEnum**](StorageCreatorTypeEnum.md) |  | [optional] 
**creation_timestamp** | **datetime** | Timestamp when given replication group was created. | [optional] 
**is_replication_destination** | **bool** | Indicates whether replication group is replication destination or not. | [optional] [default to False]
**creator_type_l10n** | **str** | Localized message string corresponding to creator_type Was added in version 3.0.0.0. | [optional] 
**virtual_volumes** | [**list[VirtualVolumeInstance]**](VirtualVolumeInstance.md) | This is the inverse of the resource type virtual_volume association. | [optional] 
**storage_container** | [**StorageContainerInstance**](StorageContainerInstance.md) | This is the embeddable reference form of storage_container_id attribute. | [optional] 
**parent** | [**ReplicationGroupInstance**](ReplicationGroupInstance.md) | This is the embeddable reference form of parent_id attribute. | [optional] 
**child_replication_groups** | [**list[ReplicationGroupInstance]**](ReplicationGroupInstance.md) | This is the inverse of the resource type replication_group association. | [optional] 
**source** | [**ReplicationGroupInstance**](ReplicationGroupInstance.md) | This is the embeddable reference form of source_id attribute. | [optional] 
**target_replication_groups** | [**list[ReplicationGroupInstance]**](ReplicationGroupInstance.md) | This is the inverse of the resource type replication_group association. | [optional] 
**virtual_machines** | [**list[VirtualMachineInstance]**](VirtualMachineInstance.md) | This is the inverse of the resource type virtual_machine association. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


