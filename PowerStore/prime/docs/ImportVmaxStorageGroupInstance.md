# ImportVmaxStorageGroupInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the VMAX storage group. | [optional] 
**name** | **str** | Name of the storage group.  This property supports case-insensitive filtering. | [optional] 
**import_vmax_id** | **str** | Unique identifier of the VMAX storage system where the storage group exists. | [optional] 
**importable_criteria** | [**CGImportableCriteriaEnum**](CGImportableCriteriaEnum.md) | Storage group import criteria. If the value is not Ready_For_Agentless_Import, storage group is not importable. | [optional] 
**importable_criteria_l10n** | **str** | Localized message string corresponding to importable_criteria Was added in version 3.0.0.0. | [optional] 
**import_vmax_volume** | [**list[ImportVmaxVolumeInstance]**](ImportVmaxVolumeInstance.md) | This is the inverse of the resource type import_vmax_volume association. | [optional] 
**import_vmax** | [**ImportVmaxInstance**](ImportVmaxInstance.md) | This is the embeddable reference form of import_vmax_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


