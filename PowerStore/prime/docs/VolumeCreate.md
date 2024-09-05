# VolumeCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique name for the volume to be created. This value must contain 128 or fewer printable Unicode characters. | 
**size** | **int** | Size of the volume to be created, in bytes. Minimum volume size is 1MB. Maximum volume size is 256TB. Size must be a multiple of 8192. | 
**host_id** | **str** | Unique identifier of the host to be attached to the volume. If not specified, an unmapped volume is created. Only one of host_id or host_group_id can be supplied. name:{name} can be used instead of {id}. For example:&#39;host_id&#39;:&#39;name:host_name&#39; | [optional] 
**host_group_id** | **str** | Unique identifier of the host group to be attached to the volume. If not specified, an unmapped volume is created. Only one of host_id or host_group_id can be supplied. name:{name} can be used instead of {id}. For example:&#39;host_group_id&#39;:&#39;name:host_group_name&#39; | [optional] 
**logical_unit_number** | **int** | Optional logical unit number when creating a  attached volume.  If no host_id or host_group_id is specified, this property is ignored. | [optional] 
**description** | **str** | Description of the volume. This value must contain 128 or fewer printable Unicode characters. | [optional] 
**appliance_id** | **str** | Identifier of the appliance on which the volume is provisioned. name:{name} can be used instead of {id}. For example:&#39;appliance_id&#39;:&#39;name:appliance_name&#39; | [optional] 
**volume_group_id** | **str** | Volume group to add the volume to.  If not specified, the volume is not added to a volume group. name:{name} can be used instead of {id}. For example:&#39;volume_group_id&#39;:&#39;name:volume_group_name&#39; | [optional] 
**min_size** | **int** | Optional minimum size for the volume, in bytes. | [optional] 
**sector_size** | **int** | Optional sector size, in bytes. Only 512-byte and 4096-byte sectors are supported. | [optional] 
**protection_policy_id** | **str** | Unique identifier of the protection policy assigned to the volume. | [optional] 
**performance_policy_id** | **str** | Unique identifier of the performance policy assigned to the volume. | [optional] 
**app_type** | [**AppTypeEnum**](AppTypeEnum.md) |  Was added in version 2.1.0.0. | [optional] 
**app_type_other** | **str** | An optional field used to describe application type usage for a volume. This field can only be set if app_type is set to Relational_Databases_Other, Big_Data_Analytics_Other, Business_Applications_Other, Healthcare_Other, Virtualization_Other or Other. If the app_type attribute is set to anything other than one of these values, the attribute will be cleared. Was added in version 2.1.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


