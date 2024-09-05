# SnapshotRuleInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the snapshot rule. | [optional] 
**name** | **str** | Snapshot rule name.  This property supports case-insensitive filtering. | [optional] 
**interval** | [**SnapRuleIntervalEnum**](SnapRuleIntervalEnum.md) |  | [optional] 
**time_of_day** | **str** | Time of the day to take a daily snapshot, with format \&quot;hh:mm\&quot; using a 24 hour clock. Either the interval parameter or the time_of_day parameter will be set, but not both.  | [optional] 
**timezone** | [**TimeZoneEnum**](TimeZoneEnum.md) |  Was added in version 2.0.0.0. | [optional] 
**days_of_week** | [**list[DaysOfWeekEnum]**](DaysOfWeekEnum.md) | Days of the week when the snapshot rule should be applied. Days are determined based on the UTC time zone, unless the time_of_day and timezone properties are set.  | [optional] 
**desired_retention** | **int** | Desired snapshot retention period in hours. The system will retain snapshots for this time period.  | [optional] 
**is_replica** | **bool** | Indicates whether this is a replica of a snapshot rule on a remote system that is the source of a replication session replicating a storage resource to the local system.  | [optional] [default to False]
**is_read_only** | **bool** | Indicates whether this snapshot rule can be modified.  Was added in version 3.0.0.0. | [optional] [default to False]
**managed_by** | [**PolicyManagedByEnum**](PolicyManagedByEnum.md) |  Was added in version 3.0.0.0. | [optional] 
**managed_by_id** | **str** | Unique identifier of the managing entity based on the value of the managed_by property, as shown below:   * User - Empty   * Metro - Unique identifier of the remote system where the policy was assigned.   * Replication - Unique identifier of the source remote system.   * VMware_vSphere - Unique identifier of the owning VMware vSphere/vCenter.  Was added in version 3.0.0.0. | [optional] 
**interval_l10n** | **str** | Localized message string corresponding to interval | [optional] 
**timezone_l10n** | **str** | Localized message string corresponding to timezone Was added in version 2.0.0.0. | [optional] 
**days_of_week_l10n** | **list[str]** | Localized message array corresponding to days_of_week | [optional] 
**managed_by_l10n** | **str** | Localized message string corresponding to managed_by Was added in version 3.0.0.0. | [optional] 
**policies** | [**list[PolicyInstance]**](PolicyInstance.md) | List of the policies that are associated with this snapshot_rule. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


