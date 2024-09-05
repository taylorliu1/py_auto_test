# NasServerCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the NAS server. | 
**description** | **str** | Description of the NAS server. | [optional] 
**current_unix_directory_service** | [**NASServerCurrentUnixDirectoryServiceEnum**](NASServerCurrentUnixDirectoryServiceEnum.md) |  | [optional] 
**default_unix_user** | **str** | Default Unix user name used for granting access in case of Windows to Unix user mapping failure. When empty, access in such case is denied. | [optional] 
**default_windows_user** | **str** | Default Windows user name used for granting access in case of Unix to Windows user mapping failure. When empty, access in such case is denied. | [optional] 
**is_username_translation_enabled** | **bool** | Enable the possibility to match a Windows account with an Unix account with different names. | [optional] [default to False]
**is_auto_user_mapping_enabled** | **bool** | A Windows user must have a corresponding matching Unix user (uid) in order to connect. This attribute enables you to automatically generates this Unix user (uid), if that Windows user does not have any in the configured Unix directory service (UDS). In a pure SMB or non multi-protocol environment, this should be set to true.  | [optional] [default to False]
**protection_policy_id** | **str** | Id of the protection policy applied to the nas server. It is mandatory for policy to have replication rule before associating to nas server. Was added in version 3.0.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


