# BondInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the bond. | [optional] 
**name** | **str** | Bond name.  This property supports case-insensitive filtering. | [optional] 
**partner_id** | **str** | Identifier of the bond with the same physical location on the other node of the appliance. Partner ports are configured symmetrically for HA and load balancing purposes within the appliance.  Was added in version 2.0.0.0. | [optional] 
**is_link_up** | **bool** | Indicates whether the bond&#39;s link is up. Values are: * true - Link is up. * false - Link is down.  | [optional] 
**status** | [**BondStatusEnum**](BondStatusEnum.md) |  Was added in version 3.0.0.0. | [optional] 
**mtu** | **int** | Maximum Transmission Unit (MTU) packet size of the bond, in bytes. | [optional] 
**mode** | [**BondingModeEnum**](BondingModeEnum.md) |  | [optional] 
**type** | [**BondingTypeEnum**](BondingTypeEnum.md) |  Was added in version 2.0.0.0. | [optional] 
**description** | **str** | User supplied description of the bond. | [optional] 
**status_l10n** | **str** | Localized message string corresponding to status Was added in version 3.0.0.0. | [optional] 
**mode_l10n** | **str** | Localized message string corresponding to mode | [optional] 
**type_l10n** | **str** | Localized message string corresponding to type Was added in version 2.0.0.0. | [optional] 
**ip_ports** | [**list[IpPortInstance]**](IpPortInstance.md) | This is the inverse of the resource type ip_port association. | [optional] 
**partner** | [**BondInstance**](BondInstance.md) | This is the embeddable reference form of partner_id attribute. | [optional] 
**eth_ports** | [**list[EthPortInstance]**](EthPortInstance.md) | This is the inverse of the resource type eth_port association. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


