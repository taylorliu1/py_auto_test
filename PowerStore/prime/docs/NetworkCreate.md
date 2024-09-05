# NetworkCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**NetworkTypeEnum**](NetworkTypeEnum.md) |  | 
**name** | **str** | Name of the network. | 
**ip_version** | [**IpVersionTypeEnum**](IpVersionTypeEnum.md) |  | 
**purposes** | [**list[NetworkPurposeEnum]**](NetworkPurposeEnum.md) | * Purposes of the network. * This returns a list of purposes for the networks that support multiple purposes per network, like storage network. * Returns an empty list for the single purposed networks, like management, vMotion, ICD and ICM.  | 
**vlan_id** | **int** | VLAN identifier. | [optional] 
**gateway** | **str** | * Network gateway in IPv4 or IPv6 format, corresponding to the network&#39;s IP version. * Specify empty string to remove the gateway.  | [optional] 
**prefix_length** | **int** | Network prefix length. (Used for both IPv4 and IPv6). | 
**storage_discovery_address** | **str** | * New storage discovery IP address in IPv4 or IPv6 format, corresponding to the network&#39;s IP version. * This can only be specified when creating the storage network. * Specify empty string to omit the storage discovery IP address.  | [optional] 
**cluster_mgmt_address** | **str** | * Cluster management IP address in IPv4 or IPv6 format, corresponding to the network&#39;s IP version. * This can only be specified when creating these network types - * - File_Mobility - floating IP address for file mobility network.  Was added in version 3.0.0.0. | [optional] 
**mtu** | **int** | Maximum Transmission Unit (MTU) packet size set on network interfaces, in bytes. | 
**add_addresses** | **list[str]** | IP addresses to add in IPv4 or IPv6 format. | [optional] 
**nvme_discovery_mode** | [**NVMeDiscoveryModeEnum**](NVMeDiscoveryModeEnum.md) |  Was added in version 3.0.0.0. | [optional] 
**nvme_cdc_address** | **str** | IP address of the NVMe Centralized Discovery Controller (CDC). This is only applicable if network contains NVMe_TCP among its purposes, and nvme_discovery_mode is set to Manual_CDC.  Was added in version 3.0.0.0. | [optional] 
**nvme_cdc_port** | **int** | TCP port of the NVMe Centralized Discovery Controller (CDC). This is only applicable if network contains NVMe_TCP among its purposes, and nvme_discovery_mode is set to Manual_CDC. The valid values: 8009 or from 49152 to 49999 or 50100 to 65535.  Was added in version 3.0.0.0. | [optional] [default to 8009]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


