# FileNisModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Name of the NIS domain. | [optional] 
**ip_addresses** | **list[str]** | A new list of NIS server IP addresses to replace the existing list. The addresses may be IPv4 or IPv6. | [optional] 
**add_ip_addresses** | **list[str]** | IP addresses to add to the current list. The addresses may be IPv4 or IPv6. Error occurs if the IP address already exists. Cannot be combined with ip_addresses. | [optional] 
**remove_ip_addresses** | **list[str]** | IP addresses to remove from the current list. The addresses may be IPv4 or IPv6. Error occurs if the IP address is not present. Cannot be combined with ip_addresses. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

