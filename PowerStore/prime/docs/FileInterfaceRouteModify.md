# FileInterfaceRouteModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | IPv4 or IPv6 address of the target network node based on the specific route type. Values are: * For a default route, the route is specified in the gateway value for the related file interface. * For a host route, the destination value is a host IP address. For an IPV4 address the prefix_length must be 32, otherwise for an IPv6 address the prefix_length must be 128. * For a subnet route, the destination value is a subnet IP address and the appropriate prefix_length must be specified accordingly.  | 
**prefix_length** | **int** | IPv4 or IPv6 prefix length for the route. | 
**gateway** | **str** | IP address of the gateway associated with the route. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


