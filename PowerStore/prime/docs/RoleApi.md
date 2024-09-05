# prime.swagger_client.RoleApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**role_get**](RoleApi.md#role_get) | **GET** /role | Collection Query
[**role_id_get**](RoleApi.md#role_id_get) | **GET** /role/{id} | Instance Query


# **role_get**
> list[RoleInstance] role_get()

Collection Query

Query roles.  This resource type collection query does not support filtering, sorting or pagination.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.RoleApi()

try:
    # Collection Query
    api_response = api_instance.role_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->role_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RoleInstance]**](RoleInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_id_get**
> RoleInstance role_id_get(id)

Instance Query

Query a specific role.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.RoleApi()
id = 'id_example' # str | Unique identifier of the role.

try:
    # Instance Query
    api_response = api_instance.role_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->role_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the role. | 

### Return type

[**RoleInstance**](RoleInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

