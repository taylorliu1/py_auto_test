# NetworkModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vlan_id** | **int** | VLAN identifier. | [optional] 
**name** | **str** | Name of the network. Was added in version 2.0.0.0. | [optional] 
**gateway** | **str** | * Network gateway in IPv4 or IPv6 format, corresponding to the network&#39;s IP version. * Specify empty string to remove the gateway.  | [optional] 
**prefix_length** | **int** | Network prefix length. (Used for both IPv4 and IPv6). | [optional] 
**cluster_mgmt_address** | **str** | * Cluster management IP address in IPv4 or IPv6 format, corresponding to the network&#39;s IP version. * This can only be specified when reconfiguring these network types, which support cluster IP - * - Management - floating IP address for external cluster management. * - File_Mobility - floating IP address for file mobility network.  * Caution: Changing the cluster management IP address for Management network will lead to losing management sessions through this address.  | [optional] 
**storage_discovery_address** | **str** | * New storage discovery IP address in IPv4 or IPv6 format, corresponding to the network&#39;s IP version. * This can only be specified when reconfiguring the storage network. * Specify empty string to remove the storage discovery IP address.  | [optional] 
**vasa_provider_credentials** | **object** | * Credentials required for re-registering the VASA vendor provider during the reconfiguration of the cluster management IP address. * Should be passed only when reconfiguring cluster management IP address.  | [optional] 
**esxi_credentials** | [**EsxiCredentials**](EsxiCredentials.md) |  | [optional] 
**mtu** | **int** | Maximum Transmission Unit (MTU) packet size set on network interfaces, in bytes. | [optional] 
**add_addresses** | **list[str]** | IP addresses to add in IPv4 or IPv6 format. | [optional] 
**remove_addresses** | **list[str]** | IP addresses to remove in IPv4 or IPv6 format. | [optional] 
**add_purposes** | [**list[NetworkPurposeEnum]**](NetworkPurposeEnum.md) | * Purposes to enable in the network. * This can only be specified when reconfiguring the network.  Was added in version 2.1.0.0. | [optional] 
**remove_purposes** | [**list[NetworkPurposeEnum]**](NetworkPurposeEnum.md) | * Purposes to disable in the network. * This can only be specified when reconfiguring the network. * Removal of ISCSI, NVMe/TCP purpose will lead to I/O disruption on external ISCSI, NVMe/TCP hosts consuming volumes via this network. It is recommended to disconnect any external hosts that may be affected (initiators should log out).  Was added in version 2.1.0.0. | [optional] 
**nvme_discovery_mode** | [**NVMeDiscoveryModeEnum**](NVMeDiscoveryModeEnum.md) |  Was added in version 3.0.0.0. | [optional] 
**nvme_cdc_address** | **str** | IP address of the NVMe Centralized Discovery Controller (CDC). This is only applicable if network contains NVMe_TCP among its purposes, and nvme_discovery_mode is set to Manual_CDC.  Was added in version 3.0.0.0. | [optional] 
**nvme_cdc_port** | **int** | TCP port of the NVMe Centralized Discovery Controller (CDC). This is only applicable if network contains NVMe_TCP among its purposes, and nvme_discovery_mode is set to Manual_CDC. The valid values: 8009 or from 49152 to 49999 or 50100 to 65535.  Was added in version 3.0.0.0. | [optional] [default to 8009]
**force** | **bool** | Indicates whether to suppress network validation errors. The option is intended to suppress false errors caused by network environment constraints.  Normally the command will fail with an error when: - Some of system network ports are in degraded state or have cabling issues, - System top-of-rack switches have configuration issues leading to network unreachability, - Network IP addresses have duplicates in the network environment, or network gateway is unreachable.  When force is true, the command will proceed instead.  Caution: Only use this option when you are certain that your requested settings are correct, and that you understand why they are failing at this time, and that you want to apply the settings anyway. Improper network settings can make the system unreachable for data and management.  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


