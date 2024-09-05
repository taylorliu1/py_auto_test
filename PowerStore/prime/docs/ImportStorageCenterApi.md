# prime.swagger_client.ImportStorageCenterApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_storage_center_get**](ImportStorageCenterApi.md#import_storage_center_get) | **GET** /import_storage_center | Collection Query
[**import_storage_center_id_discover_post**](ImportStorageCenterApi.md#import_storage_center_id_discover_post) | **POST** /import_storage_center/{id}/discover | Discover importable resources
[**import_storage_center_id_get**](ImportStorageCenterApi.md#import_storage_center_id_get) | **GET** /import_storage_center/{id} | Instance Query


# **import_storage_center_get**
> list[ImportStorageCenterInstance] import_storage_center_get()

Collection Query

Query SC arrays.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportStorageCenterApi()

try:
    # Collection Query
    api_response = api_instance.import_storage_center_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportStorageCenterApi->import_storage_center_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ImportStorageCenterInstance]**](ImportStorageCenterInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_storage_center_id_discover_post**
> import_storage_center_id_discover_post(id)

Discover importable resources

Discover the importable volumes and snapshot profiles in the SC array. Was deprecated in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportStorageCenterApi()
id = 'id_example' # str | Unique identifier of the SC array. name:{name} can be used instead of {id}.

try:
    # Discover importable resources
    api_instance.import_storage_center_id_discover_post(id)
except ApiException as e:
    print("Exception when calling ImportStorageCenterApi->import_storage_center_id_discover_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the SC array. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_storage_center_id_get**
> ImportStorageCenterInstance import_storage_center_id_get(id)

Instance Query

Query a specific SC array.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportStorageCenterApi()
id = 'id_example' # str | Unique identifier of the SC array. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.import_storage_center_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportStorageCenterApi->import_storage_center_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the SC array. name:{name} can be used instead of {id}. | 

### Return type

[**ImportStorageCenterInstance**](ImportStorageCenterInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

