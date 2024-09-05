# SnapshotRuleInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the snapshot rule. | [optional] 
**name** | **str** | Snapshot rule name. Use only AlphaNumeric chars. | [optional] 
**interval** | [**NasSnapshotRulesIntervalEnum**](NasSnapshotRulesIntervalEnum.md) |  | [optional] 
**time_of_day** | **str** | Time of the day to take a snapshot, with UTC format \&quot;hh:mm\&quot; in 24 hour time format. Either the interval parameter or the time_of_day parameter will be set, but no both. if time_of_day specified, days_of_week also need to be specified. | [optional] 
**days_of_week** | [**list[NasSnapshotRulesDaysOfWeekEnum]**](NasSnapshotRulesDaysOfWeekEnum.md) | Days of the week when the rule should be applied. | [optional] 
**retention** | **int** | No. of hours since creation, snapshot must be retained in the system. | [optional] 
**type** | [**NasSnapshotRulesTypeEnum**](NasSnapshotRulesTypeEnum.md) |  | [optional] 
**interval_l10n** | **str** | Localized message string corresponding to interval | [optional] 
**days_of_week_l10n** | **list[str]** | Localized message array corresponding to days_of_week | [optional] 
**type_l10n** | **str** | Localized message string corresponding to type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

