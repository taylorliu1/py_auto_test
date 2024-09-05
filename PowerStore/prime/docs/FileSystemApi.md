# prime.swagger_client.FileSystemApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_system_get**](FileSystemApi.md#file_system_get) | **GET** /file_system | Collection Query
[**file_system_id_clone_post**](FileSystemApi.md#file_system_id_clone_post) | **POST** /file_system/{id}/clone | Clone
[**file_system_id_delete**](FileSystemApi.md#file_system_id_delete) | **DELETE** /file_system/{id} | Delete
[**file_system_id_get**](FileSystemApi.md#file_system_id_get) | **GET** /file_system/{id} | Instance Query
[**file_system_id_patch**](FileSystemApi.md#file_system_id_patch) | **PATCH** /file_system/{id} | Modify
[**file_system_id_refresh_post**](FileSystemApi.md#file_system_id_refresh_post) | **POST** /file_system/{id}/refresh | Refresh
[**file_system_id_refresh_quota_post**](FileSystemApi.md#file_system_id_refresh_quota_post) | **POST** /file_system/{id}/refresh_quota | Refresh Quota
[**file_system_id_restore_post**](FileSystemApi.md#file_system_id_restore_post) | **POST** /file_system/{id}/restore | Restore
[**file_system_id_snapshot_post**](FileSystemApi.md#file_system_id_snapshot_post) | **POST** /file_system/{id}/snapshot | Snapshot
[**file_system_post**](FileSystemApi.md#file_system_post) | **POST** /file_system | Create


# **file_system_get**
> list[FileSystemInstance] file_system_get()

Collection Query

Query file systems.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileSystemApi()

try:
    # Collection Query
    api_response = api_instance.file_system_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemApi->file_system_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileSystemInstance]**](FileSystemInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_system_id_clone_post**
> FileSystemCloneResponse file_system_id_clone_post(id, body)

Clone

Create a clone of a file system.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileSystemApi()
id = 'id_example' # str | Unique identifier of the file system. name:{name} can be used instead of {id}.
body = prime.swagger_client.FileSystemClone() # FileSystemClone | 

try:
    # Clone
    api_response = api_instance.file_system_id_clone_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemApi->file_system_id_clone_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file system. name:{name} can be used instead of {id}. | 
 **body** | [**FileSystemClone**](FileSystemClone.md)|  | 

### Return type

[**FileSystemCloneResponse**](FileSystemCloneResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_system_id_delete**
> file_system_id_delete(id)

Delete

Delete a file system.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileSystemApi()
id = 'id_example' # str | Unique identifier of the file system. name:{name} can be used instead of {id}.

try:
    # Delete
    api_instance.file_system_id_delete(id)
except ApiException as e:
    print("Exception when calling FileSystemApi->file_system_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file system. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_system_id_get**
> FileSystemInstance file_system_id_get(id)

Instance Query

Query a specific file system.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileSystemApi()
id = 'id_example' # str | Unique identifier of the file system. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.file_system_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemApi->file_system_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file system. name:{name} can be used instead of {id}. | 

### Return type

[**FileSystemInstance**](FileSystemInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_system_id_patch**
> file_system_id_patch(id, body)

Modify

Modify a file system.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileSystemApi()
id = 'id_example' # str | Unique identifier of the file system. name:{name} can be used instead of {id}.
body = prime.swagger_client.FileSystemModify() # FileSystemModify | 

try:
    # Modify
    api_instance.file_system_id_patch(id, body)
except ApiException as e:
    print("Exception when calling FileSystemApi->file_system_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file system. name:{name} can be used instead of {id}. | 
 **body** | [**FileSystemModify**](FileSystemModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_system_id_refresh_post**
> file_system_id_refresh_post(id)

Refresh

Refresh a snapshot of a file system. The content of the snapshot is replaced with the current content of the parent file system.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileSystemApi()
id = 'id_example' # str | Unique identifier of the file system snapshot. name:{name} can be used instead of {id}.

try:
    # Refresh
    api_instance.file_system_id_refresh_post(id)
except ApiException as e:
    print("Exception when calling FileSystemApi->file_system_id_refresh_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file system snapshot. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_system_id_refresh_quota_post**
> file_system_id_refresh_quota_post(id)

Refresh Quota

Refresh the actual content of tree and user quotas objects.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileSystemApi()
id = 'id_example' # str | Unique identifier of the file system. name:{name} can be used instead of {id}.

try:
    # Refresh Quota
    api_instance.file_system_id_refresh_quota_post(id)
except ApiException as e:
    print("Exception when calling FileSystemApi->file_system_id_refresh_quota_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file system. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_system_id_restore_post**
> FileSystemRestoreResponse file_system_id_restore_post(id, body=body)

Restore

Restore from a snapshot of a file system. Success responses indicates the following: * 200 - Success with backup snapshot. * 204 - Success without backup snapshot. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileSystemApi()
id = 'id_example' # str | Unique identifier of the file system snapshot. name:{name} can be used instead of {id}.
body = prime.swagger_client.FileSystemRestore() # FileSystemRestore |  (optional)

try:
    # Restore
    api_response = api_instance.file_system_id_restore_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemApi->file_system_id_restore_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file system snapshot. name:{name} can be used instead of {id}. | 
 **body** | [**FileSystemRestore**](FileSystemRestore.md)|  | [optional] 

### Return type

[**FileSystemRestoreResponse**](FileSystemRestoreResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_system_id_snapshot_post**
> FileSystemSnapshotResponse file_system_id_snapshot_post(id, body=body)

Snapshot

Create a snapshot of a file system.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileSystemApi()
id = 'id_example' # str | Unique identifier of the file system. name:{name} can be used instead of {id}.
body = prime.swagger_client.FileSystemSnapshot() # FileSystemSnapshot |  (optional)

try:
    # Snapshot
    api_response = api_instance.file_system_id_snapshot_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemApi->file_system_id_snapshot_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file system. name:{name} can be used instead of {id}. | 
 **body** | [**FileSystemSnapshot**](FileSystemSnapshot.md)|  | [optional] 

### Return type

[**FileSystemSnapshotResponse**](FileSystemSnapshotResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_system_post**
> CreateResponse file_system_post(body)

Create

Create a file system.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileSystemApi()
body = prime.swagger_client.FileSystemCreate() # FileSystemCreate | 

try:
    # Create
    api_response = api_instance.file_system_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemApi->file_system_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileSystemCreate**](FileSystemCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

