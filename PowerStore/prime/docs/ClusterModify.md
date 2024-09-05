# ClusterModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new name for the cluster. The name can be up to 64 UTF-8 characters and cannot be an empty string. | [optional] 
**physical_mtu** | **int** | The physical ethernet port (eth_port resource) MTU setting is global for all ports in the cluster. This is the default MTU setting for IP traffic, and the upper limit on network-specific MTU settings (network resource), where this can be overridden for some specific kinds of traffic (management, data, and vmotion). This value must be in the range 1500-9000. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


