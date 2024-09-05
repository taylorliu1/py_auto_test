# prime.swagger_client.NetworkApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**network_get**](NetworkApi.md#network_get) | **GET** /network | Collection Query
[**network_id_delete**](NetworkApi.md#network_id_delete) | **DELETE** /network/{id} | Delete
[**network_id_get**](NetworkApi.md#network_id_get) | **GET** /network/{id} | Instance Query
[**network_id_patch**](NetworkApi.md#network_id_patch) | **PATCH** /network/{id} | Modify
[**network_id_scale_post**](NetworkApi.md#network_id_scale_post) | **POST** /network/{id}/scale | Add or remove IP ports
[**network_post**](NetworkApi.md#network_post) | **POST** /network | Create
[**replace**](NetworkApi.md#replace) | **POST** /network/{id}/replace | Reconfigure cluster management network settings from IPv4 to IPv6 or vice versa.


# **network_get**
> list[NetworkInstance] network_get()

Collection Query

Query the IP network configurations of the cluster.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NetworkApi()

try:
    # Collection Query
    api_response = api_instance.network_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->network_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NetworkInstance]**](NetworkInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_id_delete**
> network_id_delete(id)

Delete

Delete network. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NetworkApi()
id = 'id_example' # str | Unique identifier of the network. name:{name} can be used instead of {id}.

try:
    # Delete
    api_instance.network_id_delete(id)
except ApiException as e:
    print("Exception when calling NetworkApi->network_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the network. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_id_get**
> NetworkInstance network_id_get(id)

Instance Query

Query a specific IP network configuration.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NetworkApi()
id = 'id_example' # str | Unique identifier of the IP network. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.network_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->network_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the IP network. name:{name} can be used instead of {id}. | 

### Return type

[**NetworkInstance**](NetworkInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_id_patch**
> network_id_patch(id, body=body)

Modify

Modify IP network parameters, such as gateways, netmasks, VLAN identifiers, and IP addresses. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NetworkApi()
id = 'id_example' # str | Unique identifier of the IP network. name:{name} can be used instead of {id}.
body = prime.swagger_client.NetworkModify() # NetworkModify |  (optional)

try:
    # Modify
    api_instance.network_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling NetworkApi->network_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the IP network. name:{name} can be used instead of {id}. | 
 **body** | [**NetworkModify**](NetworkModify.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_id_scale_post**
> network_id_scale_post(id, body=body)

Add or remove IP ports

* Add IP ports for use by the storage network, or remove IP ports so they can no longer be used. * At least one IP port must be configured for use by the storage network. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NetworkApi()
id = 'id_example' # str | Unique identifier of the IP network. name:{name} can be used instead of {id}.
body = prime.swagger_client.NetworkScale() # NetworkScale |  (optional)

try:
    # Add or remove IP ports
    api_instance.network_id_scale_post(id, body=body)
except ApiException as e:
    print("Exception when calling NetworkApi->network_id_scale_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the IP network. name:{name} can be used instead of {id}. | 
 **body** | [**NetworkScale**](NetworkScale.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_post**
> CreateResponse network_post(body)

Create

Create a network. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NetworkApi()
body = prime.swagger_client.NetworkCreate() # NetworkCreate | 

try:
    # Create
    api_response = api_instance.network_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->network_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NetworkCreate**](NetworkCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace**
> replace(id, body)

Reconfigure cluster management network settings from IPv4 to IPv6 or vice versa.

Reconfigure cluster management network settings from IPv4 to IPv6 or vice versa.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NetworkApi()
id = 'id_example' # str | Unique identifier of the IP network. name:{name} can be used instead of {id}.
body = prime.swagger_client.NetworkReplace() # NetworkReplace | 

try:
    # Reconfigure cluster management network settings from IPv4 to IPv6 or vice versa.
    api_instance.replace(id, body)
except ApiException as e:
    print("Exception when calling NetworkApi->replace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the IP network. name:{name} can be used instead of {id}. | 
 **body** | [**NetworkReplace**](NetworkReplace.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

