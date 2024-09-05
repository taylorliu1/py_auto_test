# HostModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The host name. The name should not be more than 128 UTF-8 characters long and should not have any unprintable characters. | [optional] 
**description** | **str** | An optional description for the host. The description should not be more than 256 UTF-8 characters long and should not have any unprintable characters. | [optional] 
**host_connectivity** | [**HostConnectivityEnum**](HostConnectivityEnum.md) |  Was added in version 3.0.0.0. | [optional] 
**remove_initiators** | **list[str]** | The list of initiator port_names to be removed. | [optional] 
**add_initiators** | [**list[InitiatorCreateModify]**](InitiatorCreateModify.md) | The list of initiators to be added. CHAP username and password are optional. | [optional] 
**modify_initiators** | [**list[UpdateInitiatorInHost]**](UpdateInitiatorInHost.md) | Update list of existing initiators, identified by port_name, with new CHAP usernames and/or passwords. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


