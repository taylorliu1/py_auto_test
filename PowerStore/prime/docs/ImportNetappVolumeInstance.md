# ImportNetappVolumeInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the NetApp volume. | [optional] 
**wwn** | **str** | World Wide Name (WWN) of the NetApp volume. | [optional] 
**name** | **str** | Name of the NetApp volume.  This property supports case-insensitive filtering. | [optional] 
**size** | **int** | Size of the NetApp volume, in bytes. | [optional] 
**state** | [**NetAppVolumeStateEnum**](NetAppVolumeStateEnum.md) |  | [optional] 
**container_state** | [**NetAppContainerStateEnum**](NetAppContainerStateEnum.md) |  | [optional] 
**is_read_only** | **bool** | Indicates whether the NetApp volume is a read only volume. | [optional] 
**is_replication_destination** | **bool** | Indicates whether the NetApp volume is a replication destination. | [optional] 
**importable_criteria** | [**VolumeImportableCriteriaEnum**](VolumeImportableCriteriaEnum.md) | Indicates the reason when the volume is not importable. If the value is not Ready_For_Agentless_Import, the volume is not importable. | [optional] 
**import_netapp_id** | **str** | Unique identifier of the NetApp storage system to which the NetApp volume belongs. | [optional] 
**state_l10n** | **str** | Localized message string corresponding to state Was added in version 3.0.0.0. | [optional] 
**container_state_l10n** | **str** | Localized message string corresponding to container_state Was added in version 3.0.0.0. | [optional] 
**importable_criteria_l10n** | **str** | Localized message string corresponding to importable_criteria Was added in version 3.0.0.0. | [optional] 
**import_netapp** | [**ImportNetappInstance**](ImportNetappInstance.md) | This is the embeddable reference form of import_netapp_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


