# ImportPsgroupVolumeInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the volume. | [optional] 
**is_online** | **bool** | Indicates whether the volume is online. | [optional] 
**import_psgroup_id** | **str** | Unique identifier of the PS Group with which the volume is associated. | [optional] 
**name** | **str** | Name of the volume.  This property supports case-insensitive filtering. | [optional] 
**size** | **int** | Size of the volume, in bytes. | [optional] 
**block_size** | [**VolumeBlockSizeEnum**](VolumeBlockSizeEnum.md) |  | [optional] 
**wwn** | **str** | Unique WWN of the volume. | [optional] 
**is_read_only** | **bool** | Indicates whether the volume is read-only. | [optional] 
**migration_state** | [**ImportStatusEnum**](ImportStatusEnum.md) |  | [optional] 
**importable_criteria** | [**VolumeImportableCriteriaEnum**](VolumeImportableCriteriaEnum.md) | Volume import criteria. If the value is not Ready, the volume is not importable.  | [optional] 
**host_volume_ids** | **list[str]** | Unique identifiers of the host volumes associated with the volume. | [optional] 
**block_size_l10n** | **str** | Localized message string corresponding to block_size | [optional] 
**migration_state_l10n** | **str** | Localized message string corresponding to migration_state | [optional] 
**importable_criteria_l10n** | **str** | Localized message string corresponding to importable_criteria | [optional] 
**import_psgroup** | [**ImportPsgroupInstance**](ImportPsgroupInstance.md) | This is the embeddable reference form of import_psgroup_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


