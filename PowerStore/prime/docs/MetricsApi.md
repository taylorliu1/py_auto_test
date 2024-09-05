# prime.swagger_client.MetricsApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metrics_generate_post**](MetricsApi.md#metrics_generate_post) | **POST** /metrics/generate | Metrics


# **metrics_generate_post**
> list[MetricsGenerateResponse] metrics_generate_post(body)

Metrics

Retrieves metrics for specified type.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.MetricsApi()
body = prime.swagger_client.MetricsGenerate() # MetricsGenerate | 

try:
    # Metrics
    api_response = api_instance.metrics_generate_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->metrics_generate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetricsGenerate**](MetricsGenerate.md)|  | 

### Return type

[**list[MetricsGenerateResponse]**](MetricsGenerateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

