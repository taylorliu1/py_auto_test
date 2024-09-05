# NasServerInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the NAS server. | [optional] 
**name** | **str** | Name of the NAS server.  This property supports case-insensitive filtering. | [optional] 
**description** | **str** | Description of the NAS server. | [optional] 
**operational_status** | [**NASServerOperationalStatusEnum**](NASServerOperationalStatusEnum.md) |  | [optional] 
**current_node_id** | **str** | Unique identifier of the node on which the NAS server is running. | [optional] 
**preferred_node_id** | **str** | Unique identifier of the preferred node for the NAS server The initial value (on NAS server creation) is taken from the current node. | [optional] 
**default_unix_user** | **str** | Default Unix user name used for granting access in case of Windows to Unix user mapping failure. When empty, access in such case is denied. | [optional] 
**default_windows_user** | **str** | Default Windows user name used for granting access in case of Unix to Windows user mapping failure. When empty, access in such case is denied. | [optional] 
**current_unix_directory_service** | [**NASServerCurrentUnixDirectoryServiceEnum**](NASServerCurrentUnixDirectoryServiceEnum.md) |  | [optional] 
**is_username_translation_enabled** | **bool** | Enable the possibility to match a windows account to a Unix account with different names. | [optional] [default to False]
**is_auto_user_mapping_enabled** | **bool** | A Windows user must have a corresponding matching Unix user (uid) in order to connect. This attribute enables you to automatically generate this Unix user (uid), if that Windows user does not have any in the configured Unix directory service (UDS). In a pure SMB or non multi-protocol environment, this should be set to true.  | [optional] [default to False]
**production_i_pv4_interface_id** | **str** | Unique identifier of the preferred IPv4 production interface. | [optional] 
**production_i_pv6_interface_id** | **str** | Unique identifier of the preferred IPv6 production interface. | [optional] 
**backup_i_pv4_interface_id** | **str** | Unique identifier of the preferred IPv4 backup interface. | [optional] 
**backup_i_pv6_interface_id** | **str** | Unique identifier of the preferred IPv6 backup interface. | [optional] 
**current_preferred_i_pv4_interface_id** | **str** | Unique identifier of the current active preferred IPv4 interface. | [optional] 
**current_preferred_i_pv6_interface_id** | **str** | Unique identifier of the current active preferred IPv6 interface. | [optional] 
**protection_policy_id** | **str** | Id of the protection policy applied to the nas server. Was added in version 3.0.0.0. | [optional] 
**file_events_publishing_mode** | [**FileEventsPublishingModeEnum**](FileEventsPublishingModeEnum.md) |  Was added in version 3.0.0.0. | [optional] 
**is_replication_destination** | **bool** | Indicates nas server is a replication destination. Was added in version 3.0.0.0. | [optional] 
**is_production_mode_enabled** | **bool** | true (Production mode) - In this mode, the NAS Server is fully operational. A NAS Server that is not part of a replication is always in production mode. User data is accessible through regular protocols like SMB/NFS etc. Its configuration can also be changed without any restrictions. A NAS Server that is not part of a replication is always in production mode. false (Destination mode) - In this mode, user data access and configuration change is restricted. User file systems are all unmounted and so not directly accessible. The administrator may create a snapshot of a file system and share the snap. The data is then only accessible through NFS (not secure nfs) or NDMP. Only network settings of objects can be changed (overridden locally). This includes objects such as network interfaces, dns, nis, ldap etc... This allows a destination NAS Server to have appropriate local network services configured in the event of a failover. Was added in version 3.0.0.0. | [optional] 
**operational_status_l10n** | **str** | Localized message string corresponding to operational_status | [optional] 
**current_unix_directory_service_l10n** | **str** | Localized message string corresponding to current_unix_directory_service | [optional] 
**file_events_publishing_mode_l10n** | **str** | Localized message string corresponding to file_events_publishing_mode Was added in version 3.0.0.0. | [optional] 
**protection_policy** | [**PolicyInstance**](PolicyInstance.md) | This is the embeddable reference form of protection_policy_id attribute. | [optional] 
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
**file_dhsm_configs** | [**list[FileDhsmConfigInstance]**](FileDhsmConfigInstance.md) | This is the inverse of the resource type file_dhsm_config association. | [optional] 
**file_events_publishers** | [**list[FileEventsPublisherInstance]**](FileEventsPublisherInstance.md) | List of the file_events_publishers that are associated with this nas_server. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


