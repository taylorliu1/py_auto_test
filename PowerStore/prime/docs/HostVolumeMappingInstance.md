# HostVolumeMappingInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of a mapping between a host and a volume. | [optional] 
**host_id** | **str** | Unique identifier of a host attached to a volume. The host_id and host_group_id cannot both be set. | [optional] 
**host_group_id** | **str** | Unique identifier of a host group attached to a volume. The host_id and host_group_id cannot both be set. | [optional] 
**volume_id** | **str** | Unique identifier of the volume to which the host is attached. | [optional] 
**logical_unit_number** | **int** | Logical unit number for the host volume access. | [optional] 
**host** | [**HostInstance**](HostInstance.md) | This is the embeddable reference form of host_id attribute. | [optional] 
**host_group** | [**HostGroupInstance**](HostGroupInstance.md) | This is the embeddable reference form of host_group_id attribute. | [optional] 
**volume** | [**VolumeInstance**](VolumeInstance.md) | This is the embeddable reference form of volume_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


