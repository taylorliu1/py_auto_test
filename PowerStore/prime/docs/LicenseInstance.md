# LicenseInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ididentifier of the cluster license. | [optional] 
**is_licensed** | **bool** | Whether or not the cluster currently has a valid license. | [optional] 
**trial_expiration_timestamp** | **datetime** | If not currently licensed, the date the trial period expires. If the trial period expires, new provisioning operations will not be allowed. | [optional] 
**activation_file_content** | **str** | The content of the license activation file to send to the DellEMC Software Licensing Central to retrieve the software license for the cluster. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


