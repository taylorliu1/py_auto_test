# ImportSessionCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_system_id** | **str** | Unique identifier of the storage system that contains the source volume or consistency group to be imported. You can query the source volume or consistency group object to get the identifier of the source system that the volume or consistency group are part of. Alternatively, you can use the remote_system object to get this information. name:{name} can be used instead of {id}. For example:&#39;remote_system_id&#39;:&#39;name:remote_system_name&#39; | 
**source_resource_id** | **str** | Unique identifier of the volume or consistency group to be imported. Refer to the following objects for more information: * Storage Center : import_storage_center_volume, import_storage_center_consistency_group * VNX : import_vnx_volume, import_vnx_consistency_group * PS Series : import_psgroup_volume * Unity : import_unity_volume, import_unity_consistency_group | 
**name** | **str** | Name of the import session. The name must be unique in the PowerStore cluster and can contain a maximum of 128 unicode characters. It cannot contain special HTTP characters, unprintable characters, or white space. | 
**global_storage_discovery_address** | **str** | Global storage discovery iSCSI ip address that will be used for import workflow. The address can be an IPv4 address or FQDN (Fully Qualified Domain Name). Was added in version 3.0.0.0. | [optional] 
**description** | **str** | Description of the import session. The name can contain a maximum of 128 unicode characters. It cannot contain unprintable characters. | [optional] 
**type** | [**ImportSessionTypeEnum**](ImportSessionTypeEnum.md) |  Was added in version 1.0.2. | [optional] 
**host_ids** | **list[str]** | Hosts to be mapped to the destination resource for an agentless import session. Was added in version 1.0.2. | [optional] 
**host_group_ids** | **list[str]** | Unique identifiers of the host groups that map to the destination resource for an agentless import session. In case of a consistency group, if all the member volumes have the same host group mapping, then use this property, otherwise use consistency_group_member_host_group_ids. Was added in version 2.0.0.0. | [optional] 
**consistency_group_member_host_ids** | [**list[ConsistencyGroupMemberHostMapping]**](ConsistencyGroupMemberHostMapping.md) |  Was added in version 1.0.2. | [optional] 
**consistency_group_member_host_group_ids** | [**list[ConsistencyGroupMemberHostGroupMapping]**](ConsistencyGroupMemberHostGroupMapping.md) |  Was added in version 2.0.0.0. | [optional] 
**volume_group_id** | **str** | Unique identifier of the volume group to which the imported volume will belong, if any. name:{name} can be used instead of {id}. For example:&#39;volume_group_id&#39;:&#39;name:volume_group_name&#39; | [optional] 
**automatic_cutover** | **bool** | Indicates whether the import session cutover is manual (true) or automatic (false). | [optional] [default to False]
**protection_policy_id** | **str** | Unique identifier of the protection policy that will be applied to an imported volume or consistency group after the import completes. Only snapshot policies are supported in an import. Once the import completes, you can add a replication policy. If you try to import a replication policy, the import job will fail. | [optional] 
**scheduled_timestamp** | **datetime** | Date and time at which the import session is scheduled to start. The date time is specified in ISO 8601 format with the time expressed in UTC format. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


