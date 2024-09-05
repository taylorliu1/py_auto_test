# VolumeClone

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the clone. This value must contain 128 or fewer printable Unicode characters. | [optional] 
**description** | **str** | Description of the clone. This value must contain 128 or fewer printable Unicode characters. | [optional] 
**host_id** | **str** | Unique identifier of the host to be attached to the clone. Only one of host_id or host_group_id can be supplied. name:{name} can be used instead of {id}. For example:&#39;host_id&#39;:&#39;name:host_name&#39; | [optional] 
**host_group_id** | **str** | Unique identifier of the host group to be attached to the clone. Only one of host_id or host_group_id can be supplied. name:{name} can be used instead of {id}. For example:&#39;host_group_id&#39;:&#39;name:host_group_name&#39; | [optional] 
**logical_unit_number** | **int** | Optional logical unit number when creating a mapped volume.  If no host_id or host_group_id is specified, this property is ignored. | [optional] 
**performance_policy_id** | **str** | Unique identifier of the  performance policy. | [optional] 
**protection_policy_id** | **str** | Unique identifier of the protection policy. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


