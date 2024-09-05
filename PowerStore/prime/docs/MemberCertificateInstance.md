# MemberCertificateInstance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | Certificate subject or so called distinguished name. | [optional] 
**serial_number** | **str** | Certificate serial number. | [optional] 
**signature_algorithm** | **str** | Certificate signature algorithm. | [optional] 
**issuer** | **str** | Distinguished name of the certificate issuer. | [optional] 
**valid_from** | **datetime** | Date and time when the certificate becomes valid. | [optional] 
**valid_to** | **datetime** | Date and time when the certificate will expire. | [optional] 
**subject_alternative_names** | **list[str]** | Additional DNS names or IP addresses in the x509_certificate. | [optional] 
**public_key_algorithm** | **str** | Public key algorithm used to generate the key pair. | [optional] 
**key_length** | **int** | Private key length. | [optional] 
**thumbprint_algorithm** | [**ThumbprintAlgorithmEnum**](ThumbprintAlgorithmEnum.md) |  | [optional] 
**thumbprint** | **str** | Hash value of the certificate. | [optional] 
**certificate** | **str** | Base64 encoded certificate without any line breaks. | [optional] 
**depth** | **int** | Depth indicates the position of this member certificate in the X509 Certificate chain. End-entity certificate will always have a depth of 1, which is the minimum value for depth. The depth of direct issuer certificate will be incremented by 1 until reaching the root certificate. Root certificate should have the largest depth for the certificate chain. | [optional] 
**thumbprint_algorithm_l10n** | **str** | Localized message string corresponding to thumbprint_algorithm | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


