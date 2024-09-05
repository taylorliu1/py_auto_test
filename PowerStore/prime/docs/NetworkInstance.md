# NetworkInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the network. | [optional] 
**type** | [**NetworkTypeEnum**](NetworkTypeEnum.md) |  | [optional] 
**name** | **str** | Name of the network.  This property supports case-insensitive filtering. Was added in version 2.0.0.0. | [optional] 
**ip_version** | [**IpVersionTypeEnum**](IpVersionTypeEnum.md) |  | [optional] 
**purposes** | [**list[NetworkPurposeEnum]**](NetworkPurposeEnum.md) | Purposes of the network. This returns a list of purposes for the networks that support multiple purposes per network, like storage network. Empty list is returned for single purposed networks, like management, vMotion, ICD and ICM.  Was added in version 2.0.0.0. | [optional] 
**vlan_id** | **int** | VLAN identifier. | [optional] 
**prefix_length** | **int** | Network prefix length, used for both IPv4 and IPv6. | [optional] 
**gateway** | **str** | Network gateway in IPv4 or IPv6 format, corresponding to the network&#39;s IP version. | [optional] 
**mtu** | **int** | Maximum Transmission Unit (MTU) packet size set on network interfaces, in bytes. | [optional] 
**nvme_discovery_mode** | [**NVMeDiscoveryModeEnum**](NVMeDiscoveryModeEnum.md) |  Was added in version 3.0.0.0. | [optional] 
**nvme_cdc_address** | **str** | IP address of the NVMe Centralized Discovery Controller (CDC). This is only applicable if network contains NVMe_TCP among its purposes, and nvme_discovery_mode is set to Manual_CDC.  Was added in version 3.0.0.0. | [optional] 
**nvme_cdc_port** | **int** | TCP port of the NVMe Centralized Discovery Controller (CDC). This is only applicable if network contains NVMe_TCP among its purposes, and nvme_discovery_mode is set to Manual_CDC. The valid values: 8009 or from 49152 to 49999 or 50100 to 65535.  Was added in version 3.0.0.0. | [optional] [default to 8009]
**type_l10n** | **str** | Localized message string corresponding to type | [optional] 
**ip_version_l10n** | **str** | Localized message string corresponding to ip_version | [optional] 
**purposes_l10n** | **list[str]** | Localized message array corresponding to purposes Was added in version 2.0.0.0. | [optional] 
**nvme_discovery_mode_l10n** | **str** | Localized message string corresponding to nvme_discovery_mode Was added in version 3.0.0.0. | [optional] 
**ip_pool_addresses** | [**list[IpPoolAddressInstance]**](IpPoolAddressInstance.md) | This is the inverse of the resource type ip_pool_address association. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


