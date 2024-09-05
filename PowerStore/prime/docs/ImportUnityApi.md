# prime.swagger_client.ImportUnityApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_unity_get**](ImportUnityApi.md#import_unity_get) | **GET** /import_unity | Collection Query
[**import_unity_id_discover_post**](ImportUnityApi.md#import_unity_id_discover_post) | **POST** /import_unity/{id}/discover | Discover the importable volumes and consistency groups
[**import_unity_id_get**](ImportUnityApi.md#import_unity_id_get) | **GET** /import_unity/{id} | Instance Query


# **import_unity_get**
> list[ImportUnityInstance] import_unity_get()

Collection Query

Query Unity storage systems.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportUnityApi()

try:
    # Collection Query
    api_response = api_instance.import_unity_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportUnityApi->import_unity_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ImportUnityInstance]**](ImportUnityInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_unity_id_discover_post**
> import_unity_id_discover_post(id)

Discover the importable volumes and consistency groups

Discover the importable volumes and consistency groups in the Unity storage system. Was deprecated in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportUnityApi()
id = 'id_example' # str | Unique identifier of the Unity storage system. name:{name} can be used instead of {id}.

try:
    # Discover the importable volumes and consistency groups
    api_instance.import_unity_id_discover_post(id)
except ApiException as e:
    print("Exception when calling ImportUnityApi->import_unity_id_discover_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the Unity storage system. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_unity_id_get**
> ImportUnityInstance import_unity_id_get(id)

Instance Query

Query a specific Unity storage system.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportUnityApi()
id = 'id_example' # str | Unique identifier of the Unity storage system. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.import_unity_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportUnityApi->import_unity_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the Unity storage system. name:{name} can be used instead of {id}. | 

### Return type

[**ImportUnityInstance**](ImportUnityInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

