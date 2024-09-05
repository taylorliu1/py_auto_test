# LocalUserCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the new local user account to be created. The name value can be 1 to 64 UTF-8 characters long, and may only use alphanumeric characters. Dot(.) is the only special character allowed. | 
**password** | **str** | Password for the new local user account to be created. The password value can be 8 to 40 UTF-8 characters long, and include as a minimum one uppercase character, one lowercase character, one numeric character, and one special character from (!,@#$%^*?_~). | 
**role_id** | **str** | The unique identifier of the role to which the new local user will be mapped. Where role_id \&quot;1\&quot; is for Administrator, \&quot;2\&quot; is for Storage Administrator, \&quot;3\&quot; is for Operator, \&quot;4\&quot; is for VM Administrator and \&quot;5\&quot; is for Security Administrator roles. name:{name} can be used instead of {id}. For example:&#39;role_id&#39;:&#39;name:role_name&#39; | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


