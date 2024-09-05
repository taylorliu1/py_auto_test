# prime.swagger_client.NodeApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**node_get**](NodeApi.md#node_get) | **GET** /node | Collection Query
[**node_id_get**](NodeApi.md#node_id_get) | **GET** /node/{id} | Instance Query


# **node_get**
> list[NodeInstance] node_get()

Collection Query

Query the nodes in a cluster.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NodeApi()

try:
    # Collection Query
    api_response = api_instance.node_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->node_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NodeInstance]**](NodeInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **node_id_get**
> NodeInstance node_id_get(id)

Instance Query

Query a specific node in a cluster.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NodeApi()
id = 'id_example' # str | Unique identifier of the node.

try:
    # Instance Query
    api_response = api_instance.node_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->node_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the node. | 

### Return type

[**NodeInstance**](NodeInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

