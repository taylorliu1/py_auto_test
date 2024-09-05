# NfsExportInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id of the NFS Export. | [optional] 
**file_system_id** | **str** | Unique identifier of the file system on which the NFS Export was created. | [optional] 
**name** | **str** | NFS Export name.  This property supports case-insensitive filtering. | [optional] 
**path** | **str** | Local path to a location within the file system. With NFS, each export must have a unique local path. By default, the system exports the root of the file system (top-most directory) at the time the file system is created. This path specifies the unique location of the file system on the storage system. Before you can create additional exports within an NFS shared folder, you must create directories within it from a Linux/Unix host that is connected to the file system. After a directory has been created from a mounted host, you can create a corresponding export and set access permissions accordingly.  | [optional] 
**description** | **str** | NFS Export description. | [optional] 
**default_access** | [**NFSExportDefaultAccessEnum**](NFSExportDefaultAccessEnum.md) |  | [optional] 
**min_security** | [**NFSExportMinSecurityEnum**](NFSExportMinSecurityEnum.md) |  | [optional] 
**nfs_owner_username** | **str** | (*Applies to NFS shares of VMware NFS storage resources.*) Default owner of the NFS Export associated with the datastore. Required if secure NFS enabled. For NFSv3 or NFSv4 without Kerberos, the default owner is root. | [optional] 
**no_access_hosts** | **list[str]** | Hosts with no access to the NFS export or its snapshots. Hosts can be entered by Hostname, IP addresses (IPv4, IPv6, IPv4/PrefixLength, IPv6/PrefixLenght, or IPv4/subnetmask), or Netgroups prefixed with @. | [optional] 
**read_only_hosts** | **list[str]** | Hosts with read-only access to the NFS export and its snapshots. Hosts can be entered by Hostname, IP addresses (IPv4, IPv6, IPv4/PrefixLength, IPv6/PrefixLenght, or IPv4/subnetmask), or Netgroups prefixed with @. | [optional] 
**read_only_root_hosts** | **list[str]** | Hosts with read-only and ready-only for root user access to the NFS Export and its snapshots. Hosts can be entered by Hostname, IP addresses (IPv4, IPv6, IPv4/PrefixLength, IPv6/PrefixLenght, or IPv4/subnetmask), or Netgroups prefixed with @. | [optional] 
**read_write_hosts** | **list[str]** | Hosts with read and write access to the NFS export and its snapshots. Hosts can be entered by Hostname, IP addresses (IPv4, IPv6, IPv4/PrefixLength, IPv6/PrefixLenght, or IPv4/subnetmask), or Netgroups prefixed with @. | [optional] 
**read_write_root_hosts** | **list[str]** | Hosts with read and write and read and write for root user access to the NFS Export and its snapshots. Hosts can be entered by Hostname, IP addresses (IPv4, IPv6, IPv4/PrefixLength, IPv6/PrefixLenght, or IPv4/subnetmask), or Netgroups prefixed with @. | [optional] 
**anonymous_uid** | **int** | Specifies the user ID of the anonymous account. | [optional] [default to -2]
**anonymous_gid** | **int** | Specifies the group ID of the anonymous account. | [optional] [default to -2]
**is_no_suid** | **bool** | If set, do not allow access to set SUID. Otherwise, allow access. | [optional] 
**default_access_l10n** | **str** | Localized message string corresponding to default_access | [optional] 
**min_security_l10n** | **str** | Localized message string corresponding to min_security | [optional] 
**file_system** | [**FileSystemInstance**](FileSystemInstance.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

