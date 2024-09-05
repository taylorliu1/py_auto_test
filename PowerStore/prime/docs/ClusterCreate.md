# ClusterCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | [**ClusterCreateCluster**](ClusterCreateCluster.md) |  | 
**appliances** | [**list[ClusterCreateAppliances]**](ClusterCreateAppliances.md) | The configuration settings for adding appliances during cluster creation. At least one appliance is required. | 
**dns_servers** | **list[str]** |  | 
**ntp_servers** | **list[str]** |  | 
**physical_switches** | [**list[ClusterCreatePhysicalSwitches]**](ClusterCreatePhysicalSwitches.md) | Physical switch settings for a cluster. | [optional] 
**networks** | [**list[ClusterCreateNetworks]**](ClusterCreateNetworks.md) | Configuration of one or more network(s) based on network type. | 
**vcenters** | [**list[ClusterCreateVcenters]**](ClusterCreateVcenters.md) | Configure vCenter settings when creating cluster. Parameters are required when creating PowerStore X cluster and optional for PowerStore cluster.  * Note - Currently only single element is supported. | [optional] 
**security_config** | [**ClusterCreateSecurityConfig**](ClusterCreateSecurityConfig.md) |  Was added in version 3.0.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


