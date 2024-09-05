# prime.swagger_client.SnmpServerApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**snmp_server_get**](SnmpServerApi.md#snmp_server_get) | **GET** /snmp_server | Collection Query
[**snmp_server_id_delete**](SnmpServerApi.md#snmp_server_id_delete) | **DELETE** /snmp_server/{id} | Delete
[**snmp_server_id_get**](SnmpServerApi.md#snmp_server_id_get) | **GET** /snmp_server/{id} | Instance Query
[**snmp_server_id_patch**](SnmpServerApi.md#snmp_server_id_patch) | **PATCH** /snmp_server/{id} | Modify
[**snmp_server_id_test_post**](SnmpServerApi.md#snmp_server_id_test_post) | **POST** /snmp_server/{id}/test | Test
[**snmp_server_post**](SnmpServerApi.md#snmp_server_post) | **POST** /snmp_server | Create


# **snmp_server_get**
> list[SnmpServerInstance] snmp_server_get()

Collection Query

Query SNMP servers. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SnmpServerApi()

try:
    # Collection Query
    api_response = api_instance.snmp_server_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnmpServerApi->snmp_server_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SnmpServerInstance]**](SnmpServerInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snmp_server_id_delete**
> snmp_server_id_delete(id)

Delete

Delete an SNMP Server. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SnmpServerApi()
id = 'id_example' # str | Unique identifier of the SNMP server.

try:
    # Delete
    api_instance.snmp_server_id_delete(id)
except ApiException as e:
    print("Exception when calling SnmpServerApi->snmp_server_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the SNMP server. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snmp_server_id_get**
> SnmpServerInstance snmp_server_id_get(id)

Instance Query

Query a specific SNMP server. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SnmpServerApi()
id = 'id_example' # str | Unique identifier of the SNMP server.

try:
    # Instance Query
    api_response = api_instance.snmp_server_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnmpServerApi->snmp_server_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the SNMP server. | 

### Return type

[**SnmpServerInstance**](SnmpServerInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snmp_server_id_patch**
> snmp_server_id_patch(id, body)

Modify

Modify an SNMP server. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SnmpServerApi()
id = 'id_example' # str | Unique identifier of the SNMP server.
body = prime.swagger_client.SnmpServerModify() # SnmpServerModify | New values of the properties of the SNMP server.

try:
    # Modify
    api_instance.snmp_server_id_patch(id, body)
except ApiException as e:
    print("Exception when calling SnmpServerApi->snmp_server_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the SNMP server. | 
 **body** | [**SnmpServerModify**](SnmpServerModify.md)| New values of the properties of the SNMP server. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snmp_server_id_test_post**
> snmp_server_id_test_post(id)

Test

Send a test notification to a specified SNMP server to verify connectivity. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SnmpServerApi()
id = 'id_example' # str | Unique identifier of the SNMP server.

try:
    # Test
    api_instance.snmp_server_id_test_post(id)
except ApiException as e:
    print("Exception when calling SnmpServerApi->snmp_server_id_test_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the SNMP server. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snmp_server_post**
> CreateResponse snmp_server_post(body)

Create

Create an SNMP server. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SnmpServerApi()
body = prime.swagger_client.SnmpServerCreate() # SnmpServerCreate | Parameters to create an SNMP server.

try:
    # Create
    api_response = api_instance.snmp_server_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnmpServerApi->snmp_server_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SnmpServerCreate**](SnmpServerCreate.md)| Parameters to create an SNMP server. | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

