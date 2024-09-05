# LoginSessionInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the login session. | [optional] 
**user** | **str** | Fully qualified user account name being used to log in. | [optional] 
**role_ids** | **list[str]** | Roles to which the logged-in user is mapped. | [optional] 
**idle_timeout** | **int** | Remaining idle time until the session will expire, in seconds. | [optional] 
**is_password_change_required** | **bool** | Indicates whether the logged-in user requires a password change. | [optional] 
**is_built_in_user** | **bool** | Indicates whether the logged-in user is predefined. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


