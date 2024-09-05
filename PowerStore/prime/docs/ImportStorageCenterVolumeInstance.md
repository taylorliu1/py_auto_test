# ImportStorageCenterVolumeInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the SC volume. | [optional] 
**name** | **str** | Name of the SC volume.  This property supports case-insensitive filtering. | [optional] 
**size** | **int** | Size of the SC volume, in bytes. | [optional] 
**wwn** | **str** | Device identifier presented to the server to which the volume is mapped. | [optional] 
**health** | [**SCStatusEnum**](SCStatusEnum.md) |  | [optional] 
**is_active** | **bool** | Indicates whether the SC volume is active on any controller. Only volumes that are active are importable. | [optional] 
**import_storage_center_id** | **str** | Unique identifier of the SC array where the volume resides. | [optional] 
**migration_state** | [**MigrationStateEnum**](MigrationStateEnum.md) |  | [optional] 
**is_read_only** | **bool** | Indicates whether the volume is read-only. | [optional] 
**importable_criteria** | [**VolumeImportableCriteriaEnum**](VolumeImportableCriteriaEnum.md) | Volume import criteria. If the value is not Ready, the volume is not importable. | [optional] 
**host_volume_ids** | **list[str]** | List of host volume identifiers that correspond to SC volumes. | [optional] 
**import_storage_center_consistency_group_id** | **str** | Unique identifier of an SC consistency group, if the volume is part of one consistency group only. If the volume is part of multiple consistency groups, the attribute is empty. | [optional] 
**import_storage_center_consistency_group_names** | **list[str]** | Names of the consistency groups of which the volume is a member, if this volume is in multiple consistency groups. | [optional] 
**health_l10n** | **str** | Localized message string corresponding to health | [optional] 
**migration_state_l10n** | **str** | Localized message string corresponding to migration_state | [optional] 
**importable_criteria_l10n** | **str** | Localized message string corresponding to importable_criteria | [optional] 
**import_storage_center** | [**ImportStorageCenterInstance**](ImportStorageCenterInstance.md) | This is the embeddable reference form of import_storage_center_id attribute. | [optional] 
**import_storage_center_consistency_group** | [**ImportStorageCenterConsistencyGroupInstance**](ImportStorageCenterConsistencyGroupInstance.md) | This is the embeddable reference form of import_storage_center_consistency_group_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


