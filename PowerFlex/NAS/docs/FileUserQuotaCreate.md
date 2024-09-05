# FileUserQuotaCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_system_id** | **str** | Unique identifier of the filesystem in which the new user quota will be created. | 
**tree_quota_id** | **str** | Unique identifier of the tree quota in which the new user quota will be created. | [optional] 
**uid** | **int** | Unix user identifier (UID) of the user. Preferred identifier. | [optional] 
**unix_name** | **str** | Unix username. Identifers are exclusive. Only one of the four identifiers among &#x27;user uid&#x27; / &#x27;unix username&#x27; / &#x27;windows username&#x27; / &#x27;windows SID&#x27; can be used at a time. | [optional] 
**windows_name** | **str** | Windows username. The format is domain\\\\user for the domain user. Identifers are exclusive. Only one of the four identifiers among &#x27;user uid&#x27; / &#x27;unix username&#x27; / &#x27;windows username&#x27; / &#x27;windows SID&#x27; can be used at a time. | [optional] 
**windows_sid** | **str** | Windows Security Identifier of the user. Identifers are exclusive. Only one of the four identifiers among &#x27;user uid&#x27; / &#x27;unix username&#x27; / &#x27;windows username&#x27; / &#x27;windows SID&#x27; can be used at a time. | [optional] 
**hard_limit** | **int** | Hard limit of the user quota, in bytes. No hard limit when set to 0. This value can be used to compute amount of space that is consumed without limiting the space. Value is rounded up to match the physical block size of the filesystem. | [optional] 
**soft_limit** | **int** | Soft limit of the user quota, in bytes. No hard limit when set to 0. Value is rounded up to match the physical block size of the filesystem. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

