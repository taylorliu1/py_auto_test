# VolumeGroupSnapshot

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique name of the snapshot set to be created. | 
**description** | **str** | Optional description for the snapshot set. If description is not specified, the description for the snapshot set will not be set. | [optional] 
**expiration_timestamp** | **str** | Time after which the snapshot set can be auto-purged. Time must be specified in Zulu time zone. Expiration time cannot be prior to current time. Use a maximum timestamp value to set an expiration to never expire. Valid format is yyyy-MM-dd&#39;T&#39;HH:mm:ssZ or yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ. By default, expiration time will not be set. Was added in version 2.0.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


