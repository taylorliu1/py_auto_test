# DiscoveredApplianceInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of a discovered appliance. The local discovered appliance has the id \&quot;0\&quot;. | [optional] 
**link_local_address** | **str** | The link local IPv4 address for the appliance. | [optional] 
**service_name** | **str** | The service name of the appliance. | [optional] 
**service_tag** | **str** | The Dell service tag. | [optional] 
**state** | [**DiscoveredApplianceStateEnum**](DiscoveredApplianceStateEnum.md) |  | [optional] 
**type** | [**DiscoveredApplianceTypeEnum**](DiscoveredApplianceTypeEnum.md) |  | [optional] 
**mode** | [**DiscoveredApplianceModeEnum**](DiscoveredApplianceModeEnum.md) |  | [optional] 
**model** | **str** | The model of the appliance. | [optional] 
**express_service_code** | **str** | The Express service code for the appliance. | [optional] 
**is_local** | **bool** | Indicates whether appliance is local (serving this request) or not. | [optional] 
**management_service_ready** | **bool** | Indicates whether necessary management services are ready. | [optional] 
**software_version_compatibility** | [**DiscoveredApplianceSoftwareVersionCompatibilityEnum**](DiscoveredApplianceSoftwareVersionCompatibilityEnum.md) |  | [optional] 
**build_version** | **str** | Build version of the installed software package release. | [optional] 
**build_id** | **str** | Unique identifier of this build. | [optional] 
**power_score** | **int** | Power rating for this appliance. | [optional] 
**node_count** | **int** | The number of nodes deployed on an appliance. | [optional] [default to 2]
**is_unified_capable** | **bool** | Indicates whether the appliance is capable of a unified configuration | [optional] 
**drive_failure_tolerance_level_and_availability** | [**list[DiscoveredApplianceDriveFailureToleranceLevelAvailability]**](DiscoveredApplianceDriveFailureToleranceLevelAvailability.md) | Information about the drive failure tolerance levels.  Filtering on the fields of this embedded resource is not supported. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


