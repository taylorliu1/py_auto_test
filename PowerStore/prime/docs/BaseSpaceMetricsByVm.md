# BaseSpaceMetricsByVm

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_id** | **str** | Unique identifier representing a specific virtual machine. | [optional] 
**timestamp** | **datetime** | End of sample period. | [optional] 
**logical_provisioned** | **int** | Total configured size in bytes of all virtual volumes used by virtual machine. | [optional] 
**logical_used** | **int** | Total amount of data in bytes written to all virtual volumes used by virtual machine. | [optional] 
**unique_physical_used** | **int** | Amount of physical space virtual machine used after compression and deduplication. This is the space to be freed up if a virtual machine is removed. | [optional] 
**snap_clone_logical_used** | **int** | Total Amount of data in bytes host has written to all volumes used by virtual machine without any deduplication, compression or sharing. This metric includes snaps and clones in the volume family used by virtual machine. | [optional] 
**thin_savings** | **float** | Ratio of all the vVol provisioned to data they contain. This is the ratio of logical_provisioned to logical_used. For example, a VM has two 2 GB vVol&#39;s and have written 500 MB of data to them. The thin savings would be (2 * 2GB) / (2 * 0.5 GB) or 4:1, so the thin_savings value would be 4.0. | [optional] 
**snapshot_savings** | **float** | Ratio of the amount of space that would have been used by snapshots if space efficiency was not applied to logical space used solely by snapshots of vVols used by virtual machine. For example, a vVol is provisioned as 1 GB and it has two snapshots. Each snapshot has 200 MB of data. Snapshot savings will be (1 GB + 1 GB) / (0.2 GB + 0.2 GB) or 5:1. The snapshot_savings value will be 5 in this case. | [optional] 
**repeat_count** | **int** | Number of times the metrics are repeated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


