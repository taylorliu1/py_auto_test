# ClusterCreateVcenters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | IP address of vCenter in IPv4 or IPv6 or hostname format. | 
**username** | **str** | User name to login to vCenter. | 
**password** | **str** | Password to login to vCenter. | 
**is_verify_server_cert** | **bool** | Whether or not the connection will be secured with the vCenter SSL certificate. | 
**data_center_id** | **str** | VMWare ID of the datacenter. This should be specified when creating PowerStoreX cluster to join an existing datacenter. data_center_name may not also be specified with this. Was added in version 3.0.0.0. | [optional] 
**data_center_name** | **str** | Name of the data center. This should be specified when creating PowerStoreX cluster in order to create and join a new datacenter in vCenter. data_center_id may not also be specified with this. When data_center_create is false, then an existing datacenter will be used if the name matches, otherwise a new one will be created. | [optional] 
**data_center_create** | **bool** | Along with data_center_name, indicates an intent to either create or use existing data center by name. Was added in version 3.0.0.0. Was deprecated in version 3.0.0.0. | [optional] [default to False]
**esx_cluster_name** | **str** | ESXi cluster name. The default name is \&quot;Cluster-\&quot; followed by the PowerStore cluster name. This should be specified when creating PowerStore X cluster. | [optional] [default to 'name']
**vasa_provider_credentials** | [**ClusterCreateVasaProviderCredentials**](ClusterCreateVasaProviderCredentials.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


