# prime.swagger_client.VirtualMachineApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtual_machine_get**](VirtualMachineApi.md#virtual_machine_get) | **GET** /virtual_machine | Collection Query
[**virtual_machine_id_delete**](VirtualMachineApi.md#virtual_machine_id_delete) | **DELETE** /virtual_machine/{id} | Delete
[**virtual_machine_id_get**](VirtualMachineApi.md#virtual_machine_id_get) | **GET** /virtual_machine/{id} | Instance Query
[**virtual_machine_id_patch**](VirtualMachineApi.md#virtual_machine_id_patch) | **PATCH** /virtual_machine/{id} | Modify
[**virtual_machine_id_snapshot_post**](VirtualMachineApi.md#virtual_machine_id_snapshot_post) | **POST** /virtual_machine/{id}/snapshot | Snapshot


# **virtual_machine_get**
> list[VirtualMachineInstance] virtual_machine_get()

Collection Query

Query virtual machines that use storage from the cluster.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VirtualMachineApi()

try:
    # Collection Query
    api_response = api_instance.virtual_machine_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachineApi->virtual_machine_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VirtualMachineInstance]**](VirtualMachineInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_id_delete**
> virtual_machine_id_delete(id)

Delete

Delete a virtual machine snapshot. This operation cannot be used on a base virtual machine or virtual machine template.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VirtualMachineApi()
id = 'id_example' # str | Unique identifier of the virtual machine snapshot to delete. name:{name} can be used instead of {id}.

try:
    # Delete
    api_instance.virtual_machine_id_delete(id)
except ApiException as e:
    print("Exception when calling VirtualMachineApi->virtual_machine_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the virtual machine snapshot to delete. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_id_get**
> VirtualMachineInstance virtual_machine_id_get(id)

Instance Query

Query a specific virtual machine instance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VirtualMachineApi()
id = 'id_example' # str | Unique identifier of the virtual machine to query. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.virtual_machine_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachineApi->virtual_machine_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the virtual machine to query. name:{name} can be used instead of {id}. | 

### Return type

[**VirtualMachineInstance**](VirtualMachineInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_id_patch**
> virtual_machine_id_patch(id, body=body)

Modify

Modify a virtual machine. This operation cannot be used on virtual machine snapshots or templates. This method was only used to assign protection policies and deprecated. Use vCenter storage policies instead. Was deprecated in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VirtualMachineApi()
id = 'id_example' # str | Unique identifier of the virtual machine to modify. name:{name} can be used instead of {id}.
body = prime.swagger_client.VirtualMachineModify() # VirtualMachineModify |  (optional)

try:
    # Modify
    api_instance.virtual_machine_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling VirtualMachineApi->virtual_machine_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the virtual machine to modify. name:{name} can be used instead of {id}. | 
 **body** | [**VirtualMachineModify**](VirtualMachineModify.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtual_machine_id_snapshot_post**
> VirtualMachineSnapshotResponse virtual_machine_id_snapshot_post(id, body=body)

Snapshot

Create a snapshot of a virtual machine. This operation cannot be used on a virtual machine snapshot or template.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VirtualMachineApi()
id = 'id_example' # str | Unique identifier of the virtual machine to create a snapshot of. name:{name} can be used instead of {id}.
body = prime.swagger_client.VirtualMachineSnapshot() # VirtualMachineSnapshot |  (optional)

try:
    # Snapshot
    api_response = api_instance.virtual_machine_id_snapshot_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualMachineApi->virtual_machine_id_snapshot_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the virtual machine to create a snapshot of. name:{name} can be used instead of {id}. | 
 **body** | [**VirtualMachineSnapshot**](VirtualMachineSnapshot.md)|  | [optional] 

### Return type

[**VirtualMachineSnapshotResponse**](VirtualMachineSnapshotResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

