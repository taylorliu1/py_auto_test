# prime.swagger_client.LdapAccountApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ldap_account_get**](LdapAccountApi.md#ldap_account_get) | **GET** /ldap_account | Collection Query
[**ldap_account_id_delete**](LdapAccountApi.md#ldap_account_id_delete) | **DELETE** /ldap_account/{id} | Delete
[**ldap_account_id_get**](LdapAccountApi.md#ldap_account_id_get) | **GET** /ldap_account/{id} | Instance Query
[**ldap_account_id_patch**](LdapAccountApi.md#ldap_account_id_patch) | **PATCH** /ldap_account/{id} | Modify
[**ldap_account_post**](LdapAccountApi.md#ldap_account_post) | **POST** /ldap_account | Create


# **ldap_account_get**
> list[LdapAccountInstance] ldap_account_get()

Collection Query

Query LDAP account instances. Was added in version 1.0.3.  This resource type collection query does not support filtering, sorting or pagination.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.LdapAccountApi()

try:
    # Collection Query
    api_response = api_instance.ldap_account_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LdapAccountApi->ldap_account_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LdapAccountInstance]**](LdapAccountInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_account_id_delete**
> ldap_account_id_delete(id)

Delete

Delete an LDAP account. Was added in version 1.0.3.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.LdapAccountApi()
id = 'id_example' # str | Unique identifier of the LDAP account to be deleted.

try:
    # Delete
    api_instance.ldap_account_id_delete(id)
except ApiException as e:
    print("Exception when calling LdapAccountApi->ldap_account_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the LDAP account to be deleted. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_account_id_get**
> LdapAccountInstance ldap_account_id_get(id)

Instance Query

Query a specific LDAP account instance. Was added in version 1.0.3.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.LdapAccountApi()
id = 'id_example' # str | Unique identifier of the LDAP account.

try:
    # Instance Query
    api_response = api_instance.ldap_account_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LdapAccountApi->ldap_account_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the LDAP account. | 

### Return type

[**LdapAccountInstance**](LdapAccountInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_account_id_patch**
> ldap_account_id_patch(id, body)

Modify

Modify the properties of an LDAP account. Was added in version 1.0.3.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.LdapAccountApi()
id = 'id_example' # str | Unique identifier of the LDAP account to be modified.
body = prime.swagger_client.LdapAccountModify() # LdapAccountModify | 

try:
    # Modify
    api_instance.ldap_account_id_patch(id, body)
except ApiException as e:
    print("Exception when calling LdapAccountApi->ldap_account_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the LDAP account to be modified. | 
 **body** | [**LdapAccountModify**](LdapAccountModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_account_post**
> CreateResponse ldap_account_post(body)

Create

Create a new LDAP account. Was added in version 1.0.3.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.LdapAccountApi()
body = prime.swagger_client.LdapAccountCreate() # LdapAccountCreate | 

try:
    # Create
    api_response = api_instance.ldap_account_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LdapAccountApi->ldap_account_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LdapAccountCreate**](LdapAccountCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

