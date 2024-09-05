# VolumeGroupClone

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique name for the clone volume group. | 
**description** | **str** | Description for the clone volume group. If description is not specified, the description for the snapshot set will not be set. | [optional] 
**protection_policy_id** | **str** | Unique identifier of the protection policy you want to assign to the clone volume group. | [optional] 
**is_replication_destination** | **bool** | A boolean flag to indicate whether the clone volume group is a destination of a replication session. This parameter defaults to false, if not specified. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


