# HostCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The host name. The name should not be more than 128 UTF-8 characters long and should not have any unprintable characters. | 
**description** | **str** | An optional description for the host. The description should not be more than 256 UTF-8 characters long and should not have any unprintable characters. | [optional] 
**os_type** | [**OSTypeEnum**](OSTypeEnum.md) |  | 
**host_connectivity** | [**HostConnectivityEnum**](HostConnectivityEnum.md) |  Was added in version 3.0.0.0. | [optional] 
**initiators** | [**list[InitiatorCreateModify]**](InitiatorCreateModify.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


