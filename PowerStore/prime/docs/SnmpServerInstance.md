# SnmpServerInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the SNMP server. | [optional] 
**ip_address** | **str** | IPv4 address, IPv6 address, or FQDN of the SNMP server. | [optional] 
**port** | **int** | Port number to use with the address of the SNMP server. | [optional] 
**version** | [**SNMPVersionEnum**](SNMPVersionEnum.md) |  | [optional] 
**alert_severity** | [**SNMPSeverityEnum**](SNMPSeverityEnum.md) |  | [optional] 
**trap_community** | **str** | Trap Community string. Usually describes the security level. | [optional] 
**user_name** | **str** | User name, relevant only for SNMPv3. | [optional] 
**auth_protocol** | [**SNMPAuthProtocolEnum**](SNMPAuthProtocolEnum.md) |  | [optional] 
**privacy_protocol** | [**SNMPPrivacyProtocolEnum**](SNMPPrivacyProtocolEnum.md) |  | [optional] 
**version_l10n** | **str** | Localized message string corresponding to version Was added in version 2.0.0.0. | [optional] 
**alert_severity_l10n** | **str** | Localized message string corresponding to alert_severity Was added in version 2.0.0.0. | [optional] 
**auth_protocol_l10n** | **str** | Localized message string corresponding to auth_protocol Was added in version 2.0.0.0. | [optional] 
**privacy_protocol_l10n** | **str** | Localized message string corresponding to privacy_protocol Was added in version 2.0.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


