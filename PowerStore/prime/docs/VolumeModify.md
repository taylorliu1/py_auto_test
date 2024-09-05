# VolumeModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New name of the volume. This value must contain 128 or fewer printable Unicode characters. | [optional] 
**description** | **str** | New description of the volume. This value must contain 128 or fewer printable Unicode characters. | [optional] 
**size** | **int** | New size of the volume in bytes,  must be a multiple of 8192, must be bigger than the current volume size. Maximum volume size is 256TB. | [optional] 
**expiration_timestamp** | **datetime** | New expiration time of the snapshot. Expired snapshots are deleted by the snapshot aging service that runs periodically in the background. If not specified, the snapshot never expires. Use a maximum timestamp value or null to set an expiration to never expire. | [optional] 
**protection_policy_id** | **str** | Unique identifier of the protection policy assigned to the volume. | [optional] 
**performance_policy_id** | **str** | Unique identifier of the performance policy assigned to the volume. | [optional] 
**is_replication_destination** | **bool** | New value for is_replication_destination property. The modification is only supported for primary and clone volume, only when the current value is true and there is no longer a replication session using this volume as a destination, and only to false. | [optional] 
**force** | **bool** | Normally a replication destination volume cannot be modified since it is controlled by replication. However, there can be cases where replication has failed or is no longer active and the replication destination volume needs to be cleaned up. With the force option, the user will be allowed to remove the protection policy from the replication destination volume provided that the replication session has never been synchronized and the last_sync_timestamp property is empty. This parameter defaults to false, if not specified. | [optional] [default to False]
**node_affinity** | [**NodeAffinityEnum**](NodeAffinityEnum.md) | Set which node will optimized for IO. | [optional] 
**app_type** | [**AppTypeEnum**](AppTypeEnum.md) |  Was added in version 2.1.0.0. | [optional] 
**app_type_other** | **str** | An optional field used to describe application type usage for a volume. This field can only be set if app_type is set to Relational_Databases_Other, Big_Data_Analytics_Other, Business_Applications_Other, Healthcare_Other, Virtualization_Other or Other. If the app_type attribute is set to anything other than one of these values, the attribute will be cleared. Was added in version 2.1.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


