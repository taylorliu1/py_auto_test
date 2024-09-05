# SnapshotRuleCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Snapshot rule name. Use only AlphaNumeric chars. | 
**interval** | [**NasSnapshotRulesIntervalEnum**](NasSnapshotRulesIntervalEnum.md) |  | [optional] 
**time_of_day** | **str** | Time of the day to take a snapshot, with format \&quot;hh:mm\&quot; in 24 hour time format. Either the interval parameter or the time_of_day parameter may be set, but not both. if time_of_day specified, days_of_week also need to be specified. | [optional] 
**days_of_week** | [**list[NasSnapshotRulesDaysOfWeekEnum]**](NasSnapshotRulesDaysOfWeekEnum.md) | Days of the week on which the rule should be applied. Applies only for rules where the time_of_day parameter is set. | [optional] 
**retention** | **int** | Number of hours since creation of snapshot, must be retained in the system. | [optional] [default to 1]
**type** | [**NasSnapshotRulesTypeEnum**](NasSnapshotRulesTypeEnum.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

