# PerformanceMetricsSmbBuiltinclientByNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | Unique identifier of the node. | [optional] 
**appliance_id** | **str** | Unique identifier of the appliance. Was added in version 3.0.0.0. | [optional] 
**timestamp** | **datetime** | End of sample period. | [optional] 
**repeat_count** | **int** | Number of consecutive sampling periods during which there were no changes in the metrics values. If the value is omitted from the response, it is 1 (no additional repeats).  | [optional] 
**read_iops** | **float** | Total read operations per second. | [optional] 
**write_iops** | **float** | Total write operations per second. | [optional] 
**total_iops** | **float** | Total read and write operations per second. | [optional] 
**total_calls** | **float** | Total calls. | [optional] 
**avg_read_latency** | **float** | Average read latency in microseconds. | [optional] 
**avg_write_latency** | **float** | Average write latency in microseconds. | [optional] 
**avg_latency** | **float** | Average read and write latency in microseconds. | [optional] 
**avg_read_size** | **float** | Average read size in bytes. | [optional] 
**avg_write_size** | **float** | Average write size in bytes. | [optional] 
**avg_io_size** | **float** | Average read and write size in bytes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


