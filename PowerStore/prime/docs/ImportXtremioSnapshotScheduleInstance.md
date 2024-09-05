# ImportXtremioSnapshotScheduleInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the XtremIO snapshot schedule. | [optional] 
**name** | **str** | Name of the XtremIO snapshot schedule. | [optional] 
**state** | [**XtremIOScheduleStateEnum**](XtremIOScheduleStateEnum.md) |  | [optional] 
**schedule_type** | [**XtremIOScheduleTypeEnum**](XtremIOScheduleTypeEnum.md) |  | [optional] 
**schedule** | **str** | For schedule_type of interval, a triplet in the form of &#39;[hours : minutes : seconds&#39;], where a schedule using hours and minutes must have a seconds value of 0 and a schedule in seconds must have hours and minutes of 0. For example, &#39;[1:30:0&#39;] takes a snapshot every 1.5 hours and &#39;[0:0:15&#39;] takes a snapshot every 15 seconds.  â¢ For schedule_type of explicit, a triplet in the form of &#39;[day-of-week : hour : minute&#39;], where day-of week values 0 is every day, 1 is Sunday, 2 is Monday, 3 is Tuesday, 4 is Wednesday, 5 is Thursday, and 6 is Saturday (for example, &#39;[1:12:30&#39;] takes a snapshot on Sunday at 12:30, and &#39;[0:12:30&#39;] takes a snapshot every day at 12:30.  | [optional] 
**snapshots_to_keep_time** | **int** | The time period, in seconds, for which a Snapshot is retained. When the defined time has passed, the snapshot is automatically removed.  â¢ Minimum value is 60 (1 minute).  â¢ Maximum value is 15768000 (5 Years). This value is present if the retention_policy is not present. | [optional] 
**snapshots_to_keep_number** | **int** | Defines the number of Snapshots to be saved. This value is present if the retention_policy is not present. | [optional] 
**retention_policy** | [**ImportXtremioSnapshotScheduleRetentionPolicyInstance**](ImportXtremioSnapshotScheduleRetentionPolicyInstance.md) |  | [optional] 
**state_l10n** | **str** | Localized message string corresponding to state Was added in version 1.0.2. | [optional] 
**schedule_type_l10n** | **str** | Localized message string corresponding to schedule_type Was added in version 1.0.2. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


