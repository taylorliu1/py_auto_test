# VethPortInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the virtual Ethernet port instance. | [optional] 
**partner_id** | **str** | Identifier of the virtual Ethernet port with the same logical location on the other node of the appliance. Partner ports are configured symmetrically for HA and load balancing purposes within the appliance. Was added in version 2.0.0.0. | [optional] 
**appliance_id** | **str** | Unique identifier of the appliance. | [optional] 
**node_id** | **str** | Unique identifier of the cluster. | [optional] 
**name** | **str** | Virtual Ethernet port name.  This property supports case-insensitive filtering. | [optional] 
**mac_address** | **str** | Virtual Ethernet port MAC address. | [optional] 
**is_link_up** | **bool** | Indicates whether the virtual Ethernet port&#39;s link is up. Values are: * true - Link is up. * false - Link is down.  | [optional] 
**current_speed** | **int** | Virtual Ethernet port transmission speed, in bits/sec (bps). | [optional] 
**current_mtu** | **int** | Maximum Transmission Unit (MTU) packet size that the virtual Ethernet port can transmit. | [optional] 
**vswitch_name** | **str** | Name of the virtual switch that holds the virtual Ethernet port. | [optional] 
**vswitch_port_group_name** | **str** | Name of the virtual switch port group to which the virtual Ethernet port is assigned. | [optional] 
**vswitch_port_id** | **int** | Unique identifier of the virtual switch port associated with the virtual Ethernet port. | [optional] 
**vswitch_port_name** | **str** | Name of the virtual switch port associated with the virtual Ethernet port.  This property supports case-insensitive filtering. | [optional] 
**ip_ports** | [**list[IpPortInstance]**](IpPortInstance.md) | This is the inverse of the resource type ip_port association. | [optional] 
**partner** | [**VethPortInstance**](VethPortInstance.md) | This is the embeddable reference form of partner_id attribute. | [optional] 
**appliance** | [**ApplianceInstance**](ApplianceInstance.md) | This is the embeddable reference form of appliance_id attribute. | [optional] 
**node** | [**NodeInstance**](NodeInstance.md) | This is the embeddable reference form of node_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


