# swagger_client.FileNdmpServersApi

All URIs are relative to *https://10.226.47.34/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_ndmp_servers_get**](FileNdmpServersApi.md#file_ndmp_servers_get) | **GET** /file-ndmp-servers | Collection Query
[**file_ndmp_servers_id_delete**](FileNdmpServersApi.md#file_ndmp_servers_id_delete) | **DELETE** /file-ndmp-servers/{id} | Delete
[**file_ndmp_servers_id_get**](FileNdmpServersApi.md#file_ndmp_servers_id_get) | **GET** /file-ndmp-servers/{id} | Instance Query
[**file_ndmp_servers_id_patch**](FileNdmpServersApi.md#file_ndmp_servers_id_patch) | **PATCH** /file-ndmp-servers/{id} | Modify
[**file_ndmp_servers_post**](FileNdmpServersApi.md#file_ndmp_servers_post) | **POST** /file-ndmp-servers | Create

# **file_ndmp_servers_get**
> list[FileNdmpInstance] file_ndmp_servers_get()

Collection Query

List configured NDMP service instances.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileNdmpServersApi()

try:
    # Collection Query
    api_response = api_instance.file_ndmp_servers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileNdmpServersApi->file_ndmp_servers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileNdmpInstance]**](FileNdmpInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ndmp_servers_id_delete**
> file_ndmp_servers_id_delete(id)

Delete

Delete an NDMP service configuration instance of a NAS Server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileNdmpServersApi()
id = 'id_example' # str | Unique identifier of the NDMP service object.

try:
    # Delete
    api_instance.file_ndmp_servers_id_delete(id)
except ApiException as e:
    print("Exception when calling FileNdmpServersApi->file_ndmp_servers_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NDMP service object. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ndmp_servers_id_get**
> FileNdmpInstance file_ndmp_servers_id_get(id)

Instance Query

Query an NDMP service configuration instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileNdmpServersApi()
id = 'id_example' # str | Unique identifier of the NDMP service object.

try:
    # Instance Query
    api_response = api_instance.file_ndmp_servers_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileNdmpServersApi->file_ndmp_servers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NDMP service object. | 

### Return type

[**FileNdmpInstance**](FileNdmpInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ndmp_servers_id_patch**
> file_ndmp_servers_id_patch(body, id)

Modify

Modify an NDMP service configuration instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileNdmpServersApi()
body = swagger_client.FileNdmpModify() # FileNdmpModify | 
id = 'id_example' # str | Unique identifier of the NDMP service object.

try:
    # Modify
    api_instance.file_ndmp_servers_id_patch(body, id)
except ApiException as e:
    print("Exception when calling FileNdmpServersApi->file_ndmp_servers_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileNdmpModify**](FileNdmpModify.md)|  | 
 **id** | **str**| Unique identifier of the NDMP service object. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ndmp_servers_post**
> CreateResponse file_ndmp_servers_post(body)

Create

Add an NDMP service configuration to a NAS server. Only one NDMP service object can be configured per NAS server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileNdmpServersApi()
body = swagger_client.FileNdmpCreate() # FileNdmpCreate | 

try:
    # Create
    api_response = api_instance.file_ndmp_servers_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileNdmpServersApi->file_ndmp_servers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileNdmpCreate**](FileNdmpCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

