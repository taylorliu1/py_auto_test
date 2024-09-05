# ImportVnxConsistencyGroupInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the VNX consistency group. | [optional] 
**name** | **str** | Name of the consistency group.  This property supports case-insensitive filtering. | [optional] 
**import_vnx_array_id** | **str** | Unique identifier of the VNX storage system where the consistency group exists. | [optional] 
**importable_criteria** | [**CGImportableCriteriaEnum**](CGImportableCriteriaEnum.md) |  | [optional] 
**importable_criteria_l10n** | **str** | Localized message string corresponding to importable_criteria | [optional] 
**import_vnx_volumes** | [**list[ImportVnxVolumeInstance]**](ImportVnxVolumeInstance.md) | This is the inverse of the resource type import_vnx_volume association. | [optional] 
**import_vnx_array** | [**ImportVnxArrayInstance**](ImportVnxArrayInstance.md) | This is the embeddable reference form of import_vnx_array_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


