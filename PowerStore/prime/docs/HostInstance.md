# HostInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the host. | [optional] 
**name** | **str** | The host name.  This property supports case-insensitive filtering. | [optional] 
**description** | **str** | A description for the host. | [optional] 
**type** | [**HostTypeEnum**](HostTypeEnum.md) |  Was added in version 2.0.0.0. | [optional] 
**os_type** | [**OSTypeEnum**](OSTypeEnum.md) |  | [optional] 
**host_group_id** | **str** | Associated host group, if host is part of host group. | [optional] 
**host_connectivity** | [**HostConnectivityEnum**](HostConnectivityEnum.md) |  Was added in version 3.0.0.0. | [optional] 
**host_initiators** | [**list[HostInitiatorInstance]**](HostInitiatorInstance.md) |  Was deprecated in version 3.0.0.0.  Filtering on the fields of this embedded resource is not supported. | [optional] 
**type_l10n** | **str** | Localized message string corresponding to type Was added in version 2.0.0.0. | [optional] 
**os_type_l10n** | **str** | Localized message string corresponding to os_type | [optional] 
**host_connectivity_l10n** | **str** | Localized message string corresponding to host_connectivity Was added in version 3.0.0.0. | [optional] 
**initiators** | [**list[InitiatorInstance]**](InitiatorInstance.md) | This is the inverse of the resource type initiator association. | [optional] 
**host_group** | [**HostGroupInstance**](HostGroupInstance.md) | This is the embeddable reference form of host_group_id attribute. | [optional] 
**import_host_system** | [**ImportHostSystemInstance**](ImportHostSystemInstance.md) | This is the embeddable reference form of import_host_system_id attribute. | [optional] 
**mapped_hosts** | [**list[HostVolumeMappingInstance]**](HostVolumeMappingInstance.md) | This is the inverse of the resource type host_volume_mapping association. | [optional] 
**host_virtual_volume_mappings** | [**list[HostVirtualVolumeMappingInstance]**](HostVirtualVolumeMappingInstance.md) | This is the inverse of the resource type host_virtual_volume_mapping association. | [optional] 
**vsphere_hosts** | [**list[VsphereHostInstance]**](VsphereHostInstance.md) | List of the vsphere_hosts that are associated with this host. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


