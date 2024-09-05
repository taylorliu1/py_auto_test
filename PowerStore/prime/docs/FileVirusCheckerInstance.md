# FileVirusCheckerInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the virus checker instance. | [optional] 
**nas_server_id** | **str** | NAS server that is configured with these anti-virus settings. | [optional] 
**is_enabled** | **bool** | Indicates whether the anti-virus service is enabled on this NAS server. Value are: - true - Anti-virus service is enabled. Each file created or modified by an SMB client is scanned by the third-party anti-virus servers. If a virus is detected, the access to the file system is denied. If third-party anti-virus servers are not available, according the policy, the access to the file systems is denied to prevent potential viruses propagation. - false - Anti-virus service is disabled. File systems of the NAS servers are available for access without virus checking  | [optional] 
**is_config_file_uploaded** | **bool** | Indicates whether a virus checker configuration file has been uploaded. | [optional] [default to False]
**is_destination_override_enabled** | **bool** | In order to modify the configuration of this resource when the associated NAS server is a replication destination, the is_destination_override_enabled flag must be set to true. When true, a virus checker config file may be uploaded on the destination to override the source virus checker config file. Values are:   true - Enable locally set configuration. A virus checker config file may be uploaded on the destination to override the source virus checker config file.   false - Revert to use the source configuration file. Source configuration file changes will propagate directly to this resource.  Was added in version 3.0.0.0. | [optional] [default to False]
**nas_server** | [**NasServerInstance**](NasServerInstance.md) | This is the embeddable reference form of nas_server_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


