# ClusterCreateNetworks

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**NetworkTypeEnum**](NetworkTypeEnum.md) |  | 
**vlan_id** | **int** | VLAN identifier. | [optional] [default to 0]
**prefix_length** | **int** | Network prefix length, used for both IPv4 and IPv6. | 
**gateway** | **str** | Network gateway in IPv4 or IPv6 format, corresponding to the network&#39;s IP version. | [optional] [default to '']
**cluster_mgmt_address** | **str** | New cluster management IP address in IPv4 or IPv6 format, corresponding to the network&#39;s IP version. This can only be specified only when configuring the management type network. | [optional] 
**storage_discovery_address** | **str** | New storage discovery IP address in IPv4 or IPv6 format, corresponding to the network&#39;s IP version. This can only be specified only when configuring the storage type network. | [optional] 
**addresses** | **list[str]** | IP addresses in IPv4 or IPv6 format. | 
**purposes** | [**list[NetworkPurposeEnum]**](NetworkPurposeEnum.md) | Purposes of the network. Only applicable to storage networks. Omitting the property is equivalent to providing all applicable purposes, which are: ISCSI, NVMe/TCP. If provided, must include iSCSI to enable the internal host storage access. Was added in version 2.1.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


