# BaseSpaceMetricsByStorageContainer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_container_id** | **str** | Internal ID of the storage container. | [optional] 
**timestamp** | **datetime** | End of sample period. | [optional] 
**logical_provisioned** | **int** | Total configured size in bytes of the primary and clone virtual volumes within the storage container. | [optional] 
**logical_used** | **int** | Amount of data in bytes written to primary and clone virtual volumes within the storage container. | [optional] 
**shared_logical_used** | **int** | Amount of space the storage container needs to hold the data written by host and shared by snaps and fast-clones in their families; this does not include deduplication or compression. Was added in version 2.0.0.0. | [optional] 
**snapshot_savings** | **float** | Ratio of the amount of space that would have been used by snapshots if space efficiency was not applied to logical space used solely by snapshots. For example, a volume is provisioned as 1 GB and it has two snapshots. Each snapshot has 200 MB of data. Snapshot savings will be (1 GB + 1 GB) / (0.2 GB + 0.2 GB) or 5:1. The snapshot_savings value will be 5 in this case. | [optional] 
**repeat_count** | **int** | Number of times the metrics are repeated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


