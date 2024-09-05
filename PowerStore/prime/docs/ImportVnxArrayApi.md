# prime.swagger_client.ImportVnxArrayApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_vnx_array_get**](ImportVnxArrayApi.md#import_vnx_array_get) | **GET** /import_vnx_array | Collection Query
[**import_vnx_array_id_discover_post**](ImportVnxArrayApi.md#import_vnx_array_id_discover_post) | **POST** /import_vnx_array/{id}/discover | Discover Importable Resources
[**import_vnx_array_id_get**](ImportVnxArrayApi.md#import_vnx_array_id_get) | **GET** /import_vnx_array/{id} | Instance Query


# **import_vnx_array_get**
> list[ImportVnxArrayInstance] import_vnx_array_get()

Collection Query

Query VNX storage systems.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportVnxArrayApi()

try:
    # Collection Query
    api_response = api_instance.import_vnx_array_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportVnxArrayApi->import_vnx_array_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ImportVnxArrayInstance]**](ImportVnxArrayInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_vnx_array_id_discover_post**
> import_vnx_array_id_discover_post(id)

Discover Importable Resources

Discover the importable volumes and consistency groups in a VNX storage system. Was deprecated in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportVnxArrayApi()
id = 'id_example' # str | Unique identifier of the VNX storage system. name:{name} can be used instead of {id}.

try:
    # Discover Importable Resources
    api_instance.import_vnx_array_id_discover_post(id)
except ApiException as e:
    print("Exception when calling ImportVnxArrayApi->import_vnx_array_id_discover_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the VNX storage system. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_vnx_array_id_get**
> ImportVnxArrayInstance import_vnx_array_id_get(id)

Instance Query

Query a specific VNX storage system.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportVnxArrayApi()
id = 'id_example' # str | Unique identifier of a VNX storage system. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.import_vnx_array_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportVnxArrayApi->import_vnx_array_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of a VNX storage system. name:{name} can be used instead of {id}. | 

### Return type

[**ImportVnxArrayInstance**](ImportVnxArrayInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

