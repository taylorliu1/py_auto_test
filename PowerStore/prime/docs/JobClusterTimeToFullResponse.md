# JobClusterTimeToFullResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | Unique ID of the cluster. | [optional] 
**end_of_forecast** | **datetime** | Timestamp of the end of the capacity forecast. If time to full estimates are null, the relevant forecast does not reach full capacity before it ends.  In this case the end of the forecast can be used as a minimum for time to full.  | [optional] 
**time_to_full** | **datetime** | Estimated date-time at which the forecast value will reach full capacity. | [optional] 
**time_to_full_pessimistic** | **datetime** | Pessimistic date-time for time to full based on the upper bound of the forecast 95% confidence interval. | [optional] 
**time_to_full_optimistic** | **datetime** | Optimistic date-time for time to full based on the lower bound of the forecast 95% confidence interval. | [optional] 
**time_to_full_status** | [**ForecastTimeToFullStatusEnum**](ForecastTimeToFullStatusEnum.md) |  | [optional] 
**time_to_full_status_l10n** | **str** | Localized message string corresponding to time_to_full_status | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


