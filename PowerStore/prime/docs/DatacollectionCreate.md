# DatacollectionCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**DatacollectionResourceInstance**](DatacollectionResourceInstance.md) |  | [optional] 
**profiles** | **list[str]** | The profiles to use for the data collection. | [optional] 
**datacollection_profile_ids** | **list[str]** | The profiles to use for the data collection. | [optional] 
**description** | **str** | Brief note describing the purpose of the data collection. | [optional] [default to '']
**upload_to_support** | **bool** | Automatically upload this Data Collection to your support provider after it is complete. This option is only available if SupportAssist is enabled. | [optional] [default to False]
**log_from_timestamp** | **datetime** | The date and time from which to start collecting the logs. | [optional] 
**log_to_timestamp** | **datetime** | The date and time up to which the logs should be collected.  The default is the time of the creation. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


