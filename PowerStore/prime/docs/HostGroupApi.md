# prime.swagger_client.HostGroupApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**host_group_get**](HostGroupApi.md#host_group_get) | **GET** /host_group | Collection Query
[**host_group_id_attach_post**](HostGroupApi.md#host_group_id_attach_post) | **POST** /host_group/{id}/attach | Attach
[**host_group_id_delete**](HostGroupApi.md#host_group_id_delete) | **DELETE** /host_group/{id} | Delete
[**host_group_id_detach_post**](HostGroupApi.md#host_group_id_detach_post) | **POST** /host_group/{id}/detach | Detach
[**host_group_id_get**](HostGroupApi.md#host_group_id_get) | **GET** /host_group/{id} | Instance Query
[**host_group_id_patch**](HostGroupApi.md#host_group_id_patch) | **PATCH** /host_group/{id} | Modify
[**host_group_post**](HostGroupApi.md#host_group_post) | **POST** /host_group | Create


# **host_group_get**
> list[HostGroupInstance] host_group_get()

Collection Query

Query host groups

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.HostGroupApi()

try:
    # Collection Query
    api_response = api_instance.host_group_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostGroupApi->host_group_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[HostGroupInstance]**](HostGroupInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_group_id_attach_post**
> host_group_id_attach_post(id, body)

Attach

Attach host group to volume.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.HostGroupApi()
id = 'id_example' # str | Unique identifier of the host group. name:{name} can be used instead of {id}.
body = prime.swagger_client.HostGroupAttach() # HostGroupAttach | 

try:
    # Attach
    api_instance.host_group_id_attach_post(id, body)
except ApiException as e:
    print("Exception when calling HostGroupApi->host_group_id_attach_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the host group. name:{name} can be used instead of {id}. | 
 **body** | [**HostGroupAttach**](HostGroupAttach.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_group_id_delete**
> host_group_id_delete(id)

Delete

Delete a host group. Delete fails if host group is attached to a volume.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.HostGroupApi()
id = 'id_example' # str | Unique identifier of the host group. name:{name} can be used instead of {id}.

try:
    # Delete
    api_instance.host_group_id_delete(id)
except ApiException as e:
    print("Exception when calling HostGroupApi->host_group_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the host group. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_group_id_detach_post**
> host_group_id_detach_post(id, body)

Detach

Detach host group from volume.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.HostGroupApi()
id = 'id_example' # str | Unique identifier of the host group. name:{name} can be used instead of {id}.
body = prime.swagger_client.HostGroupDetach() # HostGroupDetach | 

try:
    # Detach
    api_instance.host_group_id_detach_post(id, body)
except ApiException as e:
    print("Exception when calling HostGroupApi->host_group_id_detach_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the host group. name:{name} can be used instead of {id}. | 
 **body** | [**HostGroupDetach**](HostGroupDetach.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_group_id_get**
> HostGroupInstance host_group_id_get(id)

Instance Query

Get details about a specific host group.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.HostGroupApi()
id = 'id_example' # str | Unique identifier of the host group. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.host_group_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostGroupApi->host_group_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the host group. name:{name} can be used instead of {id}. | 

### Return type

[**HostGroupInstance**](HostGroupInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_group_id_patch**
> host_group_id_patch(id, body)

Modify

Modify a host group. Modify does not support rename and add or modify at the same time. Similar to create, adding additional hosts where the host_connectivity attribute does not match the existing value of the host group will cause the operation to fail. Modifying the host_connectivity attribute will cause all hosts in the host group to take on these same values. The host_connectivity attribute may not be modified when adding or removing hosts from the host group.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.HostGroupApi()
id = 'id_example' # str | Unique identifier of the host group. name:{name} can be used instead of {id}.
body = prime.swagger_client.HostGroupModify() # HostGroupModify | 

try:
    # Modify
    api_instance.host_group_id_patch(id, body)
except ApiException as e:
    print("Exception when calling HostGroupApi->host_group_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the host group. name:{name} can be used instead of {id}. | 
 **body** | [**HostGroupModify**](HostGroupModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_group_post**
> CreateResponse host_group_post(body)

Create

Create a host group. The hosts added to a host group at creation time determine the value of the host_connectivity attribute. If all hosts added during the create operation do not have the same values for this attribute, this operation will fail.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.HostGroupApi()
body = prime.swagger_client.HostGroupCreate() # HostGroupCreate | 

try:
    # Create
    api_response = api_instance.host_group_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostGroupApi->host_group_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostGroupCreate**](HostGroupCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

