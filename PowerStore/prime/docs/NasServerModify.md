# NasServerModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the NAS server. | [optional] 
**description** | **str** | Description of the NAS server. | [optional] 
**current_node_id** | **str** | Unique identifier of the node on which the NAS server is running. | [optional] 
**preferred_node_id** | **str** | Unique identifier of the preferred node for the NAS server The initial value (on NAS server create) is taken from the current node. | [optional] 
**current_unix_directory_service** | [**NASServerCurrentUnixDirectoryServiceEnum**](NASServerCurrentUnixDirectoryServiceEnum.md) |  | [optional] 
**default_unix_user** | **str** | Default Unix user name used for granting access in case of Windows to Unix user mapping failure. When empty, access in such case is denied. | [optional] 
**default_windows_user** | **str** | Default Windows user name used for granting access in case of Unix to Windows user mapping failure. When empty, access in such case is denied. | [optional] 
**is_username_translation_enabled** | **bool** | Enable the possibility to match a windows account to a Unix account with different names | [optional] [default to False]
**is_auto_user_mapping_enabled** | **bool** | A Windows user must have a corresponding matching Unix user (uid) in order to connect. This attribute enables you to automatically generate this Unix user (uid), if that Windows user does not have any in the configured Unix directory service (UDS). In a pure SMB or non multi-protocol environment, this should be set to true.  | [optional] [default to False]
**production_i_pv4_interface_id** | **str** | Unique identifier of the preferred IPv4 production interface. | [optional] 
**production_i_pv6_interface_id** | **str** | Unique identifier of the preferred IPv6 production interface. | [optional] 
**backup_i_pv4_interface_id** | **str** | Unique identifier of the preferred IPv4 backup interface. | [optional] 
**backup_i_pv6_interface_id** | **str** | Unique identifier of the preferred IPv6 backup interface. | [optional] 
**file_events_publisher_id** | **str** | Unique identifier of the file events publisher. name:{name} can be used instead of {id}. For example:&#39;file_events_publisher_id&#39;:&#39;name:file_events_publisher_name&#39; Was added in version 3.0.0.0. | [optional] 
**file_events_publishing_mode** | [**FileEventsPublishingModeEnum**](FileEventsPublishingModeEnum.md) |  Was added in version 3.0.0.0. | [optional] 
**protection_policy_id** | **str** | Id of the protection policy applied to the nas server. Was added in version 3.0.0.0. | [optional] 
**is_replication_destination** | **bool** | Indicates nas server is a replication destination. Was added in version 3.0.0.0. | [optional] 
**is_production_mode_enabled** | **bool** | true (Production mode) - In this mode, the NAS Server is fully operational. A NAS Server that is not part of a replication is always in production mode. User data is accessible through regular protocols like SMB/NFS etc. Its configuration can also be changed without any restrictions. A NAS Server that is not part of a replication is always in production mode. false (Destination mode) - In this mode, user data access and configuration change is restricted. User file systems are all unmounted and so not directly accessible. The administrator may create a snapshot of a file system and share the snap. The data is then only accessible through NFS (not secure nfs) or NDMP. Only network settings of objects can be changed (overridden locally). This includes objects such as network interfaces, dns, nis, ldap etc... This allows a destination NAS Server to have appropriate local network services configured in the event of a failover. Was added in version 3.0.0.0. | [optional] 
**force** | **bool** | Normally a replication destination NAS server cannot be modified since it is controlled by replication. However, there can be cases where replication has failed or is no longer active and the replication destination NAS server needs to be cleaned up. With the force option, the user will be allowed to remove the protection policy from the replication destination NAS server provided that the replication session does not exists. This parameter defaults to false, if not specified. Was added in version 3.0.0.0. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


