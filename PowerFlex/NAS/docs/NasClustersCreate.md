# NasClustersCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_ip** | **str** | IP-address of SDNAS cluster. | 
**cluster_port** | **int** | Port of the SDNAS cluster.Default 3085 if not specified. | [optional] [default to 3085]
**cluster_name** | **str** | Name of the cluster. | [optional] 
**system_id** | **str** | Id of the Powerflex system. | 
**is_deployment_type_software** | **bool** | Indicates if SDNAS deployment type is software only. Default false if not specified. | [optional] [default to False]
**nas_enabled_protection_domains** | [**list[ProtectionDomain]**](ProtectionDomain.md) | List of all NAS nodes belong to this cluster | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

