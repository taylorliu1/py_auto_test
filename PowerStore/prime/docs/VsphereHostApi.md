# prime.swagger_client.VsphereHostApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vsphere_host_get**](VsphereHostApi.md#vsphere_host_get) | **GET** /vsphere_host | Collection Query
[**vsphere_host_id_get**](VsphereHostApi.md#vsphere_host_id_get) | **GET** /vsphere_host/{id} | Instance Query


# **vsphere_host_get**
> list[VsphereHostInstance] vsphere_host_get()

Collection Query

Query information about ESXi hosts objects in vCenter Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VsphereHostApi()

try:
    # Collection Query
    api_response = api_instance.vsphere_host_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VsphereHostApi->vsphere_host_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VsphereHostInstance]**](VsphereHostInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vsphere_host_id_get**
> VsphereHostInstance vsphere_host_id_get(id)

Instance Query

Query a specific vsphere_host instance. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VsphereHostApi()
id = 'id_example' # str | Unique identifier of the vsphere_host to query. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.vsphere_host_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VsphereHostApi->vsphere_host_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the vsphere_host to query. name:{name} can be used instead of {id}. | 

### Return type

[**VsphereHostInstance**](VsphereHostInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

