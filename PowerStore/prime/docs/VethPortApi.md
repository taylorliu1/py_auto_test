# prime.swagger_client.VethPortApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**veth_port_get**](VethPortApi.md#veth_port_get) | **GET** /veth_port | Collection Query
[**veth_port_id_get**](VethPortApi.md#veth_port_id_get) | **GET** /veth_port/{id} | Instance Query


# **veth_port_get**
> list[VethPortInstance] veth_port_get()

Collection Query

Query virtual Ethernet port configurations.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VethPortApi()

try:
    # Collection Query
    api_response = api_instance.veth_port_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VethPortApi->veth_port_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VethPortInstance]**](VethPortInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **veth_port_id_get**
> VethPortInstance veth_port_id_get(id)

Instance Query

Query a specific virtual Ethernet port configuration.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VethPortApi()
id = 'id_example' # str | Unique identifier of the virtual Ethernet port. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.veth_port_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VethPortApi->veth_port_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the virtual Ethernet port. name:{name} can be used instead of {id}. | 

### Return type

[**VethPortInstance**](VethPortInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

