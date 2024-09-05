# LdapAccountCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** | Unique identifier of the LDAP domain to which LDAP user or group belongs. | 
**name** | **str** | Name of the new LDAP account to be created. The name value can be 1 to 64 UTF-8 characters long, and may only use alphanumeric characters. Dot(.) is the only special character allowed. The name value has to match to the LDAP user or group in LDAP server to which the LDAP account is mapped. | 
**type** | [**LDAPAccountTypeEnum**](LDAPAccountTypeEnum.md) |  | [optional] 
**role_id** | **str** | Unique identifier of the role to which the new LDAP account will be mapped. name:{name} can be used instead of {id}. For example:&#39;role_id&#39;:&#39;name:role_name&#39; | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


