# BasePerformanceMetricsByNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | Unique identifier representing a specific node. | [optional] 
**appliance_id** | **str** | Reference to the associated appliance on which these metrics were recorded. | [optional] 
**timestamp** | **datetime** | End of sample period. | [optional] 
**avg_latency** | **float** | Average read and write latency in microseconds. | [optional] 
**avg_read_latency** | **float** | Average read latency in microseconds. | [optional] 
**avg_write_latency** | **float** | Average write latency in microseconds. | [optional] 
**avg_mirror_write_latency** | **float** | Average mirror write latency in microseconds.  This applies to metro volumes in the active-active state. Was added in version 3.0.0.0. | [optional] 
**avg_mirror_overhead_latency** | **float** | Average additional latency incurred on the source in order to do the remote mirror writes in microseconds. This applies to metro volumes in the active-active state. Was added in version 3.0.0.0. | [optional] 
**avg_read_size** | **float** | Average read size in bytes. | [optional] 
**avg_write_size** | **float** | Average write size in bytes. | [optional] 
**io_workload_cpu_utilization** | **float** | The percentage of CPU Utilization on the cores dedicated to servicing storage I/O requests. | [optional] 
**avg_io_size** | **float** | Average size of read and write operations in bytes. | [optional] 
**read_iops** | **float** | Total number of read operations by the node. | [optional] 
**write_iops** | **float** | Total write operations per second. | [optional] 
**mirror_write_iops** | **float** | Total mirror write operations per second.  This applies to metro volumes in the active-active state. Was added in version 3.0.0.0. | [optional] 
**total_iops** | **float** | Total read and write operations per second. | [optional] 
**read_bandwidth** | **float** | Read rate in bytes per second. | [optional] 
**write_bandwidth** | **float** | Write rate in byte/sec. | [optional] 
**mirror_write_bandwidth** | **float** | Metro write rate in bytes per second.  This applies to metro volumes in the active-active state. Was added in version 3.0.0.0. | [optional] 
**total_bandwidth** | **float** | Total data transfer rate in bytes per second. | [optional] 
**unaligned_read_iops** | **float** | Unaligned read input/output per second. Was deprecated in version 2.1.0.0. | [optional] 
**unaligned_write_iops** | **float** | Unaligned write input/output per second. Was deprecated in version 2.1.0.0. | [optional] 
**unaligned_iops** | **float** | Unaligned total input/output per second. Was deprecated in version 2.1.0.0. | [optional] 
**unaligned_read_bandwidth** | **float** | Unaligned read rate in bytes per second. Was deprecated in version 2.1.0.0. | [optional] 
**unaligned_write_bandwidth** | **float** | Unaligned write rate in bytes per second. Was deprecated in version 2.1.0.0. | [optional] 
**unaligned_bandwidth** | **float** | Unaligned read/write rate in bytes per second. Was deprecated in version 2.1.0.0. | [optional] 
**current_logins** | **int** | The number of logins to the target from initiators. | [optional] 
**repeat_count** | **int** | Number of times the metrics are repeated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


