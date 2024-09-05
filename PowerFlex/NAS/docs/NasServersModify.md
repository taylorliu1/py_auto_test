# NasServersModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the NAS server. | [optional] 
**description** | **str** | Description of the NAS server. | [optional] 
**current_unix_directory_service** | [**NASServersCurrentUnixDirectoryServiceEnum**](NASServersCurrentUnixDirectoryServiceEnum.md) |  | [optional] 
**default_unix_user** | **str** | Default Unix user name used for granting access in case of Windows to Unix user mapping failure. When empty, access in such case is denied. | [optional] 
**default_windows_user** | **str** | Default Windows user name used for granting access in case of Unix to Windows user mapping failure. When empty, access in such case is denied. | [optional] 
**is_username_translation_enabled** | **bool** | Enable the possibility to match a windows account to a Unix account with different names | [optional] [default to False]
**is_auto_user_mapping_enabled** | **bool** | A Windows user must have a corresponding matching Unix user (uid) in order to connect. This attribute enables you to automatically generate this Unix user (uid), if that Windows user does not have any in the configured Unix directory service (UDS). In a pure SMB or non multi-protocol environment, this should be set to true.  | [optional] [default to False]
**production_ipv4_interface_id** | **str** | Unique identifier of the preferred IPv4 production interface. | [optional] 
**production_ipv6_interface_id** | **str** | Unique identifier of the preferred IPv6 production interface. | [optional] 
**backup_ipv4_interface_id** | **str** | Unique identifier of the preferred IPv4 backup interface. | [optional] 
**backup_ipv6_interface_id** | **str** | Unique identifier of the preferred IPv6 backup interface. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

