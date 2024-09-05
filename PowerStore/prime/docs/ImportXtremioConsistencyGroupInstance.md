# ImportXtremioConsistencyGroupInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the XtremIO consistency group. | [optional] 
**name** | **str** | Name of the consistency group.  This property supports case-insensitive filtering. | [optional] 
**import_xtremio_id** | **str** | Unique identifier of the XtremIO storage system where the consistency group resides. | [optional] 
**importable_criteria** | [**CGImportableCriteriaEnum**](CGImportableCriteriaEnum.md) | Consistency group import criteria. If the value is not Ready, the consistency group is not importable. | [optional] 
**importable_criteria_l10n** | **str** | Localized message string corresponding to importable_criteria Was added in version 1.0.2. | [optional] 
**import_xtremio_volumes** | [**list[ImportXtremioVolumeInstance]**](ImportXtremioVolumeInstance.md) | This is the inverse of the resource type import_xtremio_volume association. | [optional] 
**import_xtremio** | [**ImportXtremioInstance**](ImportXtremioInstance.md) | This is the embeddable reference form of import_xtremio_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


