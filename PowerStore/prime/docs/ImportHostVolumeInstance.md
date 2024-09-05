# ImportHostVolumeInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the import host volume. | [optional] 
**host_system_id** | **str** | Unique identifier of the import host system. | [optional] 
**name** | **str** | Name of the import host volume.  This property supports case-insensitive filtering. | [optional] 
**array_type** | [**ArrayTypeEnum**](ArrayTypeEnum.md) | Product type of the storage system. | [optional] 
**array_identifier** | **str** | Unique identifier of the storage system. | [optional] 
**size** | **int** | Size of the import host volume, in bytes. | [optional] 
**status** | [**VolumeStatusEnum**](VolumeStatusEnum.md) | Status of the import host volume. | [optional] 
**is_migrating** | **bool** | Indicates whether the import host volume is migrating. | [optional] 
**active_path** | [**ActivePathEnum**](ActivePathEnum.md) | Active path of the host volume. | [optional] 
**protocols** | [**list[HostInitiatorProtocolTypeEnum]**](HostInitiatorProtocolTypeEnum.md) | Supported protocols for the import host volume. | [optional] 
**mount_paths** | **list[str]** | Mount paths on the import host system. | [optional] 
**import_state** | [**ImportOperationStatusEnum**](ImportOperationStatusEnum.md) |  | [optional] 
**naa_id** | **str** | Unique identifier of a volume that is presented to the import host. | [optional] 
**last_update_time** | **datetime** | Time when the import host volume was last updated. | [optional] 
**array_type_l10n** | **str** | Localized message string corresponding to array_type | [optional] 
**status_l10n** | **str** | Localized message string corresponding to status | [optional] 
**active_path_l10n** | **str** | Localized message string corresponding to active_path | [optional] 
**protocols_l10n** | **list[str]** | Localized message array corresponding to protocols | [optional] 
**import_state_l10n** | **str** | Localized message string corresponding to import_state | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


