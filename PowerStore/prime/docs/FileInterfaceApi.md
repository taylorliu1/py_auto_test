# prime.swagger_client.FileInterfaceApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_interface_get**](FileInterfaceApi.md#file_interface_get) | **GET** /file_interface | Collection Query
[**file_interface_id_delete**](FileInterfaceApi.md#file_interface_id_delete) | **DELETE** /file_interface/{id} | Delete
[**file_interface_id_get**](FileInterfaceApi.md#file_interface_id_get) | **GET** /file_interface/{id} | Instance Query
[**file_interface_id_patch**](FileInterfaceApi.md#file_interface_id_patch) | **PATCH** /file_interface/{id} | Modify
[**file_interface_post**](FileInterfaceApi.md#file_interface_post) | **POST** /file_interface | Create


# **file_interface_get**
> list[FileInterfaceInstance] file_interface_get()

Collection Query

Query file interfaces.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileInterfaceApi()

try:
    # Collection Query
    api_response = api_instance.file_interface_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileInterfaceApi->file_interface_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileInterfaceInstance]**](FileInterfaceInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_interface_id_delete**
> file_interface_id_delete(id)

Delete

Delete a file interface.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileInterfaceApi()
id = 'id_example' # str | Unique identifier of the file interface. name:{name} can be used instead of {id}.

try:
    # Delete
    api_instance.file_interface_id_delete(id)
except ApiException as e:
    print("Exception when calling FileInterfaceApi->file_interface_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file interface. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_interface_id_get**
> FileInterfaceInstance file_interface_id_get(id)

Instance Query

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileInterfaceApi()
id = 'id_example' # str | Unique identifier of the file interface. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.file_interface_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileInterfaceApi->file_interface_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file interface. name:{name} can be used instead of {id}. | 

### Return type

[**FileInterfaceInstance**](FileInterfaceInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_interface_id_patch**
> file_interface_id_patch(id, body)

Modify

Modify the settings of a file interface.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileInterfaceApi()
id = 'id_example' # str | Unique identifier of the file interface. name:{name} can be used instead of {id}.
body = prime.swagger_client.FileInterfaceModify() # FileInterfaceModify | 

try:
    # Modify
    api_instance.file_interface_id_patch(id, body)
except ApiException as e:
    print("Exception when calling FileInterfaceApi->file_interface_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file interface. name:{name} can be used instead of {id}. | 
 **body** | [**FileInterfaceModify**](FileInterfaceModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_interface_post**
> CreateResponse file_interface_post(body)

Create

Create a file interface.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileInterfaceApi()
body = prime.swagger_client.FileInterfaceCreate() # FileInterfaceCreate | 

try:
    # Create
    api_response = api_instance.file_interface_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileInterfaceApi->file_interface_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileInterfaceCreate**](FileInterfaceCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

