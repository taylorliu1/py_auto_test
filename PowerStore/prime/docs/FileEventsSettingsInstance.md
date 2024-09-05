# FileEventsSettingsInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events_category** | [**FileEventsCategoryEnum**](FileEventsCategoryEnum.md) |  | [optional] 
**open_file_no_access** | **bool** | Sends a notification when a file is opened for a change other than read or write access. Protocols: SMB, NFS(v4).  | [optional] [default to False]
**open_file_read** | **bool** | Sends a notification when a file is opened for read access. Protocols: SMB, NFS(v4).  | [optional] [default to False]
**open_file_write** | **bool** | Sends a notification when a file is opened for write access. Protocols: SMB, NFS(v4).  | [optional] [default to False]
**create_file** | **bool** | Sends a notification when a file is created. Protocols: SMB, NFS(v3/v4).  | [optional] [default to False]
**create_dir** | **bool** | Sends a notification when a directory is created. Protocols: SMB, NFS(v3/v4).  | [optional] [default to False]
**delete_file** | **bool** | Sends a notification when a file is deleted. Protocols: SMB, NFS(v3/v4).  | [optional] [default to False]
**delete_dir** | **bool** | Sends a notification when a directory is deleted. Protocols: SMB, NFS(v3/v4).  | [optional] [default to False]
**close_modified** | **bool** | Sends a notification when a file was modified before closing. Protocols: SMB, NFS(v4).  | [optional] [default to False]
**close_unmodified** | **bool** | Sends a notification when a file was not modified before closing. Protocols: SMB, NFS(v4).  | [optional] [default to False]
**rename_file** | **bool** | Sends a notification when a file is renamed. Protocols: SMB, NFS(v3/v4).  | [optional] [default to False]
**rename_dir** | **bool** | Sends a notification when a directory is renamed. Protocols: SMB, NFS(v3/v4).  | [optional] [default to False]
**set_acl_file** | **bool** | Sends a notification when the security descriptor (ACL) on a files is modified. Protocols: SMB.  | [optional] [default to False]
**set_acl_dir** | **bool** | Sends a notification when the secuirty descriptor (ACL) on a directory is modified. Protocols: SMB.  | [optional] [default to False]
**open_dir** | **bool** | Sends a notification when a directory is opened. Protocols: SMB.  | [optional] [default to False]
**close_dir** | **bool** | Sends a notification when a directory is closed. Protocols: SMB.  | [optional] [default to False]
**file_read** | **bool** | Sends a notification when a file read is received over NFS. Protocols: NFS(v3/v4).  | [optional] [default to False]
**file_write** | **bool** | Sends a notification when a file write is received over NFS. Protocols: NFS(v3/v4).  | [optional] [default to False]
**set_sec_file** | **bool** | Sends a notification when a file security modification is received over NFS. Protocols: NFS(v3/v4).  | [optional] [default to False]
**set_sec_dir** | **bool** | Sends a notification when a directory security modification is received over NFS. Protocols: NFS(v3/v4).  | [optional] [default to False]
**open_file_read_offline** | **bool** | Sends a notification when a offline file is opened for read access. Protocols: SMB, NFS(v4).  | [optional] [default to False]
**open_file_write_offline** | **bool** | Sends a notification when a offline file in opened for write access. Protocols: SMB, NFS(v4).  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


