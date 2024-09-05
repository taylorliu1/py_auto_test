# InitiatorInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id of the initiator. | [optional] 
**host_id** | **str** | Unique id of a host instance. | [optional] 
**port_name** | **str** | The port name, one of: IQN, WWN, or NQN. | [optional] 
**port_type** | [**InitiatorProtocolTypeEnum**](InitiatorProtocolTypeEnum.md) |  | [optional] 
**chap_single_username** | **str** | Username for CHAP authentication. This value must be 1 to 64 UTF-8 characters. CHAP username is required when the cluster CHAP mode is mutual authentication. | [optional] 
**chap_mutual_username** | **str** | Username for CHAP authentication. This value must be 1 to 64 UTF-8 characters. CHAP username is required when the cluster CHAP mode is mutual authentication. | [optional] 
**active_sessions** | [**list[ActiveSessionInstance]**](ActiveSessionInstance.md) | Array of active login sessions between an initiator and a target port.  Filtering on the fields of this embedded resource is not supported. | [optional] 
**host** | [**HostInstance**](HostInstance.md) | This is the embeddable reference form of host_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


