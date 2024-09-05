# PerformanceMetricsByAppliance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appliance_id** | **str** | Unique identifier representing a specific appliance. | [optional] 
**timestamp** | **datetime** | End of sample period. | [optional] 
**avg_read_latency** | **float** | Average read latency in microseconds. | [optional] 
**avg_read_size** | **float** | Average read size in bytes. | [optional] 
**avg_mirror_overhead_latency** | **float** | Average additional latency incurred on the source in order to do the remote mirror writes in microseconds. This applies to metro volumes in the active-active state. Was added in version 3.0.0.0. | [optional] 
**avg_latency** | **float** | Average read and write latency in microseconds. | [optional] 
**avg_write_latency** | **float** | Average write latency in microseconds. | [optional] 
**avg_mirror_write_latency** | **float** | Average mirror write latency in microseconds.  This applies to metro volumes in the active-active state. Was added in version 3.0.0.0. | [optional] 
**avg_write_size** | **float** | Average write size in bytes. | [optional] 
**read_iops** | **float** | Total read operations per second. | [optional] 
**read_bandwidth** | **float** | Read rate in bytes per second. | [optional] 
**total_iops** | **float** | Total read and write operations per second. | [optional] 
**total_bandwidth** | **float** | Total data transfer rate in bytes per second. | [optional] 
**write_iops** | **float** | Total write operations per second. | [optional] 
**mirror_write_iops** | **float** | Total mirror write operations per second.  This applies to metro volumes in the active-active state. Was added in version 3.0.0.0. | [optional] 
**write_bandwidth** | **float** | Write rate in bytes per second. | [optional] 
**mirror_write_bandwidth** | **float** | Metro write rate in bytes per second.  This applies to metro volumes in the active-active state. Was added in version 3.0.0.0. | [optional] 
**io_workload_cpu_utilization** | **float** | The percentage of CPU Utilization on the cores dedicated to servicing storage I/O requests. | [optional] 
**avg_io_size** | **float** | Average size of read and write operations in bytes. | [optional] 
**repeat_count** | **int** | Number of times the metrics are repeated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


