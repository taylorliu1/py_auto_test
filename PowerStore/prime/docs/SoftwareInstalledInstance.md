# SoftwareInstalledInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the installed software instance. | [optional] 
**is_cluster** | **bool** | Whether this information represents the common software release version that is supported on all appliances in the cluster. The value is true for the instance representing the cluster. The value is false for appliance software instances. | [optional] 
**release_version** | **str** | Version of the installed release software package release. | [optional] 
**build_version** | **str** | Build version of the installed software package release. Was added in version 2.0.0.0. | [optional] 
**release_timestamp** | **datetime** | Date and time when this software package was produced. | [optional] 
**installed_date** | **datetime** | Date and time when the software was successfully installed and committed on the cluster. If the software package has not been commited, this value is null. | [optional] 
**build_flavor** | [**SoftwareInstalledBuildFlavorEnum**](SoftwareInstalledBuildFlavorEnum.md) |  Was added in version 2.0.0.0. | [optional] 
**build_type** | [**SoftwareInstalledBuildTypeEnum**](SoftwareInstalledBuildTypeEnum.md) |  Was added in version 2.0.0.0. | [optional] 
**build_id** | **str** | Unique identifier of this build. Was added in version 2.0.0.0. | [optional] 
**build_flavor_l10n** | **str** | Localized message string corresponding to build_flavor Was added in version 2.0.0.0. | [optional] 
**build_type_l10n** | **str** | Localized message string corresponding to build_type Was added in version 2.0.0.0. | [optional] 
**appliance** | [**ApplianceInstance**](ApplianceInstance.md) | This is the embeddable reference form of appliance_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


