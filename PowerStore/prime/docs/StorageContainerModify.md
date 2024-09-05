# StorageContainerModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New name for the storage container that is unique across all storage containers in the cluster. The name must be between 1 and 64 UTF-8 characters (inclusive), and not more than 127 bytes. | [optional] 
**quota** | **int** | The number of bytes that can be provisioned against this storage container. It cannot be set lower than the current used space or 10Gb. A value of 0 means unlimited. | [optional] 
**storage_protocol** | [**StorageContainerStorageProtocolEnum**](StorageContainerStorageProtocolEnum.md) |  Was added in version 3.0.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


