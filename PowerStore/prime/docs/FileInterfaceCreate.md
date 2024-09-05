# FileInterfaceCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nas_server_id** | **str** | Unique identifier of the NAS server to which the network interface belongs, as defined by the nas_server resource type. name:{name} can be used instead of {id}. For example:&#39;nas_server_id&#39;:&#39;name:nas_server_name&#39; | 
**ip_address** | **str** | IP address of the network interface. IPv4 and IPv6 are supported. | 
**prefix_length** | **int** | Prefix length for the interface. IPv4 and IPv6 are supported. | 
**gateway** | **str** | Gateway address for the network interface. IPv4 and IPv6 are supported. | [optional] 
**vlan_id** | **int** | Virtual Local Area Network (VLAN) identifier for the interface. The interface uses the identifier to accept packets that have matching VLAN tags. | [optional] [default to 0]
**role** | [**FileInterfaceRoleEnum**](FileInterfaceRoleEnum.md) |  | [optional] 
**is_disabled** | **bool** | Indicates whether the network interface is disabled. | [optional] [default to False]
**ip_port_id** | **str** | Unique Identifier of the IP Port that is associated with the file interface. Was added in version 3.0.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


