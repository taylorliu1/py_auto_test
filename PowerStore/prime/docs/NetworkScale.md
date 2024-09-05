# NetworkScale

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_port_ids** | **list[str]** | Unique identifiers of available IP ports to be used in the network.  | [optional] 
**remove_port_ids** | **list[str]** | Unique identifiers of IP ports to remove from use in the network.  | [optional] 
**force** | **bool** | * Indicates whether to suppress network validation errors. * The option is intended to suppress false errors caused by network environment constraints.  Normally the command will fail with an error when: * system network ports on top of which IP ports are configured are in degraded state or have cabling issues, * or network IP addresses applied as a result of network scaling have duplicates in the network environment.  When force is true, the command will proceed instead.  Caution: Only use this option when you are certain, that your requested settings are correct and you understand why they are failing at this time, and you want to apply the settings anyway. Improper network settings can make the system unreachable for data.  | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


