# PerformanceMetricsSmbBranchCacheByNodeRollup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | Unique identifier of the node. | [optional] 
**appliance_id** | **str** | Unique identifier of the appliance. Was added in version 3.0.0.0. | [optional] 
**timestamp** | **datetime** | End of sample period. | [optional] 
**repeat_count** | **int** | Number of consecutive sampling periods during which there were no changes in the metrics values. If the value is omitted from the response, it is 1 (no additional repeats).  | [optional] 
**hash_max_size** | **float** | Max hash size. | [optional] 
**hash_min_size** | **float** | Max hash size. | [optional] 
**hash_avg_size** | **float** | Average hash size. | [optional] 
**hash_max_avg_size** | **float** | Average max hash size. | [optional] 
**hash_max_latency** | **float** | Max hash latency. | [optional] 
**hash_min_latency** | **float** | Min hash latency. | [optional] 
**hash_avg_latency** | **float** | Average hash latency. | [optional] 
**hash_max_avg_latency** | **float** | Average max hash latency. | [optional] 
**total_tasks** | **float** | Total tasks. | [optional] 
**total_rejected_tasks** | **float** | Total rejected task. | [optional] 
**max_used_threads** | **float** | Max used threads | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


