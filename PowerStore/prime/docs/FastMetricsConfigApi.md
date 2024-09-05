# prime.swagger_client.FastMetricsConfigApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fast_metrics_config_get**](FastMetricsConfigApi.md#fast_metrics_config_get) | **GET** /fast_metrics_config | Collection Query
[**fast_metrics_config_id_delete**](FastMetricsConfigApi.md#fast_metrics_config_id_delete) | **DELETE** /fast_metrics_config/{id} | Delete
[**fast_metrics_config_id_get**](FastMetricsConfigApi.md#fast_metrics_config_id_get) | **GET** /fast_metrics_config/{id} | Instance Query
[**fast_metrics_config_post**](FastMetricsConfigApi.md#fast_metrics_config_post) | **POST** /fast_metrics_config | Create


# **fast_metrics_config_get**
> list[FastMetricsConfigInstance] fast_metrics_config_get()

Collection Query

Query fast metrics config instances for entities. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FastMetricsConfigApi()

try:
    # Collection Query
    api_response = api_instance.fast_metrics_config_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FastMetricsConfigApi->fast_metrics_config_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FastMetricsConfigInstance]**](FastMetricsConfigInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fast_metrics_config_id_delete**
> fast_metrics_config_id_delete(id)

Delete

Delete a fast_metrics_config instance. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FastMetricsConfigApi()
id = 'id_example' # str | Unique identifier of the fast_metrics_config instance to delete.

try:
    # Delete
    api_instance.fast_metrics_config_id_delete(id)
except ApiException as e:
    print("Exception when calling FastMetricsConfigApi->fast_metrics_config_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the fast_metrics_config instance to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fast_metrics_config_id_get**
> FastMetricsConfigInstance fast_metrics_config_id_get(id)

Instance Query

Query a specific fast_metrics_config instance. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FastMetricsConfigApi()
id = 'id_example' # str | Unique identifier of the fast_metrics_config instance to query.

try:
    # Instance Query
    api_response = api_instance.fast_metrics_config_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FastMetricsConfigApi->fast_metrics_config_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the fast_metrics_config instance to query. | 

### Return type

[**FastMetricsConfigInstance**](FastMetricsConfigInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fast_metrics_config_post**
> CreateResponse fast_metrics_config_post(body)

Create

Configure fast metrics for an entity. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FastMetricsConfigApi()
body = prime.swagger_client.FastMetricsConfigCreate() # FastMetricsConfigCreate | 

try:
    # Create
    api_response = api_instance.fast_metrics_config_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FastMetricsConfigApi->fast_metrics_config_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FastMetricsConfigCreate**](FastMetricsConfigCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

