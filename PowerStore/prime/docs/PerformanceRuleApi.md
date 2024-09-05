# prime.swagger_client.PerformanceRuleApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**performance_rule_get**](PerformanceRuleApi.md#performance_rule_get) | **GET** /performance_rule | Collection query
[**performance_rule_id_get**](PerformanceRuleApi.md#performance_rule_id_get) | **GET** /performance_rule/{id} | Instance query


# **performance_rule_get**
> list[PerformanceRuleInstance] performance_rule_get()

Collection query

Get performance rules.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.PerformanceRuleApi()

try:
    # Collection query
    api_response = api_instance.performance_rule_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceRuleApi->performance_rule_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PerformanceRuleInstance]**](PerformanceRuleInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **performance_rule_id_get**
> PerformanceRuleInstance performance_rule_id_get(id)

Instance query

Get a performance rule by id.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.PerformanceRuleApi()
id = 'id_example' # str | Performance Rule id. name:{name} can be used instead of {id}.

try:
    # Instance query
    api_response = api_instance.performance_rule_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceRuleApi->performance_rule_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Performance Rule id. name:{name} can be used instead of {id}. | 

### Return type

[**PerformanceRuleInstance**](PerformanceRuleInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

