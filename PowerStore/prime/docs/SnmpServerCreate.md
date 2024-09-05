# SnmpServerCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | IPv4 address, IPv6 address, or FQDN of the SNMP server. | 
**port** | **int** | Port number to use with the address of the SNMP server: 162, [1024-49151] | 
**version** | [**SNMPVersionEnum**](SNMPVersionEnum.md) |  | 
**alert_severity** | [**SNMPSeverityEnum**](SNMPSeverityEnum.md) |  | 
**trap_community** | **str** | Trap Community string. Usually describes the security level, relevant only for SNMPv2c. | [optional] 
**user_name** | **str** | User name, relevant only for SNMPv3. | [optional] 
**auth_protocol** | [**SNMPAuthProtocolEnum**](SNMPAuthProtocolEnum.md) |  | [optional] 
**privacy_protocol** | [**SNMPPrivacyProtocolEnum**](SNMPPrivacyProtocolEnum.md) |  | [optional] 
**authpass** | **str** | Passphrase, used for both Authentication and Privacy protocols, relevant only for SNMPv3. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


