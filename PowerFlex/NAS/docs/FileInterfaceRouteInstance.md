# FileInterfaceRouteInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the file interface route. | [optional] 
**file_interface_id** | **str** | Unique identifier of the associated file interface. | [optional] 
**destination** | **str** | IPv4 or IPv6 address of the target network node based on the specific route type. Values are: * For a default route, there is no value because the system will use the specified gateway IP address. * For a host route, the value is the host IP address. * For a subnet route, the value is a subnet IP address.  | [optional] 
**prefix_length** | **int** | IPv4 or IPv6 prefix length for the route. | [optional] 
**gateway** | **str** | IP address of the gateway associated with the route. | [optional] 
**operational_status** | [**FileInterfaceRouteOperationalStatusEnum**](FileInterfaceRouteOperationalStatusEnum.md) |  | [optional] 
**operational_status_l10n** | **str** | Localized message string corresponding to operational_status | [optional] 
**file_interface** | [**FileInterfaceInstance**](FileInterfaceInstance.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

