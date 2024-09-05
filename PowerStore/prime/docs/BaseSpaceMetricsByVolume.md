# BaseSpaceMetricsByVolume

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appliance_id** | **str** | Reference to the associated appliance on which these metrics were recorded. | [optional] 
**volume_id** | **str** | ID of the volume. | [optional] 
**timestamp** | **datetime** | End of sample period. | [optional] 
**logical_provisioned** | **int** | Configured size in bytes of a volume which amount of data can be written to. This metric includes primaries, snaps and clones. | [optional] 
**logical_used** | **int** | Amount of data in bytes host has written to a volume without any deduplication, compression or sharing. This metric includes primaries, snaps and clones. | [optional] 
**thin_savings** | **float** | Ratio of all the volumes provisioned to data being written to them. For example, an appliance has two 2 GB volumes and have written 500 MB of data to them. The thin savings would be (2 GB * 2) / (0.5 GB * 2) or 4:1, so the thin_savings value would be 4.0. | [optional] 
**repeat_count** | **int** | Number of times the metrics are repeated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


