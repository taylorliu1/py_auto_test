# NfsExportCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_system_id** | **str** | Unique identifier of the file system on which the NFS Export will be created. name:{name} can be used instead of {id}. For example:&#39;file_system_id&#39;:&#39;name:file_system_name&#39; | 
**path** | **str** | Local path to export relative to the file system root directory. With NFS, each export of a file_system or file_snap must have a unique local path. Before you can create additional Exports within an NFS shared folder, you must create directories within it from a Linux/Unix host that is connected to the file system. After a directory has been created from a mounted host, you can create a corresponding Export and set access permissions accordingly.  | 
**name** | **str** | NFS Export name. | 
**description** | **str** | User defined NFS Export description. | [optional] 
**default_access** | [**NFSExportDefaultAccessEnum**](NFSExportDefaultAccessEnum.md) |  | [optional] 
**min_security** | [**NFSExportMinSecurityEnum**](NFSExportMinSecurityEnum.md) |  | [optional] 
**no_access_hosts** | **list[str]** | Hosts with no access to the NFS export or its snapshots. Hosts can be entered by Hostname, IP addresses (IPv4, IPv6, IPv4/PrefixLength, IPv6/PrefixLenght, or IPv4/subnetmask), or Netgroups prefixed with @. The maximum length of an Host name is 255 bytes, and the sum of lengths of all the items in the list is limited to 4096 bytes. | [optional] 
**read_only_hosts** | **list[str]** | Hosts with read-only access to the NFS export and its snapshots. Hosts can be entered by Hostname, IP addresses (IPv4, IPv6, IPv4/PrefixLength, IPv6/PrefixLenght, or IPv4/subnetmask), or Netgroups prefixed with @. The maximum length of an Host name is 255 bytes, and the sum of lengths of all the items in the list is limited to 4096 bytes. | [optional] 
**read_only_root_hosts** | **list[str]** | Hosts with read-only and ready-only for root user access to the NFS Export and its snapshots. Hosts can be entered by Hostname, IP addresses (IPv4, IPv6, IPv4/PrefixLength, IPv6/PrefixLenght, or IPv4/subnetmask), or Netgroups prefixed with @. The maximum length of an Host name is 255 bytes, and the sum of lengths of all the items in the list is limited to 4096 bytes. | [optional] 
**read_write_hosts** | **list[str]** | Hosts with read and write access to the NFS export and its snapshots.Hosts can be entered by Hostname, IP addresses (IPv4, IPv6, IPv4/PrefixLength, IPv6/PrefixLenght, or IPv4/subnetmask), or Netgroups prefixed with @. The maximum length of an Host name is 255 bytes, and the sum of lengths of all the items in the list is limited to 4096 bytes. | [optional] 
**read_write_root_hosts** | **list[str]** | Hosts with read and write and read and write for root user access to the NFS Export and its snapshots. Hosts can be entered by Hostname, IP addresses (IPv4, IPv6, IPv4/PrefixLength, IPv6/PrefixLenght, or IPv4/subnetmask), or Netgroups prefixed with @. The maximum length of an Host name is 255 bytes, and the sum of lengths of all the items in the list is limited to 4096 bytes. | [optional] 
**anonymous_uid** | **int** | Specifies the user ID of the anonymous account. | [optional] [default to -2]
**anonymous_gid** | **int** | Specifies the group ID of the anonymous account. | [optional] [default to -2]
**is_no_suid** | **bool** | If set, do not allow access to set SUID. Otherwise, allow access. | [optional] [default to False]
**nfs_owner_username** | **str** | (*Applies to NFS shares of VMware NFS storage resources.*) Default owner of the NFS Export associated with the datastore. Required if secure NFS enabled. For NFSv3 or NFSv4 without Kerberos, the default owner is root. Was added in version 3.0.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


