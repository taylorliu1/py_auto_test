# FileImportSessionCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the import session. The name must be unique in the PowerStore cluster and can contain a maximum of 32 unicode characters. It cannot contain special HTTP characters, unprintable characters, or white space. | 
**remote_system_id** | **str** | Unique identifier of the storage system that contains the source NAS server to be imported.     You can query the source NAS server object to get the identifier of the source system.     Alternatively, you can use the remote_system object to get this information. name:{name} can be used instead of {id}. For example:&#39;remote_system_id&#39;:&#39;name:remote_system_name&#39; | 
**source_resource_id** | **str** | Unique identifier of the source NAS server to be imported. Refer to the following objects for more information: * VNX - import_vnx_nas_server. | 
**description** | **str** | Description of the file import session.     The name can contain a maximum of 128 Unicode characters.     It cannot contain unprintable characters. | [optional] 
**import_file_interface_id** | **str** | Unique identifier of the file interface in the destination system that is used for importing data from the source system. | 
**source_smb_admin_username** | **str** | User name for authentication to SMB Server on the source NAS server with administrator privilege. This is required for SMB import. | [optional] 
**source_smb_admin_password** | **str** | Password for authentication to SMB Server on the source NAS Server with administrator privilege. This is required for SMB import. | [optional] 
**scheduled_timestamp** | **str** | Indicates the desired date and time at which the file import session should be scheduled to run. The date is specified in ISO 8601 format with time expressed in UTC format. | [optional] 
**protection_policy_id** | **str** | Unique identifier of the protection policy that will be applied to an imported NAS server or filesystem after the import completes. Only snapshot policies are supported in an import. Once the import completes, you can add a replication policy. If you try to import a replication policy, the import job will fail. | [optional] 
**source_dhsm_username** | **str** | The username for authentication to DHSM Server on the source NAS Server required for importing FLR filesystems. | [optional] 
**source_dhsm_password** | **str** | The password for authentication to DHSM Server on the source NAS Server required for importing FLR filesystems. | [optional] 
**file_interfaces** | [**list[FileImportSessionFileInterfaceMapping]**](FileImportSessionFileInterfaceMapping.md) | Optional list of mappings from source file interfaces to local bond/FSN. By default, all file interfaces associated with source NAS Server will be mapped with system bond/FSN. For alternate mappings for some or all of the source file interfaces, use this to specify the file interface and bond/FSN pairs. Any source file interfaces without an explicit mapping will be mapped to the system bond/FSN.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


