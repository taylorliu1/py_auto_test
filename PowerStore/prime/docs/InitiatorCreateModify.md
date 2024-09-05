# InitiatorCreateModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_name** | **str** | IQN name aka address or NQN name for NVMEoF port types. | 
**port_type** | [**InitiatorProtocolTypeEnum**](InitiatorProtocolTypeEnum.md) |  | 
**chap_single_username** | **str** | Username for CHAP authentication. This value must be 1 to 64 UTF-8 characters. CHAP username is required when the cluster CHAP mode is single authentication. | [optional] 
**chap_single_password** | **str** | Password for CHAP authentication. This value must be 12 to 64 UTF-8 characters. This password cannot be queried. CHAP password is required when the cluster CHAP mode is single authentication. | [optional] 
**chap_mutual_username** | **str** | Username for CHAP authentication. This value must be 1 to 64 UTF-8 characters. CHAP username is required when the cluster CHAP mode is mutual authentication. | [optional] 
**chap_mutual_password** | **str** | Password for CHAP authentication. This value must be 12 to 64 UTF-8 characters. This password cannot be queried. CHAP password is required when the cluster CHAP mode is mutual authentication. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


