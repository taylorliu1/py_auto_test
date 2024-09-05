# prime.swagger_client.VirtualVolumeApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtual_volume_get**](VirtualVolumeApi.md#virtual_volume_get) | **GET** /virtual_volume | Collection Query
[**virtual_volume_id_delete**](VirtualVolumeApi.md#virtual_volume_id_delete) | **DELETE** /virtual_volume/{id} | Delete
[**virtual_volume_id_get**](VirtualVolumeApi.md#virtual_volume_id_get) | **GET** /virtual_volume/{id} | Instance Query


# **virtual_volume_get**
> list[VirtualVolumeInstance] virtual_volume_get()

Collection Query

Get virtual volumes.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VirtualVolumeApi()

try:
    # Collection Query
    api_response = api_instance.virtual_volume_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualVolumeApi->virtual_volume_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VirtualVolumeInstance]**](VirtualVolumeInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_volume_id_delete**
> virtual_volume_id_delete(id, body=body)

Delete

Delete a virtual volume. Virtual volumes should be managed via vCenter operations in a normal situation. This operation is implemented for unusual cases like manual clean up.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VirtualVolumeApi()
id = 'id_example' # str | Unique identifier of the virtual volume to delete. name:{name} can be used instead of {id}.
body = prime.swagger_client.VirtualVolumeDelete() # VirtualVolumeDelete | Options to delete a virtual volume. (optional)

try:
    # Delete
    api_instance.virtual_volume_id_delete(id, body=body)
except ApiException as e:
    print("Exception when calling VirtualVolumeApi->virtual_volume_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the virtual volume to delete. name:{name} can be used instead of {id}. | 
 **body** | [**VirtualVolumeDelete**](VirtualVolumeDelete.md)| Options to delete a virtual volume. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_volume_id_get**
> VirtualVolumeInstance virtual_volume_id_get(id)

Instance Query

Get a specific virtual volume.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VirtualVolumeApi()
id = 'id_example' # str | Id of the virtual volume. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.virtual_volume_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualVolumeApi->virtual_volume_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the virtual volume. name:{name} can be used instead of {id}. | 

### Return type

[**VirtualVolumeInstance**](VirtualVolumeInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

