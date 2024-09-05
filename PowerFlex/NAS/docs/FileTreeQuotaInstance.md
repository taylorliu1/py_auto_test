# FileTreeQuotaInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the tree quota. | [optional] 
**file_system_id** | **str** | Unique identifier of the associated file system. | [optional] 
**path** | **str** | Path relative to the root of the associated filesystem. | [optional] 
**description** | **str** | Description of the tree quota. | [optional] 
**is_user_quotas_enforced** | **bool** | Whether user quota are enabled on this tree quota. The tree quota itself is enforced regardless of this parameter.  | [optional] 
**state** | [**FileQuotaStateEnum**](FileQuotaStateEnum.md) |  | [optional] 
**hard_limit** | **int** | Hard limit of the tree quota, in bytes. No hard limit when set to 0. This value can be used to compute amount of space that is consumed without limiting the space. | [optional] 
**soft_limit** | **int** | Soft limit of the tree quota, in bytes. No hard limit when set to 0. | [optional] 
**remaining_grace_period** | **int** | Remaining grace period, in seconds, after the soft limit is exceeded: - 0 - Grace period has already expired - -1 - No grace period in-progress, or infinite grace period set The grace period of user quotas is set in the file system quota config.  | [optional] 
**size_used** | **int** | Size already used on the tree quota, in bytes. | [optional] 
**grace_period** | **int** | Grace period of tree quota, in seconds. No hard limit when set to -1. This will override the default grace period set at filesystem level. | [optional] [default to 0]
**state_l10n** | **str** | Localized message string corresponding to state | [optional] 
**file_system** | [**FileSystemInstance**](FileSystemInstance.md) |  | [optional] 
**file_user_tree_quotas** | [**list[FileUserQuotaInstance]**](FileUserQuotaInstance.md) | This is the inverse of the resource type file_user_quota association. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

