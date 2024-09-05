# ClusterInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the cluster. | [optional] 
**global_id** | **str** | The global unique identifier of the cluster. | [optional] 
**name** | **str** | The name of the cluster. | [optional] 
**management_address** | **str** | The floating management IP address for the cluster in IPv4 or IPv6 format. | [optional] 
**storage_discovery_address** | **str** | The floating storage discovery IP address for the cluster in IPv4 or IPv6 format. If multiple storage discovery addresses are configured, this property will be set to \&quot;null\&quot;. In this case the required storage network should be used to retrieve the discovery address. | [optional] 
**master_appliance_id** | **str** | The unique identifier of the appliance acting as primary. Was deprecated in version 2.0.0.0. | [optional] 
**primary_appliance_id** | **str** | The unique identifier of the appliance acting as primary. Was added in version 2.0.0.0. | [optional] 
**appliance_count** | **int** | Number of appliances configured in this cluster. | [optional] 
**physical_mtu** | **int** | The physical ethernet port (eth_port resource) MTU setting is global for all ports in the cluster. This is the default MTU setting for IP traffic, and the upper limit on network-specific MTU settings (network resource), where this can be overridden for some specific kinds of traffic (management, data, and vMotion). | [optional] 
**is_encryption_enabled** | **bool** | Whether or not Data at Rest Encryption is enabled on the cluster. | [optional] 
**compatibility_level** | **int** | The behavioral version of the software version API, and it is used to ensure the compatibility across potentially different software versions. | [optional] 
**state** | [**ClusterStateEnum**](ClusterStateEnum.md) |  | [optional] 
**state_l10n** | **str** | Localized string corresponding to state. | [optional] 
**system_time** | **datetime** | Current clock time for the system. System time and all the system reported times are in UTC (GMT+0:00) format. The system time is controlled via NTP. It cannot be set directly. Was added in version 2.0.0.0. | [optional] 
**nvm_subsystem_nqn** | **str** | NVMe Subsystem NQN for cluster. It cannot be set directly. Was added in version 3.0.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


