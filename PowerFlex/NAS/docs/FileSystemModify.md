# FileSystemModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | File system description. (255 UTF-8 characters). | [optional] 
**size_total** | **int** | Size, in bytes, presented to the host or end user. This can be used for both expand and shrink on a file system. Value is always rounded up to next MB.  | [optional] 
**access_policy** | [**FileSystemAccessPolicyEnum**](FileSystemAccessPolicyEnum.md) |  | [optional] 
**locking_policy** | [**FileSystemLockingPolicyEnum**](FileSystemLockingPolicyEnum.md) |  | [optional] 
**folder_rename_policy** | [**FileSystemFolderRenamePolicyEnum**](FileSystemFolderRenamePolicyEnum.md) |  | [optional] 
**is_smb_sync_writes_enabled** | **bool** | Indicates whether the synchronous writes option is enabled on the file system. Values are: * true - Synchronous writes option is enabled on the file system. * false - Synchronous writes option is disabled on the file system.  | [optional] 
**is_smb_op_locks_enabled** | **bool** | Indicates whether opportunistic file locking is enabled on the file system. Values are: * true - Opportunistic file locking is enabled on the file system. * false - Opportunistic file locking is disabled on the file system.  | [optional] 
**is_smb_notify_on_access_enabled** | **bool** | Indicates whether file access notifications are enabled on the file system. Values are: * true - File access notifications are enabled on the file system. * false - File access notifications on file access are disabled on the file system.  | [optional] 
**is_smb_notify_on_write_enabled** | **bool** | Indicates whether notifications on file writes are enabled on the file system. Values are: * true - File writes notifications are enabled on the file system. * false - File writes notifications are disabled on the file system.  | [optional] 
**smb_notify_on_change_dir_depth** | **int** | Lowest directory level to which the enabled notifications apply, if any. | [optional] 
**is_smb_no_notify_enabled** | **bool** | Indicates whether notifications of changes to a directory file structure are enabled. Values are: * true - Change directory notifications are enabled. * false - Change directory notifications are disabled.  | [optional] 
**is_async_m_time_enabled** | **bool** | Indicates whether asynchronous MTIME is enabled on the file system or protocol snaps that are mounted writeable. Values are: * true - Asynchronous MTIME is enabled on the file system. * false - Asynchronous MTIME is disabled on the file system.  | [optional] 
**protection_policy_id** | **str** | Id of the protection policy applied to the file system. | [optional] 
**is_quota_enabled** | **bool** | Indicates whether quota is enabled.  Quotas are not supported for read-only file systems.  Default value for the grace period is set to infinite&#x3D;-1 to match Windows&#x27; quota policy Values are: * true - Start tracking usages for all users on a file system or a quota tree, and user quota limits will be enforced. * false - Stop tracking usages for all users on a file system or a quota tree, and user quota limits will not be enforced.  | [optional] 
**grace_period** | **int** | Grace period of soft limits (seconds):  -1: default: Infinite grace (Windows policy).   0: Use system default of 1 week.  positive: Grace period after which the soft limit is treated as a hard limit (seconds).  | [optional] [default to -1]
**default_hard_limit** | **int** | Default hard limit of user quotas and tree quotas (bytes). The hard limit value is always rounded up to match the file system&#x27;s physical block size. (0 means &#x27;No limitation&#x27;. This value can be used to compute the amount of space consumed without limiting the space).  | [optional] 
**default_soft_limit** | **int** | Default soft limit of user quotas and tree quotas (bytes). Value is always rounded up to match the file system&#x27;s physical block size. (0 means &#x27;No limitation&#x27;.)  | [optional] 
**expiration_timestamp** | **datetime** | Time when the snapshot will expire. Use 1970-01-01T00:00:00.000Z to set expiration timestamp to null. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

