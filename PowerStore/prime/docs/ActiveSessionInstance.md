# ActiveSessionInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_name** | **str** | IQN or WWN of the target port that the initiator is logged into. | [optional] 
**appliance_id** | **str** | Unique identifier of the appliance containing the session. | [optional] 
**node_id** | **str** | Unique identifier of node on the appliance on which active session is created. | [optional] 
**bond_id** | **str** | Unique identifier of the bond the initiator is logged into.  Null if one of the following is non-null: veth_id, eth_port_id or fc_port_id. | [optional] 
**fc_port_id** | **str** | Unique identifier of the FC port the initiator is logged into.  Null if one of the following is non-null: bond_id, veth_id or eth_port_id | [optional] 
**veth_id** | **str** | Unique identifier of the virtual Ethernet port the initiator is logged into.  Null if one of the following is non-null: bond, eth_port_id or fc_port_id. | [optional] 
**eth_port_id** | **str** | Unique identifier of the Ethernet port the initiator is logged into. Null if one of the following is non-null: bond_id, veth_id or fc_port_id. | [optional] 
**nvme_transport_addresses** | **list[str]** | List of addresses of the NVMe/NVMe-vVol initiator. These can either be the IPs of the endpoints for NVMe over TCP, or they can be the WWNs if using NVMe over FC. It may be that the same NQN will be applied to multiple WWNs or IP addresses, since NQNs are unique per host sub-system, and not unique per port. This field is null for FC(SCSI) and iSCSI initiators. Was added in version 3.0.0.0. | [optional] 
**nvme_transport_type** | [**NvmeTransportTypeEnum**](NvmeTransportTypeEnum.md) |  Was added in version 3.0.0.0. | [optional] 
**nvme_transport_type_l10n** | **str** | Localized message string corresponding to nvme_transport_type Was added in version 3.0.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


