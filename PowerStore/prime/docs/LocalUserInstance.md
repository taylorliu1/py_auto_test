# LocalUserInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the local user account. | [optional] 
**name** | **str** | Name of the local user account. | [optional] 
**is_built_in** | **bool** | Whether the user account is built-in or not. | [optional] 
**is_locked** | **bool** | Whether the user account is locked or not. Defaults to false at creation time. | [optional] 
**is_default_password** | **bool** | Whether the user account has a default password or not. Only applies to default user accounts. | [optional] 
**role_id** | **str** | Unique identifier of the role local user account is mapped to. | [optional] 
**password_expiration_timestamp** | **datetime** | Timestamp when the password will expire. Was added in version 3.0.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


