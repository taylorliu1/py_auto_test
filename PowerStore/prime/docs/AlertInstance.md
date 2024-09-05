# AlertInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the alert. | [optional] 
**event_code** | **str** | The event code of the latest event for this alert. | [optional] 
**severity** | [**SeverityEnum**](SeverityEnum.md) | Severity of the latest event for this alert. | [optional] 
**resource_type** | [**ResourceTypeEnum**](ResourceTypeEnum.md) | Type of the resource instance which generated this alert. | [optional] 
**resource_id** | **str** | Unique identifier of the resource instance which generated this alert. | [optional] 
**resource_name** | **str** | Name of the resource instance which generated this alert.  This property supports case-insensitive filtering. | [optional] 
**description_l10n** | **str** | Latest event&#39;s description text for this alert. | [optional] 
**generated_timestamp** | **datetime** | Timestamp of the latest event for this alert. | [optional] 
**state** | [**AlertStateEnum**](AlertStateEnum.md) |  | [optional] 
**is_acknowledged** | **bool** | Whether an alert has been acknowledged. | [optional] 
**raised_timestamp** | **datetime** | Timestamp of the first event for this alert. | [optional] 
**cleared_timestamp** | **datetime** | Timestamp of the event that cleared this alert. | [optional] 
**called_home_timestamp** | **datetime** | Timestamp when the event resulted in a notification to support (via Secured Remote Services), if any. | [optional] 
**email_sent_timestamp** | **datetime** | Timestamp when the email was sent for the raised alert, if any. | [optional] 
**snmp_sent_timestamp** | **datetime** | Timestamp when the SNMP trap was sent for the raised alert, if any. Was added in version 2.0.0.0. | [optional] 
**acknowledged_timestamp** | **datetime** | Timestamp when the alert was acknowledged, if any. | [optional] 
**events** | [**list[EventInstance]**](EventInstance.md) | List of events associated with this alert.  Filtering on the fields of this embedded resource is not supported. | [optional] 
**severity_l10n** | **str** | Localized message string corresponding to severity | [optional] 
**resource_type_l10n** | **str** | Localized message string corresponding to resource_type | [optional] 
**state_l10n** | **str** | Localized message string corresponding to state | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


