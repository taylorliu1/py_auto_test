# FileEventsPoolInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the file event pool instance. | [optional] 
**name** | **str** | Name assigned to the set of Windows servers where file event service software is installed.   This property supports case-insensitive filtering. | [optional] 
**file_events_publisher_servers** | **list[str]** | File event service server addresses, in IPv4, IPv6, or FQDN format. Up to five file event service servers may be set per file events pool.  | [optional] 
**destination_file_events_publisher_servers** | **list[str]** | This value is used to modify file event service server addresses of this resource when the associated NAS server is a replication destination i.e, is_replica is set.  - If this value is set, file event service server addresses on the destination will be overridden with these values. - If this value is empty, file event service server addresses on the destination will be reset to the ones from the source.  File event service server addresses, in IPv4, IPv6, or FQDN format. Up to five file event service servers may be set per file events pool.  | [optional] 
**file_events_settings** | [**list[FileEventsSettingsInstance]**](FileEventsSettingsInstance.md) | List of up to three (one per category) sets of file event settings.   Filtering on the fields of this embedded resource is not supported. | [optional] 
**is_replica** | **bool** | Flag indicates if the file events pool is a replicated pool.  | [optional] [default to False]
**file_events_publishers** | [**list[FileEventsPublisherInstance]**](FileEventsPublisherInstance.md) | List of the file_events_publishers that are associated with this file_events_pool. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


