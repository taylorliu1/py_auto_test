# FileInterfaceRouteInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the file interface route. | [optional] 
**file_interface_id** | **str** | Unique identifier of the associated file interface. | [optional] 
**destination** | **str** | IPv4 or IPv6 address of the target network node based on the specific route type. Values are: * For a default route, the route is specified in the gateway value for the related file interface. * For a host route, the destination value is a host IP address. For an IPV4 address the prefix_length must be 32, otherwise for an IPv6 address the prefix_length must be 128. * For a subnet route, the destination value is a subnet IP address and the appropriate prefix_length must be specified accordingly.  | [optional] 
**prefix_length** | **int** | IPv4 or IPv6 prefix length for the route. | [optional] 
**gateway** | **str** | IP address of the gateway associated with the route. | [optional] 
**operational_status** | [**FileInterfaceRouteOperationalStatusEnum**](FileInterfaceRouteOperationalStatusEnum.md) |  | [optional] 
**operational_status_l10n** | **str** | Localized message string corresponding to operational_status | [optional] 
**file_interface** | [**FileInterfaceInstance**](FileInterfaceInstance.md) | This is the embeddable reference form of file_interface_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


