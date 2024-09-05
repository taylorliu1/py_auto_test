# prime.swagger_client.ImportPsgroupApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_psgroup_get**](ImportPsgroupApi.md#import_psgroup_get) | **GET** /import_psgroup | Collection Query
[**import_psgroup_id_discover_post**](ImportPsgroupApi.md#import_psgroup_id_discover_post) | **POST** /import_psgroup/{id}/discover | Discover importable storage resources
[**import_psgroup_id_get**](ImportPsgroupApi.md#import_psgroup_id_get) | **GET** /import_psgroup/{id} | Instance Query


# **import_psgroup_get**
> list[ImportPsgroupInstance] import_psgroup_get()

Collection Query

Query PS Group storage arrays.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportPsgroupApi()

try:
    # Collection Query
    api_response = api_instance.import_psgroup_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportPsgroupApi->import_psgroup_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ImportPsgroupInstance]**](ImportPsgroupInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_psgroup_id_discover_post**
> import_psgroup_id_discover_post(id)

Discover importable storage resources

Discover the importable volumes and snapshot schedules in the PS Group. Was deprecated in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportPsgroupApi()
id = 'id_example' # str | Unique identifier of the PS Group. name:{name} can be used instead of {id}.

try:
    # Discover importable storage resources
    api_instance.import_psgroup_id_discover_post(id)
except ApiException as e:
    print("Exception when calling ImportPsgroupApi->import_psgroup_id_discover_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the PS Group. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_psgroup_id_get**
> ImportPsgroupInstance import_psgroup_id_get(id)

Instance Query

Query a specific PS Group storage array.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportPsgroupApi()
id = 'id_example' # str | Unique identifier of the PS Group. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.import_psgroup_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportPsgroupApi->import_psgroup_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the PS Group. name:{name} can be used instead of {id}. | 

### Return type

[**ImportPsgroupInstance**](ImportPsgroupInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

