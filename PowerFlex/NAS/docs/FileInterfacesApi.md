# swagger_client.FileInterfacesApi

All URIs are relative to *https://10.226.47.34/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_interfaces_get**](FileInterfacesApi.md#file_interfaces_get) | **GET** /file-interfaces | Collection Query
[**file_interfaces_id_delete**](FileInterfacesApi.md#file_interfaces_id_delete) | **DELETE** /file-interfaces/{id} | Delete
[**file_interfaces_id_get**](FileInterfacesApi.md#file_interfaces_id_get) | **GET** /file-interfaces/{id} | Instance Query
[**file_interfaces_id_patch**](FileInterfacesApi.md#file_interfaces_id_patch) | **PATCH** /file-interfaces/{id} | Modify
[**file_interfaces_post**](FileInterfacesApi.md#file_interfaces_post) | **POST** /file-interfaces | Create

# **file_interfaces_get**
> list[FileInterfaceInstance] file_interfaces_get()

Collection Query

Query file interfaces.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileInterfacesApi()

try:
    # Collection Query
    api_response = api_instance.file_interfaces_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileInterfacesApi->file_interfaces_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileInterfaceInstance]**](FileInterfaceInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_interfaces_id_delete**
> file_interfaces_id_delete(id)

Delete

Delete a file interface.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileInterfacesApi()
id = 'id_example' # str | Unique identifier of the file interface.

try:
    # Delete
    api_instance.file_interfaces_id_delete(id)
except ApiException as e:
    print("Exception when calling FileInterfacesApi->file_interfaces_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file interface. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_interfaces_id_get**
> FileInterfaceInstance file_interfaces_id_get(id)

Instance Query

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileInterfacesApi()
id = 'id_example' # str | Unique identifier of the file interface.

try:
    # Instance Query
    api_response = api_instance.file_interfaces_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileInterfacesApi->file_interfaces_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file interface. | 

### Return type

[**FileInterfaceInstance**](FileInterfaceInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_interfaces_id_patch**
> file_interfaces_id_patch(body, id)

Modify

Modify the settings of a file interface.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileInterfacesApi()
body = swagger_client.FileInterfaceModify() # FileInterfaceModify | 
id = 'id_example' # str | Unique identifier of the file interface.

try:
    # Modify
    api_instance.file_interfaces_id_patch(body, id)
except ApiException as e:
    print("Exception when calling FileInterfacesApi->file_interfaces_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileInterfaceModify**](FileInterfaceModify.md)|  | 
 **id** | **str**| Unique identifier of the file interface. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_interfaces_post**
> CreateResponse file_interfaces_post(body)

Create

Create a file interface.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileInterfacesApi()
body = swagger_client.FileInterfaceCreate() # FileInterfaceCreate | 

try:
    # Create
    api_response = api_instance.file_interfaces_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileInterfacesApi->file_interfaces_post: %s\n" % e)
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

