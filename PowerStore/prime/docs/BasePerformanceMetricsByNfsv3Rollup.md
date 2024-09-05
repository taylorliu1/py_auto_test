# BasePerformanceMetricsByNfsv3Rollup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | Unique identifier of the node. | [optional] 
**appliance_id** | **str** | Unique identifier of the appliance. Was added in version 3.0.0.0. | [optional] 
**timestamp** | **datetime** | Time at the beginning of sample period. | [optional] 
**repeat_count** | **int** | Number of consecutive sampling periods during which there were no changes in the metrics values. If the value is omitted from the response, it is 1 (no additional repeats).  | [optional] 
**avg_md_ops** | **float** | Average md operations per second. | [optional] 
**max_failed_md_ops** | **float** | Max failed operations per second. | [optional] 
**avg_failed_md_ops** | **float** | Average failed operations per second. | [optional] 
**avg_md_latency** | **float** | Average md latency per second. | [optional] 
**max_avg_md_latency** | **float** | Maximum average md latency per second. | [optional] 
**max_read_iops** | **float** | Maximum read operations per second. | [optional] 
**avg_read_iops** | **float** | Average read operations per second. | [optional] 
**max_write_iops** | **float** | Maximum write operations per second. | [optional] 
**avg_write_iops** | **float** | Average write operations per second. | [optional] 
**max_total_iops** | **float** | Maximum read and write operations per second. | [optional] 
**avg_total_iops** | **float** | Average read and write operations per second. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


