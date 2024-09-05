# VolumeInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the volume instance. | [optional] 
**name** | **str** | Name of the volume. This value must contain 128 or fewer printable Unicode characters.  This property supports case-insensitive filtering. | [optional] 
**description** | **str** | Description of the volume. This value must contain 128 or fewer printable Unicode characters. | [optional] 
**type** | [**VolumeTypeEnum**](VolumeTypeEnum.md) |  | [optional] 
**wwn** | **str** | World wide name of the volume. | [optional] 
**nsid** | **int** | NVMe Namespace unique identifier in the NVME subsystem. Used for volumes attached to NVMEoF hosts. Was added in version 2.0.0.0. | [optional] 
**nguid** | **str** | NVMe Namespace globally unique identifier. Used for volumes attached to NVMEoF hosts. Was added in version 2.0.0.0. | [optional] 
**appliance_id** | **str** | Unique identifier of the appliance on which the volume is provisioned. | [optional] 
**state** | [**VolumeStateEnum**](VolumeStateEnum.md) |  | [optional] 
**size** | **int** |  Size of the volume in bytes. Minimum volume size is 1MB. Maximum volume size is 256TB. Size must be a multiple of 8192. | [optional] 
**logical_used** | **int** | Current amount of data (in bytes) host has written to a volume without dedupe, compression or sharing. This metric applies to primaries, snaps and clones. The value is null initially when a volume is created and is collected at 5 minute intervals. Was added in version 3.0.0.0. | [optional] 
**node_affinity** | [**NodeAffinityEnum**](NodeAffinityEnum.md) | Node affinity.  Node which offers optimized IO for volume, values are: | [optional] 
**creation_timestamp** | **datetime** | Time when the volume was created. | [optional] 
**protection_policy_id** | **str** | Unique identifier of the protection policy assigned to the volume. Only applicable to primary and clone volumes. | [optional] 
**performance_policy_id** | **str** | Unique identifier of the performance policy assigned to the volume. | [optional] 
**is_replication_destination** | **bool** | Indicates whether this volume is a replication destination. This field is false on both ends when a volume is a metro volume. Areplication destination will be created by the system when a replication session is created. When there is an active replication session, all the user operations are restricted including modification, deletion, host operation, snapshot, clone, etc. After the replication session is deleted, the replication destination volume will remain as it is until the end user changes it to be a non-replication destination. After the change, it becomes a primary volume. If the end user keeps it as a replication destination, when the replication session is recreated, the replication destination volume could potentially be reused in the new session to avoid a time-consuming full sync. This property is only valid for primary and clone volumes. | [optional] [default to False]
**migration_session_id** | **str** | Unique identifier of the migration session assigned to the volume if it is part of a migration activity. | [optional] 
**metro_replication_session_id** | **str** | Unique identifier of the replication session assigned to the volume if it has been configured as a metro volume between two PowerStore clusters. The volume can only be modified, refreshed, or restored when the metro_replication_session is in the paused state. Was added in version 3.0.0.0. | [optional] 
**is_host_access_available** | **bool** | Indicates whether the volume is available to host. This attribute is only applicable to primary volumes and clones. Was added in version 3.0.0.0. | [optional] 
**protection_data** | [**ProtectionDataInstance**](ProtectionDataInstance.md) |  | [optional] 
**location_history** | [**list[LocationHistoryInstance]**](LocationHistoryInstance.md) | Filtering on the fields of this embedded resource is not supported. | [optional] 
**app_type** | [**AppTypeEnum**](AppTypeEnum.md) |  Was added in version 2.1.0.0. | [optional] 
**app_type_other** | **str** | An optional field used to describe application type usage for a volume. This field can only be set if app_type is set to Relational_Databases_Other, Big_Data_Analytics_Other, Business_Applications_Other, Healthcare_Other, Virtualization_Other or Other. If the app_type attribute is set to anything other than one of these values, the attribute will be cleared. Was added in version 2.1.0.0. | [optional] 
**type_l10n** | **str** | Localized message string corresponding to type | [optional] 
**state_l10n** | **str** | Localized message string corresponding to state | [optional] 
**node_affinity_l10n** | **str** | Localized message string corresponding to node_affinity | [optional] 
**app_type_l10n** | **str** | Localized message string corresponding to app_type Was added in version 2.1.0.0. | [optional] 
**appliance** | [**ApplianceInstance**](ApplianceInstance.md) | This is the embeddable reference form of appliance_id attribute. | [optional] 
**protection_policy** | [**PolicyInstance**](PolicyInstance.md) | This is the embeddable reference form of protection_policy_id attribute. | [optional] 
**migration_session** | [**MigrationSessionInstance**](MigrationSessionInstance.md) | This is the embeddable reference form of migration_session_id attribute. | [optional] 
**mapped_volumes** | [**list[HostVolumeMappingInstance]**](HostVolumeMappingInstance.md) | This is the inverse of the resource type host_volume_mapping association. | [optional] 
**volume_groups** | [**list[VolumeGroupInstance]**](VolumeGroupInstance.md) | List of the volume_groups that are associated with this volume. | [optional] 
**datastores** | [**list[DatastoreInstance]**](DatastoreInstance.md) | List of the datastores that are associated with this volume. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


