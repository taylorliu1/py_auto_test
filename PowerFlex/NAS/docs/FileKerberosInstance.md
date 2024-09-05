# FileKerberosInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the Kerberos service settings instance. | [optional] 
**nas_server_id** | **str** | Unique identifier of the associated NAS Server instance that uses this Kerberos object. Only one Kerberos object per NAS Server is supported. | [optional] 
**realm** | **str** | Realm name of the Kerberos Service. | [optional] 
**kdc_addresses** | **list[str]** | Fully Qualified domain names of the Kerberos Key Distribution Center (KDC) servers. IPv4 and IPv6 addresses are not supported. | [optional] 
**port_number** | **int** | KDC servers TCP port. | [optional] [default to 88]
**nas_server** | [**NasServersInstance**](NasServersInstance.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

