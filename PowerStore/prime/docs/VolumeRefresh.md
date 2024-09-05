# VolumeRefresh

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_object_id** | **str** | Unique identifier of the source volume that will be used for the refresh operation. | 
**create_backup_snap** | **bool** | Indicates whether a backup snapshot of the target volume will be created before it is refreshed from the source volume. | [optional] [default to False]
**backup_snap_profile** | [**VolumeSnapshot**](VolumeSnapshot.md) | Profile to be used to create the backup snapshot. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


