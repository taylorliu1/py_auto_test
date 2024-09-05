# IpPortModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_current_usages** | [**list[IpPortUsageEnum]**](IpPortUsageEnum.md) | Usages to add to the current usages of an IP port. The current usages of an IP port can be extended with external replication if this usage is in the port&#39;s list of available usages. The same settings will be applied to the partner IP port.  WARNING: Only one IP port on each node can be assigned to the External_Replication usage. Assigning another IP port to this usage will automatically unassign the currently used IP port on the same node. To unassign an IP port from being used for external replication, choose another IP port and add External_Replication to its list of current usages.  | [optional] 
**network_id** | **str** | Unique identifier of the network in which IP port usages will be changed Was added in version 2.0.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


