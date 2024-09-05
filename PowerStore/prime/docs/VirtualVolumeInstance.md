# VirtualVolumeInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the virtual volume. | [optional] 
**name** | **str** | The name of the virtual volume, based on metadata provided by vSphere.  This property supports case-insensitive filtering. | [optional] 
**size** | **int** | The size of the virtual volume in bytes. | [optional] 
**type** | [**VirtualVolumeTypeEnum**](VirtualVolumeTypeEnum.md) |  | [optional] 
**usage_type** | [**VirtualVolumeUsageTypeEnum**](VirtualVolumeUsageTypeEnum.md) |  | [optional] 
**appliance_id** | **str** | The appliance where the virtual volume resides. | [optional] 
**storage_container_id** | **str** | The storage container where the virtual volume resides. | [optional] 
**io_priority** | [**IoPriorityEnum**](IoPriorityEnum.md) |  | [optional] 
**profile_id** | **str** | The ID of the storage profile governing this virtual volume. | [optional] 
**replication_group_id** | **str** | The unique identifier of the replication group object that this virtual volume belongs to. Was added in version 3.0.0.0. | [optional] 
**creator_type** | [**StorageCreatorTypeEnum**](StorageCreatorTypeEnum.md) |  | [optional] 
**is_readonly** | **bool** | Indicates whether the virtual volume is read-only. | [optional] 
**migration_session_id** | **str** | If the virtual volume is part of a migration activity, the session ID for that migration. | [optional] 
**virtual_machine_uuid** | **str** | UUID of the virtual machine that owns this virtual volume. | [optional] 
**family_id** | **str** | Family id of the virtual volume. This is the id of the primary object at the root of the family tree. For a primary virtual volume this will be the same as the id of the object. For snap-sets and clone vVols it will be set to the source objects family ID. | [optional] 
**parent_id** | **str** | For snapshots and clones, the ID of the parent virtual volume. The parent_id is set when an virtual volume is created and will only change if its parent virtual volume is deleted. | [optional] 
**source_id** | **str** | Id of the virtual volume from which the content has been sourced. Data is sourced from another virtual volume when a snapshot or clone is created, or when a refresh or restore occurs. Only applies to snap and clones. | [optional] 
**source_timestamp** | **datetime** | The source data time-stamp of the virtual volume. | [optional] 
**creation_timestamp** | **datetime** | Timestamp of the moment virtual volume was created at. | [optional] 
**naa_name** | **str** | The NAA name used by hosts for I/O.  This is the VASA equivalent of a LUN&#39;s WWN. Was added in version 3.0.0.0. | [optional] 
**is_replication_destination** | **bool** | Indicates whether virtual volume is replication destination or not. Was added in version 3.0.0.0. | [optional] 
**location_history** | [**list[LocationHistoryInstance]**](LocationHistoryInstance.md) | Filtering on the fields of this embedded resource is not supported. | [optional] 
**protection_policy_id** | **str** | The unique identifier of the protection policy applied to this virtual volume. Was added in version 3.0.0.0. | [optional] 
**nsid** | **int** | NVMe Namespace unique identifier in the NVMe subsystem. Was added in version 3.0.0.0. | [optional] 
**nguid** | **str** | NVMe Namespace globally unique identifier. Was added in version 3.0.0.0. | [optional] 
**type_l10n** | **str** | Localized message string corresponding to type | [optional] 
**usage_type_l10n** | **str** | Localized message string corresponding to usage_type | [optional] 
**io_priority_l10n** | **str** | Localized message string corresponding to io_priority | [optional] 
**creator_type_l10n** | **str** | Localized message string corresponding to creator_type | [optional] 
**appliance** | [**ApplianceInstance**](ApplianceInstance.md) | This is the embeddable reference form of appliance_id attribute. | [optional] 
**storage_container** | [**StorageContainerInstance**](StorageContainerInstance.md) | This is the embeddable reference form of storage_container_id attribute. | [optional] 
**replication_group** | [**ReplicationGroupInstance**](ReplicationGroupInstance.md) | This is the embeddable reference form of replication_group_id attribute. | [optional] 
**migration_session** | [**MigrationSessionInstance**](MigrationSessionInstance.md) | This is the embeddable reference form of migration_session_id attribute. | [optional] 
**parent** | [**VirtualVolumeInstance**](VirtualVolumeInstance.md) | This is the embeddable reference form of parent_id attribute. | [optional] 
**child_virtual_volumes** | [**list[VirtualVolumeInstance]**](VirtualVolumeInstance.md) | This is the inverse of the resource type virtual_volume association. | [optional] 
**source** | [**VirtualVolumeInstance**](VirtualVolumeInstance.md) | This is the embeddable reference form of source_id attribute. | [optional] 
**target_virtual_volumes** | [**list[VirtualVolumeInstance]**](VirtualVolumeInstance.md) | This is the inverse of the resource type virtual_volume association. | [optional] 
**protection_policy** | [**PolicyInstance**](PolicyInstance.md) | This is the embeddable reference form of protection_policy_id attribute. | [optional] 
**host_virtual_volume_mappings** | [**list[HostVirtualVolumeMappingInstance]**](HostVirtualVolumeMappingInstance.md) | This is the inverse of the resource type host_virtual_volume_mapping association. | [optional] 
**virtual_machines** | [**list[VirtualMachineInstance]**](VirtualMachineInstance.md) | List of the virtual_machines that are associated with this virtual_volume. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


