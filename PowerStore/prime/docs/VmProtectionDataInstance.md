# VmProtectionDataInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by_rule_id** | **str** | Unique identifier of the protection rule that created the VM snapshot. | [optional] 
**created_by_rule_name** | **str** | Name of the rule that created the VM snapshot. This value is not updated if the name of the rule changes after snapshot creation. | [optional] 
**creator_type** | [**StorageCreatorTypeEnum**](StorageCreatorTypeEnum.md) |  | [optional] 
**expiration_timestamp** | **datetime** | Date when the VM snapshot can be automatically purged. | [optional] 
**source_timestamp** | **datetime** | Time when the snapshot was created. | [optional] 
**source_id** | **str** | For VM snapshots, this value is the same as parent_id. | [optional] 
**parent_id** | **str** | VM from which the snapshot was created. | [optional] 
**creator_type_l10n** | **str** | Localized message string corresponding to creator_type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


