# RemoteSystemCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**management_address** | **str** | Management IP address of the remote system instance. IPv4 and FQDN are supported for non-PowerStore remote systems. Both IPv4 and IPv6 and FQDN are supported for PowerStore remote systems.  | [optional] 
**management_port** | **int** | Management port is applicable only for creating PowerMax/VMAX remote system.  Was added in version 3.0.0.0. | [optional] [default to 5443]
**name** | **str** | User-specified name of the remote system. Used only for non-PowerStore systems. This value must contain 128 or fewer printable Unicode characters.  | [optional] 
**description** | **str** | User-specified description of the remote system.  | [optional] 
**type** | [**RemoteSystemTypeEnum**](RemoteSystemTypeEnum.md) |  | [optional] 
**remote_username** | **str** | Username used to access the remote system.  | [optional] 
**remote_password** | **str** | Password used to access the remote system.  | [optional] 
**data_connection_type** | [**DataConnectionTypeEnum**](DataConnectionTypeEnum.md) |  Was added in version 3.0.0.0. | [optional] 
**iscsi_addresses** | **list[str]** | iSCSI target IP addresses for the data connection to the remote system. Must be specified when creating a non-PowerStore remote system.  | [optional] 
**import_chap_info** | [**ChapCredentialsInstance**](ChapCredentialsInstance.md) | Chap information to be used for session and discovery. This is applicable to non-PowerStore remote systems.  | [optional] 
**discovery_chap_mode** | [**RemoteSystemChapModeEnum**](RemoteSystemChapModeEnum.md) |  | [optional] 
**session_chap_mode** | [**RemoteSystemChapModeEnum**](RemoteSystemChapModeEnum.md) |  | [optional] 
**data_network_latency** | [**RemoteSystemLatencyEnum**](RemoteSystemLatencyEnum.md) |  | [optional] 
**file_connection_address** | **str** | Control station address of the VNX to establish file management connection from PowerStore. Not applicable for other remote systems. This address can be modified. Provide IP aliasing address to transparently handle connection failures from primary to secondary control station.  Was added in version 3.0.0.0. | [optional] 
**vnx_file_username** | **str** | User-specified VNX NAS administrator username. nasadmin account is preferred for file import.  Was added in version 3.0.0.0. | [optional] 
**vnx_file_password** | **str** | Password used to access the control station.  Was added in version 3.0.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


