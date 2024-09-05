# ImportXtremioSnapshotScheduleRetentionPolicyInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the snapshot schedule retention policy. | [optional] 
**name** | **str** | The name of the Retention Policy. | [optional] 
**short_period_duration** | **int** | The duration of the short term period ranging from 1 to 500. | [optional] 
**short_period_unit** | [**XtremIODurationUnitEnum**](XtremIODurationUnitEnum.md) |  | [optional] 
**short_retention_copies** | **int** | The short term retention number of copies ranging from 1 to 500. The value of 0 indicates that this period is not in use. | [optional] 
**middle_period_duration** | **int** | The duration of the middle term period ranging from 1 to 500. | [optional] 
**middle_period_unit** | [**XtremIODurationUnitEnum**](XtremIODurationUnitEnum.md) |  | [optional] 
**middle_retention_copies** | **int** | The middle term retention number of copies ranging from 1 to 500. The value of 0 indicates that this period is not in use. | [optional] 
**long_period_duration** | **int** | The duration of the long term period ranging from 1 to 500. | [optional] 
**long_period_unit** | [**XtremIODurationUnitEnum**](XtremIODurationUnitEnum.md) |  | [optional] 
**long_retention_copies** | **int** | The long term retention number of copies ranging from 1 to 500. The value of 0 indicates that this period is not in use. | [optional] 
**short_period_unit_l10n** | **str** | Localized message string corresponding to short_period_unit Was added in version 1.0.2. | [optional] 
**middle_period_unit_l10n** | **str** | Localized message string corresponding to middle_period_unit Was added in version 1.0.2. | [optional] 
**long_period_unit_l10n** | **str** | Localized message string corresponding to long_period_unit Was added in version 1.0.2. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


