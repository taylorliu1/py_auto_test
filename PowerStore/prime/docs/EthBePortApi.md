# prime.swagger_client.EthBePortApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eth_be_port_get**](EthBePortApi.md#eth_be_port_get) | **GET** /eth_be_port | Collection Query
[**eth_be_port_id_get**](EthBePortApi.md#eth_be_port_id_get) | **GET** /eth_be_port/{id} | Instance Query


# **eth_be_port_get**
> list[EthBePortInstance] eth_be_port_get()

Collection Query

Query the Ethernet Backend port configuration for cluster nodes. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.EthBePortApi()

try:
    # Collection Query
    api_response = api_instance.eth_be_port_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EthBePortApi->eth_be_port_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EthBePortInstance]**](EthBePortInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **eth_be_port_id_get**
> EthBePortInstance eth_be_port_id_get(id)

Instance Query

Query a specific Ethernet Backend port configuration. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.EthBePortApi()
id = 'id_example' # str | Unique identifier of the Ethernet Backend port. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.eth_be_port_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EthBePortApi->eth_be_port_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the Ethernet Backend port. name:{name} can be used instead of {id}. | 

### Return type

[**EthBePortInstance**](EthBePortInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

