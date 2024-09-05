# ReplicationRuleInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the replication rule. | [optional] 
**name** | **str** | Name of the replication rule.  This property supports case-insensitive filtering. | [optional] 
**rpo** | [**RPOEnum**](RPOEnum.md) |  | [optional] 
**remote_system_id** | **str** | Unique identifier of the remote system to which this replication rule will replicate the associated storage resources.  | [optional] 
**is_replica** | **bool** | Indicates whether this is a replica of a replication rule on a remote system that is the source of a replication session replicating a storage resource to the local system.  | [optional] [default to False]
**is_read_only** | **bool** | Indicates whether this replication rule can be modified.  Was added in version 3.0.0.0. | [optional] [default to False]
**alert_threshold** | **int** | Number of minutes the system will wait before generating a compliance alert when a replication session does not meet the RPO. By default, this will be set to the number of minutes in the configured RPO.  | [optional] 
**managed_by** | [**PolicyManagedByEnum**](PolicyManagedByEnum.md) |  Was added in version 3.0.0.0. | [optional] 
**managed_by_id** | **str** | Unique identifier of the managing entity based on the value of the managed_by property, as shown below:   * User - Empty   * Metro - Unique identifier of the remote system where the policy was assigned.   * Replication - Unique identifier of the source remote system.   * VMware_vSphere - Unique identifier of the owning VMware vSphere/vCenter.  Was added in version 3.0.0.0. | [optional] 
**rpo_l10n** | **str** | Localized message string corresponding to rpo | [optional] 
**managed_by_l10n** | **str** | Localized message string corresponding to managed_by Was added in version 3.0.0.0. | [optional] 
**replication_sessions** | [**list[ReplicationSessionInstance]**](ReplicationSessionInstance.md) | This is the inverse of the resource type replication_session association. | [optional] 
**policies** | [**list[PolicyInstance]**](PolicyInstance.md) | List of the policies that are associated with this replication_rule. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


