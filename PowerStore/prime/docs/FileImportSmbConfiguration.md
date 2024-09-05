# FileImportSmbConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_standalone** | **bool** | Indicates whether the source SMB server is standalone. A &#39;true&#39; value indicated the SMB server is standalone and &#39;false&#39; value indicates the SMB server is joined to an Active Directory. | [optional] 
**computer_name** | **str** | DNS name of the associated computer account when the source SMB server is joined to an Active Directory domain. | [optional] 
**domain** | **str** | Domain name where the source SMB server is registered in Active Directory, if applicable. | [optional] 
**organizational_unit** | **str** | Organizational unit of the source SMB server in Active Directory, if applicable. | [optional] 
**netbios_name** | **str** | NetBIOS or network name of the standalone source SMB server. SMB server joined to Active Directory also has a NetBIOS Name, defaulted to the first 15 characters of the computer name attribute. Administrators can specify a custom NetBIOS name for a SMB server using this attribute. | [optional] 
**workgroup** | **str** | Windows network workgroup for the source SMB server. This is applicable to stand-alone SMB servers only. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


