# NasServerDelete

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_skip_domain_unjoin** | **bool** | Indicates whether to keep the associated SMB servers joined to the Active Directory when the NAS server is deleted. Values are:\\n - true - Keep the associated SMB servers joined to the Active Directory when the NAS server is deleted. - false - (Default) Try to unjoin the associated SMB servers from the Active Directory before deleting the NAS server. | [optional] [default to False]
**domain_user_name** | **str** | Administrator login used to unjoin the associated SMB servers from the Active Directory (AD) domain before deleting the NAS server. This parameter is required when the skipDomainUnjoin parameter is false or not set, and the NAS server has SMB servers joined to an AD domain. | [optional] 
**domain_password** | **str** | Administrator password used to unjoin the associated SMB servers from the Active Directory (AD) domain before deleting the NAS server. This parameter is required when the skipDomainUnjoin parameter is false or not set, and the NAS server has SMB servers joined to an AD domain. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


