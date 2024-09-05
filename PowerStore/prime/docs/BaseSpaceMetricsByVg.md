# BaseSpaceMetricsByVg

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vg_id** | **str** | Unique identifier representing a volume group. | [optional] 
**timestamp** | **datetime** | End of sample period. | [optional] 
**logical_provisioned** | **int** | Total configured size in bytes of all member volumes in a volume group. | [optional] 
**logical_used** | **int** | Total amount of data in bytes written to all member volumes in a volume group. | [optional] 
**snap_clone_logical_used** | **int** | Total amount of data in bytes host has written to all volumes in the volume group without any deduplication, compression or sharing. This metric includes used snaps and clones in the volume group. | [optional] 
**thin_savings** | **float** | Ratio of all the volumes provisioned to data being written to them. For example, a volume group has two 2 GB volumes and have written 500 MB of data to them. The thin savings would be (2 * 2 GB) / (2 * 0.5 GB) or 4:1, so the thin_savings value would be 4.0. | [optional] 
**snapshot_savings** | **float** | Ratio of the amount of space that would have been used by snapshots in the volume group if space efficiency was not applied to logical space used solely by snapshots. For example, two volumes are provisioned as 1 GB and each has two snapshots. Each snapshot has 200 MB of data. Snapshot savings will be (1 GB * 2 + 1 GB * 2) / (0.2 GB * 2 + 0.2 GB * 2) or 5:1. The snapshot_savings value will be 5 in this case. | [optional] 
**repeat_count** | **int** | Number of times the metrics are repeated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


