# FileNisInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the NIS Service. | [optional] 
**nas_server_id** | **str** | Unique identifier of the associated NAS Server instance that uses this NIS Service object. Only one NIS Service per NAS Server is supported. | [optional] 
**domain** | **str** | Name of the NIS domain. | [optional] 
**ip_addresses** | **list[str]** | The list of NIS server IP addresses. | [optional] 
**is_destination_override_enabled** | **bool** | Used in replication context when the user wants to override the settings on the destination. Was added in version 3.0.0.0. | [optional] [default to False]
**source_parameters** | **object** | Information about the corresponding source NAS Server&#39;s File NIS settings. Only populated when is_destination_override_enabled flag is set to true. Was added in version 3.0.0.0.  Filtering on the fields of this embedded resource is not supported. | [optional] 
**nas_server** | [**NasServerInstance**](NasServerInstance.md) | This is the embeddable reference form of nas_server_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


