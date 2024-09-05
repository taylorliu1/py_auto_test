# ImportXtremioVolumeInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the XtremIO volume. | [optional] 
**wwn** | **str** | World Wide Name (WWN) of the XtremIO volume. | [optional] 
**name** | **str** | Name of the XtremIO volume.  This property supports case-insensitive filtering. | [optional] 
**size** | **int** | Size of the XtremIO volume, in bytes. | [optional] 
**severity** | [**XtremIOObjectSeverityEnum**](XtremIOObjectSeverityEnum.md) |  | [optional] 
**certainty** | [**XtremIOCertaintyEnum**](XtremIOCertaintyEnum.md) |  | [optional] 
**is_read_only** | **bool** | Indicates whether the XtremIO volume is a read only volume. | [optional] 
**is_replication_destination** | **bool** | Indicates whether the XtremIO volume is a replication destination. | [optional] 
**importable_criteria** | [**VolumeImportableCriteriaEnum**](VolumeImportableCriteriaEnum.md) | Indicates the reason when the volume is not importable. If the value is not Ready, the volume is not importable. | [optional] 
**import_xtremio_id** | **str** | Unique identifier of the XtremIO storage system to which the XtremIO volume belongs. | [optional] 
**import_xtremio_consistency_group_id** | **str** | Unique identifier of the consistency group to which the XtremIO volume belongs. This value is null if the volume does not belong to a consistency group or a volume belongs to multiple consistency groups. The volume that belongs to multiple consistency groups will be imported as an individual volume and the attribute import_xtremio_consistency_group_names contains the names of the consistency groups of which the volume is a member. | [optional] 
**import_xtremio_consistency_group_names** | **list[str]** | Names of the consistency groups of which the volume is a member, if the volume belong to multiple consistency groups. The attribute will be empty for a volume that is part of a single consistency group. | [optional] 
**severity_l10n** | **str** | Localized message string corresponding to severity Was added in version 1.0.2. | [optional] 
**certainty_l10n** | **str** | Localized message string corresponding to certainty Was added in version 1.0.2. | [optional] 
**importable_criteria_l10n** | **str** | Localized message string corresponding to importable_criteria Was added in version 1.0.2. | [optional] 
**import_xtremio** | [**ImportXtremioInstance**](ImportXtremioInstance.md) | This is the embeddable reference form of import_xtremio_id attribute. | [optional] 
**import_xtremio_consistency_group** | [**ImportXtremioConsistencyGroupInstance**](ImportXtremioConsistencyGroupInstance.md) | This is the embeddable reference form of import_xtremio_consistency_group_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


