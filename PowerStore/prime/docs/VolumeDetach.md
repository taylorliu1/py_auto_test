# VolumeDetach

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_id** | **str** | Unique identifier of the host to be detached from this volume. Only one of host_id or host_group_id can be supplied. name:{name} can be used instead of {id}. For example:&#39;host_id&#39;:&#39;name:host_name&#39; | [optional] 
**host_group_id** | **str** | Unique identifier of the host group to be detached from this volume. Only one of host_id or host_group_id can be supplied. name:{name} can be used instead of {id}. For example:&#39;host_group_id&#39;:&#39;name:host_group_name&#39; | [optional] 
**clear_host_agent_data** | **bool** | Indicates if any saved host agent metadata should be cleared if this is the final detach of a volume being imported from another storage array, i.e. no other hosts or host groups are attached to the volume. Was added in version 3.0.0.0. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


