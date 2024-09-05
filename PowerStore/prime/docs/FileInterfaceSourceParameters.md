# FileInterfaceSourceParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | IP address of the network interface. IPv4 and IPv6 are supported. | [optional] 
**prefix_length** | **int** | Prefix length for the interface. IPv4 and IPv6 are supported. | [optional] 
**gateway** | **str** | Gateway address for the network interface. IPv4 and IPv6 are supported. | [optional] 
**vlan_id** | **int** | Virtual Local Area Network (VLAN) identifier for the interface. The interface uses the identifier to accept packets that have matching VLAN tags. | [optional] [default to 0]
**ip_port_id** | **str** | Unique identifier of the IP Port that is associated with the file interfacesinterface. Was added in version 3.0.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


