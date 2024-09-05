# prime.swagger_client.InitiatorApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**initiator_get**](InitiatorApi.md#initiator_get) | **GET** /initiator | Collection Query
[**initiator_id_get**](InitiatorApi.md#initiator_id_get) | **GET** /initiator/{id} | Instance Query


# **initiator_get**
> list[InitiatorInstance] initiator_get()

Collection Query

List initiator information. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.InitiatorApi()

try:
    # Collection Query
    api_response = api_instance.initiator_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InitiatorApi->initiator_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InitiatorInstance]**](InitiatorInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initiator_id_get**
> InitiatorInstance initiator_id_get(id)

Instance Query

Get details about a specific initiator by id. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.InitiatorApi()
id = 'id_example' # str | Unique id of the initiator.

try:
    # Instance Query
    api_response = api_instance.initiator_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InitiatorApi->initiator_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique id of the initiator. | 

### Return type

[**InitiatorInstance**](InitiatorInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

