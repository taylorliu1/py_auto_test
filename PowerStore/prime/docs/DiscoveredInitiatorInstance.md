# DiscoveredInitiatorInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | IQN - for iSCSi Initiators; WWN - for SCSI over FC initiators; NQN - for NVMe/NVMe-vVol initiators. | [optional] 
**nvme_transport_addresses** | **list[str]** | List of discovered NVMe Initiators&#39; addresses. For NVMe/FC - nvme_wwns list; for NVMe/TCP - ip address list. It may be that same nqn (NVMe identifier) will be applied to multiple WWNs (FC port address) and/or multiple IP addresses for NVMe/TCP over Eth port. Was added in version 2.0.0.0. | [optional] 
**nvme_transport_types** | [**list[NvmeTransportTypeEnum]**](NvmeTransportTypeEnum.md) | List of transport types for discovered NVMe initiators. For NVMe/FC, there will be only 1 item of type FC. For NVMe/TCP, there will be only 1 item of type TCP. If the same nqn (NVMe identifier) is applied to NVMe/FC and NVMe/TCP, the list will have both FC and TCP. If the protocol_type is not NVMe this value will be null. Was added in version 2.1.0.0. | [optional] 
**protocol_type** | [**InitiatorProtocolTypeEnum**](InitiatorProtocolTypeEnum.md) |  | [optional] 
**protocol_type_l10n** | **str** | Localized message string corresponding to protocol_type Was deprecated in version 3.0.0.0. | [optional] 
**nvme_transport_types_l10n** | **list[str]** | Localized message array corresponding to nvme_transport_types Was added in version 2.1.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


