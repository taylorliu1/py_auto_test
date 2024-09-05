# prime.swagger_client.ImportNetappApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_netapp_get**](ImportNetappApi.md#import_netapp_get) | **GET** /import_netapp | Collection Query
[**import_netapp_id_get**](ImportNetappApi.md#import_netapp_id_get) | **GET** /import_netapp/{id} | Instance Query


# **import_netapp_get**
> list[ImportNetappInstance] import_netapp_get()

Collection Query

List NetApp storage systems configured for import. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportNetappApi()

try:
    # Collection Query
    api_response = api_instance.import_netapp_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportNetappApi->import_netapp_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ImportNetappInstance]**](ImportNetappInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_netapp_id_get**
> ImportNetappInstance import_netapp_id_get(id)

Instance Query

Query a specific NetApp storage system that is configured for import Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportNetappApi()
id = 'id_example' # str | Unique identifier of the NetApp storage system. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.import_netapp_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportNetappApi->import_netapp_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NetApp storage system. name:{name} can be used instead of {id}. | 

### Return type

[**ImportNetappInstance**](ImportNetappInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

