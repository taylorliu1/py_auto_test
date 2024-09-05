# FileEventsPoolModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name assigned to the set of Windows servers where file event service software is installed.  | [optional] 
**file_events_publisher_servers** | **list[str]** | File event service server addresses, in IPv4, IPv6, or FQDN format. Up to five file event service servers may be set per file events pool.  | [optional] 
**destination_file_events_publisher_servers** | **list[str]** | If this value is set file event service server addresses will be overridden on the destination with these values. File event service server addresses, in IPv4, IPv6, or FQDN format. Up to five file event service servers may be set per file events pool.  | [optional] 
**file_events_settings** | [**list[FileEventsSettingsInstance]**](FileEventsSettingsInstance.md) | List of up to three (one per category) sets of file event settings.  | [optional] 
**remove_categories** | [**list[FileEventsCategoryEnum]**](FileEventsCategoryEnum.md) | List of up to three (one per category) sets of file event settings to be removed.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


