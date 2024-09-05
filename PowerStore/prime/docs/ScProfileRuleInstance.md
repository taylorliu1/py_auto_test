# ScProfileRuleInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the snapshot profile rule. | [optional] 
**expiration** | **int** | Length of time to keep snapshots before deleting them, in minutes. | [optional] 
**frequency** | [**ScScheduleTypeEnum**](ScScheduleTypeEnum.md) | Frequency at which the snapshot will be taken. | [optional] 
**start_date_time** | **datetime** | Date and time when the snapshot will be created. This applies to the value Once in the ScScheduleTypeEnum. | [optional] 
**start_time** | **str** | Time when snapshot creation will start. | [optional] 
**end_time** | **str** | Time when snapshot creation will stop. | [optional] 
**interval** | **int** | Time interval between any two snapshot creations, in minutes. | [optional] 
**month_of_year** | [**list[MonthOfYearEnum]**](MonthOfYearEnum.md) | Months of the year in which a snapshot will be taken. | [optional] 
**week_of_month** | [**list[WeekOfMonthEnum]**](WeekOfMonthEnum.md) | Weeks of the month in which a snapshot will be taken. | [optional] 
**day_of_week** | [**list[DayOfWeekEnum]**](DayOfWeekEnum.md) | Days of the week in which a snapshot will be taken. | [optional] 
**date_of_month** | **list[int]** | Dates of the month in which a snapshot will be taken. | [optional] 
**frequency_l10n** | **str** | Localized message string corresponding to frequency | [optional] 
**month_of_year_l10n** | **list[str]** | Localized message array corresponding to month_of_year | [optional] 
**week_of_month_l10n** | **list[str]** | Localized message array corresponding to week_of_month | [optional] 
**day_of_week_l10n** | **list[str]** | Localized message array corresponding to day_of_week | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


