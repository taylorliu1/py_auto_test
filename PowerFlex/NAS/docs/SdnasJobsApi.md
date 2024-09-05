# swagger_client.SdnasJobsApi

All URIs are relative to *https://10.226.47.34/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sdnas_jobs_get**](SdnasJobsApi.md#sdnas_jobs_get) | **GET** /sdnas-jobs | Collection query
[**sdnas_jobs_id_get**](SdnasJobsApi.md#sdnas_jobs_id_get) | **GET** /sdnas-jobs/{id} | Instance query

# **sdnas_jobs_get**
> list[SdnasJobsInstance] sdnas_jobs_get()

Collection query

Query sdnas jobs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SdnasJobsApi()

try:
    # Collection query
    api_response = api_instance.sdnas_jobs_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SdnasJobsApi->sdnas_jobs_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SdnasJobsInstance]**](SdnasJobsInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sdnas_jobs_id_get**
> SdnasJobsInstance sdnas_jobs_id_get(id)

Instance query

Query a specific job.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SdnasJobsApi()
id = 'id_example' # str | Unique id of the sdnas job.

try:
    # Instance query
    api_response = api_instance.sdnas_jobs_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SdnasJobsApi->sdnas_jobs_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique id of the sdnas job. | 

### Return type

[**SdnasJobsInstance**](SdnasJobsInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

