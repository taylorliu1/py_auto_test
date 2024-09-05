# NetworkReplace

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vlan_id** | **int** | VLAN identifier. | 
**gateway** | **str** | Network gateway in IPv4 or IPv6 format, corresponding to the network&#39;s IP version. Specify empty string to remove the gateway.  | 
**prefix_length** | **int** | Network prefix length. (Used for both IPv4 and IPv6). | 
**cluster_mgmt_address** | **str** | New cluster management IP address in IPv4 or IPv6 format, corresponding to the network&#39;s IP version. | 
**vasa_provider_credentials** | **object** | Credentials required for re-registering the VASA vendor provider during the replacement of the cluster management IP address. Should be passed only when reconfiguring PowerStoreX cluster.  | [optional] 
**esxi_credentials** | [**EsxiCredentials**](EsxiCredentials.md) |  | [optional] 
**mtu** | **int** | Maximum Transmission Unit (MTU) packet size set on network interfaces, in bytes. | 
**ip_pool_addresses** | **list[str]** | List of new IP addresses in IPv4 or IPv6 format. | 
**dns_addresses** | **list[str]** | List of new DNS server IP addresses in IPv4 or IPv6 format. | 
**ntp_addresses** | **list[str]** | List of new NTP server FQDNs or IP addresses in IPv4 or IPv6 format. | 
**vcenter_address** | **str** | New vCenter FQDNs or IP address in IPv4 or IPv6 format. Required only when reconfiguring PowerStoreX cluster. | [optional] 
**smtp_config** | [**NetworkReplaceSmtpConfig**](NetworkReplaceSmtpConfig.md) |  | [optional] 
**physical_switches** | [**list[NetworkReplacePhysicalSwitch]**](NetworkReplacePhysicalSwitch.md) | List of new physical switches settings. If this property is omitted, physical switches configuration will not be modified. | [optional] 
**force** | **bool** | Indicates whether to suppress network validation errors. The option is intended to suppress false errors caused by network environment constraints.  Normally the command will fail with an error when: - some of system network ports are in degraded state or have cabling issues, - system top-of-rack switches have configuration issues leading to network unreachability, - network IP addresses have duplicates in the network environment, - or network gateway is unreachable.  When force is true, the command will proceed instead.  Caution: Only use this option when you are certain your requested settings are correct and you understand why they are failing at this time, and you want to apply the settings anyway. Improper network settings can make the system unreachable for data and management.  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


