# FileDnsInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the DNS server. | [optional] 
**nas_server_id** | **str** | Unique identifier of the associated NAS Server instance that uses this DNS object. Only one DNS object per NAS Server is supported. | [optional] 
**domain** | **str** | Name of the DNS domain, where the NAS Server does host names lookup when an FQDN is not specified in the request. | [optional] 
**ip_addresses** | **list[str]** | The list of DNS server IP addresses. The addresses may be IPv4 or IPv6. | [optional] 
**transport** | [**FileDNSTransportEnum**](FileDNSTransportEnum.md) |  | [optional] 
**transport_l10n** | **str** | Localized message string corresponding to transport | [optional] 
**nas_server** | [**NasServersInstance**](NasServersInstance.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

