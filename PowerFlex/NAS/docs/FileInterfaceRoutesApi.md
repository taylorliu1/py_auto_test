# swagger_client.FileInterfaceRoutesApi

All URIs are relative to *https://10.226.47.34/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_interface_routes_get**](FileInterfaceRoutesApi.md#file_interface_routes_get) | **GET** /file-interface-routes | Collection Query
[**file_interface_routes_id_delete**](FileInterfaceRoutesApi.md#file_interface_routes_id_delete) | **DELETE** /file-interface-routes/{id} | Delete
[**file_interface_routes_id_get**](FileInterfaceRoutesApi.md#file_interface_routes_id_get) | **GET** /file-interface-routes/{id} | Instance Query
[**file_interface_routes_id_patch**](FileInterfaceRoutesApi.md#file_interface_routes_id_patch) | **PATCH** /file-interface-routes/{id} | Modify
[**file_interface_routes_post**](FileInterfaceRoutesApi.md#file_interface_routes_post) | **POST** /file-interface-routes | Create

# **file_interface_routes_get**
> list[FileInterfaceRouteInstance] file_interface_routes_get()

Collection Query

Query file interface routes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileInterfaceRoutesApi()

try:
    # Collection Query
    api_response = api_instance.file_interface_routes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileInterfaceRoutesApi->file_interface_routes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileInterfaceRouteInstance]**](FileInterfaceRouteInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_interface_routes_id_delete**
> file_interface_routes_id_delete(id)

Delete

Delete file interface route.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileInterfaceRoutesApi()
id = 'id_example' # str | Unique identifier of the file interface route object.

try:
    # Delete
    api_instance.file_interface_routes_id_delete(id)
except ApiException as e:
    print("Exception when calling FileInterfaceRoutesApi->file_interface_routes_id_delete: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_interface_routes_id_get**
> FileInterfaceRouteInstance file_interface_routes_id_get(id)

Instance Query

Query a specific file interface route for details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileInterfaceRoutesApi()
id = 'id_example' # str | Unique identifier of the file interface route object.

try:
    # Instance Query
    api_response = api_instance.file_interface_routes_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileInterfaceRoutesApi->file_interface_routes_id_get: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_interface_routes_id_patch**
> file_interface_routes_id_patch(id, body=body)

Modify

Modify file interface route settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileInterfaceRoutesApi()
id = 'id_example' # str | Unique identifier of the file interface route object.
body = swagger_client.FileInterfaceRouteModify() # FileInterfaceRouteModify |  (optional)

try:
    # Modify
    api_instance.file_interface_routes_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling FileInterfaceRoutesApi->file_interface_routes_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file interface route object. | 
 **body** | [**FileInterfaceRouteModify**](FileInterfaceRouteModify.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_interface_routes_post**
> CreateResponse file_interface_routes_post(body)

Create

Create and configure a new file interface route. There are 3 route types Subnet, Default, and Host. * The default route establishes a static route to a default gateway. To create a default route, provide only the default gateway IP address. * The host route establishes a static route to a specific host. To create a host route, provide the IP address of the specific host in the destination field, and the gateway. * The subnet route establishes a static route to a particular subnet. To create a subnet route, provide the IP address of the target subnet in the destination, the prefix length for that subnet, and the gateway. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileInterfaceRoutesApi()
body = swagger_client.FileInterfaceRouteCreate() # FileInterfaceRouteCreate | 

try:
    # Create
    api_response = api_instance.file_interface_routes_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileInterfaceRoutesApi->file_interface_routes_post: %s\n" % e)
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

