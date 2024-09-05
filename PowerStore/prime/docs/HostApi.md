# prime.swagger_client.HostApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_get**](HostApi.md#host_get) | **GET** /host | Collection Query.
[**host_id_attach_post**](HostApi.md#host_id_attach_post) | **POST** /host/{id}/attach | Attach
[**host_id_delete**](HostApi.md#host_id_delete) | **DELETE** /host/{id} | Delete
[**host_id_detach_post**](HostApi.md#host_id_detach_post) | **POST** /host/{id}/detach | Detach
[**host_id_get**](HostApi.md#host_id_get) | **GET** /host/{id} | Instance Query
[**host_id_patch**](HostApi.md#host_id_patch) | **PATCH** /host/{id} | Modify
[**host_post**](HostApi.md#host_post) | **POST** /host | Create


# **host_get**
> list[HostInstance] host_get()

Collection Query.

Query hosts

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.HostApi()

try:
    # Collection Query.
    api_response = api_instance.host_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostApi->host_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[HostInstance]**](HostInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_id_attach_post**
> host_id_attach_post(id, body)

Attach

Attach host to volume.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.HostApi()
id = 'id_example' # str | Unique identifier of the host. name:{name} can be used instead of {id}.
body = prime.swagger_client.HostAttach() # HostAttach | 

try:
    # Attach
    api_instance.host_id_attach_post(id, body)
except ApiException as e:
    print("Exception when calling HostApi->host_id_attach_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the host. name:{name} can be used instead of {id}. | 
 **body** | [**HostAttach**](HostAttach.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_id_delete**
> host_id_delete(id, body=body)

Delete

Delete a host. Delete fails if host is attached to a volume or consistency group.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.HostApi()
id = 'id_example' # str | Unique identifier of the host. name:{name} can be used instead of {id}.
body = prime.swagger_client.HostDelete() # HostDelete |  (optional)

try:
    # Delete
    api_instance.host_id_delete(id, body=body)
except ApiException as e:
    print("Exception when calling HostApi->host_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the host. name:{name} can be used instead of {id}. | 
 **body** | [**HostDelete**](HostDelete.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_id_detach_post**
> host_id_detach_post(id, body)

Detach

Detach host from volume.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.HostApi()
id = 'id_example' # str | Unique identifier of the host. name:{name} can be used instead of {id}.
body = prime.swagger_client.HostDetach() # HostDetach | 

try:
    # Detach
    api_instance.host_id_detach_post(id, body)
except ApiException as e:
    print("Exception when calling HostApi->host_id_detach_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the host. name:{name} can be used instead of {id}. | 
 **body** | [**HostDetach**](HostDetach.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_id_get**
> HostInstance host_id_get(id)

Instance Query

Query details about a specific host.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.HostApi()
id = 'id_example' # str | Unique identifier of the host. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.host_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostApi->host_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the host. name:{name} can be used instead of {id}. | 

### Return type

[**HostInstance**](HostInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_id_patch**
> host_id_patch(id, body)

Modify

Modify a host. Only one of add, remove and update initiator operations are supported in a single request.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.HostApi()
id = 'id_example' # str | Unique identifier of the host. name:{name} can be used instead of {id}.
body = prime.swagger_client.HostModify() # HostModify | 

try:
    # Modify
    api_instance.host_id_patch(id, body)
except ApiException as e:
    print("Exception when calling HostApi->host_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the host. name:{name} can be used instead of {id}. | 
 **body** | [**HostModify**](HostModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_post**
> CreateResponse host_post(body)

Create

Add a host.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.HostApi()
body = prime.swagger_client.HostCreate() # HostCreate | 

try:
    # Create
    api_response = api_instance.host_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostApi->host_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostCreate**](HostCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

