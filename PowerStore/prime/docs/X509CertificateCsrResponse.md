# X509CertificateCsrResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of x509_certificate. | [optional] 
**type** | [**X509CertificateUsageTypeEnum**](X509CertificateUsageTypeEnum.md) |  | [optional] 
**service** | [**X509CertificateServiceEnum**](X509CertificateServiceEnum.md) |  | [optional] 
**scope** | **str** | Scope defines a subset of certificates belonging to one service. Scope here defines what Certificate Signing Request (CSR) can be generated. The scope for CSR Response only includes: - Certificate with Service Management_HTTP and Type of Server, Scope value can only be External - Certificate with Service VASA_HTTP and Type of Server, Scope value can be null(unused and optional) - Certificate with Service KMIP_HTTP and Type of Client, Scope value can be null(unused and optional) - Certificate with Service Syslog_HTTP and Type of Client, Scope value can be null(unused and optional)  | [optional] 
**is_current** | **bool** | Indicates whether this is the current X509 certificate to be used by the service or this X509 certificate will be used in the future. When is_current is false for a X509 Certificate, this X509 Certificate will not be picked up by the service. Potential usage of this attribute is to prepare for the certificate roll-over/rotation. | [optional] 
**is_valid** | **bool** | Indicate whether this is a valid X509 Certificate. When X509 certificate is expired or X509 Certificate of server type missing either a private key or a valid certificate entry, it will be false. | [optional] 
**members** | [**list[MemberCertificateInstance]**](MemberCertificateInstance.md) | Member certificates included in this x509_certificate. It will be empty in csr creation response. | [optional] 
**certificate_request** | **str** | PEM encoded certificate signing request. | [optional] 
**type_l10n** | **str** | Localized message string corresponding to type Was added in version 2.0.0.0. | [optional] 
**service_l10n** | **str** | Localized message string corresponding to service Was added in version 2.0.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


