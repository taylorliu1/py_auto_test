# FileUserQuotaInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the user quota. | [optional] 
**file_system_id** | **str** | Unique identifier of the associated filesystem. | [optional] 
**tree_quota_id** | **str** | Unique identifier of the associated tree quota. Values are: - null - if the user quota is not within a quota tree. - tree_quota instance id - if the user quota is within a quota tree.  | [optional] 
**uid** | **int** | Unix user identifier (UID) of the user. | [optional] 
**unix_name** | **str** | Unix username. | [optional] 
**windows_name** | **str** | Windows username. The format is domain\\\\user for the domain user. | [optional] 
**windows_sid** | **str** | Windows Security Identifier of the user. | [optional] 
**state** | [**FileQuotaStateEnum**](FileQuotaStateEnum.md) |  | [optional] 
**hard_limit** | **int** | Hard limit of the user quota, in bytes. No hard limit when set to 0. This value can be used to compute amount of space that is consumed without limiting the space. | [optional] 
**soft_limit** | **int** | Soft limit of the user quota, in bytes. No hard limit when set to 0. | [optional] 
**remaining_grace_period** | **int** | Remaining grace period, in seconds, after the soft limit is exceeded:   - 0 - Grace period has already expired   - -1 - No grace period in-progress, or infinite grace period set The grace period of user quotas is set in the file system quota configuration.  | [optional] 
**size_used** | **int** | Size currently consumed by the user on the filesystem, in bytes. | [optional] 
**state_l10n** | **str** | Localized message string corresponding to state | [optional] 
**file_system** | [**FileSystemInstance**](FileSystemInstance.md) | This is the embeddable reference form of file_system_id attribute. | [optional] 
**tree_quota** | [**FileTreeQuotaInstance**](FileTreeQuotaInstance.md) | This is the embeddable reference form of tree_quota_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


