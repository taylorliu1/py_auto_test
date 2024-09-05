# FileKerberosModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**realm** | **str** | Realm name of the Kerberos Service. | [optional] 
**kdc_addresses** | **list[str]** | Fully Qualified domain names of the Kerberos Key Distribution Center (KDC) servers. IPv4 and IPv6 addresses are not supported. | [optional] 
**add_kdc_addresses** | **list[str]** | Fully Qualified domain names of the Kerberos Key Distribution Center (KDC) servers to add to the current list. Error occurs if name already exists. Cannot be combined with kdc_addresses. IPv4 and IPv6 addresses are not supported. | [optional] 
**remove_kdc_addresses** | **list[str]** | Fully Qualified domain names of the Kerberos Key Distribution Center (KDC) servers to remove from the current list. Error occurs if name is not in the existing list. Cannot be combined with kdc_addresses. IPv4 and IPv6 addresses are not supported. | [optional] 
**port_number** | **int** | KDC servers TCP port. | [optional] [default to 88]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


