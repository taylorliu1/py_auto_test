# RemoteSyslogServerInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique remote syslog server identifier. | [optional] 
**remote_server_address** | **str** | IPv4 or IPv6 address, or DNS name of the log server. | [optional] 
**port** | **int** | Port used for connection to the remote server. | [optional] 
**protocol_type** | [**ProtocolTypeEnum**](ProtocolTypeEnum.md) |  | [optional] 
**encryption** | [**EncryptionTypeEnum**](EncryptionTypeEnum.md) |  | [optional] 
**audit_types** | [**list[AuditEventTypeEnum]**](AuditEventTypeEnum.md) | Audit type selections. If empty, all types will be sent to the remote log server. Otherwise, only audit events of the specified type(s) will be sent. | [optional] 
**is_enabled** | **bool** | If true, then this instance will receive audit messages. | [optional] 
**status** | [**RemoteSyslogServerStatusEnum**](RemoteSyslogServerStatusEnum.md) |  | [optional] 
**protocol_type_l10n** | **str** | Localized message string corresponding to protocol_type Was added in version 2.0.0.0. | [optional] 
**encryption_l10n** | **str** | Localized message string corresponding to encryption Was added in version 2.0.0.0. | [optional] 
**audit_types_l10n** | **list[str]** | Localized message array corresponding to audit_types Was added in version 2.0.0.0. | [optional] 
**status_l10n** | **str** | Localized message string corresponding to status Was added in version 2.0.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


