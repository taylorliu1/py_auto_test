# SnapshotRuleCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the snapshot rule. | 
**interval** | [**SnapRuleIntervalEnum**](SnapRuleIntervalEnum.md) |  | [optional] 
**time_of_day** | **str** | Time of the day to take a daily snapshot, with format \&quot;hh:mm\&quot; using a 24 hour clock. Either the interval parameter or the time_of_day parameter may be set, but not both.  | [optional] 
**timezone** | [**TimeZoneEnum**](TimeZoneEnum.md) |  Was added in version 2.0.0.0. | [optional] 
**days_of_week** | [**list[DaysOfWeekEnum]**](DaysOfWeekEnum.md) | Days of the week when the snapshot rule should be applied. Days are determined based on the UTC time zone, unless the time_of_day and timezone properties are set.  | [optional] 
**desired_retention** | **int** | Desired snapshot retention period in hours. The system will retain snapshots for this time period.  | 
**is_read_only** | **bool** | Indicates whether this snapshot rule can be modified.  Was added in version 3.0.0.0. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


