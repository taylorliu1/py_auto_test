# VsphereHostInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the vsphere_host instance. | [optional] 
**name** | **str** | User-assigned name of the ESXi host in vCenter.  This property supports case-insensitive filtering. | [optional] 
**vsphere_object_id** | **str** | Unique identifier of the vsphere_host in vCenter. | [optional] 
**vcenter_id** | **str** | Unique identifier of a vCenter instance. | [optional] 
**version** | **str** | ESXi host version. | [optional] 
**build** | **str** | ESXi host build. | [optional] 
**vcenter** | [**VcenterInstance**](VcenterInstance.md) | This is the embeddable reference form of vcenter_id attribute. | [optional] 
**license_assignments** | [**list[VsphereHostLicenseAssignmentInstance]**](VsphereHostLicenseAssignmentInstance.md) | This is the inverse of the resource type vsphere_host_license_assignment association. | [optional] 
**virtual_machines** | [**list[VirtualMachineInstance]**](VirtualMachineInstance.md) | List of the virtual_machines that are associated with this vsphere_host. | [optional] 
**datastores** | [**list[DatastoreInstance]**](DatastoreInstance.md) | List of the datastores that are associated with this vsphere_host. | [optional] 
**hosts** | [**list[HostInstance]**](HostInstance.md) | List of the hosts that are associated with this vsphere_host. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


