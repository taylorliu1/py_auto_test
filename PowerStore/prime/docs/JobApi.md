# prime.swagger_client.JobApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**job_get**](JobApi.md#job_get) | **GET** /job | Collection query
[**job_id_get**](JobApi.md#job_id_get) | **GET** /job/{id} | Instance query


# **job_get**
> list[JobInstance] job_get()

Collection query

Query jobs.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.JobApi()

try:
    # Collection query
    api_response = api_instance.job_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->job_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[JobInstance]**](JobInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_id_get**
> JobInstance job_id_get(id)

Instance query

Query a specific job.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.JobApi()
id = 'id_example' # str | Unique id of the job.

try:
    # Instance query
    api_response = api_instance.job_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->job_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique id of the job. | 

### Return type

[**JobInstance**](JobInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

