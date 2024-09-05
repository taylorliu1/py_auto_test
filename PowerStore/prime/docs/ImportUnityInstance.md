# ImportUnityInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the Unity storage system that is a source storage system for import. This is the serial number of the storage system. | [optional] 
**name** | **str** | Name of the Unity storage system.  This property supports case-insensitive filtering. | [optional] 
**management_address** | **str** | Management address to use for communicating with the Unity storage system. The address can be an IPv4 address or FQDN (Fully Qualified Domain Name). | [optional] 
**model** | **str** | Model name of the Unity storage system. | [optional] 
**software_version** | **str** | Software version of the Unity storage system. | [optional] 
**api_version** | **str** | Version of the API that the Unity storage system supports. | [optional] 
**health** | [**UnityHealthEnum**](UnityHealthEnum.md) |  | [optional] 
**user_name** | **str** | User account name used to communicate with the Unity storage system. | [optional] 
**serial_number** | **str** | Serial number of the system | [optional] 
**last_updated_timestamp** | **datetime** | Date and time when the Unity storage system details were last updated. These details include the Unity storage system and information about its importable volumes and consistency groups. The timestamp is updated when the Unity storage system is created and whenever the importable volumes and consistency groups are discovered. | [optional] 
**supported_import_type** | [**SupportedImportTypeEnum**](SupportedImportTypeEnum.md) |  Was added in version 1.0.2. | [optional] 
**health_l10n** | **str** | Localized message string corresponding to health | [optional] 
**supported_import_type_l10n** | **str** | Localized message string corresponding to supported_import_type Was added in version 1.0.2. | [optional] 
**import_unity_volumes** | [**list[ImportUnityVolumeInstance]**](ImportUnityVolumeInstance.md) | This is the inverse of the resource type import_unity_volume association. | [optional] 
**import_unity_consistency_groups** | [**list[ImportUnityConsistencyGroupInstance]**](ImportUnityConsistencyGroupInstance.md) | This is the inverse of the resource type import_unity_consistency_group association. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


