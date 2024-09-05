# FileNisModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Name of the NIS domain. | [optional] 
**ip_addresses** | **list[str]** | A new list of NIS server IP addresses to replace the existing list. The addresses may be IPv4 or IPv6. | [optional] 
**add_ip_addresses** | **list[str]** | IP addresses to add to the current list. The addresses may be IPv4 or IPv6. Error occurs if the IP address already exists. Cannot be combined with ip_addresses. | [optional] 
**remove_ip_addresses** | **list[str]** | IP addresses to remove from the current list. The addresses may be IPv4 or IPv6. Error occurs if the IP address is not present. Cannot be combined with ip_addresses. | [optional] 
**is_destination_override_enabled** | **bool** | In order to modify any properties of this resource when the associated NAS server is a replication destination, the is_destination_override_enabled flag must be set to true. When true these properties may be modified: ip_addresses, add_ip_addresses, remove_ip_addresses. Values are:   true - Enable locally set properties. Source property changes will propagate to the source_parameters of the resource.   false - Reset the properties to the ones from the source. Source property changes will propagate directly to this resource.  Was added in version 3.0.0.0. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


