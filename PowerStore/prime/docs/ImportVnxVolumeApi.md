# prime.swagger_client.ImportVnxVolumeApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_vnx_volume_get**](ImportVnxVolumeApi.md#import_vnx_volume_get) | **GET** /import_vnx_volume | Collection Query
[**import_vnx_volume_id_get**](ImportVnxVolumeApi.md#import_vnx_volume_id_get) | **GET** /import_vnx_volume/{id} | Instance Query


# **import_vnx_volume_get**
> list[ImportVnxVolumeInstance] import_vnx_volume_get()

Collection Query

Query VNX volumes.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportVnxVolumeApi()

try:
    # Collection Query
    api_response = api_instance.import_vnx_volume_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportVnxVolumeApi->import_vnx_volume_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ImportVnxVolumeInstance]**](ImportVnxVolumeInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_vnx_volume_id_get**
> ImportVnxVolumeInstance import_vnx_volume_id_get(id)

Instance Query

Query a specific VNX volume.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportVnxVolumeApi()
id = 'id_example' # str | Unique identifier of the VNX volume. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.import_vnx_volume_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportVnxVolumeApi->import_vnx_volume_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the VNX volume. name:{name} can be used instead of {id}. | 

### Return type

[**ImportVnxVolumeInstance**](ImportVnxVolumeInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

