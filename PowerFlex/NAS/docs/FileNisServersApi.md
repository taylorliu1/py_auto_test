# swagger_client.FileNisServersApi

All URIs are relative to *https://10.226.47.34/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_nis_servers_get**](FileNisServersApi.md#file_nis_servers_get) | **GET** /file-nis-servers | Collection Query
[**file_nis_servers_id_delete**](FileNisServersApi.md#file_nis_servers_id_delete) | **DELETE** /file-nis-servers/{id} | Delete
[**file_nis_servers_id_get**](FileNisServersApi.md#file_nis_servers_id_get) | **GET** /file-nis-servers/{id} | Instance Query
[**file_nis_servers_id_patch**](FileNisServersApi.md#file_nis_servers_id_patch) | **PATCH** /file-nis-servers/{id} | Modify
[**file_nis_servers_post**](FileNisServersApi.md#file_nis_servers_post) | **POST** /file-nis-servers | Create

# **file_nis_servers_get**
> list[FileNisInstance] file_nis_servers_get()

Collection Query

Query the NIS settings of NAS Servers.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileNisServersApi()

try:
    # Collection Query
    api_response = api_instance.file_nis_servers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileNisServersApi->file_nis_servers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileNisInstance]**](FileNisInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_nis_servers_id_delete**
> file_nis_servers_id_delete(id)

Delete

Delete NIS settings of a NAS Server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileNisServersApi()
id = 'id_example' # str | Unique identifier of the NIS object.

try:
    # Delete
    api_instance.file_nis_servers_id_delete(id)
except ApiException as e:
    print("Exception when calling FileNisServersApi->file_nis_servers_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NIS object. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_nis_servers_id_get**
> FileNisInstance file_nis_servers_id_get(id)

Instance Query

Query a specific NIS settings object of a NAS Server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileNisServersApi()
id = 'id_example' # str | Unique identifier of the NIS object.

try:
    # Instance Query
    api_response = api_instance.file_nis_servers_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileNisServersApi->file_nis_servers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NIS object. | 

### Return type

[**FileNisInstance**](FileNisInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_nis_servers_id_patch**
> file_nis_servers_id_patch(body, id)

Modify

Modify the NIS settings of a NAS Server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileNisServersApi()
body = swagger_client.FileNisModify() # FileNisModify | 
id = 'id_example' # str | Unique identifier of the NIS object.

try:
    # Modify
    api_instance.file_nis_servers_id_patch(body, id)
except ApiException as e:
    print("Exception when calling FileNisServersApi->file_nis_servers_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileNisModify**](FileNisModify.md)|  | 
 **id** | **str**| Unique identifier of the NIS object. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_nis_servers_post**
> CreateResponse file_nis_servers_post(body)

Create

Create a new NIS Service on a NAS Server. Only one NIS Setting object can be created per NAS Server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileNisServersApi()
body = swagger_client.FileNisCreate() # FileNisCreate | 

try:
    # Create
    api_response = api_instance.file_nis_servers_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileNisServersApi->file_nis_servers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileNisCreate**](FileNisCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

