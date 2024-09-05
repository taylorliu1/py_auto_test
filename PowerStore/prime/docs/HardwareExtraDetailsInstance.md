# HardwareExtraDetailsInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_model** | **str** | CPU model name. Available on Node hardware type. | [optional] 
**physical_memory_size_gb** | **int** | Total amount of physical memory in gigabytes. Available on the Node hardware type. | [optional] 
**cpu_cores** | **int** | Total number of physical cores. Available on the Node hardware type. | [optional] 
**cpu_sockets** | **int** | Total number of physical sockets. Available on the Node hardware type. | [optional] 
**bus_number** | **int** | Bus number of the Expansion_Shelf. Available on the Expansion_Shelf hardware type. | [optional] 
**enclosure_number** | **int** | Enclosure number of the Expansion_Shelf. Available on the Expansion_Shelf hardware type. | [optional] 
**model_name** | **str** | Model name of the hardware.  Available on the IO_Module and M2_Drive hardware types. | [optional] 
**rpm_reading** | **str** | rpm_reading. Was added in version 2.0.0.0. | [optional] 
**firmware_version** | **str** | Firmware version of the hardware. Available on the Drive hardware type. | [optional] 
**mode** | [**HardwareSFPModeEnum**](HardwareSFPModeEnum.md) |  | [optional] 
**supported_speeds** | [**list[HardwareSFPSpeedEnum]**](HardwareSFPSpeedEnum.md) |  | [optional] 
**supported_protocol** | [**HardwareSFPSupportedProtocolEnum**](HardwareSFPSupportedProtocolEnum.md) |  | [optional] 
**connector_type** | [**HardwareSFPConnectorTypeEnum**](HardwareSFPConnectorTypeEnum.md) |  | [optional] 
**drive_type** | [**HardwareDriveTypeEnum**](HardwareDriveTypeEnum.md) |  | [optional] 
**size** | **int** | Size of the drive in bytes. Available on the Drive hardware type. | [optional] 
**encryption_status** | [**HardwareDriveEncryptionStatusEnum**](HardwareDriveEncryptionStatusEnum.md) |  | [optional] 
**fips_status** | [**HardwareDriveFIPSStatusEnum**](HardwareDriveFIPSStatusEnum.md) |  | [optional] 
**dell_service_tag** | **str** | Dell service tag of the hardware. Available on the Base_Enclosure and Expansion_Enclosure hardware types. | [optional] 
**express_service_code** | **str** | Express service code of the hardware. Available on the Base_Enclosure and Expansion_Enclosure hardware types. | [optional] 
**enclosure_model_description** | [**HardwareEnclosureModelDescriptionEnum**](HardwareEnclosureModelDescriptionEnum.md) |  Was added in version 3.0.0.0. | [optional] 
**mode_l10n** | **str** | Localized message string corresponding to mode | [optional] 
**supported_speeds_l10n** | **list[str]** | Localized message array corresponding to supported_speeds | [optional] 
**supported_protocol_l10n** | **str** | Localized message string corresponding to supported_protocol | [optional] 
**connector_type_l10n** | **str** | Localized message string corresponding to connector_type | [optional] 
**drive_type_l10n** | **str** | Localized message string corresponding to drive_type | [optional] 
**encryption_status_l10n** | **str** | Localized message string corresponding to encryption_status | [optional] 
**fips_status_l10n** | **str** | Localized message string corresponding to fips_status | [optional] 
**enclosure_model_description_l10n** | **str** | Localized message string corresponding to enclosure_model_description Was added in version 3.0.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


