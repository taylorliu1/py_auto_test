# SmbShareInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the SMB Share. | [optional] 
**file_system_id** | **str** | The file system from which the share was created. | [optional] 
**name** | **str** | SMB share name.  This property supports case-insensitive filtering. | [optional] 
**path** | **str** | Local path to the file system or any existing sub-folder of the file system that is shared over the network. This path is relative to the NAS Server and must start with the filesystem&#39;s mountpoint path, which is the filesystem name. For example to share the top-level of a filesystem named svr1fs1, which is on the /svr1fs1 mountpoint of the NAS Server, use /svr1fs1 in the path parameter. SMB shares allow you to create multiple network shares for the same local path.  | [optional] 
**description** | **str** | User defined SMB share description. | [optional] 
**is_continuous_availability_enabled** | **bool** | Indicates whether continuous availability for Server Message Block (SMB) 3.0 is enabled for the SMB Share. Values are: - true - Continuous availability for SMB 3.0 is enabled for the SMB Share. - false - Continuous availability for SMB 3.0 is disabled for the SMB Share.  | [optional] 
**is_encryption_enabled** | **bool** | Indicates whether encryption for Server Message Block (SMB) 3.0 is enabled at the shared folder level. Values are: - true - Encryption for SMB 3.0 is enabled. - false - Encryption for SMB 3.0 is disabled.  | [optional] 
**is_abe_enabled** | **bool** | Indicates whether Access-based Enumeration (ABE) is enabled. ABE filters the list of available files and folders on a server to include only those to which the requesting user has access. Values are: - true - ABE is enabled. - false - ABE is disabled.  | [optional] 
**is_branch_cache_enabled** | **bool** | Indicates whether BranchCache optimization is enabled. BranchCache optimization technology copies content from your main office or hosted cloud content servers and caches the content at branch office locations, allowing client computers at branch offices to access the content locally rather than over the WAN. Values are: - true - BranchCache is enabled. - false - BranchCache is disabled.  | [optional] 
**offline_availability** | [**SMBShareOfflineAvailabilityEnum**](SMBShareOfflineAvailabilityEnum.md) |  | [optional] 
**umask** | **str** | The default UNIX umask for new files created on the Share. If not specified the umask defaults to 022. | [optional] [default to '022']
**offline_availability_l10n** | **str** | Localized message string corresponding to offline_availability | [optional] 
**file_system** | [**FileSystemInstance**](FileSystemInstance.md) | This is the embeddable reference form of file_system_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


