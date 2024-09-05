# ImportHostSystemCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**os_type** | [**HAOSTypeEnum**](HAOSTypeEnum.md) |  | 
**agent_address** | **str** | Hostname or IPv4 address of the import host system. | 
**agent_port** | **int** | TCP port of the import host system. | 
**user_name** | **str** | Username for the import host system. | 
**password** | **str** | Password for the specified username. | 
**chap_single_username** | **str** | Username for single CHAP authentication. This username is required when the cluster is using single authentication CHAP mode. | [optional] 
**chap_single_password** | **str** | Password for single CHAP authentication. This password is required when the cluster is using single authentication CHAP mode. | [optional] 
**chap_mutual_username** | **str** | Username for mutual CHAP authentication. This username is required when the cluster is using mutual authentication CHAP mode. | [optional] 
**chap_mutual_password** | **str** | Password for mutual CHAP authentication. This password is required when the cluster is using mutual authentication CHAP mode. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


