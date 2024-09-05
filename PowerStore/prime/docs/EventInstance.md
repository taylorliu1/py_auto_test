# EventInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of this occurrence of an event. | [optional] 
**event_code** | **str** | Identifies the specific kind of event that has occurred. | [optional] 
**severity** | [**SeverityEnum**](SeverityEnum.md) | The severity of the event. | [optional] 
**resource_type** | [**ResourceTypeEnum**](ResourceTypeEnum.md) | The type of the object which generated this event. | [optional] 
**resource_id** | **str** | Unique identifier of the resource instance which generated this event. | [optional] 
**resource_name** | **str** | Name of the resource instance which generated this event.  This property supports case-insensitive filtering. | [optional] 
**generated_timestamp** | **datetime** | Timestamp at which this event occured. | [optional] 
**description_l10n** | **str** | Description of this event. | [optional] 
**system_impact_l10n** | **str** | Describes the possible effect on the system of this event. | [optional] 
**repair_flow_l10n** | **str** | Suggestions for how to resolve any problems that may arise from this event. | [optional] 
**severity_l10n** | **str** | Localized message string corresponding to severity | [optional] 
**resource_type_l10n** | **str** | Localized message string corresponding to resource_type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


