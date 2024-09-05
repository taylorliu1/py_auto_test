# FileVirusCheckerInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the virus checker instance. | [optional] 
**nas_server_id** | **str** | NAS server that is configured with these anti-virus settings. | [optional] 
**is_enabled** | **bool** | Indicates whether the anti-virus service is enabled on this NAS server. Value are: - true - Anti-virus service is enabled. Each file created or modified by an SMB client is scanned by the third-party anti-virus servers. If a virus is detected, the access to the file system is denied. If third-party anti-virus servers are not available, according the policy, the access to the file systems is denied to prevent potential viruses propagation. - false - Anti-virus service is disabled. File systems of the NAS servers are available for access without virus checking  | [optional] 
**is_config_file_uploaded** | **bool** | Indicates whether a virus checker configuration file has been uploaded. | [optional] [default to False]
**nas_server** | [**NasServersInstance**](NasServersInstance.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

