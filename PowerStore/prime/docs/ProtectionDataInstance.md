# ProtectionDataInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by_rule_id** | **str** | Unique identifier of the snapshot rule that created the snapshot. | [optional] 
**created_by_rule_name** | **str** | The name of the rule that created the snapshot. This value will not change if the name of the rule changes after creating the snapshot. | [optional] 
**creator_type** | [**StorageCreatorTypeEnum**](StorageCreatorTypeEnum.md) | StorageCreatorTypeEnum | [optional] 
**expiration_timestamp** | **datetime** | Date when the snapshot can be automatically purged. | [optional] 
**source_timestamp** | **datetime** | The time at which the resource was sourced from the resource identified by source_id. | [optional] 
**family_id** | **str** | Family identifier of the resource. This is the identifier of the primary object at the root of the family tree. For a primary resource this will be the same as the unique identifier of the object. For snapshots and clone resources it will be set to the source object&#39;s family identifier. | [optional] 
**source_id** | **str** | Unique identifier of the resource from which the content has been sourced. Data is sourced from another resource when a snapshot or clone is created, or when a refresh or restore occurs. | [optional] 
**parent_id** | **str** | Unique identifier of the resource from which a snapshot or clone resource is created. The parent_id is set when a resource is created and will only change if its parent resource is deleted. When a resource is deleted, its children get reparented to the parent of the deleted resource. If the deleted parent is of type Primary, the parent_id of the child resources will be set to null. | [optional] 
**copy_signature** | **str** | Used for tracking replicated copies of a snapshot set. | [optional] 
**is_app_consistent** | **bool** | A boolean flag that indicates whether the snapshot is application consistent. Only App Sync can create application consistent snapshots. | [optional] [default to False]
**creator_type_l10n** | **str** | Localized message string corresponding to creator_type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


