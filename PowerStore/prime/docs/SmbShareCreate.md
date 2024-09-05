# SmbShareCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_system_id** | **str** | Unique identifier of the file system on which the SMB Share will be created. name:{name} can be used instead of {id}. For example:&#39;file_system_id&#39;:&#39;name:file_system_name&#39; | 
**path** | **str** | Local path to the file system or any existing sub-folder of the file system that is shared over the network. This path is relative to the NAS Server and must start with the filesystem&#39;s mountpoint path, which is the filesystem name. For example to share the top-level of a filesystem named svr1fs1, which is on the /svr1fs1 mountpoint of the NAS Server, use /svr1fs1 in the path parameter. SMB shares allow you to create multiple network shares for the same local path.  | 
**name** | **str** | SMB share name. | 
**description** | **str** | SMB share description. | [optional] 
**is_abe_enabled** | **bool** | Indicates whether Access-based Enumeration (ABE) is enabled. ABE filters the list of available files and folders on a server to include only those to which the requesting user has access. Values are: - true - ABE is enabled. - false - ABE is disabled.  | [optional] [default to False]
**is_branch_cache_enabled** | **bool** | Indicates whether BranchCace optimization is enabled. BranchCache optimization technology copies content from your main office or hosted cloud content servers and caches the content at branch office locations, allowing client computers at branch offices to access the content locally rather than over the WAN. Values are: - true - BranchCache is enabled. - false - BranchCache is disabled.  | [optional] [default to False]
**offline_availability** | [**SMBShareOfflineAvailabilityEnum**](SMBShareOfflineAvailabilityEnum.md) |  | [optional] 
**umask** | **str** | The default UNIX umask for new files created on the Share. If not specified the umask defaults to 022. | [optional] [default to '022']
**is_continuous_availability_enabled** | **bool** | Indicates whether continuous availability for Server Message Block (SMB) 3.0 is enabled for the SMB Share. Values are: - true - Continuous availability for SMB 3.0 is enabled for the SMB Share. - false - Continuous availability for SMB 3.0 is disabled for the SMB Share.  | [optional] [default to False]
**is_encryption_enabled** | **bool** | Indicates whether encryption for Server Message Block (SMB) 3.0 is enabled at the shared folder level. Values are: - true - encryption for SMB 3.0 is enabled. - false - encryption for SMB 3.0 is disabled.  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


