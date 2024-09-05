# BasePerformanceMetricsFileByClusterRollup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | Time at the beginning of sample period. | [optional] 
**repeat_count** | **int** | Number of consecutive sampling periods during which there were no changes in the metrics values. If the value is omitted from the response, it is 1 (no additional repeats).  | [optional] 
**avg_read_iops** | **float** | Average read operations per second. | [optional] 
**avg_write_iops** | **float** | Average write operations per second. | [optional] 
**avg_total_iops** | **float** | Average read and write operations per second. | [optional] 
**max_read_iops** | **float** | Maximum read operations per second. | [optional] 
**max_write_iops** | **float** | Maximum write operations per second. | [optional] 
**max_iops** | **float** | Maximum read and write operations per second. | [optional] 
**avg_read_bandwidth** | **float** | Average read rate in bytes per second. | [optional] 
**avg_write_bandwidth** | **float** | Average write rate in bytes per second. | [optional] 
**avg_total_bandwidth** | **float** | Average data transfer rate in bytes per second. | [optional] 
**max_read_bandwidth** | **float** | Maximum read rate in bytes per second. | [optional] 
**max_write_bandwidth** | **float** | Maximum write rate in bytes per second. | [optional] 
**max_total_bandwidth** | **float** | Maximum data transfer rate in bytes per second. | [optional] 
**avg_read_latency** | **float** | Maximum of average read latency in microseconds. | [optional] 
**avg_write_latency** | **float** | Maximum of average write latency in microseconds. | [optional] 
**avg_latency** | **float** | Maximum of average read and write latency in microseconds. | [optional] 
**max_avg_read_latency** | **float** | Maximum of average read latency in microseconds. | [optional] 
**max_avg_write_latency** | **float** | Maximum of average write latency in microseconds. | [optional] 
**max_avg_latency** | **float** | Maximum of average read and write latency in microseconds. | [optional] 
**avg_read_size** | **float** | Average read size in bytes. | [optional] 
**avg_write_size** | **float** | Average write size in bytes. | [optional] 
**avg_io_size** | **float** | Average read and write size in bytes. | [optional] 
**max_avg_read_size** | **float** | Maximum of average read size in bytes. | [optional] 
**max_avg_write_size** | **float** | Maximum of average write size in bytes. | [optional] 
**max_avg_io_size** | **float** | Maximum of average read and write size in bytes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


