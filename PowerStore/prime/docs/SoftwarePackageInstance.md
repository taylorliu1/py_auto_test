# SoftwarePackageInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the software package. | [optional] 
**name** | **str** | Name of the software package.  This property supports case-insensitive filtering. | [optional] 
**description_l10n** | **str** | Summary of the contents in this package. | [optional] 
**justification_l10n** | **str** | Explanation of why this software release is recommended for this cluster. | [optional] 
**software_package_type** | [**SoftwarePackageTypeEnum**](SoftwarePackageTypeEnum.md) |  | [optional] 
**software_package_state** | [**SoftwarePackageStateEnum**](SoftwarePackageStateEnum.md) |  | [optional] 
**size** | **int** | File size of the software package in bytes. | [optional] 
**is_reboot_required** | **bool** | Whether a reboot is required during the upgrade process. | [optional] 
**release_version** | **str** | Version number of the software package. | [optional] 
**build_version** | **str** | Build number of the software package. Was added in version 2.0.0.0. | [optional] 
**release_timestamp** | **datetime** | Date and time when this software package was produced. | [optional] 
**installed_date** | **datetime** | Date and time when this software package was successfully installed and committed on the cluster. If the software package has not been committed, this value is null. | [optional] 
**build_flavor** | [**SoftwarePackageBuildFlavorEnum**](SoftwarePackageBuildFlavorEnum.md) |  Was added in version 2.0.0.0. | [optional] 
**build_type** | [**SoftwarePackageBuildTypeEnum**](SoftwarePackageBuildTypeEnum.md) |  Was added in version 2.0.0.0. | [optional] 
**build_id** | **str** | Unique identifier of this build. Was added in version 2.0.0.0. | [optional] 
**software_package_type_l10n** | **str** | Localized message string corresponding to software_package_type | [optional] 
**software_package_state_l10n** | **str** | Localized message string corresponding to software_package_state | [optional] 
**build_flavor_l10n** | **str** | Localized message string corresponding to build_flavor Was added in version 2.0.0.0. | [optional] 
**build_type_l10n** | **str** | Localized message string corresponding to build_type Was added in version 2.0.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


