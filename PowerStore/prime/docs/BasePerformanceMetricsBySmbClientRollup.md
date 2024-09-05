# BasePerformanceMetricsBySmbClientRollup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | Unique identifier of the node. | [optional] 
**appliance_id** | **str** | Unique identifier of the appliance. Was added in version 3.0.0.0. | [optional] 
**timestamp** | **datetime** | Time at the beginning of sample period. | [optional] 
**repeat_count** | **int** | Number of consecutive sampling periods during which there were no changes in the metrics values. If the value is omitted from the response, it is 1 (no additional repeats).  | [optional] 
**avg_read_iops** | **float** | Average read operations per second. | [optional] 
**avg_write_iops** | **float** | Average write operations per second. | [optional] 
**avg_iops** | **float** | Average read and write operations per second. | [optional] 
**avg_calls** | **float** | Average calls. | [optional] 
**max_read_iops** | **float** | Maximum read operations per second. | [optional] 
**max_write_iops** | **float** | Maximum write operations per second. | [optional] 
**max_iops** | **float** | Maximum read and write operations per second. | [optional] 
**max_calls** | **float** | Maximum calls. | [optional] 
**avg_read_latency** | **float** | Maximum read latency in microseconds. | [optional] 
**avg_write_latency** | **float** | Maximum write latency in microseconds. | [optional] 
**avg_latency** | **float** | Maximum read and write latency in microseconds. | [optional] 
**max_avg_read_latency** | **float** | Maximum of average read latency in microseconds. | [optional] 
**max_avg_write_latency** | **float** | Maximum of average write latency in microseconds. | [optional] 
**max_avg_latency** | **float** | Maximum of average read and write latency in microseconds. | [optional] 
**avg_read_size** | **float** | Average read size in bytes. | [optional] 
**avg_write_size** | **float** | Average write size in bytes. | [optional] 
**avg_io_size** | **float** | Average read and write size in bytes. | [optional] 
**max_avg_read_size** | **float** | Maximum of average read size in bytes. | [optional] 
**max_avg_write_size** | **float** | Maximum of average write size in bytes. | [optional] 
**max_avg_size** | **float** | Maximum of average read and write size in bytes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


