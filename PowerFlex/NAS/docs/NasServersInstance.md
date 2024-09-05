# NasServersInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the NAS server. | [optional] 
**name** | **str** | Name of the NAS server.  This property supports case-insensitive filtering. | [optional] 
**protection_domain_id** | **str** | Unique identifier of the NAS enabled Protection Domain. | [optional] 
**storage_pool_id** | **str** | Storage Pool Id of NAS configuration volumes. | [optional] 
**description** | **str** | Description of the NAS server. | [optional] 
**operational_status** | [**NASServersOperationalStatusEnum**](NASServersOperationalStatusEnum.md) |  | [optional] 
**primary_node_id** | **str** | Unique identifier of the primary node on which the NAS server is running. | [optional] 
**backup_node_id** | **str** | Unique identifier of the backup node of NAS server. | [optional] 
**default_unix_user** | **str** | Default Unix user name used for granting access in case of Windows to Unix user mapping failure. When empty, access in such case is denied. | [optional] 
**default_windows_user** | **str** | Default Windows user name used for granting access in case of Unix to Windows user mapping failure. When empty, access in such case is denied. | [optional] 
**current_unix_directory_service** | [**NASServersCurrentUnixDirectoryServiceEnum**](NASServersCurrentUnixDirectoryServiceEnum.md) |  | [optional] 
**is_username_translation_enabled** | **bool** | Enable the possibility to match a windows account to a Unix account with different names. | [optional] [default to False]
**is_auto_user_mapping_enabled** | **bool** | A Windows user must have a corresponding matching Unix user (uid) in order to connect. This attribute enables you to automatically generate this Unix user (uid), if that Windows user does not have any in the configured Unix directory service (UDS). In a pure SMB or non multi-protocol environment, this should be set to true.  | [optional] [default to False]
**production_ipv4_interface_id** | **str** | Unique identifier of the preferred IPv4 production interface. | [optional] 
**production_ipv6_interface_id** | **str** | Unique identifier of the preferred IPv6 production interface. | [optional] 
**backup_ipv4_interface_id** | **str** | Unique identifier of the preferred IPv4 backup interface. | [optional] 
**backup_ipv6_interface_id** | **str** | Unique identifier of the preferred IPv6 backup interface. | [optional] 
**current_preferred_ipv4_interface_id** | **str** | Unique identifier of the current active preferred IPv4 interface. | [optional] 
**current_preferred_ipv6_interface_id** | **str** | Unique identifier of the current active preferred IPv6 interface. | [optional] 
**operational_status_l10n** | **str** | Localized message string corresponding to operational_status | [optional] 
**current_unix_directory_service_l10n** | **str** | Localized message string corresponding to current_unix_directory_service | [optional] 
**file_interfaces** | [**list[FileInterfaceInstance]**](FileInterfaceInstance.md) | This is the inverse of the resource type file_interface association. | [optional] 
**file_ndmps** | [**list[FileNdmpInstance]**](FileNdmpInstance.md) | This is the inverse of the resource type file_ndmp association. | [optional] 
**file_virus_checkers** | [**list[FileVirusCheckerInstance]**](FileVirusCheckerInstance.md) | This is the inverse of the resource type file_virus_checker association. | [optional] 
**nfs_servers** | [**list[NfsServerInstance]**](NfsServerInstance.md) | This is the inverse of the resource type nfs_server association. | [optional] 
**smb_servers** | [**list[SmbServerInstance]**](SmbServerInstance.md) | This is the inverse of the resource type smb_server association. | [optional] 
**file_dnses** | [**list[FileDnsInstance]**](FileDnsInstance.md) | This is the inverse of the resource type file_dns association. | [optional] 
**file_ftps** | [**list[FileFtpInstance]**](FileFtpInstance.md) | This is the inverse of the resource type file_ftp association. | [optional] 
**file_kerberoses** | [**list[FileKerberosInstance]**](FileKerberosInstance.md) | This is the inverse of the resource type file_kerberos association. | [optional] 
**file_ldaps** | [**list[FileLdapInstance]**](FileLdapInstance.md) | This is the inverse of the resource type file_ldap association. | [optional] 
**file_nises** | [**list[FileNisInstance]**](FileNisInstance.md) | This is the inverse of the resource type file_nis association. | [optional] 
**file_systems** | [**list[FileSystemInstance]**](FileSystemInstance.md) | This is the inverse of the resource type file_system association. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

