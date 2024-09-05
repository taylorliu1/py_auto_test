# DatastoreInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the datastore instance. | [optional] 
**instance_uuid** | **str** | UUID instance of the datastore in vCenter. | [optional] 
**name** | **str** | User-assigned name of the datastore in vCenter.  This property supports case-insensitive filtering. | [optional] 
**type** | [**DatastoreTypeEnum**](DatastoreTypeEnum.md) |  | [optional] 
**vsphere_object_id** | **str** | Unique identifier of the datastore in vCenter. | [optional] 
**vcenter_id** | **str** | Unique identifier of a vCenter instance. | [optional] 
**storage_container_id** | **str** | Unique identifier of a backing storage_container instance (for vVol type only). | [optional] 
**nfs_export_id** | **str** | Unique identifier of a backing nfs_export instance (for NFS type only). | [optional] 
**type_l10n** | **str** | Localized message string corresponding to type Was added in version 3.0.0.0. | [optional] 
**vcenter** | [**VcenterInstance**](VcenterInstance.md) | This is the embeddable reference form of vcenter_id attribute. | [optional] 
**storage_container** | [**StorageContainerInstance**](StorageContainerInstance.md) | This is the embeddable reference form of storage_container_id attribute. | [optional] 
**nfs_export** | [**NfsExportInstance**](NfsExportInstance.md) | This is the embeddable reference form of nfs_export_id attribute. | [optional] 
**virtual_machines** | [**list[VirtualMachineInstance]**](VirtualMachineInstance.md) | List of the virtual_machines that are associated with this datastore. | [optional] 
**volumes** | [**list[VolumeInstance]**](VolumeInstance.md) | List of the volumes that are associated with this datastore. | [optional] 
**vsphere_hosts** | [**list[VsphereHostInstance]**](VsphereHostInstance.md) | List of the vsphere_hosts that are associated with this datastore. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


