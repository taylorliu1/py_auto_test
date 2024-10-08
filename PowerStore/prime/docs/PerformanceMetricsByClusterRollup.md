# PerformanceMetricsByClusterRollup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | Identifier of the cluster. | [optional] 
**timestamp** | **datetime** | End of sample period. | [optional] 
**avg_read_latency** | **float** | Weighted average read latency in microseconds. | [optional] 
**avg_write_latency** | **float** | Weighted average write latency in microseconds. | [optional] 
**avg_mirror_write_latency** | **float** | Weighted average mirror write latency in microseconds.  This applies to metro volumes in the active-active state. Was added in version 3.0.0.0. | [optional] 
**avg_mirror_overhead_latency** | **float** | Weighted additional latency incurred on the source in order to do the remote mirror writes in microseconds. This applies to metro volumes in the active-active state. Was added in version 3.0.0.0. | [optional] 
**avg_latency** | **float** | Weighted average latency in microseconds. | [optional] 
**avg_read_size** | **float** | Weighted average read size in bytes. | [optional] 
**avg_write_size** | **float** | Weighted average write size in bytes. | [optional] 
**avg_io_size** | **float** | Average size of read and write operations in bytes. | [optional] 
**avg_read_iops** | **float** | Average reads per second. | [optional] 
**avg_write_iops** | **float** | Average writes per second. | [optional] 
**avg_mirror_write_iops** | **float** | Average mirror write operations per second.  This applies to metro volumes in the active-active state. Was added in version 3.0.0.0. | [optional] 
**avg_total_iops** | **float** | Average total input and output operations per second. | [optional] 
**avg_read_bandwidth** | **float** | Weighted average  read bandwidth in bytes per second. | [optional] 
**avg_write_bandwidth** | **float** | Weighted average write bandwidth in bytes per second. | [optional] 
**avg_mirror_write_bandwidth** | **float** | Weighted average mirror write rate in byte per second.  This applies to metro volumes in the active-active state. Was added in version 3.0.0.0. | [optional] 
**avg_total_bandwidth** | **float** | Weighted average total bandwidth in bytes per second. | [optional] 
**max_avg_read_latency** | **float** | Maximum read latency in microseconds. | [optional] 
**max_avg_write_latency** | **float** | Maximum of average write latency in microseconds. | [optional] 
**max_avg_mirror_write_latency** | **float** | Maximum of average mirror write latency in microseconds.  This applies to metro volumes in the active-active state. Was added in version 3.0.0.0. | [optional] 
**max_avg_mirror_overhead_latency** | **float** | Maximum of average additional latency incurred on the source in order to do the remote mirror writes in microseconds. This applies to metro volumes in the active-active state. Was added in version 3.0.0.0. | [optional] 
**max_avg_latency** | **float** | Maximum of average latency in microseconds. | [optional] 
**max_avg_read_size** | **float** | Maximum of average read size in bytes. | [optional] 
**max_avg_write_size** | **float** | Maximum of average write size in bytes. | [optional] 
**max_avg_io_size** | **float** | Maximum average size of input and output operations in bytes. | [optional] 
**max_read_iops** | **float** | Maximum reads per second. | [optional] 
**max_write_iops** | **float** | Maximum writes per second. | [optional] 
**max_mirror_write_iops** | **float** | Maximum mirror write operations per second.  This applies to metro volumes in the active-active state. Was added in version 3.0.0.0. | [optional] 
**max_total_iops** | **float** | Maximum totals per second. | [optional] 
**max_read_bandwidth** | **float** | Maximum read bandwidth in bytes per second. | [optional] 
**max_write_bandwidth** | **float** | Maximum write bandwidth in bytes per second. | [optional] 
**max_mirror_write_bandwidth** | **float** | Maximum mirror write rate in byte per second.  This applies to metro volumes in the active-active state. Was added in version 3.0.0.0. | [optional] 
**max_total_bandwidth** | **float** | Maximum total bandwidth in bytes per second. | [optional] 
**repeat_count** | **int** | Number of times the metrics are repeated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


