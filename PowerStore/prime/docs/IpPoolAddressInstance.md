# IpPoolAddressInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the IP address. | [optional] 
**name** | **str** | Name of the IP address.  This property supports case-insensitive filtering. Was added in version 2.0.0.0. | [optional] 
**network_id** | **str** | Unique identifier of the network to which the IP address belongs. | [optional] 
**ip_port_id** | **str** | Unique identifier of the port that uses this IP address to provide access to storage network services, such as iSCSI. This attribute can be set only for an IP address used by networks of type Storage. | [optional] 
**appliance_id** | **str** | Unique identifier of the appliance to which the IP address belongs. | [optional] 
**node_id** | **str** | Unique identifier of the cluster node to which the IP address belongs. | [optional] 
**address** | **str** | IP address value, in IPv4 or IPv6 format. | [optional] 
**purposes** | [**list[IpPurposeTypeEnum]**](IpPurposeTypeEnum.md) | IP address purposes. | [optional] 
**purposes_l10n** | **list[str]** | Localized message array corresponding to purposes | [optional] 
**nvme_discovered_cdcs** | [**list[NvmeDiscoveredCdcInstance]**](NvmeDiscoveredCdcInstance.md) | This is the inverse of the resource type nvme_discovered_cdc association. | [optional] 
**network** | [**NetworkInstance**](NetworkInstance.md) | This is the embeddable reference form of network_id attribute. | [optional] 
**ip_port** | [**IpPortInstance**](IpPortInstance.md) | This is the embeddable reference form of ip_port_id attribute. | [optional] 
**appliance** | [**ApplianceInstance**](ApplianceInstance.md) | This is the embeddable reference form of appliance_id attribute. | [optional] 
**node** | [**NodeInstance**](NodeInstance.md) | This is the embeddable reference form of node_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


