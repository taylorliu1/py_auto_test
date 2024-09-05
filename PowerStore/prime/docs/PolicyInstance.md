# PolicyInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the policy. | [optional] 
**name** | **str** | Policy name.  This property supports case-insensitive filtering. | [optional] 
**description** | **str** | Policy description. | [optional] 
**type** | [**PolicyTypeEnum**](PolicyTypeEnum.md) |  | [optional] 
**managed_by** | [**PolicyManagedByEnum**](PolicyManagedByEnum.md) |  Was added in version 3.0.0.0. | [optional] 
**managed_by_id** | **str** | Unique identifier of the managing entity based on the value of the managed_by property, as shown below:   * User - Empty   * Metro - Unique identifier of the remote system where the policy was assigned.   * Replication - Unique identifier of the source remote system.   * VMware_vSphere - Unique identifier of the owning VMware vSphere/vCenter. Was added in version 3.0.0.0. | [optional] 
**is_read_only** | **bool** | Indicates whether this policy can be modified.  Was added in version 3.0.0.0. | [optional] [default to False]
**is_replica** | **bool** | Indicates if this is a replica of a policy on a remote system that is the source of a replication session replicating a resource to the local system. A policy of this type is restricted from many operations.  | [optional] [default to False]
**type_l10n** | **str** | Localized message string corresponding to type | [optional] 
**managed_by_l10n** | **str** | Localized message string corresponding to managed_by Was added in version 3.0.0.0. | [optional] 
**virtual_volumes** | [**list[VirtualVolumeInstance]**](VirtualVolumeInstance.md) | This is the inverse of the resource type virtual_volume association. | [optional] 
**virtual_machines** | [**list[VirtualMachineInstance]**](VirtualMachineInstance.md) | This is the inverse of the resource type virtual_machine association. | [optional] 
**volumes** | [**list[VolumeInstance]**](VolumeInstance.md) | This is the inverse of the resource type volume association. | [optional] 
**volume_groups** | [**list[VolumeGroupInstance]**](VolumeGroupInstance.md) | This is the inverse of the resource type volume_group association. | [optional] 
**nas_servers** | [**list[NasServerInstance]**](NasServerInstance.md) | This is the inverse of the resource type nas_server association. | [optional] 
**file_systems** | [**list[FileSystemInstance]**](FileSystemInstance.md) | This is the inverse of the resource type file_system association. | [optional] 
**performance_rules** | [**list[PerformanceRuleInstance]**](PerformanceRuleInstance.md) | List of the performance_rules that are associated with this policy. | [optional] 
**snapshot_rules** | [**list[SnapshotRuleInstance]**](SnapshotRuleInstance.md) | List of the snapshot_rules that are associated with this policy. | [optional] 
**replication_rules** | [**list[ReplicationRuleInstance]**](ReplicationRuleInstance.md) | List of the replication_rules that are associated with this policy. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


