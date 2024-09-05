# X509CertificateResetCertificates

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | [**X509CertificateServiceEnum**](X509CertificateServiceEnum.md) |  | 
**scope** | **str** | Scope defines a subset of certificates belonging to one Service. Scope has different meanings from different Services and types. For example, in Replication_HTTP, CA type certificates will use scope to indicate the origin of these certificates. Service, type and scope mapping are listed as here -- Certificate with Service Management_HTTP and Type of Server, Scope value can be null(unused and optional); Certificate with Service Replication_HTTP and Type of Client, Scope value can be null(unused and optional); Certificate with Service Replication_HTTP and Type of CA, Scope value has to be the serial number of remote cluster; Certificate with Service VASA_HTTP and Type of Server, Scope value can be null(unused and optional); Certificate with Service VASA_HTTP and Type of CA, Scope value can be null(unused and optional); Certificate with Service Import_HTTP and Type of CA, Scope value can be null(unused and optional); Certificate with Service LDAP_HTTP and Type of CA, Scope value is LDAP Domain Name; Certificate with Service KMIP_HTTP and Type of Server, Scope value can be null(unused and optional); Was added in version 3.0.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


