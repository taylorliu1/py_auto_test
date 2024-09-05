# FileTreeQuotaCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_system_id** | **str** | Unique identifier of the associated file system. name:{name} can be used instead of {id}. For example:&#39;file_system_id&#39;:&#39;name:file_system_name&#39; | 
**path** | **str** | Path relative to the root of the associated filesystem. | 
**description** | **str** | Description of the tree quota. | [optional] 
**hard_limit** | **int** | Hard limit of the tree quota, in bytes. No hard limit when set to 0. This value can be used to compute amount of space that is consumed without limiting the space. Value is always rounded up to match the physical block size of the filesystem. | [optional] 
**soft_limit** | **int** | Soft limit of the tree quota, in bytes. No hard limit when set to 0. Value is always rounded up to match the physical block size of the filesystem. | [optional] 
**is_user_quotas_enforced** | **bool** | Whether the quota must be enabled for all users, and whether user quota limits, if any, are enforced. Values are: * true  - Start tracking usage for all users on the quota tree, and enforce user quota limits. * false - Stop tracking usage for all users on the quota tree, and do not enforce user quota limits.  | [optional] 
**grace_period** | **int** | Grace period of soft limit (seconds). This will override the default grace period set at filesystem level.  * -1: Infinite grace period (Windows policy).  *  0: Use default grace period of 1 week (default).  * Positive: Grace period after which the soft limit is treated as a hard limit (seconds).  Was added in version 2.0.0.0. | [optional] [default to 0]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


