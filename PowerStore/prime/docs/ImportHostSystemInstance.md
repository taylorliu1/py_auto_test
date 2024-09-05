# ImportHostSystemInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the import host system. | [optional] 
**agent_address** | **str** | Hostname or IPv4 address of the import host system. | [optional] 
**agent_type** | [**HostAgentTypeEnum**](HostAgentTypeEnum.md) |  | [optional] 
**agent_port** | **int** | TCP port on the import host system. | [optional] 
**agent_version** | **str** | Version of the import host system. | [optional] 
**agent_api_version** | **str** | API version of the import host system. | [optional] 
**os_type** | [**HAOSTypeEnum**](HAOSTypeEnum.md) |  | [optional] 
**os_version** | **str** | Operating system version of the import host system. | [optional] 
**agent_status** | [**HostAgentStatusEnum**](HostAgentStatusEnum.md) |  | [optional] 
**user_name** | **str** | Username for the import host system. | [optional] 
**last_update_time** | **datetime** | Time when the import host system was last updated. | [optional] 
**agent_type_l10n** | **str** | Localized message string corresponding to agent_type | [optional] 
**os_type_l10n** | **str** | Localized message string corresponding to os_type | [optional] 
**agent_status_l10n** | **str** | Localized message string corresponding to agent_status | [optional] 
**hosts** | [**list[HostInstance]**](HostInstance.md) | This is the inverse of the resource type host association. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


