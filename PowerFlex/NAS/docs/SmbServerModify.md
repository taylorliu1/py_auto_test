# SmbServerModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_standalone** | **bool** | Indicates whether the SMB server is standalone. Values are: - true - SMB server is standalone. - false - SMB server is joined to the Active Directory.  | [optional] 
**computer_name** | **str** | DNS Name of the associated Computer Account when the SMB server is joined to an Active Directory domain. This name is limited to 63 bytes and must not contain the following characters -   - comma (.)   - tilde (~)   - colon (:)   - exclamation point (!)   - at sign (@)   - number sign (#)   - dollar sign ($)   - percent (%)   - caret (^)   - ampersand (&amp;)   - apostrophe (&#x27;)   - period (.) - note that if you enter string with period only the first word will be kept   - parentheses (())   - braces ({})   - underscore (_)   - white space (blank) as defined by the Microsoft naming convention (see https://support.microsoft.com/en-us/help/909264/)  | [optional] 
**domain** | **str** | Domain name where SMB server is registered in Active Directory, if applicable. | [optional] 
**netbios_name** | **str** | NetBIOS name is the network name of the standalone SMB server. SMB servers joined to Active Directory also have NetBIOS Name, defaulted to the 15 first characters of the computer_name attribute. Administrators can specify a custom NetBIOS Name for an SMB server using this attribute. NetBIOS name is limited to 15 characters and cannot contain the following characters -   - backslash (\\)   - slash mark (/)   - colon (:)   - asterisk (*)   - question mark (?)   - quotation mark (\&quot;\&quot;)   - less than sign (&lt;)   - greater than sign (&gt;)   - vertical bar (|) as defined by the Microsoft naming convention (see https://support.microsoft.com/en-us/help/909264/)  | [optional] 
**workgroup** | **str** | Applies to standalone SMB servers only. Windows network workgroup for the SMB server. Workgroup names are limited to 15 alphanumeric ASCII characters.  | [optional] 
**description** | **str** | Description of the SMB server in UTF-8 characters. | [optional] 
**local_admin_password** | **str** | Password for the local administrator account of the SMB server. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

