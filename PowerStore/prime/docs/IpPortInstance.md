# IpPortInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the IP port. | [optional] 
**partner_id** | **str** | Identifier of the IP port that is configured on top of physical Ethernet port or virtual Ethernet port or bond with the same physical location on the other node of the appliance. Partner ports are configured symmetrically for HA and load balancing purposes within the appliance. | [optional] 
**target_iqn** | **str** | iSCSI qualified name used by the target configured on top of the IP port initially or as a result of network scaling. If the IP port is not used by an iSCSI connection, this attribute should be empty. | [optional] 
**available_usages** | [**list[IpPortUsageEnum]**](IpPortUsageEnum.md) | Available IP port usages. | [optional] 
**current_usages** | [**list[IpPortUsageEnum]**](IpPortUsageEnum.md) | Current IP port usages. | [optional] 
**bond_id** | **str** | Unique identifier of the bond on top of which the IP port is configured. If the IP port is configured on top of an Ethernet front-end port, this attribute should be empty.  | [optional] 
**eth_port_id** | **str** | Unique identifier of the physical Ethernet front-end port on top of which the IP port is configured. This attribute can be set when the IP port is used by a Unified appliance. It should be empty if the IP port is used by a Unified+ appliance or if the IP port is configured on top of a bond on a Unified appliance.  | [optional] 
**veth_port_id** | **str** | Unique identifier of the virtual Ethernet front-end port on top of which the IP port is configured. This attribute can be set when the IP port is used by a Unified+ appliance. For a Unified appliance, the value of veth_port_id should be empty.  | [optional] 
**available_usages_l10n** | **list[str]** | Localized message array corresponding to available_usages | [optional] 
**current_usages_l10n** | **list[str]** | Localized message array corresponding to current_usages | [optional] 
**ip_pool_addresses** | [**list[IpPoolAddressInstance]**](IpPoolAddressInstance.md) | This is the inverse of the resource type ip_pool_address association. | [optional] 
**partner** | [**IpPortInstance**](IpPortInstance.md) | This is the embeddable reference form of partner_id attribute. | [optional] 
**bond** | [**BondInstance**](BondInstance.md) | This is the embeddable reference form of bond_id attribute. | [optional] 
**eth_port** | [**EthPortInstance**](EthPortInstance.md) | This is the embeddable reference form of eth_port_id attribute. | [optional] 
**veth_port** | [**VethPortInstance**](VethPortInstance.md) | This is the embeddable reference form of veth_port_id attribute. | [optional] 
**file_interfaces** | [**list[FileInterfaceInstance]**](FileInterfaceInstance.md) | This is the inverse of the resource type file_interface association. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


