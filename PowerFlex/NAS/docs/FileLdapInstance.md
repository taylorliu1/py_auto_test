# FileLdapInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the LDAP service object. | [optional] 
**nas_server_id** | **str** | Unique identifier of the associated NAS Server instance that uses this LDAP object.  Only one LDAP object per NAS Server is supported.  | [optional] 
**base_dn** | **str** | Name of the LDAP base DN.  Base Distinguished Name (BDN) of the root of the LDAP directory tree. The appliance uses the DN to bind to the LDAP service and locate in the LDAP directory tree to begin a search for information.   The base DN can be expressed as a fully-qualified domain name or in X.509 format by using the attribute dc&#x3D;. For example, if the fully-qualified domain name is mycompany.com, the base DN is expressed as dc&#x3D;mycompany,dc&#x3D;com. | [optional] 
**profile_dn** | **str** | For an iPlanet LDAP server, specifies the DN of the entry with the configuration profile. | [optional] 
**addresses** | **list[str]** | The list of LDAP server IP addresses. The addresses may be IPv4 or IPv6. | [optional] 
**port_number** | **int** | The TCP/IP port used by the NAS Server to connect to the LDAP servers. The default port number for LDAP is 389 and LDAPS is 636. | [optional] 
**authentication_type** | [**FileLDAPAuthenticationTypeEnum**](FileLDAPAuthenticationTypeEnum.md) |  | [optional] 
**protocol** | [**FileLDAPProtocolEnum**](FileLDAPProtocolEnum.md) |  | [optional] 
**is_verify_server_certificate** | **bool** | Indicates whether a Certification Authority certificate is used to verify the LDAP server certificate for secure SSL connections. Values are:  * true - verifies LDAP server&#x27;s certificate.  * false - doesn&#x27;t verify LDAP server&#x27;s certificate.  | [optional] 
**bind_dn** | **str** | Bind Distinguished Name (DN) to be used when binding. | [optional] 
**is_smb_account_used** | **bool** | Indicates whether SMB authentication is used to authenticate to the LDAP server. Values are:      * true - Indicates that the SMB settings are used for Kerberos authentication.     * false - Indicates that Kerberos uses its own settings.  | [optional] 
**principal** | **str** | Specifies the principal name for Kerberos authentication. | [optional] 
**realm** | **str** | Specifies the realm name for Kerberos authentication. | [optional] 
**schema_type** | [**FileLDAPSchemaTypeEnum**](FileLDAPSchemaTypeEnum.md) |  | [optional] 
**is_config_file_uploaded** | **bool** | Indicates whether an LDAP configuration file has been uploaded. | [optional] [default to False]
**is_certificate_uploaded** | **bool** | Indicates whether an LDAP certificate file has been uploaded. | [optional] [default to False]
**authentication_type_l10n** | **str** | Localized message string corresponding to authentication_type | [optional] 
**protocol_l10n** | **str** | Localized message string corresponding to protocol | [optional] 
**schema_type_l10n** | **str** | Localized message string corresponding to schema_type | [optional] 
**nas_server** | [**NasServersInstance**](NasServersInstance.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

