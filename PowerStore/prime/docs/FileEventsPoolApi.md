# prime.swagger_client.FileEventsPoolApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_events_pool_get**](FileEventsPoolApi.md#file_events_pool_get) | **GET** /file_events_pool | Collection Query
[**file_events_pool_id_delete**](FileEventsPoolApi.md#file_events_pool_id_delete) | **DELETE** /file_events_pool/{id} | Delete
[**file_events_pool_id_get**](FileEventsPoolApi.md#file_events_pool_id_get) | **GET** /file_events_pool/{id} | Instance Query
[**file_events_pool_id_patch**](FileEventsPoolApi.md#file_events_pool_id_patch) | **PATCH** /file_events_pool/{id} | Modify
[**file_events_pool_post**](FileEventsPoolApi.md#file_events_pool_post) | **POST** /file_events_pool | Create


# **file_events_pool_get**
> list[FileEventsPoolInstance] file_events_pool_get()

Collection Query

Query file events pools. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileEventsPoolApi()

try:
    # Collection Query
    api_response = api_instance.file_events_pool_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileEventsPoolApi->file_events_pool_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileEventsPoolInstance]**](FileEventsPoolInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_events_pool_id_delete**
> file_events_pool_id_delete(id)

Delete

Delete a file events pool. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileEventsPoolApi()
id = 'id_example' # str | Unique identifier of the file events pool. name:{name} can be used instead of {id}.

try:
    # Delete
    api_instance.file_events_pool_id_delete(id)
except ApiException as e:
    print("Exception when calling FileEventsPoolApi->file_events_pool_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file events pool. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_events_pool_id_get**
> FileEventsPoolInstance file_events_pool_id_get(id)

Instance Query

Query one file events pool. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileEventsPoolApi()
id = 'id_example' # str | Unique identifier of the file events pool. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.file_events_pool_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileEventsPoolApi->file_events_pool_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file events pool. name:{name} can be used instead of {id}. | 

### Return type

[**FileEventsPoolInstance**](FileEventsPoolInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_events_pool_id_patch**
> file_events_pool_id_patch(id, body)

Modify

Modify the settings of a file events pool. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileEventsPoolApi()
id = 'id_example' # str | Unique identifier of the events pool. name:{name} can be used instead of {id}.
body = prime.swagger_client.FileEventsPoolModify() # FileEventsPoolModify | 

try:
    # Modify
    api_instance.file_events_pool_id_patch(id, body)
except ApiException as e:
    print("Exception when calling FileEventsPoolApi->file_events_pool_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the events pool. name:{name} can be used instead of {id}. | 
 **body** | [**FileEventsPoolModify**](FileEventsPoolModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_events_pool_post**
> CreateResponse file_events_pool_post(body)

Create

Create a file events pool. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileEventsPoolApi()
body = prime.swagger_client.FileEventsPoolCreate() # FileEventsPoolCreate | 

try:
    # Create
    api_response = api_instance.file_events_pool_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileEventsPoolApi->file_events_pool_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileEventsPoolCreate**](FileEventsPoolCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

