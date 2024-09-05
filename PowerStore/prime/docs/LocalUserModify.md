# LocalUserModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** | The unique identifier of the new role to which the local user has to be mapped. Where role_id \&quot;1\&quot; is for Administrator, \&quot;2\&quot; is for Storage Administrator, \&quot;3\&quot; is for Operator, \&quot;4\&quot; is for VM Administrator and \&quot;5\&quot; is for Security Administrator. A local user with either an administration or a security administration role can change the role of any other local user. You cannot change the role of the account you are currently logged-in to. name:{name} can be used instead of {id}. For example:&#39;role_id&#39;:&#39;name:role_name&#39; | [optional] 
**is_locked** | **bool** | Lock or unlock the local user account. Local user with administration/security administration role can lock or unlock any other local user account. You cannot lock an account you are currently logged-in to. | [optional] 
**current_password** | **str** | Current password of the local user. Any local user can change his own password by providing current_password along with the new password. | [optional] 
**password** | **str** | New password of the local user. Local user with administrator or security administrator role can reset the password of other local user accounts without providing the current password. You cannot reset the password of the account you are currently logged-in to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


