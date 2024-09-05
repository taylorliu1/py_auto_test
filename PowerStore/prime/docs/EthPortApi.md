# prime.swagger_client.EthPortApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eth_port_get**](EthPortApi.md#eth_port_get) | **GET** /eth_port | Collection Query
[**eth_port_id_get**](EthPortApi.md#eth_port_id_get) | **GET** /eth_port/{id} | Instance Query
[**eth_port_id_patch**](EthPortApi.md#eth_port_id_patch) | **PATCH** /eth_port/{id} | Modify


# **eth_port_get**
> list[EthPortInstance] eth_port_get()

Collection Query

Get Ethernet front-end port configuration for all cluster nodes.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.EthPortApi()

try:
    # Collection Query
    api_response = api_instance.eth_port_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EthPortApi->eth_port_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EthPortInstance]**](EthPortInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **eth_port_id_get**
> EthPortInstance eth_port_id_get(id)

Instance Query

Get Ethernet front-end port configuration by instance identifier.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.EthPortApi()
id = 'id_example' # str | Ethernet front-end port instance identifier. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.eth_port_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EthPortApi->eth_port_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Ethernet front-end port instance identifier. name:{name} can be used instead of {id}. | 

### Return type

[**EthPortInstance**](EthPortInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **eth_port_id_patch**
> eth_port_id_patch(id, body)

Modify

Change the properties of the front-end port. Note that setting the port's requested speed may not cause the port speed to change immediately. In cases where the SFP is not inserted or the port is down the requested speed will be set but the current_speed will still show the old value until the SFP is able to change speed. By default, the partner port speed on the other node in the appliance is set to the same requested speed. If the requested speed is not supported by the partner port it is left unchanged.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.EthPortApi()
id = 'id_example' # str | Unique identifier of the port. name:{name} can be used instead of {id}.
body = prime.swagger_client.EthPortModify() # EthPortModify | 

try:
    # Modify
    api_instance.eth_port_id_patch(id, body)
except ApiException as e:
    print("Exception when calling EthPortApi->eth_port_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the port. name:{name} can be used instead of {id}. | 
 **body** | [**EthPortModify**](EthPortModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

