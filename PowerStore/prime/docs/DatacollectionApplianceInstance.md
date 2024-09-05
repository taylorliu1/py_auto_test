# DatacollectionApplianceInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for this instance. | [optional] 
**appliance_serial_number** | **str** | The serial number of the appliance where this data collection was created. | [optional] 
**start_timestamp** | **datetime** | The date and time that this data collection started on this appliance. | [optional] 
**end_timestamp** | **datetime** | The date and time that this data collection completed on the appliance. | [optional] 
**compressed_size** | **int** | The uncompressed size of this data collection in bytes. | [optional] 
**uncompressed_size** | **int** | The compressed size of this data collection in bytes. | [optional] 
**download_uri** | **str** | The download URI for this file. | [optional] 
**status** | [**DatacollectionStatusEnum**](DatacollectionStatusEnum.md) |  | [optional] 
**status_message_l10n** | **str** | Additional status detail | [optional] 
**uploaded** | **datetime** | The last date and time that this collection was uploaded to your service provider. | [optional] 
**downloaded** | **datetime** | The last date and time that this collection was downloaded. | [optional] 
**upload_in_progress** | **bool** | Indicates whether upload of the data collection bundle is in progress. | [optional] 
**node** | **str** | The node where the data collection bundle is located. | [optional] 
**log_from_timestamp** | **datetime** | The date and time from which to start collecting the logs. | [optional] 
**log_to_timestamp** | **datetime** | The date and time up to which the logs should be collected. | [optional] 
**status_l10n** | **str** | Localized message string corresponding to status Was added in version 3.0.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


