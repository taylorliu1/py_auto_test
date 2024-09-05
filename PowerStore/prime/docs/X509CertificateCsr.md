# X509CertificateCsr

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**X509CertificateUsageTypeEnum**](X509CertificateUsageTypeEnum.md) |  | 
**service** | [**X509CertificateServiceEnum**](X509CertificateServiceEnum.md) |  | 
**scope** | **str** | Scope defines a subset of certificates belonging to one Service. Scope here defines what Certificate Signing Request (CSR) can be generated. The scope for CSR Generation only includes: - Certificate with Service Management_HTTP and Type of Server, Scope value can only be External - Certificate with Service VASA_HTTP and Type of Server, Scope value can be null(unused and optional) - Certificate with Service KMIP_HTTP and Type of Client, Scope value can be null(unused and optional) - Certificate with Service Syslog_HTTP and Type of Client, Scope value can be null(unused and optional)  | [optional] 
**common_name** | **str** | Part of distinguished name. e.g., www.dell.common. | [optional] 
**dns_name** | **list[str]** | DNS names in the certificate extensions | [optional] 
**ip_addresses** | **list[str]** | IP addresses in the certificate extensions | [optional] 
**organizational_unit** | **str** | Part of distinguished name. e.g., Security Department. | [optional] 
**organization** | **str** | Part of distinguished name. e.g., Dell-EMC. | [optional] 
**locality** | **str** | Part of distinguished name. e.g., Hopkinton. | [optional] 
**state** | **str** | Part of distinguished name. e.g., Massachusetts. | [optional] 
**country** | **str** | Part of distinguished name. e.g., US. | [optional] 
**key_length** | **int** | Private key length. It can only be 2048 or 4096. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


