# prime.swagger_client.PhysicalSwitchApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**physical_switch_get**](PhysicalSwitchApi.md#physical_switch_get) | **GET** /physical_switch | Collection Query
[**physical_switch_id_delete**](PhysicalSwitchApi.md#physical_switch_id_delete) | **DELETE** /physical_switch/{id} | Delete
[**physical_switch_id_get**](PhysicalSwitchApi.md#physical_switch_id_get) | **GET** /physical_switch/{id} | Instance Query
[**physical_switch_id_patch**](PhysicalSwitchApi.md#physical_switch_id_patch) | **PATCH** /physical_switch/{id} | Modify
[**physical_switch_post**](PhysicalSwitchApi.md#physical_switch_post) | **POST** /physical_switch | Create


# **physical_switch_get**
> list[PhysicalSwitchInstance] physical_switch_get()

Collection Query

Query physical switches settings for a cluster.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.PhysicalSwitchApi()

try:
    # Collection Query
    api_response = api_instance.physical_switch_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhysicalSwitchApi->physical_switch_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PhysicalSwitchInstance]**](PhysicalSwitchInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **physical_switch_id_delete**
> physical_switch_id_delete(id)

Delete

Delete the physical switch settings.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.PhysicalSwitchApi()
id = 'id_example' # str | Unique identifier of the physical switch settings. name:{name} can be used instead of {id}.

try:
    # Delete
    api_instance.physical_switch_id_delete(id)
except ApiException as e:
    print("Exception when calling PhysicalSwitchApi->physical_switch_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the physical switch settings. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **physical_switch_id_get**
> PhysicalSwitchInstance physical_switch_id_get(id)

Instance Query

Query a specific physical switch settings.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.PhysicalSwitchApi()
id = 'id_example' # str | Unique identifier of the physical switch settings. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.physical_switch_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhysicalSwitchApi->physical_switch_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the physical switch settings. name:{name} can be used instead of {id}. | 

### Return type

[**PhysicalSwitchInstance**](PhysicalSwitchInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **physical_switch_id_patch**
> physical_switch_id_patch(id, body=body)

Modify

Modify a physical switch settings.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.PhysicalSwitchApi()
id = 'id_example' # str | Unique identifier of the physical switch settings. name:{name} can be used instead of {id}.
body = prime.swagger_client.PhysicalSwitchModify() # PhysicalSwitchModify |  (optional)

try:
    # Modify
    api_instance.physical_switch_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling PhysicalSwitchApi->physical_switch_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the physical switch settings. name:{name} can be used instead of {id}. | 
 **body** | [**PhysicalSwitchModify**](PhysicalSwitchModify.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **physical_switch_post**
> CreateResponse physical_switch_post(body)

Create

Create a physical switch settings.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.PhysicalSwitchApi()
body = prime.swagger_client.PhysicalSwitchCreate() # PhysicalSwitchCreate | 

try:
    # Create
    api_response = api_instance.physical_switch_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PhysicalSwitchApi->physical_switch_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhysicalSwitchCreate**](PhysicalSwitchCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

