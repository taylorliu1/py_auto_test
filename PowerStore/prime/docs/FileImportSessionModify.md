# FileImportSessionModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Import Session. | [optional] 
**description** | **str** | Description of the file import session.     The name can contain a maximum of 128 Unicode characters.     It cannot contain unprintable characters. | [optional] 
**scheduled_timestamp** | **datetime** | Indicates the new date and time at which the import session is scheduled to run. The date is specified in ISO 8601 format with time expressed in UTC format. | [optional] 
**source_smb_admin_username** | **str** | User name for authentication to SMB Server on the source NAS Server with administrator privilege. | [optional] 
**source_smb_admin_password** | **str** | Password for authentication to SMB Server on the source NAS Server with administrator privilege. | [optional] 
**source_dhsm_username** | **str** | The username for authentication to DHSM Server on the source NAS Server required for importing FLR filesystems. | [optional] 
**source_dhsm_password** | **str** | The password for authentication to DHSM Server on the source NAS Server required for importing FLR filesystems. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


