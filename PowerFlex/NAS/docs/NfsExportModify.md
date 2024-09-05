# NfsExportModify

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | NFS Export description. | [optional] 
**default_access** | [**NFSExportDefaultAccessEnum**](NFSExportDefaultAccessEnum.md) |  | [optional] 
**min_security** | [**NFSExportMinSecurityEnum**](NFSExportMinSecurityEnum.md) |  | [optional] 
**no_access_hosts** | **list[str]** | Hosts with no access to the NFS export or its snapshots. Hosts can be entered by Hostname, IP addresses (IPv4, IPv6, IPv4/PrefixLength, IPv6/PrefixLenght, or IPv4/subnetmask), or Netgroups prefixed with @. | [optional] 
**add_no_access_hosts** | **list[str]** | Hosts to add to the no_access_host list. Hosts can be entered by Hostname, IP addresses (IPv4, IPv6, IPv4/PrefixLength, IPv6/PrefixLenght, or IPv4/subnetmask), or Netgroups prefixed with @. Error if the host already exists in the list. Cannot be combined with no_access_hosts. | [optional] 
**remove_no_access_hosts** | **list[str]** | Hosts to remove from the current no_access_hosts list. Hosts can be entered by Hostname, IP addresses (IPv4, IPv6, IPv4/PrefixLength, IPv6/PrefixLenght, or IPv4/subnetmask), or Netgroups prefixed with @. Error if the host is not present. Cannot combine with no_access_hosts. | [optional] 
**read_only_hosts** | **list[str]** | Hosts with read-only access to the NFS export and its snapshots. Hosts can be entered by Hostname, IP addresses (IPv4, IPv6, IPv4/PrefixLength, IPv6/PrefixLenght, or IPv4/subnetmask), or Netgroups prefixed with @. | [optional] 
**add_read_only_hosts** | **list[str]** | Hosts to add to the current read_only_hosts list. Hosts can be entered by Hostname, IP addresses (IPv4, IPv6, IPv4/PrefixLength, IPv6/PrefixLenght, or IPv4/subnetmask), or Netgroups prefixed with @. Error if the host already exists. Cannot combine with read_only_hosts. | [optional] 
**remove_read_only_hosts** | **list[str]** | Hosts to remove from the current read_only_hosts list. Hosts can be entered by Hostname, IP addresses (IPv4, IPv6, IPv4/PrefixLength, IPv6/PrefixLenght, or IPv4/subnetmask), or Netgroups prefixed with @. Error if the host is not present. Cannot combine with read_only_hosts. | [optional] 
**read_only_root_hosts** | **list[str]** | Hosts with read-only and ready-only for root user access to the NFS Export and its snapshots. Hosts can be entered by Hostname, IP addresses (IPv4, IPv6, IPv4/PrefixLength, IPv6/PrefixLenght, or IPv4/subnetmask), Netgroups prefixed with @. | [optional] 
**add_read_only_root_hosts** | **list[str]** | Hosts to add to the current read_only_root_hosts list. Hosts can be entered by Hostname, IP addresses (IPv4, IPv6, IPv4/PrefixLength, IPv6/PrefixLenght, or IPv4/subnetmask), or Netgroups prefixed with @. Error if the host already exists. Cannot combine with read_only_root_hosts. | [optional] 
**remove_read_only_root_hosts** | **list[str]** | Hosts to remove from the current read_only_root_hosts list. Hosts can be entered by Hostname, IP addresses (IPv4, IPv6, IPv4/PrefixLength, IPv6/PrefixLenght, or IPv4/subnetmask), or Netgroups prefixed with @. Error if The host is not present. Cannot combine with read_only_root_hosts. | [optional] 
**read_write_hosts** | **list[str]** | Hosts with read and write access to the NFS export and its snapshots. Hosts can be entered by Hostname, IP addresses (IPv4, IPv6, IPv4/PrefixLength, IPv6/PrefixLenght, or IPv4/subnetmask) or, Netgroups prefixed with @. | [optional] 
**add_read_write_hosts** | **list[str]** | Hosts to add to the current read_write_hosts list. Hosts can be entered by Hostname, IP addresses (IPv4, IPv6, IPv4/PrefixLength, IPv6/PrefixLenght, or IPv4/subnetmask), or Netgroups prefixed with @. Error if Host is already exists. Cannot combine with read_write_hosts. | [optional] 
**remove_read_write_hosts** | **list[str]** | Hosts to remove from the current read_write_hosts list. Hosts can be entered by Hostname, IP addresses (IPv4, IPv6, IPv4/PrefixLength, IPv6/PrefixLenght, or IPv4/subnetmask), or Netgroups prefixed with @. Error if Host is not present. Cannot combine with read_write_hosts. | [optional] 
**read_write_root_hosts** | **list[str]** | Hosts with read and write and read and write for root user access to the NFS Export and its snapshots. Hosts can be entered by Hostname, IP addresses (IPv4, IPv6, IPv4/PrefixLength, IPv6/PrefixLenght, or IPv4/subnetmask), or Netgroups prefixed with @. | [optional] 
**add_read_write_root_hosts** | **list[str]** | Hosts to add to the current read_write_root_hosts list. Hosts can be entered by Hostname, IP addresses (IPv4, IPv6, IPv4/PrefixLength, IPv6/PrefixLenght, or IPv4/subnetmask), or Netgroups prefixed with @. Error if the host already exists. Cannot combine with read_write_root_hosts. | [optional] 
**remove_read_write_root_hosts** | **list[str]** | Hosts to remove from the current read_write_root_hosts list. Hosts can be entered by Hostname, IP addresses (IPv4, IPv6, IPv4/PrefixLength, IPv6/PrefixLenght, or IPv4/subnetmask), or Netgroups prefixed with @. Error if the host is not present. Cannot combine with read_write_root_hosts. | [optional] 
**anonymous_uid** | **int** | Specifies the user ID of the anonymous account. | [optional] [default to -2]
**anonymous_gid** | **int** | Specifies the group ID of the anonymous account. | [optional] [default to -2]
**is_no_suid** | **bool** | If set, do not allow access to set SUID. Otherwise, allow access. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

