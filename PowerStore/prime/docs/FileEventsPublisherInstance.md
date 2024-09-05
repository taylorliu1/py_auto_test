# FileEventsPublisherInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the file events publisher. | [optional] 
**name** | **str** | Unique name of the file events publisher.  This property supports case-insensitive filtering. | [optional] 
**is_enabled** | **bool** | Whether or not the event publisher will publish events. | [optional] 
**heartbeat** | **int** | Time interval to scan each CEPA server (in seconds) for online/offline status.  | [optional] [default to 10]
**connection_timeout** | **int** | Timeout in milliseconds while attempting to send event to a CEPA server to determine that is offline.  | [optional] [default to 1000]
**post_event_policy** | [**PostEventPolicyEnum**](PostEventPolicyEnum.md) |  | [optional] 
**deny_access_when_all_servers_offline** | **bool** | Behavior when no configured file events servers respond. Values are: false - allow I/O to the file system to continue. true - deny I/O to the filesystem when an event cannot be published to any server.  | [optional] [default to False]
**username** | **str** | Name of a Windows user allowing Events Publishing to connect to CEPA servers. To ensure that a secure connection (via Microsoft RPC protocol) is used disable HTTP by setting http_port to 0.  | [optional] 
**http_port** | **int** | TCP port number used but the service to connect to the CEPA server(s) with HTTP. Default port number is 12228. Set this value to 0 to disable HTTP. When enabled, connection via HTTP is attempted first. If HTTP connection is disabled, or the connection fails, then connection through MSRPC is attempted if all CEPP server(s) are defined by FQDN. The SMB account of the NAS server in the AD Domain is used to make the connection via MSRPC. Note that HTTP connections should only be used on secure networks, as it is neither SSL nor authenticated.  | [optional] [default to 12228]
**is_replica** | **bool** | Flag indicates if the file events publisher is a replicated publisher.  | [optional] [default to False]
**post_event_policy_l10n** | **str** | Localized message string corresponding to post_event_policy Was added in version 3.0.0.0. | [optional] 
**file_events_pools** | [**list[FileEventsPoolInstance]**](FileEventsPoolInstance.md) | List of the file_events_pools that are associated with this file_events_publisher. | [optional] 
**nas_servers** | [**list[NasServerInstance]**](NasServerInstance.md) | List of the nas_servers that are associated with this file_events_publisher. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


