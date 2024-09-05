# RemoteSyslogServerCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_server_address** | **str** | IPv4 or IPv6 address, or DNS name of the log server. | 
**port** | **int** | Port used for connection to the remote server. | 
**protocol_type** | [**ProtocolTypeEnum**](ProtocolTypeEnum.md) |  | 
**encryption** | [**EncryptionTypeEnum**](EncryptionTypeEnum.md) |  | [optional] 
**audit_types** | [**list[AuditEventTypeEnum]**](AuditEventTypeEnum.md) | Audit type selections. If empty, all types will be sent to the remote log server. Otherwise, only audit events of the specified type(s) will be sent. | 
**is_enabled** | **bool** | If true, then this instance will receive audit messages. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


