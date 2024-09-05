# FileTreeQuotaModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the tree quota. | [optional] 
**hard_limit** | **int** | Hard limit of the tree quota, in bytes. No hard limit when set to 0. This value can be used to compute amount of space that is consumed without limiting the space. Value is always rounded up to match the physical block size of the filesystem. | [optional] 
**soft_limit** | **int** | Soft limit of the tree quota, in bytes. No hard limit when set to 0. Value is always rounded up to match the physical block size of the filesystem. | [optional] 
**is_user_quotas_enforced** | **bool** | Whether the quota must be enabled for all users, and whether user quota limits, if any, are enforced. Values are: - true - start tracking usage for all users on the quota tree, and enforce user quota limits. - false - stop tracking usage for all users on the quota tree, and do not enforce user quota limits.  | [optional] 
**grace_period** | **int** | Grace period of tree quota, in seconds. No hard limit when set to -1. This will override the default grace period set at filesystem level. | [optional] [default to 0]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

