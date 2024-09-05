# ImportUnitySnapshotScheduleRuleInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the snapshot schedule rule . | [optional] 
**type** | [**UnityScheduleTypeEnum**](UnityScheduleTypeEnum.md) | Type of the snapshot schedule rule. | [optional] 
**minute** | **int** | Snapshot schedule frequency.[0..59]. | [optional] 
**hours** | **list[int]** | Hourly frequency for the snapshot schedule rule.[0..23]. | [optional] 
**days_of_week** | [**list[UnityDayofWeekEnum]**](UnityDayofWeekEnum.md) | Days of the week for which the snapshot schedule rule applies. | [optional] 
**days_of_month** | **list[int]** | Days of the month for which the snapshot schedule rule applies. [1..31]. | [optional] 
**interval** | **int** | Number of days or hours between snaps, depending on the rule type. [1..31]. | [optional] 
**is_auto_delete** | **bool** | Indicates whether the system can automatically delete the snapshot based on pool automatic-deletion thresholds. | [optional] 
**retention_time** | **int** | (Applies when the value of the isAutoDelete attribute is false.) Period of time for which to keep the snapshot, in seconds. | [optional] 
**type_l10n** | **str** | Localized message string corresponding to type | [optional] 
**days_of_week_l10n** | **list[str]** | Localized message array corresponding to days_of_week | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


