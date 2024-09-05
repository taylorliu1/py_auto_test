# SmbServerInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the SMB server. | [optional] 
**nas_server_id** | **str** | Unique identifier of the NAS server. | [optional] 
**computer_name** | **str** | DNS name of the associated computer account when the SMB server is joined to an Active Directory domain. This name&#39;s minimum length is 2 characters, it is limited to 63 bytes and must not contain the following characters -   - comma (.)   - tilde (~)   - colon (:)   - exclamation point (!)   - at sign (@)   - number sign (#)   - dollar sign ($)   - percent (%)   - caret (^)   - ampersand (&amp;)   - apostrophe (&#39;)   - period (.) - note that if you enter string with period only the first word will be kept   - parentheses (())   - braces ({})   - underscore (_)   - white space (blank) as defined by the Microsoft naming convention (see https://support.microsoft.com/en-us/help/909264/)  | [optional] 
**domain** | **str** | Domain name where SMB server is registered in Active Directory, if applicable. | [optional] 
**netbios_name** | **str** | NetBIOS name is the network name of the standalone SMB server. SMB server joined to Active Directory also have NetBIOS Name, defaulted to the 15 first characters of the computerName attribute. Administrators can specify a custom NetBIOS Name for a SMB server using this attribute. NetBIOS Name are limited to 15 characters and cannot contain the following characters -   - backslash (\\)   - slash mark (/)   - colon (:)   - asterisk (*)   - question mark (?)   - quotation mark (\&quot;\&quot;)   - less than sign (&lt;)   - greater than sign (&gt;)   - vertical bar (|) as definied by the Microsoft naming convention (see https://support.microsoft.com/en-us/help/909264/)  | [optional] 
**workgroup** | **str** | Applies to stand-alone SMB servers only. Windows network workgroup for the SMB server. Workgroup names are limited to 15 alphanumeric ASCII characters.  | [optional] 
**description** | **str** | Description of the SMB server. | [optional] 
**is_standalone** | **bool** | Indicates whether the SMB server is standalone. Values are: - true - SMB server is standalone. - false - SMB server is a domain SMB server to be joined to the Active Directory.  | [optional] 
**is_joined** | **bool** | Indicates whether the SMB server is joined to the Active Directory. Always false for standalone SMB servers. | [optional] 
**nas_server** | [**NasServerInstance**](NasServerInstance.md) | This is the embeddable reference form of nas_server_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


