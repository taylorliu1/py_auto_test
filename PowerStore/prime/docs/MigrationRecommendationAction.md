# MigrationRecommendationAction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | ID of storage resource migrated by this action. | 
**resource_type** | [**MigrationResourceTypeEnum**](MigrationResourceTypeEnum.md) |  | 
**src_appliance_id** | **str** | ID of appliance that is the source for this migration action. | 
**dst_appliance_id** | **str** | ID of appliance that is the destination for this migration action. | 
**cost** | **int** | Unitless value describing estimated cost to perform relative to other migration actions. | 
**host_connectivity_to_destination** | **bool** | Whether all hosts for the migrating resource have connectivity to the destination appliance. | 
**action_state** | [**MigrationRecommendationActionStateEnum**](MigrationRecommendationActionStateEnum.md) |  | 
**primary_id** | **str** | Unique ID of the primary object. | 
**primary_name** | **str** | Name of the primary object. | 
**migration_primary_resource_type** | [**MigrationRecommendationPrimaryResourceTypeEnum**](MigrationRecommendationPrimaryResourceTypeEnum.md) |  | 
**migration_reason** | [**MigrationRecommendationReasonEnum**](MigrationRecommendationReasonEnum.md) |  | 
**active** | **bool** | Whether this migration action in active or not. New recommendations will consist entirely of active recommendations but this may be changed with the modify operation. Was added in version 2.0.0.0. | [optional] 
**connected_appliance_ids** | **list[str]** | List of appliance ids to which the host attached to this resource has connectivity. Was added in version 2.0.0.0. | [optional] 
**resource_type_l10n** | **str** | Localized message string corresponding to resource_type | [optional] 
**action_state_l10n** | **str** | Localized message string corresponding to action_state | [optional] 
**migration_primary_resource_type_l10n** | **str** | Localized message string corresponding to migration_primary_resource_type | [optional] 
**migration_reason_l10n** | **str** | Localized message string corresponding to migration_reason | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


