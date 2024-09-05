# AuditEventInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the audit log entry. | [optional] 
**type** | [**AuditEventTypeEnum**](AuditEventTypeEnum.md) |  | [optional] 
**timestamp** | **datetime** | Time the event occurred to one second precision. | [optional] 
**username** | **str** | Fully qualified name of the user who initiated the event to be audited. For example, domain_name/name. | [optional] 
**is_successful** | **bool** | Whether the event was successful or not. | [optional] 
**client_address** | **str** | FQDN/IP Address of the client from where the event was initiated. | [optional] 
**server_address** | **str** | IP Address on which the request was targeted. | [optional] 
**appliance_id** | **str** | Unique identifier of the appliance where the event occurred. | [optional] 
**job_id** | **str** | Unique identifier of the job associated with the audit event (if any). | [optional] 
**resource_type** | [**ResourceTypeEnum**](ResourceTypeEnum.md) |  | [optional] 
**resource_action** | [**ResourceActionEnum**](ResourceActionEnum.md) |  | [optional] 
**message_code** | **str** | Unique identifier of the message for this audit_event. | [optional] 
**message_arguments** | **list[str]** | Arguments (if applicable) for the audit_event message. | [optional] 
**message_l10n** | **str** | Localized message string corresponding to message_code. | [optional] 
**type_l10n** | **str** | Localized message string corresponding to type | [optional] 
**resource_type_l10n** | **str** | Localized message string corresponding to resource_type | [optional] 
**resource_action_l10n** | **str** | Localized message string corresponding to resource_action | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


