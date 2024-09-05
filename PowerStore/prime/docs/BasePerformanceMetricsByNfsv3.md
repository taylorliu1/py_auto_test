# BasePerformanceMetricsByNfsv3

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | Unique identifier of the nfs. | [optional] 
**appliance_id** | **str** | Unique identifier of the appliance. Was added in version 3.0.0.0. | [optional] 
**timestamp** | **datetime** | End of sample period. | [optional] 
**repeat_count** | **int** | Number of consecutive sampling periods during which there were no changes in the metrics values. If the value is omitted from the response, it is 1 (no additional repeats).  | [optional] 
**md_ops** | **float** | Total md operations per second. | [optional] 
**failed_md_ops** | **float** | Total failed md operations per second. | [optional] 
**avg_md_latency** | **float** | Average md latency operations per second. | [optional] 
**read_iops** | **float** | Total read iops in microseconds. | [optional] 
**write_iops** | **float** | Total write iops in microseconds. | [optional] 
**total_iops** | **float** | Total read and write iops in microseconds. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


