# VolumeGroupRefresh

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_object_id** | **str** | Unique identifier of the volume group to refresh from. This is referred to as the source volume group. | 
**create_backup_snap** | **bool** | This parameter specifies whether a backup snapshot set of the target volume group needs to be created before refreshing it. This parameter defaults to true, if not specified. | [optional] [default to True]
**backup_snap_profile** | [**VolumeGroupSnapshot**](VolumeGroupSnapshot.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


