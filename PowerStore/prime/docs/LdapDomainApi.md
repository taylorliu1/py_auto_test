# prime.swagger_client.LdapDomainApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ldap_domain_get**](LdapDomainApi.md#ldap_domain_get) | **GET** /ldap_domain | Collection Query
[**ldap_domain_id_delete**](LdapDomainApi.md#ldap_domain_id_delete) | **DELETE** /ldap_domain/{id} | Delete
[**ldap_domain_id_get**](LdapDomainApi.md#ldap_domain_id_get) | **GET** /ldap_domain/{id} | Instance Query
[**ldap_domain_id_patch**](LdapDomainApi.md#ldap_domain_id_patch) | **PATCH** /ldap_domain/{id} | Modify
[**ldap_domain_id_verify_post**](LdapDomainApi.md#ldap_domain_id_verify_post) | **POST** /ldap_domain/{id}/verify | Verify
[**ldap_domain_post**](LdapDomainApi.md#ldap_domain_post) | **POST** /ldap_domain | Create


# **ldap_domain_get**
> list[LdapDomainInstance] ldap_domain_get()

Collection Query

Query list of LDAP domain. Was added in version 1.0.3.  This resource type collection query does not support filtering, sorting or pagination.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.LdapDomainApi()

try:
    # Collection Query
    api_response = api_instance.ldap_domain_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LdapDomainApi->ldap_domain_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LdapDomainInstance]**](LdapDomainInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_domain_id_delete**
> ldap_domain_id_delete(id)

Delete

Delete an LDAP domain. Was added in version 1.0.3.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.LdapDomainApi()
id = 'id_example' # str | Unique identifier of the LDAP domain to be deleted.

try:
    # Delete
    api_instance.ldap_domain_id_delete(id)
except ApiException as e:
    print("Exception when calling LdapDomainApi->ldap_domain_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the LDAP domain to be deleted. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_domain_id_get**
> LdapDomainInstance ldap_domain_id_get(id)

Instance Query

Query a specific LDAP domain. Was added in version 1.0.3.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.LdapDomainApi()
id = 'id_example' # str | Unique identifier of the LDAP domain.

try:
    # Instance Query
    api_response = api_instance.ldap_domain_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LdapDomainApi->ldap_domain_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the LDAP domain. | 

### Return type

[**LdapDomainInstance**](LdapDomainInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_domain_id_patch**
> ldap_domain_id_patch(id, body)

Modify

Modify the properties of an LDAP domain. Was added in version 1.0.3.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.LdapDomainApi()
id = 'id_example' # str | Unique identifier of the LDAP domain to be modified.
body = prime.swagger_client.LdapDomainModify() # LdapDomainModify | 

try:
    # Modify
    api_instance.ldap_domain_id_patch(id, body)
except ApiException as e:
    print("Exception when calling LdapDomainApi->ldap_domain_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the LDAP domain to be modified. | 
 **body** | [**LdapDomainModify**](LdapDomainModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_domain_id_verify_post**
> ldap_domain_id_verify_post(id)

Verify

verifying the connectivity to the LDAP domain server. Was added in version 1.0.3.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.LdapDomainApi()
id = 'id_example' # str | Unique identifier of the instance.

try:
    # Verify
    api_instance.ldap_domain_id_verify_post(id)
except ApiException as e:
    print("Exception when calling LdapDomainApi->ldap_domain_id_verify_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the instance. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_domain_post**
> CreateResponse ldap_domain_post(body)

Create

Create a new LDAP domain. Was added in version 1.0.3.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.LdapDomainApi()
body = prime.swagger_client.LdapDomainCreate() # LdapDomainCreate | 

try:
    # Create
    api_response = api_instance.ldap_domain_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LdapDomainApi->ldap_domain_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LdapDomainCreate**](LdapDomainCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

