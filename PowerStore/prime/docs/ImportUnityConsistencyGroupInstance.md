# ImportUnityConsistencyGroupInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the Unity consistency group. | [optional] 
**name** | **str** | Name of the consistency group.  This property supports case-insensitive filtering. | [optional] 
**import_unity_id** | **str** | Unique identifier of the Unity storage system where the consistency group resides. | [optional] 
**importable_criteria** | [**CGImportableCriteriaEnum**](CGImportableCriteriaEnum.md) | Consistency group import criteria. | [optional] 
**importable_criteria_l10n** | **str** | Localized message string corresponding to importable_criteria | [optional] 
**import_unity_volumes** | [**list[ImportUnityVolumeInstance]**](ImportUnityVolumeInstance.md) | This is the inverse of the resource type import_unity_volume association. | [optional] 
**import_unity** | [**ImportUnityInstance**](ImportUnityInstance.md) | This is the embeddable reference form of import_unity_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


