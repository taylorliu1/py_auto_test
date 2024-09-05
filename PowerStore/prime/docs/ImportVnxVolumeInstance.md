# ImportVnxVolumeInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the VNX volume. | [optional] 
**name** | **str** | Name of the VNX volume.  This property supports case-insensitive filtering. | [optional] 
**wwn** | **str** | World wide name of the VNX volume. | [optional] 
**size** | **int** | Size of the VNX volume in bytes. | [optional] 
**health** | [**VnxVolumeStateEnum**](VnxVolumeStateEnum.md) |  | [optional] 
**migration_state** | [**VnxVolumeMigrationStateEnum**](VnxVolumeMigrationStateEnum.md) |  | [optional] 
**import_vnx_array_id** | **str** | Unique identifier of the VNX storage system where the volume exists. | [optional] 
**import_vnx_consistency_group_id** | **str** | Unique identifier of the VNX consistency group, if the volume is in a consistency group. | [optional] 
**importable_criteria** | [**VolumeImportableCriteriaEnum**](VolumeImportableCriteriaEnum.md) |  | [optional] 
**host_volume_ids** | **list[str]** | List of host volume identifiers associated with the VNX volume. | [optional] 
**health_l10n** | **str** | Localized message string corresponding to health | [optional] 
**migration_state_l10n** | **str** | Localized message string corresponding to migration_state | [optional] 
**importable_criteria_l10n** | **str** | Localized message string corresponding to importable_criteria | [optional] 
**import_vnx_array** | [**ImportVnxArrayInstance**](ImportVnxArrayInstance.md) | This is the embeddable reference form of import_vnx_array_id attribute. | [optional] 
**import_vnx_consistency_group** | [**ImportVnxConsistencyGroupInstance**](ImportVnxConsistencyGroupInstance.md) | This is the embeddable reference form of import_vnx_consistency_group_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


