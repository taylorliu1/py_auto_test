# HostGroupModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A new host group name. The name should not be more than 128 UTF-8 characters long and should not have any unprintable characters. | [optional] 
**description** | **str** | An optional description for the host group. The description should not be more than 256 UTF-8  characters long and should not have any unprintable characters. | [optional] 
**host_connectivity** | [**HostConnectivityEnum**](HostConnectivityEnum.md) |  Was added in version 3.0.0.0. | [optional] 
**remove_host_ids** | **list[str]** | List of hosts to be removed from the host group. The operation fails if the host group is attached to any volume and the list includes all hosts in the host group. | [optional] 
**add_host_ids** | **list[str]** | List of hosts to be added to host group. The operation fails if the host(s) to be added are attached to volume. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


