# JobInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the job. | [optional] 
**resource_action** | [**ResourceActionEnum**](ResourceActionEnum.md) |  | [optional] 
**resource_type** | [**ResourceTypeEnum**](ResourceTypeEnum.md) |  | [optional] 
**resource_id** | **str** | Unique identifier of the resource on which the job is operating. | [optional] 
**resource_name** | **str** | Name of the resource on which the job is operating.  This property supports case-insensitive filtering. | [optional] 
**description_l10n** | **str** | Description of the job. | [optional] 
**state** | [**JobStateEnum**](JobStateEnum.md) |  Was deprecated in version 1.0.2. | [optional] 
**start_time** | **datetime** | Date and time when the job execution started. | [optional] 
**phase** | [**JobPhaseEnum**](JobPhaseEnum.md) |  Was added in version 1.0.2. | [optional] 
**end_time** | **datetime** | Date and time when the job execution completed. | [optional] 
**estimated_completion_time** | **datetime** | Estimated completion date and time. | [optional] 
**progress_percentage** | **int** | Percent complete of the job. | [optional] 
**parent_id** | **str** | Unique identifier of the parent job, if applicable. | [optional] 
**root_id** | **str** | Unique identifier of the root job, if applicable. The root job is the job at the top of the parent hierarchy. | [optional] 
**user** | **str** | Name of the user associated with the job. | [optional] 
**response_body** | [**BaseResponse**](BaseResponse.md) |  | [optional] 
**response_status** | [**HttpStatusEnum**](HttpStatusEnum.md) |  Was added in version 2.0.0.0. | [optional] 
**step_order** | **int** | Order of a given job step with respect to its siblings within the job hierarchy. | [optional] 
**resource_action_l10n** | **str** | Localized message string corresponding to resource_action | [optional] 
**resource_type_l10n** | **str** | Localized message string corresponding to resource_type | [optional] 
**state_l10n** | **str** | Localized message string corresponding to state Was deprecated in version 1.0.2. | [optional] 
**phase_l10n** | **str** | Localized message string corresponding to phase Was added in version 1.0.2. | [optional] 
**response_status_l10n** | **str** | Localized message string corresponding to response_status Was added in version 2.0.0.0. | [optional] 
**parent** | [**JobInstance**](JobInstance.md) | This is the embeddable reference form of parent_id attribute. | [optional] 
**children** | [**list[JobInstance]**](JobInstance.md) | This is the inverse of the resource type job association. | [optional] 
**root** | [**JobInstance**](JobInstance.md) | This is the embeddable reference form of root_id attribute. | [optional] 
**leafs** | [**list[JobInstance]**](JobInstance.md) | This is the inverse of the resource type job association. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


