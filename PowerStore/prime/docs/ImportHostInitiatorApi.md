# prime.swagger_client.ImportHostInitiatorApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_host_initiator_get**](ImportHostInitiatorApi.md#import_host_initiator_get) | **GET** /import_host_initiator | Collection Query
[**import_host_initiator_id_get**](ImportHostInitiatorApi.md#import_host_initiator_id_get) | **GET** /import_host_initiator/{id} | Instance Query


# **import_host_initiator_get**
> list[ImportHostInitiatorInstance] import_host_initiator_get()

Collection Query

Query import host initiators.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportHostInitiatorApi()

try:
    # Collection Query
    api_response = api_instance.import_host_initiator_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportHostInitiatorApi->import_host_initiator_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ImportHostInitiatorInstance]**](ImportHostInitiatorInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_host_initiator_id_get**
> ImportHostInitiatorInstance import_host_initiator_id_get(id)

Instance Query

Query a specific import host initiator instance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportHostInitiatorApi()
id = 'id_example' # str | Unique identifier of the import host initiator to query.

try:
    # Instance Query
    api_response = api_instance.import_host_initiator_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportHostInitiatorApi->import_host_initiator_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the import host initiator to query. | 

### Return type

[**ImportHostInitiatorInstance**](ImportHostInitiatorInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

