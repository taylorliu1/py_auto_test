# MigrationRecommendationInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of recommendation. | [optional] 
**created_timestamp** | **datetime** | Time at which recommendation was created. | [optional] 
**state** | [**MigrationRecommendationStateEnum**](MigrationRecommendationStateEnum.md) |  | [optional] 
**estimated_cost** | **int** | Unitless value describing estimated cost to migrate all volumes for this recommendation relative to other recommendations. | [optional] 
**type** | [**MigrationRecommendationTypeEnum**](MigrationRecommendationTypeEnum.md) | Type of request that generated a migration recommendation. Evacuate_Appliance - A recommendation to evacuate space by auto selecting storage objects from an appliance using specified size.  | [optional] 
**request_parameters** | [**MigrationRecommendationCreate**](MigrationRecommendationCreate.md) |  | [optional] 
**sessions_created_timestamp** | **datetime** | Time at which migration sessions were created for the recommendation.  Null if migration sessions have not been created. | [optional] 
**sessions_completed_timestamp** | **datetime** | Time at which all migration sessions for the recommendation were complete. Null if migration sessions have not been created/started or if any migration pursuant to the recommendation is still ongoing.  | [optional] 
**rescan_host_list** | **list[str]** | IDs of hosts that must be rescanned after migration sessions are created but before migration sessions are started. | [optional] 
**migration_actions** | [**list[MigrationRecommendationAction]**](MigrationRecommendationAction.md) | Filtering on the fields of this embedded resource is not supported. | [optional] 
**state_l10n** | **str** | Localized message string corresponding to state | [optional] 
**type_l10n** | **str** | Localized message string corresponding to type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


