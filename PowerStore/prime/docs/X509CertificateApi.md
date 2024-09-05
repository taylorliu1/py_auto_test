# prime.swagger_client.X509CertificateApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**x509_certificate_csr_post**](X509CertificateApi.md#x509_certificate_csr_post) | **POST** /x509_certificate/csr | Generate CSR
[**x509_certificate_exchange_post**](X509CertificateApi.md#x509_certificate_exchange_post) | **POST** /x509_certificate/exchange | Exchange Certificates
[**x509_certificate_get**](X509CertificateApi.md#x509_certificate_get) | **GET** /x509_certificate | Collection Query
[**x509_certificate_id_get**](X509CertificateApi.md#x509_certificate_id_get) | **GET** /x509_certificate/{id} | Instance Query
[**x509_certificate_id_patch**](X509CertificateApi.md#x509_certificate_id_patch) | **PATCH** /x509_certificate/{id} | Modify
[**x509_certificate_post**](X509CertificateApi.md#x509_certificate_post) | **POST** /x509_certificate | Create
[**x509_certificate_reset_certificates_post**](X509CertificateApi.md#x509_certificate_reset_certificates_post) | **POST** /x509_certificate/reset_certificates | Reset certificates by service


# **x509_certificate_csr_post**
> X509CertificateCsrResponse x509_certificate_csr_post(body)

Generate CSR

Generate a new certificate signing request. A new X509 Certificate instance will be created to hold the private key and passphrase, whose is_current and is_valid attributes will both be false. Only Management_HTTP, Syslog_HTTP and VASA_HTTP are supported service types. For Management_HTTP serivce, scope must to be provided with value External; any other value will be rejected. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.X509CertificateApi()
body = prime.swagger_client.X509CertificateCsr() # X509CertificateCsr | Request body.

try:
    # Generate CSR
    api_response = api_instance.x509_certificate_csr_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling X509CertificateApi->x509_certificate_csr_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**X509CertificateCsr**](X509CertificateCsr.md)| Request body. | 

### Return type

[**X509CertificateCsrResponse**](X509CertificateCsrResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **x509_certificate_exchange_post**
> x509_certificate_exchange_post(body)

Exchange Certificates

Exchange certificates between two clusters. Add CA certificates to the trust store of each cluster and assign roles to the client certificates. After this process, certificate-based authentication can be used for communication between clusters. This exchange REST API can only be triggered with service Replication_HTTP.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.X509CertificateApi()
body = prime.swagger_client.X509CertificateExchange() # X509CertificateExchange | Request body.

try:
    # Exchange Certificates
    api_instance.x509_certificate_exchange_post(body)
except ApiException as e:
    print("Exception when calling X509CertificateApi->x509_certificate_exchange_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**X509CertificateExchange**](X509CertificateExchange.md)| Request body. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **x509_certificate_get**
> list[X509CertificateInstance] x509_certificate_get()

Collection Query

Query to list X509 Certificates instances.  This resource type collection query does not support filtering, sorting or pagination.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.X509CertificateApi()

try:
    # Collection Query
    api_response = api_instance.x509_certificate_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling X509CertificateApi->x509_certificate_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[X509CertificateInstance]**](X509CertificateInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **x509_certificate_id_get**
> X509CertificateInstance x509_certificate_id_get(id)

Instance Query

Query a specific X509 Certificate instance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.X509CertificateApi()
id = 'id_example' # str | Unique identifier of the X509 Certificate.

try:
    # Instance Query
    api_response = api_instance.x509_certificate_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling X509CertificateApi->x509_certificate_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the X509 Certificate. | 

### Return type

[**X509CertificateInstance**](X509CertificateInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **x509_certificate_id_patch**
> x509_certificate_id_patch(id, body)

Modify

Update/modify a X509 Certificate instance by unique identifier. This request may only be used when certificate usage type is server or client certificate. Please note that for Management_HTTP service, is_current must be set to true to avoid losing the management connection to the server. Setting the is_current flag to true on the new certificate will delete any existing current certificate. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.X509CertificateApi()
id = 'id_example' # str | Unique identifier of the X509 Certificate.
body = prime.swagger_client.X509CertificateModify() # X509CertificateModify | Request body.

try:
    # Modify
    api_instance.x509_certificate_id_patch(id, body)
except ApiException as e:
    print("Exception when calling X509CertificateApi->x509_certificate_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the X509 Certificate. | 
 **body** | [**X509CertificateModify**](X509CertificateModify.md)| Request body. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **x509_certificate_post**
> CreateResponse x509_certificate_post(body)

Create

Add/import a new X509 Certificate. When certificate usage type in the request is server or client, private key and passphrase are required. Private key presented in the request should be encrypted in PKCS8 format. For the current release following services are supported - Import_HTTP, LDAP_HTTP, Syslog_HTTP for which the certificate can be imported. CA certificates of type CA_Client_Validation and CA_Server_Validation are supported for all service types. If the imported client/server certificate with is_current flag is set to true and corresponding CA Client Validation or CA Server Validation certificate's is_current flag is not set or updated to true , will cause a loss in connection to the client/server. There can be multiple CA certs for a given service with is_current flag set to true. But for client/server certificates, setting the is_current flag to true on the new certificate will delete the existing current certificate. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.X509CertificateApi()
body = prime.swagger_client.X509CertificateCreate() # X509CertificateCreate | Request body.

try:
    # Create
    api_response = api_instance.x509_certificate_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling X509CertificateApi->x509_certificate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**X509CertificateCreate**](X509CertificateCreate.md)| Request body. | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **x509_certificate_reset_certificates_post**
> x509_certificate_reset_certificates_post(body)

Reset certificates by service

Reset x509 certificates for one service to the initial state for the system. This is used to recover system from an invalid certificates or private key for services like VASA provider (VASA_HTTP) when VASA Provider certificates are invalid. This can restore the VASA Provider certificate to a new self-signed certificate, so that VASA Provider can be re-registered with vCenter. This is valid only for the VASA_HTTP service and requires either the Administrator, Security Administrator, or VASA administrator role. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.X509CertificateApi()
body = prime.swagger_client.X509CertificateResetCertificates() # X509CertificateResetCertificates | Request body.

try:
    # Reset certificates by service
    api_instance.x509_certificate_reset_certificates_post(body)
except ApiException as e:
    print("Exception when calling X509CertificateApi->x509_certificate_reset_certificates_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**X509CertificateResetCertificates**](X509CertificateResetCertificates.md)| Request body. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

