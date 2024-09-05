# FileUserQuotaModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hard_limit** | **int** | Hard limit of the user quota, in bytes. No hard limit when set to 0. This value can be used to compute amount of space that is consumed without limiting the space. Value is rounded up to match the physical block size of the filesystem. | [optional] 
**soft_limit** | **int** | Soft limit of the user quota, in bytes. No hard limit when set to 0. Value is rounded up to match the physical block size of the filesystem. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

