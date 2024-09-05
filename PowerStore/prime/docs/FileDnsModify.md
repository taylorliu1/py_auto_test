# FileDnsModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Name of the DNS domain, where the NAS Server does host names lookup when an FQDN is not specified in the request. | [optional] 
**ip_addresses** | **list[str]** | A new list of DNS server IP addresses to replace the existing list. The addresses may be IPv4 or IPv6. | [optional] 
**add_ip_addresses** | **list[str]** | IP addresses to add to the current list. The addresses may be IPv4 or IPv6. Error occurs if an IP address already exists. Cannot be combined with ip_addresses. | [optional] 
**remove_ip_addresses** | **list[str]** | IP addresses to remove from the current list. The addresses may be IPv4 or IPv6. Error occurs if IP address is not present. Cannot be combined with ip_addresses. | [optional] 
**transport** | [**FileDNSTransportEnum**](FileDNSTransportEnum.md) |  | [optional] 
**is_destination_override_enabled** | **bool** | Used in replication context when the user wants to override the settings on the destination. Was added in version 3.0.0.0. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


