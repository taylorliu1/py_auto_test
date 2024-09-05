# prime.swagger_client.FileNisApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_nis_get**](FileNisApi.md#file_nis_get) | **GET** /file_nis | Collection Query
[**file_nis_id_delete**](FileNisApi.md#file_nis_id_delete) | **DELETE** /file_nis/{id} | Delete
[**file_nis_id_get**](FileNisApi.md#file_nis_id_get) | **GET** /file_nis/{id} | Instance Query
[**file_nis_id_patch**](FileNisApi.md#file_nis_id_patch) | **PATCH** /file_nis/{id} | Modify
[**file_nis_post**](FileNisApi.md#file_nis_post) | **POST** /file_nis | Create


# **file_nis_get**
> list[FileNisInstance] file_nis_get()

Collection Query

Query the NIS settings of NAS Servers.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileNisApi()

try:
    # Collection Query
    api_response = api_instance.file_nis_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileNisApi->file_nis_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileNisInstance]**](FileNisInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_nis_id_delete**
> file_nis_id_delete(id)

Delete

Delete NIS settings of a NAS Server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileNisApi()
id = 'id_example' # str | Unique identifier of the NIS object.

try:
    # Delete
    api_instance.file_nis_id_delete(id)
except ApiException as e:
    print("Exception when calling FileNisApi->file_nis_id_delete: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_nis_id_get**
> FileNisInstance file_nis_id_get(id)

Instance Query

Query a specific NIS settings object of a NAS Server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileNisApi()
id = 'id_example' # str | Unique identifier of the NIS object.

try:
    # Instance Query
    api_response = api_instance.file_nis_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileNisApi->file_nis_id_get: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_nis_id_patch**
> file_nis_id_patch(id, body)

Modify

Modify the NIS settings of a NAS Server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileNisApi()
id = 'id_example' # str | Unique identifier of the NIS object.
body = prime.swagger_client.FileNisModify() # FileNisModify | 

try:
    # Modify
    api_instance.file_nis_id_patch(id, body)
except ApiException as e:
    print("Exception when calling FileNisApi->file_nis_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NIS object. | 
 **body** | [**FileNisModify**](FileNisModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_nis_post**
> CreateResponse file_nis_post(body)

Create

Create a new NIS Service on a NAS Server. Only one NIS Setting object can be created per NAS Server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileNisApi()
body = prime.swagger_client.FileNisCreate() # FileNisCreate | 

try:
    # Create
    api_response = api_instance.file_nis_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileNisApi->file_nis_post: %s\n" % e)
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

