# VolumeSnapshot

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the snapshot to be created. This value must contain 128 or fewer printable Unicode characters. The default name of the volume snapshot is the date and time when the snapshot is taken. | [optional] 
**description** | **str** | Description of the snapshot. This value must contain 128 or fewer printable Unicode characters. | [optional] 
**performance_policy_id** | **str** | Unique identifier of the performance policy assigned to the snapshot. | [optional] 
**expiration_timestamp** | **datetime** | Time at which the snapshot will expire. Expired snapshots are deleted by the snapshot aging service that runs periodically in the background. If not specified, the snapshot never expires. Use a maximum timestamp value to set an expiration to never expire. | [optional] 
**creator_type** | [**StorageCreatorTypeEnum**](StorageCreatorTypeEnum.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


