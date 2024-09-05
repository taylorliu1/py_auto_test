# SecurityConfigInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the security configuration. | [optional] 
**idle_timeout** | **int** | Idle time (in seconds) after which login sessions will expire and require re-authentication. | [optional] 
**protocol_mode** | [**SecurityProtocolModeEnum**](SecurityProtocolModeEnum.md) |  Was added in version 2.0.0.0. | [optional] 
**is_http_redirect_enabled** | **bool** | If true, redirecting HTTP requests to HTTPs is enabled. If false, HTTP redirection is disabled and only HTTPs is supported. Was added in version 3.0.0.0. | [optional] [default to False]
**protocol_mode_l10n** | **str** | Localized message string corresponding to protocol_mode\\nWas added in version 2.0.0.0. Was deprecated in version 3.0.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


