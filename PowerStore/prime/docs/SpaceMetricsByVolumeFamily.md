# SpaceMetricsByVolumeFamily

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appliance_id** | **str** | Reference to the associated appliance on which these metrics were recorded. | [optional] 
**family_id** | **str** | ID of the family. | [optional] 
**timestamp** | **datetime** | End of sample period. | [optional] 
**logical_provisioned** | **int** | Configured size in bytes of a volume which amount of data can be written to. This metric includes primaries, snaps and clones. | [optional] 
**logical_used** | **int** | Amount of data in bytes host has written to a volume family without any deduplication, compression or sharing. This metric includes primaries, snaps and clones. | [optional] 
**shared_logical_used** | **int** | Amount of space the volume family needs to hold the data written by host and shared by snaps and fast-clones in the family. This does not include deduplication or compression. | [optional] 
**unique_physical_used** | **int** | Amount of physical space volume family used after compression and deduplication. This is the space to be freed up if a volume family is removed from the appliance. | [optional] 
**snap_clone_logical_used** | **int** | Total Amount of data in bytes host has written to all volumes in the volume family without any deduplication, compression or sharing. This metric includes snaps and clones in the volume family. | [optional] 
**snapshot_savings** | **float** | Ratio of the amount of space that would have been used by snapshots if space efficiency was not applied to logical space used solely by snapshots. For example, a volume is provisioned as 1 GB bytes and it has two snapshots. Each snapshot has 200 MB of data. Snapshot savings will be (1 GB + 1 GB) / (0.2 GB + 0.2 GB) or 5:1. The snapshot_savings value will be 5 in this case. | [optional] 
**repeat_count** | **int** | Number of times the metrics are repeated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


