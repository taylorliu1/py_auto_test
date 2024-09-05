# FileSystemCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the file system. (255 UTF-8 characters). | 
**description** | **str** | File system description. (255 UTF-8 characters). | [optional] 
**size_total** | **int** | Size that the file system presents to the host or end user. (Bytes) Value is always rounded up to next MB.  | 
**storage_pool_id** | **str** | Id of the Storage pool on which the file system has to be provisioned. | 
**nas_server_id** | **str** | Id of the NAS Server on which the file system is mounted. | 
**access_policy** | [**FileSystemAccessPolicyEnum**](FileSystemAccessPolicyEnum.md) |  | [optional] 
**locking_policy** | [**FileSystemLockingPolicyEnum**](FileSystemLockingPolicyEnum.md) |  | [optional] 
**folder_rename_policy** | [**FileSystemFolderRenamePolicyEnum**](FileSystemFolderRenamePolicyEnum.md) |  | [optional] 
**is_smb_sync_writes_enabled** | **bool** | Indicates whether the synchronous writes option is enabled on the file system. Values are: * true - Synchronous writes option is enabled on the file system. * false - Synchronous writes option is disabled on the file system.  | [optional] [default to False]
**is_smb_no_notify_enabled** | **bool** | Indicates whether notifications of changes to directory file structure are enabled. * true - Change directory notifications are enabled. * false - Change directory notifications are disabled.                        | [optional] [default to False]
**is_smb_op_locks_enabled** | **bool** | Indicates whether opportunistic file locking is enabled on the file system. Values are: * true - Opportunistic file locking is enabled on the file system. * false - Opportunistic file locking is disabled on the file system.  | [optional] [default to True]
**is_smb_notify_on_access_enabled** | **bool** | Indicates whether file access notifications are enabled on the file system. Values are: * true - File access notifications are enabled on the file system. * false - File access notifications are disabled on the file system.  | [optional] [default to False]
**is_smb_notify_on_write_enabled** | **bool** | Indicates whether file writes notifications are enabled on the file system. Values are: * true - File writes notifications are enabled on the file system. * false - File writes notifications are disabled on the file system.  | [optional] [default to False]
**smb_notify_on_change_dir_depth** | **int** | Lowest directory level to which the enabled notifications apply, if any. | [optional] 
**is_async_m_time_enabled** | **bool** | Indicates whether asynchronous MTIME is enabled on the file system or protocol snaps that are mounted writeable. Values are: * true - Asynchronous MTIME is enabled on the file system. * false - Asynchronous MTIME is disabled on the file system.  | [optional] [default to False]
**protection_policy_id** | **str** | Id of the protection policy applied to the file system. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

