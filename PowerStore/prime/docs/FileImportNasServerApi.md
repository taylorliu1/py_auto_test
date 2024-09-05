# prime.swagger_client.FileImportNasServerApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_import_nas_server_get**](FileImportNasServerApi.md#file_import_nas_server_get) | **GET** /file_import_nas_server | Collection Query
[**file_import_nas_server_id_get**](FileImportNasServerApi.md#file_import_nas_server_id_get) | **GET** /file_import_nas_server/{id} | Instance Query


# **file_import_nas_server_get**
> list[FileImportNasServerInstance] file_import_nas_server_get()

Collection Query

Query importable source NAS servers discovered on existing remote systems. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileImportNasServerApi()

try:
    # Collection Query
    api_response = api_instance.file_import_nas_server_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileImportNasServerApi->file_import_nas_server_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileImportNasServerInstance]**](FileImportNasServerInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_import_nas_server_id_get**
> FileImportNasServerInstance file_import_nas_server_id_get(id)

Instance Query

Query a specific discovered File Import NAS Server. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileImportNasServerApi()
id = 'id_example' # str | Unique identifier of a File Import NAS Server of the remote system. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.file_import_nas_server_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileImportNasServerApi->file_import_nas_server_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of a File Import NAS Server of the remote system. name:{name} can be used instead of {id}. | 

### Return type

[**FileImportNasServerInstance**](FileImportNasServerInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

