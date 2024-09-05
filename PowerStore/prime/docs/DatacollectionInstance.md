# DatacollectionInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for this instance. | [optional] 
**status** | [**DatacollectionStatusEnum**](DatacollectionStatusEnum.md) |  | [optional] 
**status_message** | **str** | If the data collection failed, the reason for the failure. | [optional] 
**start_timestamp** | **datetime** | The date and time at which the data collection started. | [optional] 
**end_timestamp** | **datetime** | The date and time at which the data collection completed or failed. | [optional] 
**uncompressed_size** | **int** | The uncompressed size of the collection in bytes. | [optional] 
**compressed_size** | **int** | The compressed size of the collection in bytes. | [optional] 
**description** | **str** | Brief note describing collection. | [optional] 
**creator_type** | [**DatacollectionCreatorTypeEnum**](DatacollectionCreatorTypeEnum.md) |  | [optional] 
**uploaded** | **datetime** | The last date and time that this collection was uploaded to your service provider. | [optional] 
**downloaded** | **datetime** | The last date and time that this collection was downloaded. | [optional] 
**profiles** | [**list[DatacollectionProfileInstance]**](DatacollectionProfileInstance.md) | Profiles used to create this data collection.  Filtering on the fields of this embedded resource is not supported. | [optional] 
**appliances** | [**list[DatacollectionApplianceInstance]**](DatacollectionApplianceInstance.md) | Appliances associated with this data collection.  Filtering on the fields of this embedded resource is not supported. | [optional] 
**log_from_timestamp** | **datetime** | The date and time from which to start collecting the logs.\&quot; | [optional] 
**log_to_timestamp** | **datetime** | The date and time to which the logs should be collected.\&quot; | [optional] 
**status_l10n** | **str** | Localized message string corresponding to status Was added in version 3.0.0.0. | [optional] 
**creator_type_l10n** | **str** | Localized message string corresponding to creator_type Was added in version 3.0.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


