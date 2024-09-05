# BasePerformanceMetricsByInitiator

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initiator_id** | **str** | Reference to the associated initiator for which these metrics were recorded. | [optional] 
**timestamp** | **datetime** | End of sample period. | [optional] 
**read_iops** | **float** | Total read operations per second. | [optional] 
**write_iops** | **float** | Total write operations per second. | [optional] 
**total_iops** | **float** | Total read and write operations per second. | [optional] 
**avg_read_latency** | **float** | Average read latency in microseconds. | [optional] 
**avg_write_latency** | **float** | Average write latency in microseconds. | [optional] 
**avg_latency** | **float** | Average read and write latency in microseconds. | [optional] 
**read_bandwidth** | **float** | Read rate in bytes per second. | [optional] 
**write_bandwidth** | **float** | Write rate in bytes per second. | [optional] 
**total_bandwidth** | **float** | Total data transfer rate in bytes per second. | [optional] 
**avg_read_size** | **float** | Average read size in bytes. | [optional] 
**avg_write_size** | **float** | Average write size in bytes. | [optional] 
**avg_io_size** | **float** | Average size of read and write operations in bytes. | [optional] 
**repeat_count** | **int** | Number of times the metrics are repeated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


