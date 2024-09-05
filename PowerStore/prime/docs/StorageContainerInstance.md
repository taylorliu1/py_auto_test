# StorageContainerInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of the storage container. | [optional] 
**name** | **str** | Name for the storage container.  This should be unique across all storage containers in the cluster. Name can be from 1 to 64 UTF-8 characters, and not more than 127 bytes.  This property supports case-insensitive filtering. | [optional] 
**quota** | **int** | The total number of bytes that can be provisioned/reserved against this storage container.  A value of 0 means there is no limit.  It is possible to set the quota to a value that overprovisions the amount of space available in the system. | [optional] 
**storage_protocol** | [**StorageContainerStorageProtocolEnum**](StorageContainerStorageProtocolEnum.md) |  Was added in version 3.0.0.0. | [optional] 
**storage_protocol_l10n** | **str** | Localized message string corresponding to storage_protocol Was added in version 3.0.0.0. | [optional] 
**virtual_volumes** | [**list[VirtualVolumeInstance]**](VirtualVolumeInstance.md) | This is the inverse of the resource type virtual_volume association. | [optional] 
**replication_groups** | [**list[ReplicationGroupInstance]**](ReplicationGroupInstance.md) | This is the inverse of the resource type replication_group association. | [optional] 
**datastores** | [**list[DatastoreInstance]**](DatastoreInstance.md) | This is the inverse of the resource type datastore association. | [optional] 
**destinations** | [**list[StorageContainerDestinationInstance]**](StorageContainerDestinationInstance.md) | This is the inverse of the resource type storage_container_destination association. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


