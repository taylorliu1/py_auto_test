# FileLdapInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the LDAP service object. | [optional] 
**nas_server_id** | **str** | Unique identifier of the associated NAS Server instance that uses this LDAP object. Only one LDAP object per NAS Server is supported.  | [optional] 
**base_dn** | **str** | Name of the LDAP base DN.  Base Distinguished Name (BDN) of the root of the LDAP directory tree. The appliance uses the DN to bind to the LDAP service and locate in the LDAP directory tree to begin a search for information.   The base DN can be expressed as a fully-qualified domain name or in X.509 format by using the attribute dc&#x3D;. For example, if the fully-qualified domain name is mycompany.com, the base DN is expressed as dc&#x3D;mycompany,dc&#x3D;com. | [optional] 
**profile_dn** | **str** | For an iPlanet LDAP server, specifies the DN of the entry with the configuration profile. | [optional] 
**addresses** | **list[str]** | The list of LDAP server IP addresses. The addresses may be IPv4 or IPv6. | [optional] 
**port_number** | **int** | The TCP/IP port used by the NAS Server to connect to the LDAP servers. The default port number for LDAP is 389 and LDAPS is 636. | [optional] 
**authentication_type** | [**FileLDAPAuthenticationTypeEnum**](FileLDAPAuthenticationTypeEnum.md) |  | [optional] 
**protocol** | [**FileLDAPProtocolEnum**](FileLDAPProtocolEnum.md) |  | [optional] 
**is_verify_server_certificate** | **bool** | Indicates whether a Certification Authority certificate is used to verify the LDAP server certificate for secure SSL connections. Values are:  * true - verifies LDAP server&#39;s certificate.  * false - doesn&#39;t verify LDAP server&#39;s certificate.  | [optional] 
**bind_dn** | **str** | Bind Distinguished Name (DN) to be used when binding. | [optional] 
**is_smb_account_used** | **bool** | Indicates whether SMB authentication is used to authenticate to the LDAP server. Values are:     * true - Indicates that the SMB settings are used for Kerberos authentication.     * false - Indicates that Kerberos uses its own settings.  | [optional] 
**principal** | **str** | Specifies the principal name for Kerberos authentication. | [optional] 
**realm** | **str** | Specifies the realm name for Kerberos authentication. | [optional] 
**schema_type** | [**FileLDAPSchemaTypeEnum**](FileLDAPSchemaTypeEnum.md) |  | [optional] 
**is_config_file_uploaded** | **bool** | Indicates whether an LDAP configuration file has been uploaded. | [optional] [default to False]
**is_certificate_uploaded** | **bool** | Indicates whether an LDAP certificate file has been uploaded. | [optional] [default to False]
**is_destination_override_enabled** | **bool** | In order to modify any properties of this resource when the associated NAS server is a replication destination, the is_destination_override_enabled flag must be set to true. When true these properties may be modified: addresses Values are:   true - Enable locally set properties. Source property changes will propagate to the source_parameters of the resource.   false - Reset the properties to the ones from the source. Source property changes will propagate directly to this resource.  Was added in version 3.0.0.0. | [optional] [default to False]
**source_parameters** | **object** | Information about the corresponding source NAS Server&#39;s File LDAP settings. Only populated when is_destination_override_enabled flag is set to true. Was added in version 3.0.0.0.  Filtering on the fields of this embedded resource is not supported. | [optional] 
**authentication_type_l10n** | **str** | Localized message string corresponding to authentication_type | [optional] 
**protocol_l10n** | **str** | Localized message string corresponding to protocol | [optional] 
**schema_type_l10n** | **str** | Localized message string corresponding to schema_type | [optional] 
**nas_server** | [**NasServerInstance**](NasServerInstance.md) | This is the embeddable reference form of nas_server_id attribute. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


