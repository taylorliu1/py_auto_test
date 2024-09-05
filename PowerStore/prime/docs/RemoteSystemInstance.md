# RemoteSystemInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the remote system instance.  | [optional] 
**name** | **str** | User-specified name of the remote system instance.   This property supports case-insensitive filtering. | [optional] 
**description** | **str** | User-specified description of the remote system instance.  | [optional] 
**serial_number** | **str** | Serial number of the remote system instance.  | [optional] 
**version** | **str** | Version of the remote system.  Was added in version 2.0.0.0. | [optional] 
**management_address** | **str** | Management address of the remote system instance.  | [optional] 
**management_port** | **int** | Management port of PowerMax/VMAX remote system.  Was added in version 3.0.0.0. | [optional] 
**type** | [**RemoteSystemTypeEnum**](RemoteSystemTypeEnum.md) | Type of the remote system.  | [optional] 
**user_name** | **str** | Username used to access the non-PowerStore remote systems.  | [optional] 
**state** | [**RemoteSystemStateEnum**](RemoteSystemStateEnum.md) | Current state of the remote system.  | [optional] 
**data_connection_type** | [**DataConnectionTypeEnum**](DataConnectionTypeEnum.md) | Type of the data connection.  Was added in version 3.0.0.0. | [optional] 
**data_connection_state** | [**DataConnectionStateEnum**](DataConnectionStateEnum.md) | State of the data connection.  | [optional] 
**iscsi_addresses** | **list[str]** | iSCSI target addresses for the data connection to the remote system.  | [optional] 
**fc_target_wwns** | **list[str]** | FC target WWN discovered by Powerstore for the data connection to the remote system.  Was added in version 3.0.0.0. | [optional] 
**discovery_chap_mode** | [**RemoteSystemChapModeEnum**](RemoteSystemChapModeEnum.md) | Discovery chap mode for the non-PowerStore remote system.  | [optional] 
**session_chap_mode** | [**RemoteSystemChapModeEnum**](RemoteSystemChapModeEnum.md) | Session chap mode for the non-PowerStore remote system.  | [optional] 
**data_network_latency** | [**RemoteSystemLatencyEnum**](RemoteSystemLatencyEnum.md) | Network latency for the remote system.  | [optional] 
**data_connections** | [**list[DataConnectionInstance]**](DataConnectionInstance.md) | List of data connections from each appliance in the local cluster to target address.   Filtering on the fields of this embedded resource is not supported. | [optional] 
**capabilities** | [**list[RemoteProtectionCapabilityEnum]**](RemoteProtectionCapabilityEnum.md) | List of remote protection capabilities.  Was added in version 3.0.0.0. | [optional] 
**file_connection_address** | **str** | A public IPv4 or IPv6 address of a file remote system instance. File mobility network cluster IP address for PowerStore. Control station address for VNX2.  Was added in version 3.0.0.0. | [optional] 
**file_connection_state** | [**RemoteSystemFileConnectionStateEnum**](RemoteSystemFileConnectionStateEnum.md) |  Was added in version 3.0.0.0. | [optional] 
**vnx_file_username** | **str** | User-specified VNX NAS administrator username. nasadmin account is preferred for file import.  Was added in version 3.0.0.0. | [optional] 
**appliance_details** | [**list[RemoteApplianceDetails]**](RemoteApplianceDetails.md) | Details of all the appliances of the remote PowerStore system.  Was added in version 3.0.0.0.  Filtering on the fields of this embedded resource is not supported. | [optional] 
**type_l10n** | **str** | Localized message string corresponding to type | [optional] 
**state_l10n** | **str** | Localized message string corresponding to state | [optional] 
**data_connection_type_l10n** | **str** | Localized message string corresponding to data_connection_type Was added in version 3.0.0.0. | [optional] 
**data_connection_state_l10n** | **str** | Localized message string corresponding to data_connection_state | [optional] 
**discovery_chap_mode_l10n** | **str** | Localized message string corresponding to discovery_chap_mode | [optional] 
**session_chap_mode_l10n** | **str** | Localized message string corresponding to session_chap_mode | [optional] 
**data_network_latency_l10n** | **str** | Localized message string corresponding to data_network_latency | [optional] 
**capabilities_l10n** | **list[str]** | Localized message array corresponding to capabilities Was added in version 3.0.0.0. | [optional] 
**file_connection_state_l10n** | **str** | Localized message string corresponding to file_connection_state Was added in version 3.0.0.0. | [optional] 
**import_sessions** | [**list[ImportSessionInstance]**](ImportSessionInstance.md) | This is the inverse of the resource type import_session association. | [optional] 
**storage_container_destinations** | [**list[StorageContainerDestinationInstance]**](StorageContainerDestinationInstance.md) | This is the inverse of the resource type storage_container_destination association. | [optional] 
**replication_sessions** | [**list[ReplicationSessionInstance]**](ReplicationSessionInstance.md) | This is the inverse of the resource type replication_session association. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


