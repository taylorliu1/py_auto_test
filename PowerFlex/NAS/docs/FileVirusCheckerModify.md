# FileVirusCheckerModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | Indicates whether the anti-virus service is enabled on this NAS server. Value are: - true - Anti-virus service is enabled. Each file created or modified by an SMB client is scanned by the third-party anti-virus servers. If a virus is detected, the access to the file system is denied. If third-party anti-virus servers are not available, according the policy, the access to the file systems is denied to prevent potential viruses propagation. - false - Anti-virus service is disabled. File systems of the NAS servers are available for access without virus checking.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

