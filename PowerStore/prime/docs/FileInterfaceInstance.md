# FileInterfaceInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the file interface. | [optional] 
**nas_server_id** | **str** | Unique identifier of the NAS server. | [optional] 
**ip_address** | **str** | IP address of the network interface. IPv4 and IPv6 are supported. | [optional] 
**prefix_length** | **int** | Prefix length for the interface. IPv4 and IPv6 are supported. | [optional] 
**gateway** | **str** | Gateway address for the network interface. IPv4 and IPv6 are supported. | [optional] 
**vlan_id** | **int** | Virtual Local Area Network (VLAN) identifier for the interface. The interface uses the identifier to accept packets that have matching VLAN tags. | [optional] [default to 0]
**name** | **str** | Name of the network interface.  This property supports case-insensitive filtering. | [optional] 
**role** | [**FileInterfaceRoleEnum**](FileInterfaceRoleEnum.md) |  | [optional] 
**is_disabled** | **bool** | Indicates whether the network interface is disabled. | [optional] [default to False]
**is_destination_override_enabled** | **bool** | Used in replication context when the user wants to override the settings on the destination. Was added in version 3.0.0.0. | [optional] [default to False]
**ip_port_id** | **str** | Unique Identifier of the IP Port that is associated with the file interface. Was added in version 3.0.0.0. | [optional] 
**source_parameters** | [**FileInterfaceSourceParameters**](FileInterfaceSourceParameters.md) |  Was added in version 3.0.0.0. | [optional] 
**role_l10n** | **str** | Localized message string corresponding to role | [optional] 
**nas_server** | [**NasServerInstance**](NasServerInstance.md) | This is the embeddable reference form of nas_server_id attribute. | [optional] 
**ip_port** | [**IpPortInstance**](IpPortInstance.md) | This is the embeddable reference form of ip_port_id attribute. | [optional] 
**file_interface_routes** | [**list[FileInterfaceRouteInstance]**](FileInterfaceRouteInstance.md) | This is the inverse of the resource type file_interface_route association. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


