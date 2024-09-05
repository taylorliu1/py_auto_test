# DataConnectionInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | Unique identifier of the local, initiating node.  | [optional] 
**initiator_address** | **str** | Initiating address from the local node. IP for ISCSI and TCP data connection type. WWN for FC data connection type.  | [optional] 
**target_address** | **str** | Target address from the remote system. IP for ISCSI and TCP data connection type. WWN for FC data connection type.  | [optional] 
**status** | [**TransitConnectionStatusEnum**](TransitConnectionStatusEnum.md) |  | [optional] 
**data_connection_type** | [**DataConnectionTypeEnum**](DataConnectionTypeEnum.md) |  Was added in version 3.0.0.0. | [optional] 
**status_l10n** | **str** | Localized message string corresponding to status | [optional] 
**data_connection_type_l10n** | **str** | Localized message string corresponding to data_connection_type Was added in version 3.0.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


