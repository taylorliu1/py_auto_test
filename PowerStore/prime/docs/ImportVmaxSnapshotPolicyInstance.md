# ImportVmaxSnapshotPolicyInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of the VMAX snapshot policy. | [optional] 
**snapshot_count** | **int** | The number of snapshots that will be taken before the oldest ones are no longer required. | [optional] 
**interval_minutes** | **int** | The number of minutes between each policy execution. | [optional] 
**offset_minutes** | **int** | The number of minutes after 00:00 on Monday morning that the policy will execute. | [optional] 
**provider_name** | **str** | The name of the cloud provider associated with this policy. Only applies to cloud policies. | [optional] 
**retention_days** | **int** | The number of days that snapshots will be retained in the cloud for. Only applies to cloud policies. | [optional] 
**suspended** | **bool** | Set if the snapshot policy has been suspended. | [optional] [default to False]
**secure** | **bool** | Set if the snapshot policy creates secure snapshots. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


