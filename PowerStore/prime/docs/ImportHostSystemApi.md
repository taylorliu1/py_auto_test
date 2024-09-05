# prime.swagger_client.ImportHostSystemApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_host_system_get**](ImportHostSystemApi.md#import_host_system_get) | **GET** /import_host_system | Collection Query
[**import_host_system_id_delete**](ImportHostSystemApi.md#import_host_system_id_delete) | **DELETE** /import_host_system/{id} | Delete
[**import_host_system_id_get**](ImportHostSystemApi.md#import_host_system_id_get) | **GET** /import_host_system/{id} | Instance Query
[**import_host_system_id_refresh_post**](ImportHostSystemApi.md#import_host_system_id_refresh_post) | **POST** /import_host_system/{id}/refresh | Refresh
[**import_host_system_post**](ImportHostSystemApi.md#import_host_system_post) | **POST** /import_host_system | Create


# **import_host_system_get**
> list[ImportHostSystemInstance] import_host_system_get()

Collection Query

Query import host systems that are attached to volumes.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportHostSystemApi()

try:
    # Collection Query
    api_response = api_instance.import_host_system_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportHostSystemApi->import_host_system_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ImportHostSystemInstance]**](ImportHostSystemInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_host_system_id_delete**
> import_host_system_id_delete(id)

Delete

Delete an import host system. You cannot delete an import host system if there are import sessions active in the system referencing the import host system instance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportHostSystemApi()
id = 'id_example' # str | Unique identifier of the import host system

try:
    # Delete
    api_instance.import_host_system_id_delete(id)
except ApiException as e:
    print("Exception when calling ImportHostSystemApi->import_host_system_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the import host system | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_host_system_id_get**
> ImportHostSystemInstance import_host_system_id_get(id)

Instance Query

Query a specific import host system instance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportHostSystemApi()
id = 'id_example' # str | Unique identifier of the import host system to query.

try:
    # Instance Query
    api_response = api_instance.import_host_system_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportHostSystemApi->import_host_system_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the import host system to query. | 

### Return type

[**ImportHostSystemInstance**](ImportHostSystemInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_host_system_id_refresh_post**
> import_host_system_id_refresh_post(id)

Refresh

Refresh the details of a specific import host system. Use this operation when there is a change to the import host or import host volumes.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportHostSystemApi()
id = 'id_example' # str | Unique identifier of the import host system for which to refresh details.

try:
    # Refresh
    api_instance.import_host_system_id_refresh_post(id)
except ApiException as e:
    print("Exception when calling ImportHostSystemApi->import_host_system_id_refresh_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the import host system for which to refresh details. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_host_system_post**
> CreateResponse import_host_system_post(request)

Create

Add an import host system so that it can be mapped to a volume. Before mapping an import host system, ensure that a host agent is installed. Host agents can be installed on Linux, Windows, and ESXi host systems only.  While adding import_host_system if Host is not present a new Host shall be created. If Host is already present, the same Host will be updated with the import_host_system details.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportHostSystemApi()
request = prime.swagger_client.ImportHostSystemCreate() # ImportHostSystemCreate | Request parameters.

try:
    # Create
    api_response = api_instance.import_host_system_post(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportHostSystemApi->import_host_system_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ImportHostSystemCreate**](ImportHostSystemCreate.md)| Request parameters. | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

