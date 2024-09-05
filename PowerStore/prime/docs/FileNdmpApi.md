# prime.swagger_client.FileNdmpApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_ndmp_get**](FileNdmpApi.md#file_ndmp_get) | **GET** /file_ndmp | Collection Query
[**file_ndmp_id_delete**](FileNdmpApi.md#file_ndmp_id_delete) | **DELETE** /file_ndmp/{id} | Delete
[**file_ndmp_id_get**](FileNdmpApi.md#file_ndmp_id_get) | **GET** /file_ndmp/{id} | Instance Query
[**file_ndmp_id_patch**](FileNdmpApi.md#file_ndmp_id_patch) | **PATCH** /file_ndmp/{id} | Modify
[**file_ndmp_post**](FileNdmpApi.md#file_ndmp_post) | **POST** /file_ndmp | Create


# **file_ndmp_get**
> list[FileNdmpInstance] file_ndmp_get()

Collection Query

Query configured NDMP service instances.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileNdmpApi()

try:
    # Collection Query
    api_response = api_instance.file_ndmp_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileNdmpApi->file_ndmp_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileNdmpInstance]**](FileNdmpInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ndmp_id_delete**
> file_ndmp_id_delete(id)

Delete

Delete an NDMP service configuration instance of a NAS Server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileNdmpApi()
id = 'id_example' # str | Unique identifier of the NDMP service object.

try:
    # Delete
    api_instance.file_ndmp_id_delete(id)
except ApiException as e:
    print("Exception when calling FileNdmpApi->file_ndmp_id_delete: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ndmp_id_get**
> FileNdmpInstance file_ndmp_id_get(id)

Instance Query

Query an NDMP service configuration instance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileNdmpApi()
id = 'id_example' # str | Unique identifier of the NDMP service object.

try:
    # Instance Query
    api_response = api_instance.file_ndmp_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileNdmpApi->file_ndmp_id_get: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ndmp_id_patch**
> file_ndmp_id_patch(id, body)

Modify

Modify an NDMP service configuration instance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileNdmpApi()
id = 'id_example' # str | Unique identifier of the NDMP service object.
body = prime.swagger_client.FileNdmpModify() # FileNdmpModify | 

try:
    # Modify
    api_instance.file_ndmp_id_patch(id, body)
except ApiException as e:
    print("Exception when calling FileNdmpApi->file_ndmp_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NDMP service object. | 
 **body** | [**FileNdmpModify**](FileNdmpModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ndmp_post**
> CreateResponse file_ndmp_post(body)

Create

Add an NDMP service configuration to a NAS server. Only one NDMP service object can be configured per NAS server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileNdmpApi()
body = prime.swagger_client.FileNdmpCreate() # FileNdmpCreate | 

try:
    # Create
    api_response = api_instance.file_ndmp_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileNdmpApi->file_ndmp_post: %s\n" % e)
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

