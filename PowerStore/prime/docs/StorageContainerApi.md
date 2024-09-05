# prime.swagger_client.StorageContainerApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storage_container_get**](StorageContainerApi.md#storage_container_get) | **GET** /storage_container | Collection Query
[**storage_container_id_delete**](StorageContainerApi.md#storage_container_id_delete) | **DELETE** /storage_container/{id} | Delete
[**storage_container_id_get**](StorageContainerApi.md#storage_container_id_get) | **GET** /storage_container/{id} | Instance Query
[**storage_container_id_mount_post**](StorageContainerApi.md#storage_container_id_mount_post) | **POST** /storage_container/{id}/mount | Mount
[**storage_container_id_patch**](StorageContainerApi.md#storage_container_id_patch) | **PATCH** /storage_container/{id} | Modify
[**storage_container_id_unmount_post**](StorageContainerApi.md#storage_container_id_unmount_post) | **POST** /storage_container/{id}/unmount | Unmount
[**storage_container_post**](StorageContainerApi.md#storage_container_post) | **POST** /storage_container | Create


# **storage_container_get**
> list[StorageContainerInstance] storage_container_get()

Collection Query

List storage containers.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.StorageContainerApi()

try:
    # Collection Query
    api_response = api_instance.storage_container_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageContainerApi->storage_container_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[StorageContainerInstance]**](StorageContainerInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_container_id_delete**
> storage_container_id_delete(id, body=body)

Delete

Delete a storage container.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.StorageContainerApi()
id = 'id_example' # str | Storage container ID. name:{name} can be used instead of {id}.
body = prime.swagger_client.StorageContainerDelete() # StorageContainerDelete | Options to delete storage_container. (optional)

try:
    # Delete
    api_instance.storage_container_id_delete(id, body=body)
except ApiException as e:
    print("Exception when calling StorageContainerApi->storage_container_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Storage container ID. name:{name} can be used instead of {id}. | 
 **body** | [**StorageContainerDelete**](StorageContainerDelete.md)| Options to delete storage_container. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_container_id_get**
> StorageContainerInstance storage_container_id_get(id)

Instance Query

Query a specific instance of storage container.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.StorageContainerApi()
id = 'id_example' # str | Storage container ID. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.storage_container_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageContainerApi->storage_container_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Storage container ID. name:{name} can be used instead of {id}. | 

### Return type

[**StorageContainerInstance**](StorageContainerInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_container_id_mount_post**
> storage_container_id_mount_post(id, body=body)

Mount

Mount a storage container as a vVol datastore in vCenter.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.StorageContainerApi()
id = 'id_example' # str | Storage container ID. name:{name} can be used instead of {id}.
body = prime.swagger_client.StorageContainerMount() # StorageContainerMount |  (optional)

try:
    # Mount
    api_instance.storage_container_id_mount_post(id, body=body)
except ApiException as e:
    print("Exception when calling StorageContainerApi->storage_container_id_mount_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Storage container ID. name:{name} can be used instead of {id}. | 
 **body** | [**StorageContainerMount**](StorageContainerMount.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_container_id_patch**
> storage_container_id_patch(id, body)

Modify

Modify a storage container.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.StorageContainerApi()
id = 'id_example' # str | Storage container ID. name:{name} can be used instead of {id}.
body = prime.swagger_client.StorageContainerModify() # StorageContainerModify | Fields to update.

try:
    # Modify
    api_instance.storage_container_id_patch(id, body)
except ApiException as e:
    print("Exception when calling StorageContainerApi->storage_container_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Storage container ID. name:{name} can be used instead of {id}. | 
 **body** | [**StorageContainerModify**](StorageContainerModify.md)| Fields to update. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_container_id_unmount_post**
> storage_container_id_unmount_post(id)

Unmount

Unmount a storage container, which removes the vVol datastore from vCenter.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.StorageContainerApi()
id = 'id_example' # str | Storage container ID. name:{name} can be used instead of {id}.

try:
    # Unmount
    api_instance.storage_container_id_unmount_post(id)
except ApiException as e:
    print("Exception when calling StorageContainerApi->storage_container_id_unmount_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Storage container ID. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_container_post**
> CreateResponse storage_container_post(body)

Create

Create a virtual volume (vVol) storage container.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.StorageContainerApi()
body = prime.swagger_client.StorageContainerCreate() # StorageContainerCreate | 

try:
    # Create
    api_response = api_instance.storage_container_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageContainerApi->storage_container_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StorageContainerCreate**](StorageContainerCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

