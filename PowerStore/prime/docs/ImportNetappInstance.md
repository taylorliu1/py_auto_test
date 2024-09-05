# ImportNetappInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the storage system that is a source storage system for import. | [optional] 
**name** | **str** | Name of the NetApp storage system.  This property supports case-insensitive filtering. | [optional] 
**management_address** | **str** | Management address to use for communicating with the NetApp storage system. The address can be an IPv4 address or FQDN (Fully Qualified Domain Name). | [optional] 
**serial_number** | **str** | Serial number will be the SVM uuid. | [optional] 
**api_version** | **str** | Version of the ONTAP API that manages the NetApp storage system. | [optional] 
**supported_import_type** | [**SupportedImportTypeEnum**](SupportedImportTypeEnum.md) |  | [optional] 
**state** | [**NetAppSVMStateEnum**](NetAppSVMStateEnum.md) |  | [optional] 
**user_name** | **str** | User account name used to communicate with the NetApp storage system. | [optional] 
**last_updated_timestamp** | **datetime** | Date and time when the NetApp storage system details were last updated. These details include the NetApp storage system and information about its importable volumes. The timestamp is updated when the NetApp storage system is created and whenever the importable volumes is discovered. | [optional] 
**supported_import_type_l10n** | **str** | Localized message string corresponding to supported_import_type Was added in version 3.0.0.0. | [optional] 
**state_l10n** | **str** | Localized message string corresponding to state Was added in version 3.0.0.0. | [optional] 
**import_netapp_volumes** | [**list[ImportNetappVolumeInstance]**](ImportNetappVolumeInstance.md) | This is the inverse of the resource type import_netapp_volume association. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


