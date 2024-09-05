# FileKerberosCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nas_server_id** | **str** | Unique identifier of the associated NAS Server instance that uses this Kerberos object. Only one Kerberos object per NAS Server is supported. name:{name} can be used instead of {id}. For example:&#39;nas_server_id&#39;:&#39;name:nas_server_name&#39; | 
**realm** | **str** | Realm name of the Kerberos Service. | 
**kdc_addresses** | **list[str]** | Fully Qualified domain names of the Kerberos Key Distribution Center (KDC) servers. IPv4 and IPv6 addresses are not supported. | 
**port_number** | **int** | KDC servers TCP port. | [optional] [default to 88]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


