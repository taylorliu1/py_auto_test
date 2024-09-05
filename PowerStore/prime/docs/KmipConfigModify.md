# KmipConfigModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | Whether KMIP is enabled. To enable KMIP, at least one operational member server must be defined. | [optional] 
**servers** | **list[str]** | Replace all of the KMIP server addresses. Addresses may be IPv4, IPv6, or host names. Replace operation is mutually exclusive and is NOT allowed to be combined with add/remove_members operations. | [optional] 
**add_servers** | **list[str]** | Add KMIP server addresses. Addresses may be IPv4, IPv6, or host names. Note, members may be removed and added as a combined operation call but they are executed sequentially. The remove_members operation will be run BEFORE the add_members operation. | [optional] 
**remove_servers** | **list[str]** | Remove KMIP server addresses. Note, members may be removed and added as a combined operation call but they are executed sequentially. The remove_members operation will be run BEFORE the add_members operation. | [optional] 
**port** | **int** | Port number for establishing connection to a KMIP server (defaults to 5696). | [optional] [default to 5696]
**server_timeout** | **int** | Timeout for establishing a connection to a KMIP server. If the system does not receive a reply from the KMIP server before the specified timeout, it stops sending requests. Default value is 5 (5 seconds). | [optional] [default to 5]
**username** | **str** | Username for accessing the KMIP server. | [optional] 
**password** | **str** | Password for accessing the KMIP server. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


