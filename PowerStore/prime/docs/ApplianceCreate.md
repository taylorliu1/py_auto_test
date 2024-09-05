# ApplianceCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_local_address** | **str** | The link local address is a dynamically set local IPv4 address. It is unique to this appliance and is set by Zeroconf. Use the PowerStore Discovery Tool to get the link local address.  | 
**name** | **str** | The name of the new appliance. By default, the name is the cluster name followed by \&quot;-appliance-\&quot; and a unique number. The maximum size is 64 characters.  | [optional] 
**ignore_network_warnings** | **bool** | Set to true to ignore warnings about unreachable external network services discovered while adding an appliance. This can be useful for configuring a system before delivery into the intended deployment environment. The default is false, and these warnings will cause add appliance to fail.  | [optional] [default to False]
**drive_failure_tolerance_level** | [**DriveFailureToleranceLevelEnum**](DriveFailureToleranceLevelEnum.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


