# prime.swagger_client.FileImportInterfaceApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_import_interface_get**](FileImportInterfaceApi.md#file_import_interface_get) | **GET** /file_import_interface | Collection Query
[**file_import_interface_id_delete**](FileImportInterfaceApi.md#file_import_interface_id_delete) | **DELETE** /file_import_interface/{id} | Delete
[**file_import_interface_id_get**](FileImportInterfaceApi.md#file_import_interface_id_get) | **GET** /file_import_interface/{id} | Instance Query
[**file_import_interface_id_patch**](FileImportInterfaceApi.md#file_import_interface_id_patch) | **PATCH** /file_import_interface/{id} | Modify
[**file_import_interface_post**](FileImportInterfaceApi.md#file_import_interface_post) | **POST** /file_import_interface | Create


# **file_import_interface_get**
> list[FileImportInterfaceInstance] file_import_interface_get()

Collection Query

Query file import interfaces. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileImportInterfaceApi()

try:
    # Collection Query
    api_response = api_instance.file_import_interface_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileImportInterfaceApi->file_import_interface_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileImportInterfaceInstance]**](FileImportInterfaceInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_import_interface_id_delete**
> file_import_interface_id_delete(id)

Delete

Delete a file import interface. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileImportInterfaceApi()
id = 'id_example' # str | Unique identifier of the file import interface.

try:
    # Delete
    api_instance.file_import_interface_id_delete(id)
except ApiException as e:
    print("Exception when calling FileImportInterfaceApi->file_import_interface_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file import interface. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_import_interface_id_get**
> FileImportInterfaceInstance file_import_interface_id_get(id)

Instance Query

Query a specific file import interface. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileImportInterfaceApi()
id = 'id_example' # str | Unique identifier of the file import interface.

try:
    # Instance Query
    api_response = api_instance.file_import_interface_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileImportInterfaceApi->file_import_interface_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file import interface. | 

### Return type

[**FileImportInterfaceInstance**](FileImportInterfaceInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_import_interface_id_patch**
> file_import_interface_id_patch(id, body)

Modify

Modify the settings of a file import interface. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileImportInterfaceApi()
id = 'id_example' # str | Unique identifier of the file import interface.
body = prime.swagger_client.FileImportInterfaceModify() # FileImportInterfaceModify | 

try:
    # Modify
    api_instance.file_import_interface_id_patch(id, body)
except ApiException as e:
    print("Exception when calling FileImportInterfaceApi->file_import_interface_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file import interface. | 
 **body** | [**FileImportInterfaceModify**](FileImportInterfaceModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_import_interface_post**
> CreateResponse file_import_interface_post(body)

Create

Create a file import interface. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileImportInterfaceApi()
body = prime.swagger_client.FileImportInterfaceCreate() # FileImportInterfaceCreate | 

try:
    # Create
    api_response = api_instance.file_import_interface_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileImportInterfaceApi->file_import_interface_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileImportInterfaceCreate**](FileImportInterfaceCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

