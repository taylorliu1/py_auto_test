# BaseCopyMetricsByVg

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | End of sampling period. | [optional] 
**repeat_count** | **int** | Number of consecutive sampling periods during which there were no changes in the metrics values. If the value is omitted from the response, it is 1 (no additional repeats).  | [optional] 
**session_type** | [**CopySessionTypeEnum**](CopySessionTypeEnum.md) |  | [optional] 
**vg_id** | **str** | Unique identifier of the volume group. | [optional] 
**data_transferred** | **int** | Number of bytes transferred during this sampling period. | [optional] 
**data_remaining** | **int** | Number of bytes remaining to be copied at the end of this sampling period. | [optional] 
**transfer_time** | **int** | The time (in milliseconds) spent in copy activity during this sampling period.  | [optional] 
**transfer_rate** | **float** | Data transfer rate (in bytes/second) computed using data_transferred and transfer_time.  | [optional] 
**read_time** | **int** | Time (in milliseconds) spent doing reads during this sampling period.  | [optional] 
**write_time** | **int** | Time (in milliseconds) spent doing writes during this sampling period.  | [optional] 
**session_type_l10n** | **str** | Localized message string corresponding to session_type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


