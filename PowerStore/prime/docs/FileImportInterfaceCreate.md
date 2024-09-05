# FileImportInterfaceCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | IP address of the import interface. IPv4 and IPv6 are supported. | 
**prefix_length** | **int** | Prefix length for the import interface. IPv4 and IPv6 are supported. | [default to 24]
**gateway** | **str** | Gateway address for the import interface. IPv4 and IPv6 are supported. | [optional] 
**vlan_id** | **int** | Virtual Local Area Network (VLAN) identifier for the import interface. The import interface uses the identifier to accept packets that have matching VLAN tags. | [optional] [default to 0]
**ip_port_id** | **str** | Unique indentifier of the IP Port. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


