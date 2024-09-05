# ImportVmaxVolumeInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the VMAX volume. | [optional] 
**wwn** | **str** | World Wide Name (WWN) of the VMAX volume. | [optional] 
**name** | **str** | Name of the VMAX volume.  This property supports case-insensitive filtering. | [optional] 
**size** | **int** | Size of the VMAX volume, in bytes. | [optional] 
**state** | [**VmaxVolumeStateEnum**](VmaxVolumeStateEnum.md) |  | [optional] 
**is_read_only** | **bool** | Indicates whether the VMAX volume is a read only volume. | [optional] 
**is_snap_vx_target** | **bool** | Indicates whether the VMAX volume is a SnapVX target. | [optional] 
**importable_criteria** | [**VolumeImportableCriteriaEnum**](VolumeImportableCriteriaEnum.md) |  | [optional] 
**import_vmax_id** | **str** | Unique identifier of the VMAX storage system to which the VMAX volume belongs. | [optional] 
**import_vmax_storage_group_id** | **str** | Unique identifier of the storage group to which the VMAX volume belongs. | [optional] 
**is_replication_destination** | **bool** | Indicates whether the VMAX storage group is a replication destination. | [optional] 
**block_size** | [**VolumeBlockSizeEnum**](VolumeBlockSizeEnum.md) |  | [optional] 
**state_l10n** | **str** | Localized message string corresponding to state Was added in version 3.0.0.0. | [optional] 
**importable_criteria_l10n** | **str** | Localized message string corresponding to importable_criteria Was added in version 3.0.0.0. | [optional] 
**block_size_l10n** | **str** | Localized message string corresponding to block_size Was added in version 3.0.0.0. | [optional] 
**import_vmax** | [**ImportVmaxInstance**](ImportVmaxInstance.md) | This is the embeddable reference form of import_vmax_id attribute. | [optional] 
**import_vmax_storage_group** | [**ImportVmaxStorageGroupInstance**](ImportVmaxStorageGroupInstance.md) | This is the embeddable reference form of import_vmax_storage_group_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


