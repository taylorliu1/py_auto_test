# HostInitiatorInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_name** | **str** | IQN name aka address for iSCSI or WWN name for FC (SCSI) or NQN name for all NVMe-oF port types. | [optional] 
**port_type** | [**InitiatorProtocolTypeEnum**](InitiatorProtocolTypeEnum.md) |  | [optional] 
**chap_single_username** | **str** | Username for CHAP authentication. This value must be 1 to 64 UTF-8 characters. CHAP username is required when the cluster CHAP mode is single authentication. | [optional] 
**chap_mutual_username** | **str** | Username for CHAP authentication. This value must be 1 to 64 UTF-8 characters. CHAP username is required when the cluster CHAP mode is mutual authentication. | [optional] 
**active_sessions** | [**list[ActiveSessionInstance]**](ActiveSessionInstance.md) | Array of active login sessions between an initiator and a target port. | [optional] 
**port_type_l10n** | **str** | Localized message string corresponding to port_type Was deprecated in version 3.0.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


