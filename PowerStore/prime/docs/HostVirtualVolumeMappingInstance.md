# HostVirtualVolumeMappingInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of a mapping between a host and a virtual volume. | [optional] 
**host_id** | **str** | Unique identifier of a host attached to a virtual volume. The host_id and host_group_id cannot both be set. | [optional] 
**host_group_id** | **str** | Unique identifier of a host group attached to a virtual volume. The host_id and host_group_id cannot both be set. | [optional] 
**virtual_volume_id** | **str** | Unique identifier of the virtual volume to which the host is attached. | [optional] 
**host** | [**HostInstance**](HostInstance.md) | This is the embeddable reference form of host_id attribute. | [optional] 
**host_group** | [**HostGroupInstance**](HostGroupInstance.md) | This is the embeddable reference form of host_group_id attribute. | [optional] 
**virtual_volume** | [**VirtualVolumeInstance**](VirtualVolumeInstance.md) | This is the embeddable reference form of virtual_volume_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


