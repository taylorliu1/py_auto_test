# prime.swagger_client.HostVirtualVolumeMappingApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_virtual_volume_mapping_get**](HostVirtualVolumeMappingApi.md#host_virtual_volume_mapping_get) | **GET** /host_virtual_volume_mapping | Collection Query
[**host_virtual_volume_mapping_id_get**](HostVirtualVolumeMappingApi.md#host_virtual_volume_mapping_id_get) | **GET** /host_virtual_volume_mapping/{id} | Instance Query


# **host_virtual_volume_mapping_get**
> list[HostVirtualVolumeMappingInstance] host_virtual_volume_mapping_get()

Collection Query

Query associations between a virtual volume and the host(s) it is attached to.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.HostVirtualVolumeMappingApi()

try:
    # Collection Query
    api_response = api_instance.host_virtual_volume_mapping_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostVirtualVolumeMappingApi->host_virtual_volume_mapping_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[HostVirtualVolumeMappingInstance]**](HostVirtualVolumeMappingInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_virtual_volume_mapping_id_get**
> HostVirtualVolumeMappingInstance host_virtual_volume_mapping_id_get(id)

Instance Query

Query a specific virtual volume mapping.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.HostVirtualVolumeMappingApi()
id = 'id_example' # str | Unique identifier of the virtual volume mapping.

try:
    # Instance Query
    api_response = api_instance.host_virtual_volume_mapping_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostVirtualVolumeMappingApi->host_virtual_volume_mapping_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the virtual volume mapping. | 

### Return type

[**HostVirtualVolumeMappingInstance**](HostVirtualVolumeMappingInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

