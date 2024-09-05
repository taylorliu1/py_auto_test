# SmbServerJoin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_user_name** | **str** | Name of a domain-user with sufficient privileges to join the Active Directory domain. | 
**domain_password** | **str** | Password of the domain-user specified to join the Active Directory domain. | 
**organizational_unit** | **str** | Organizational unit of the SMB server in Active Directory, if applicable. | [optional] 
**reuse_computer_account** | **bool** | If set to yes: try to reuse the existing SMB server account in the Active Directory when joining. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

