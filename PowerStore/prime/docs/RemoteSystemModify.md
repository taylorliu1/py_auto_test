# RemoteSystemModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | User-specified name of the remote system. Used only for non-PowerStore type remote systems. This value must contain 128 or fewer printable Unicode characters.  | [optional] 
**description** | **str** | User-specified description of the remote system.  | [optional] 
**management_address** | **str** | Management address of the remote system.  | [optional] 
**management_port** | **int** | Management port is applicable for PowerMax/VMAX remote system port.  Was added in version 3.0.0.0. | [optional] 
**remote_username** | **str** | Username used to access the remote system. Used only for non-PowerStore systems.  | [optional] 
**remote_password** | **str** | Password used to access the remote system. Used only for non-PowerStore systems.  | [optional] 
**data_network_latency** | [**RemoteSystemLatencyEnum**](RemoteSystemLatencyEnum.md) | Network latency for the PowerStore remote system.  | [optional] 
**file_connection_address** | **str** | Control station address of the VNX to establish file management connection from PowerStore. Not applicable for other remote systems. This address can be modified. Provide IP aliasing address to transparently handle connection failures from primary to secondary control station.  Was added in version 3.0.0.0. | [optional] 
**vnx_file_username** | **str** | User-specified VNX NAS administrator username. nasadmin account is preferred for file import.  Was added in version 3.0.0.0. | [optional] 
**vnx_file_password** | **str** | Password used to access the control station.  Was added in version 3.0.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


