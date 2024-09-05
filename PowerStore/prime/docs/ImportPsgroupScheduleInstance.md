# ImportPsgroupScheduleInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the snapshot schedule. | [optional] 
**type** | [**ImportPsgroupScheduleTypeEnum**](ImportPsgroupScheduleTypeEnum.md) |  | [optional] 
**active_date** | **int** | Number of days for which the snapshot schedule has been active. | [optional] 
**inactive_date** | **int** | Number of days for which the snapshot schedule has been inactive. | [optional] 
**repetition_interval** | **int** | Repeat interval of the snapshot schedule, in days. The value is 1 for the schedule frequencies Once and Hourly. It can be greater than 1 for the schedule frequencies Daily and Weekly. | [optional] 
**start_time** | **int** | Time when snapshot creation begins each day, in minutes. | [optional] 
**end_time** | **int** | Time when snapshot creation ends each day, in minutes. | [optional] 
**frequency** | **int** | Frequency at which snapshots are created, in minutes. | [optional] 
**status** | [**ImportPsgroupScheduleStatusEnum**](ImportPsgroupScheduleStatusEnum.md) |  | [optional] 
**keep_count** | **int** | Number of snapshots to retain. | [optional] 
**type_l10n** | **str** | Localized message string corresponding to type | [optional] 
**status_l10n** | **str** | Localized message string corresponding to status | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


