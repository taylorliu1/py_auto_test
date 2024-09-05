# prime.swagger_client.FileInterfaceRouteApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_interface_route_get**](FileInterfaceRouteApi.md#file_interface_route_get) | **GET** /file_interface_route | Collection Query
[**file_interface_route_id_delete**](FileInterfaceRouteApi.md#file_interface_route_id_delete) | **DELETE** /file_interface_route/{id} | Delete
[**file_interface_route_id_get**](FileInterfaceRouteApi.md#file_interface_route_id_get) | **GET** /file_interface_route/{id} | Instance Query
[**file_interface_route_id_patch**](FileInterfaceRouteApi.md#file_interface_route_id_patch) | **PATCH** /file_interface_route/{id} | Modify
[**file_interface_route_post**](FileInterfaceRouteApi.md#file_interface_route_post) | **POST** /file_interface_route | Create


# **file_interface_route_get**
> list[FileInterfaceRouteInstance] file_interface_route_get()

Collection Query

Query file interface routes.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileInterfaceRouteApi()

try:
    # Collection Query
    api_response = api_instance.file_interface_route_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileInterfaceRouteApi->file_interface_route_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileInterfaceRouteInstance]**](FileInterfaceRouteInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_interface_route_id_delete**
> file_interface_route_id_delete(id)

Delete

Delete file interface route.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileInterfaceRouteApi()
id = 'id_example' # str | Unique identifier of the file interface route object.

try:
    # Delete
    api_instance.file_interface_route_id_delete(id)
except ApiException as e:
    print("Exception when calling FileInterfaceRouteApi->file_interface_route_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file interface route object. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_interface_route_id_get**
> FileInterfaceRouteInstance file_interface_route_id_get(id)

Instance Query

Query a specific file interface route for details.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileInterfaceRouteApi()
id = 'id_example' # str | Unique identifier of the file interface route object.

try:
    # Instance Query
    api_response = api_instance.file_interface_route_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileInterfaceRouteApi->file_interface_route_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file interface route object. | 

### Return type

[**FileInterfaceRouteInstance**](FileInterfaceRouteInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_interface_route_id_patch**
> file_interface_route_id_patch(id, body)

Modify

Modify file interface route settings.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileInterfaceRouteApi()
id = 'id_example' # str | Unique identifier of the file interface route object.
body = prime.swagger_client.FileInterfaceRouteModify() # FileInterfaceRouteModify | 

try:
    # Modify
    api_instance.file_interface_route_id_patch(id, body)
except ApiException as e:
    print("Exception when calling FileInterfaceRouteApi->file_interface_route_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file interface route object. | 
 **body** | [**FileInterfaceRouteModify**](FileInterfaceRouteModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_interface_route_post**
> CreateResponse file_interface_route_post(body)

Create

Create and configure a new file interface route. There are three types of routes - Subnet, Default, and Host. * A default route establishes a static route to a default gateway. To create a default route, specify gateway value for the related file interface. * A host route establishes a static route to a specific host. To create a host route, provide the IP address of the specific host in the destination field, and the gateway. * A subnet route establishes a static route to a particular subnet. To create a subnet route, provide the IP address of the target subnet in the destination, the prefix length for that subnet, and the gateway. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileInterfaceRouteApi()
body = prime.swagger_client.FileInterfaceRouteCreate() # FileInterfaceRouteCreate | 

try:
    # Create
    api_response = api_instance.file_interface_route_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileInterfaceRouteApi->file_interface_route_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileInterfaceRouteCreate**](FileInterfaceRouteCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

