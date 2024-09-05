# NfsServerCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nas_server_id** | **str** | Unique identifier of the NAS server. name:{name} can be used instead of {id}. For example:&#39;nas_server_id&#39;:&#39;name:nas_server_name&#39; | 
**host_name** | **str** | The name that will be used by NFS clients to connect to this NFS server. This name is required when using secure NFS, except when is_use_smb_config_enabled is true. In this case host_name is forced to the SMB server computer name, and must not be specified.  | [optional] 
**is_nfsv3_enabled** | **bool** | Indicates whether NFSv3 is enabled on the NAS server. When enabled, NFS shares can be accessed with NFSv3. When disabled, NFS shares can not be accessed with NFSv3 protocol. - true - NFSv3 is enabled on the specified NAS server. - false - NFSv3 is disabled on the specified NAS server.  | [optional] [default to True]
**is_nfsv4_enabled** | **bool** | Indicates whether NFSv4 is enabled on the NAS server. When enabled, NFS shares can be accessed with NFSv4. When disabled, NFS shares can not be accessed with NFSv4 protocol. - true - NFSv4 is enabled on the specified NAS server. - false - NFSv4 is disabled on the specified NAS server.  | [optional] [default to False]
**is_secure_enabled** | **bool** | Indicates whether secure NFS is enabled on the NFS server. - true - Secure NFS is enabled. - false - Secure NFS is disabled.  | [optional] [default to False]
**is_use_smb_config_enabled** | **bool** | Indicates whether SMB authentication is used to authenticate to the KDC. Values are: - true: Indicates that the configured SMB Server settings are used for Kerberos authentication. - false: Indicates that Kerberos uses its own settings.  | [optional] [default to False]
**is_extended_credentials_enabled** | **bool** | Indicates whether the NFS server supports more than 16 Unix groups in a Unix credential. Valid values are: - true - NFS server supports more than 16 Unix groups in a Unix credential. The NFS server will send additional request to Unix Directory service to identify Unix groups. - false - NFS server supports more than 16 Unix groups in a Unix credential. The NFS server will send additional request to Unix Directory service to identify Unix groups. Note - The NFS server builds its own Unix credential when it supports more than 16 groups. This process can slow the performance.  | [optional] [default to False]
**credentials_cache_ttl** | **int** | Sets the Time-To-Live (in minutes) expiration time in minutes for a Windows entry in the credentials cache. When failed mapping entries expire, the system retries mapping the UID to the SID. | [optional] [default to 15]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


