# prime.swagger_client.ImportVmaxApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_vmax_get**](ImportVmaxApi.md#import_vmax_get) | **GET** /import_vmax | Collection Query
[**import_vmax_id_get**](ImportVmaxApi.md#import_vmax_id_get) | **GET** /import_vmax/{id} | Instance Query


# **import_vmax_get**
> list[ImportVmaxInstance] import_vmax_get()

Collection Query

Query VMAX storage systems. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportVmaxApi()

try:
    # Collection Query
    api_response = api_instance.import_vmax_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportVmaxApi->import_vmax_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ImportVmaxInstance]**](ImportVmaxInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_vmax_id_get**
> ImportVmaxInstance import_vmax_id_get(id)

Instance Query

Query a specific VMAX storage system. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportVmaxApi()
id = 'id_example' # str | Unique identifier of the VMAX storage system.

try:
    # Instance Query
    api_response = api_instance.import_vmax_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportVmaxApi->import_vmax_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the VMAX storage system. | 

### Return type

[**ImportVmaxInstance**](ImportVmaxInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

