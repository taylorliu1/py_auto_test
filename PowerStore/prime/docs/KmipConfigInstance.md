# KmipConfigInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for this instance. | [optional] 
**is_enabled** | **bool** | Whether KMIP is enabled. At least one member (KMIP servers) must be defined to enable KMIP. | [optional] 
**port** | **int** | Port number for establishing connection to a KMIP server (defaults to 5696). | [optional] 
**server_timeout** | **int** | Timeout in seconds for establishing a connection to a KMIP server. If the system does not receive a reply from the KMIP server before the specified timeout, it stops sending requests. Default value is 5 (5 seconds). | [optional] 
**username** | **str** | Username for accessing the KMIP server. | [optional] 
**servers** | [**list[KmipConfigMemberInstance]**](KmipConfigMemberInstance.md) | Array of member KMIP servers with the address and status of each.  Filtering on the fields of this embedded resource is not supported. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


