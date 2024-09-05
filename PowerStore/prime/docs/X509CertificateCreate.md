# X509CertificateCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**X509CertificateUsageTypeEnum**](X509CertificateUsageTypeEnum.md) |  | 
**service** | [**X509CertificateServiceEnum**](X509CertificateServiceEnum.md) |  | 
**scope** | **str** | Scope defines a subset of certificates belonging to one Service. Scope has different meanings from different Services and types. For example, in Replication_HTTP, CA type certificates will use scope to indicate the origin of these certificates. Service, type and scope mapping are listed as below. - Certificate with Service Management_HTTP and Type of Server, Scope value can be can only be &#39;External&#39;. - Certificate with Service Replication_HTTP and Type of Client, Scope value can be null(unused and optional). - Certificate with Service Replication_HTTP and Type of CA, Scope value has to be the serial number of remote cluster. - Certificate with Service VASA_HTTP and Type of Server, Scope value can be null(unused and optional). - Certificate with Service VASA_HTTP and Type of CA, Scope value can be null(unused and optional). - Certificate with Service Import_HTTP and Type of CA, Scope value can be null(unused and optional). - Certificate with Service LDAP_HTTP and Type of CA, Scope value is LDAP Domain Name. - Certificate with Service KMIP_HTTP and Type of Client, Scope value can be null(unused and optional). - Certificate with Service Syslog_HTTP and Type of Client, Scope value can be null(unused and optional)  | [optional] 
**certificate** | **str** | Concatenated PEM encoded (including header, footer and line break) X509 certificate string from end-entity certificate to root certificate. End-entity certificate has to be put at the top and the sequence should be maintained as the certificate chain from end-entity certificate to the root certificate. | 
**private_key** | **str** | PEM encoded (including header, footer and line break) private key following encrypted PKCS8. | [optional] 
**passphrase** | **str** | Passphrase used to encrypt private key. | [optional] 
**is_current** | **bool** | Indicates whether this is the current X509 certificate to be used by the service or this X509 certificate will be used in the future. When is_current is false for a X509 certificate, this X509 certificate will not be picked up by the service. Potential usage of this attribute is to prepare for the certificate roll-over/rotation. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


