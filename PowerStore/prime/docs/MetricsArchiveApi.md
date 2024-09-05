# prime.swagger_client.MetricsArchiveApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metrics_archive_generate_post**](MetricsArchiveApi.md#metrics_archive_generate_post) | **POST** /metrics_archive/generate | Generate
[**metrics_archive_get**](MetricsArchiveApi.md#metrics_archive_get) | **GET** /metrics_archive | Collection Query
[**metrics_archive_id_download_get**](MetricsArchiveApi.md#metrics_archive_id_download_get) | **GET** /metrics_archive/{id}/download | Download Query
[**metrics_archive_id_get**](MetricsArchiveApi.md#metrics_archive_id_get) | **GET** /metrics_archive/{id} | Instance Query


# **metrics_archive_generate_post**
> MetricsArchiveGenerateResponse metrics_archive_generate_post(body=body)

Generate

Generate a new metrics archive from the collected metrics and config data.  Only one metrics archive generation operation may be running at a time. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.MetricsArchiveApi()
body = prime.swagger_client.MetricsArchiveGenerate() # MetricsArchiveGenerate |  (optional)

try:
    # Generate
    api_response = api_instance.metrics_archive_generate_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsArchiveApi->metrics_archive_generate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetricsArchiveGenerate**](MetricsArchiveGenerate.md)|  | [optional] 

### Return type

[**MetricsArchiveGenerateResponse**](MetricsArchiveGenerateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics_archive_get**
> list[MetricsArchiveInstance] metrics_archive_get()

Collection Query

Query metrics archives. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.MetricsArchiveApi()

try:
    # Collection Query
    api_response = api_instance.metrics_archive_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsArchiveApi->metrics_archive_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MetricsArchiveInstance]**](MetricsArchiveInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics_archive_id_download_get**
> MetricsArchiveFile metrics_archive_id_download_get(id)

Download Query

Download a specific metrics archive instance. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.MetricsArchiveApi()
id = 'id_example' # str | Unique identifier of the metrics archive. name:{name} can be used instead of {id}. Was added in version 3.0.0.0.

try:
    # Download Query
    api_response = api_instance.metrics_archive_id_download_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsArchiveApi->metrics_archive_id_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the metrics archive. name:{name} can be used instead of {id}. Was added in version 3.0.0.0. | 

### Return type

[**MetricsArchiveFile**](MetricsArchiveFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/binary

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics_archive_id_get**
> MetricsArchiveInstance metrics_archive_id_get(id)

Instance Query

Query a specific metrics archive instance. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.MetricsArchiveApi()
id = 'id_example' # str | Unique identifier of the metrics archive. name:{name} can be used instead of {id}. Was added in version 3.0.0.0.

try:
    # Instance Query
    api_response = api_instance.metrics_archive_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsArchiveApi->metrics_archive_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the metrics archive. name:{name} can be used instead of {id}. Was added in version 3.0.0.0. | 

### Return type

[**MetricsArchiveInstance**](MetricsArchiveInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

