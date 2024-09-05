# NodeInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the node. | [optional] 
**slot** | **int** | Slot number of the node. | [optional] 
**appliance_id** | **str** | Unique identifier of the appliance to which the node belongs. | [optional] 
**appliance** | [**ApplianceInstance**](ApplianceInstance.md) | This is the embeddable reference form of appliance_id attribute. | [optional] 
**ip_pool_addresses** | [**list[IpPoolAddressInstance]**](IpPoolAddressInstance.md) | This is the inverse of the resource type ip_pool_address association. | [optional] 
**veth_ports** | [**list[VethPortInstance]**](VethPortInstance.md) | This is the inverse of the resource type veth_port association. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


