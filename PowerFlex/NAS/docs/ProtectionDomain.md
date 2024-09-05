# ProtectionDomain

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the NAS enabled Protection Domain. | 
**name** | **str** | Name of NAS enabled Protection Domain. | 
**is_primary** | **bool** | Indicates if this Protection Domains hosts cluster and postgres VDM.Default false if not specified. | [optional] [default to False]
**storage_pool_id** | **str** | Storage Pool Id of NAS configuration volumes. | 
**mgmt_interface** | **str** | Networking interface available for management. | 
**data_interfaces** | **list[str]** | Networking interfaces available for data. | 
**nas_nodes** | [**list[SDNASNode]**](SDNASNode.md) | List of all NAS nodes belong to this cluster | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

