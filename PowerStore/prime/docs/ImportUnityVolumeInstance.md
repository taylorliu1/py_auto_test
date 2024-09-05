# ImportUnityVolumeInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the Unity volume. | [optional] 
**wwn** | **str** | World Wide Name (WWN) of the Unity volume. | [optional] 
**name** | **str** | Name of the Unity volume.  This property supports case-insensitive filtering. | [optional] 
**size** | **int** | Size of the Unity volume, in bytes. | [optional] 
**import_unity_id** | **str** | Unique identifier of the Unity storage system to which the Unity volume belongs. | [optional] 
**import_unity_consistency_group_id** | **str** | Unique identifier of the consistency group to which the Unity volume belongs. This value is null if the volume does not belong to a consistency group. | [optional] 
**health** | [**UnityHealthEnum**](UnityHealthEnum.md) |  | [optional] 
**type** | [**UnityVolumeTypeEnum**](UnityVolumeTypeEnum.md) |  | [optional] 
**migration_state** | [**UnityVolumeMigrationStateEnum**](UnityVolumeMigrationStateEnum.md) |  | [optional] 
**is_replication_destination** | **bool** | Indicates whether the Unity volume is a replication destination. | [optional] 
**is_thin_clone** | **bool** | Indicates whether the Unity volume is a thin clone.  | [optional] 
**importable_criteria** | [**VolumeImportableCriteriaEnum**](VolumeImportableCriteriaEnum.md) | Volume import criteria. If the value is not Ready, the volume is not importable and the value specifies the reason it is not importable. | [optional] 
**host_volume_ids** | **list[str]** | List of host volume identifiers that correspond to Unity volumes. | [optional] 
**health_l10n** | **str** | Localized message string corresponding to health | [optional] 
**type_l10n** | **str** | Localized message string corresponding to type | [optional] 
**migration_state_l10n** | **str** | Localized message string corresponding to migration_state | [optional] 
**importable_criteria_l10n** | **str** | Localized message string corresponding to importable_criteria | [optional] 
**import_unity** | [**ImportUnityInstance**](ImportUnityInstance.md) | This is the embeddable reference form of import_unity_id attribute. | [optional] 
**import_unity_consistency_group** | [**ImportUnityConsistencyGroupInstance**](ImportUnityConsistencyGroupInstance.md) | This is the embeddable reference form of import_unity_consistency_group_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


