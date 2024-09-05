# ImportStorageCenterConsistencyGroupInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the SC consistency group. | [optional] 
**name** | **str** | Name of the SC consistency group.  This property supports case-insensitive filtering. | [optional] 
**import_storage_center_id** | **str** | Unique identifier of the SC array. | [optional] 
**importable_criteria** | [**CGImportableCriteriaEnum**](CGImportableCriteriaEnum.md) | Volume import criteria. If the value is not Ready, the volume is not importable. | [optional] 
**importable_criteria_l10n** | **str** | Localized message string corresponding to importable_criteria | [optional] 
**import_storage_center_volumes** | [**list[ImportStorageCenterVolumeInstance]**](ImportStorageCenterVolumeInstance.md) | This is the inverse of the resource type import_storage_center_volume association. | [optional] 
**import_storage_center** | [**ImportStorageCenterInstance**](ImportStorageCenterInstance.md) | This is the embeddable reference form of import_storage_center_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


