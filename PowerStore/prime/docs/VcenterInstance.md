# VcenterInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the vCenter instance. | [optional] 
**instance_uuid** | **str** | UUID instance of the vCenter. | [optional] 
**address** | **str** | IP address of vCenter host, in IPv4, IPv6, or hostname format. | [optional] 
**username** | **str** | User name to login to vCenter. | [optional] 
**version** | **str** | Version of the vCenter including its build number. Was added in version 3.0.0.0. | [optional] 
**vendor_provider_status** | [**VendorProviderStatusEnum**](VendorProviderStatusEnum.md) | General status of the VASA vendor provider in vCenter. A VASA vendor provider is required for HCI deployments, and optional for SAN deployments. To register or re-register the VASA vendor provider, pass appropriate storage system credentials using the modify request. Was added in version 2.0.0.0. | [optional] 
**vendor_provider_status_l10n** | **str** | Localized message string corresponding to vendor_provider_status Was added in version 2.0.0.0. | [optional] 
**virtual_machines** | [**list[VirtualMachineInstance]**](VirtualMachineInstance.md) | This is the inverse of the resource type virtual_machine association. | [optional] 
**datastores** | [**list[DatastoreInstance]**](DatastoreInstance.md) | This is the inverse of the resource type datastore association. | [optional] 
**vsphere_hosts** | [**list[VsphereHostInstance]**](VsphereHostInstance.md) | This is the inverse of the resource type vsphere_host association. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


