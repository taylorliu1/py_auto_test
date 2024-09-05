# NvmeDiscoveredCdcInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the CDC. | [optional] 
**ip_pool_address_id** | **str** | Identifier of the IP address being used for NVMe/TCP through which CDC was discovered. | [optional] 
**nvme_cdc_address** | **str** | IP address of the CDC. | [optional] 
**nvme_cdc_port** | **int** | TCP port of the CDC. | [optional] 
**nvme_cdc_nqn** | **str** | NVMe Qualified Name of the CDC. | [optional] 
**nvme_cdc_connection_state** | [**NvmeCdcConnectionStateEnum**](NvmeCdcConnectionStateEnum.md) |  | [optional] 
**nvme_cdc_connection_state_l10n** | **str** | Localized message string corresponding to nvme_cdc_connection_state Was added in version 3.0.0.0. | [optional] 
**ip_pool_address** | [**IpPoolAddressInstance**](IpPoolAddressInstance.md) | This is the embeddable reference form of ip_pool_address_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


