# prime.swagger_client.IpPortApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ip_port_get**](IpPortApi.md#ip_port_get) | **GET** /ip_port | Collection Query
[**ip_port_id_get**](IpPortApi.md#ip_port_id_get) | **GET** /ip_port/{id} | Instance Query
[**ip_port_id_patch**](IpPortApi.md#ip_port_id_patch) | **PATCH** /ip_port/{id} | Modify


# **ip_port_get**
> list[IpPortInstance] ip_port_get()

Collection Query

Query IP port configurations.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.IpPortApi()

try:
    # Collection Query
    api_response = api_instance.ip_port_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpPortApi->ip_port_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[IpPortInstance]**](IpPortInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_port_id_get**
> IpPortInstance ip_port_id_get(id)

Instance Query

Query a specific IP port configuration.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.IpPortApi()
id = 'id_example' # str | Unique identifier of the IP port.

try:
    # Instance Query
    api_response = api_instance.ip_port_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpPortApi->ip_port_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the IP port. | 

### Return type

[**IpPortInstance**](IpPortInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_port_id_patch**
> ip_port_id_patch(id, body=body)

Modify

Modify IP port parameters.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.IpPortApi()
id = 'id_example' # str | Unique identifier of the IP port.
body = prime.swagger_client.IpPortModify() # IpPortModify |  (optional)

try:
    # Modify
    api_instance.ip_port_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling IpPortApi->ip_port_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the IP port. | 
 **body** | [**IpPortModify**](IpPortModify.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

