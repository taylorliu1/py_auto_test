# prime.swagger_client.FileEventsPublisherApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_events_publisher_get**](FileEventsPublisherApi.md#file_events_publisher_get) | **GET** /file_events_publisher | Collection Query
[**file_events_publisher_id_delete**](FileEventsPublisherApi.md#file_events_publisher_id_delete) | **DELETE** /file_events_publisher/{id} | Delete
[**file_events_publisher_id_get**](FileEventsPublisherApi.md#file_events_publisher_id_get) | **GET** /file_events_publisher/{id} | Instance Query
[**file_events_publisher_id_patch**](FileEventsPublisherApi.md#file_events_publisher_id_patch) | **PATCH** /file_events_publisher/{id} | Modify
[**file_events_publisher_post**](FileEventsPublisherApi.md#file_events_publisher_post) | **POST** /file_events_publisher | Create


# **file_events_publisher_get**
> list[FileEventsPublisherInstance] file_events_publisher_get()

Collection Query

List file events publisher service instances. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileEventsPublisherApi()

try:
    # Collection Query
    api_response = api_instance.file_events_publisher_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileEventsPublisherApi->file_events_publisher_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileEventsPublisherInstance]**](FileEventsPublisherInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_events_publisher_id_delete**
> file_events_publisher_id_delete(id)

Delete

Delete file events publisher. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileEventsPublisherApi()
id = 'id_example' # str | Unique identifier of the file events publisher. name:{name} can be used instead of {id}.

try:
    # Delete
    api_instance.file_events_publisher_id_delete(id)
except ApiException as e:
    print("Exception when calling FileEventsPublisherApi->file_events_publisher_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file events publisher. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_events_publisher_id_get**
> FileEventsPublisherInstance file_events_publisher_id_get(id)

Instance Query

Query configuration details of a specific file events publisher service.  Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileEventsPublisherApi()
id = 'id_example' # str | Unique identifier of the File Events Publisher. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.file_events_publisher_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileEventsPublisherApi->file_events_publisher_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the File Events Publisher. name:{name} can be used instead of {id}. | 

### Return type

[**FileEventsPublisherInstance**](FileEventsPublisherInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_events_publisher_id_patch**
> file_events_publisher_id_patch(id, body)

Modify

Modify a file events publisher. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileEventsPublisherApi()
id = 'id_example' # str | Unique identifier of the file events publisher. name:{name} can be used instead of {id}.
body = prime.swagger_client.FileEventsPublisherModify() # FileEventsPublisherModify | 

try:
    # Modify
    api_instance.file_events_publisher_id_patch(id, body)
except ApiException as e:
    print("Exception when calling FileEventsPublisherApi->file_events_publisher_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file events publisher. name:{name} can be used instead of {id}. | 
 **body** | [**FileEventsPublisherModify**](FileEventsPublisherModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_events_publisher_post**
> CreateResponse file_events_publisher_post(body)

Create

Create a file events publisher. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileEventsPublisherApi()
body = prime.swagger_client.FileEventsPublisherCreate() # FileEventsPublisherCreate | 

try:
    # Create
    api_response = api_instance.file_events_publisher_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileEventsPublisherApi->file_events_publisher_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileEventsPublisherCreate**](FileEventsPublisherCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

