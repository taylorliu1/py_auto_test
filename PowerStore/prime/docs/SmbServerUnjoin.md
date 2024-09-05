# SmbServerUnjoin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_user_name** | **str** | Name of a domain-user with sufficient privileges to unjoin from the Active Directory domain. | [optional] 
**domain_password** | **str** | Password of the domain-user specified to unjoin from the Active Directory domain. | [optional] 
**is_skip_ad_unjoin** | **bool** | If set to yes: Will not remove the account from the Active Directory. This is to be used in case that no DC is available. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


