# prime.swagger_client.IpPoolAddressApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ip_pool_address_get**](IpPoolAddressApi.md#ip_pool_address_get) | **GET** /ip_pool_address | Collection Query
[**ip_pool_address_id_get**](IpPoolAddressApi.md#ip_pool_address_id_get) | **GET** /ip_pool_address/{id} | Instance Query


# **ip_pool_address_get**
> list[IpPoolAddressInstance] ip_pool_address_get()

Collection Query

Query configured IP addresses.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.IpPoolAddressApi()

try:
    # Collection Query
    api_response = api_instance.ip_pool_address_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpPoolAddressApi->ip_pool_address_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[IpPoolAddressInstance]**](IpPoolAddressInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_pool_address_id_get**
> IpPoolAddressInstance ip_pool_address_id_get(id)

Instance Query

Query a specific IP address.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.IpPoolAddressApi()
id = 'id_example' # str | Unique identifier of a configured IP address. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.ip_pool_address_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpPoolAddressApi->ip_pool_address_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of a configured IP address. name:{name} can be used instead of {id}. | 

### Return type

[**IpPoolAddressInstance**](IpPoolAddressInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

