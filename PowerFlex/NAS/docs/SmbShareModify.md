# SmbShareModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | NFS Share description. | [optional] 
**is_abe_enabled** | **bool** | Indicates whether Access-based Enumeration (ABE) is enabled. ABE filters the list of available files and folders on a server to include only those, that the requesting user has access to. Values are: - true - ABE is enabled. - false - ABE is disabled.  | [optional] 
**is_branch_cache_enabled** | **bool** | Indicates whether BranchCace optimization is enabled. BranchCache optimization technology copies content from your main office or hosted cloud content servers and caches the content at branch office locations, allowing client computers at branch offices to access the content locally rather than over the WAN. Values are: - true - BranchCache is enabled. - false - BranchCache is disabled.  | [optional] 
**offline_availability** | [**SMBShareOfflineAvailabilityEnum**](SMBShareOfflineAvailabilityEnum.md) |  | [optional] 
**umask** | **str** | The default UNIX umask for new files created on the Share. | [optional] 
**is_continuous_availability_enabled** | **bool** | Indicates whether continuous availability for Server Message Block (SMB) 3.0 is enabled for the SMB Share. Values are: - true - Continuous availability for SMB 3.0 is enabled for the SMB Share. - false - Continuous availability for SMB 3.0 is disabled for the SMB Share.  | [optional] 
**is_encryption_enabled** | **bool** | Indicates whether encryption for Server Message Block (SMB) 3.0 is enabled at the shared folder level. Values are: - true - encryption for SMB 3.0 is enabled. - false - encryption for SMB 3.0 is disabled.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

