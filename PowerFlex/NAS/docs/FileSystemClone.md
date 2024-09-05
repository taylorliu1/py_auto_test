# FileSystemClone

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the clone. | 
**description** | **str** | Description of the clone. | [optional] 
**access_policy** | [**FileSystemAccessPolicyEnum**](FileSystemAccessPolicyEnum.md) |  | [optional] 
**locking_policy** | [**FileSystemLockingPolicyEnum**](FileSystemLockingPolicyEnum.md) |  | [optional] 
**folder_rename_policy** | [**FileSystemFolderRenamePolicyEnum**](FileSystemFolderRenamePolicyEnum.md) |  | [optional] 
**is_smb_sync_writes_enabled** | **bool** | Indicates whether the synchronous writes option is enabled on the file system. Values are: * true - Synchronous writes option is enabled on the file system. * false - Synchronous writes option is disabled on the file system.  | [optional] 
**is_smb_no_notify_enabled** | **bool** | Indicates whether notifications of changes to directory file structure are enabled. * true - Change directory notifications are enabled. * false - Change directory notifications are disabled.                        | [optional] 
**is_smb_op_locks_enabled** | **bool** | Indicates if opportunistic file locking is enabled on the file system. Values are: * true - Opportunistic file locking is enabled on the file system. * false - Opportunistic file locking is disabled on the file system.  | [optional] 
**is_smb_notify_on_access_enabled** | **bool** | Indicates whether file access notifications are enabled on the file system. Values are: * true - File system notifications are enabled on the file system. * false - File system notifications are disabled on the file system.  | [optional] 
**is_smb_notify_on_write_enabled** | **bool** | Indicates whether file writes notifications are enabled on the file system. Values are: * true - File writes notifications are enabled on the file system. * false - File writes notifications are disabled on the file system.  | [optional] 
**smb_notify_on_change_dir_depth** | **int** | Lowest directory level to which the enabled notifications apply, if any. | [optional] 
**is_async_m_time_enabled** | **bool** | Indicates whether asynchronous MTIME is enabled on the file system. Values are: * true - Asynchronous MTIME is enabled on the file system. * false - Asynchronous MTIME is disabled on the file system.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

