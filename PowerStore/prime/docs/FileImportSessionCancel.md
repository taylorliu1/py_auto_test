# FileImportSessionCancel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force** | **bool** | Normally a cancel will fail if the source system is unresponsive. When the force flag is true, the cancel will continue anyway. Note that source system cleanup will not be done. | [optional] [default to False]
**domain_admin_username** | **str** | User name for authentication to Active Directory domain with permissions to join computers. This is required for a non-standalone SMB import. | [optional] 
**domain_admin_password** | **str** | Password for authentication to Active Directory domain with permissions to join computers. This is required for a non-standalone SMB import. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


