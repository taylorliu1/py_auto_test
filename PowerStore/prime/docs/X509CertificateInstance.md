# X509CertificateInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of X509 Certificate instance. | [optional] 
**type** | [**X509CertificateUsageTypeEnum**](X509CertificateUsageTypeEnum.md) |  | [optional] 
**service** | [**X509CertificateServiceEnum**](X509CertificateServiceEnum.md) |  | [optional] 
**scope** | **str** | Scope defines a subset of certificates belonging to one Service. Scope has different meanings from different Services and types. For example, in Replication_HTTP, CA type certificates will use scope to indicate the origin of these certificates. Service, type and scope mapping are listed as below. - Certificate with Service Management_HTTP and Type of Server, Scope value can be External. - Certificate with Service Replication_HTTP and Type of Client, Scope value can be null(unused and optional). - Certificate with Service Replication_HTTP and Type of CA, Scope value has to be the serial number of remote cluster. - Certificate with Service VASA_HTTP and Type of Server, Scope value can be null(unused and optional). - Certificate with Service VASA_HTTP and Type of CA, Scope value can be null(unused and optional). - Certificate with Service Import_HTTP and Type of CA, Scope value can be null(unused and optional). - Certificate with Service LDAP_HTTP and Type of CA, Scope value is LDAP Domain Name. - Certificate with Service KMIP_HTTP and Type of Client, Scope value can be null(unused and optional). - Certificate with Service Syslog_HTTP and Type of Client, Scope value can be null(unused and optional).  Was added in version 3.0.0.0. | [optional] 
**is_current** | **bool** | Indicates whether this is the current X509 Certificate to be used by the service or this X509 Certificate will be used in the future. When is_current is false for a X509 Certificate, this X509 Certificate will not be picked up by the service. Potential usage of this attribute is to prepare for the certificate roll-over/rotation. | [optional] 
**is_valid** | **bool** | Indicates whether this is a valid X509 certificate. When X509 certificate is expired or X509 Certificate of server type missing either a private key or a valid certificate entry, it will be false. | [optional] 
**members** | [**list[MemberCertificateInstance]**](MemberCertificateInstance.md) | Member certificates included in this x509_certificate. Member certificates should be remained in an ordered sequence.  Filtering on the fields of this embedded resource is not supported. | [optional] 
**type_l10n** | **str** | Localized message string corresponding to type | [optional] 
**service_l10n** | **str** | Localized message string corresponding to service | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


