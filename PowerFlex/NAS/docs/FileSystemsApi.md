# swagger_client.FileSystemsApi

All URIs are relative to *https://10.226.47.34/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_system_id_clone_post**](FileSystemsApi.md#file_system_id_clone_post) | **POST** /file_system/{id}/clone | Clone
[**file_systems_get**](FileSystemsApi.md#file_systems_get) | **GET** /file-systems | Collection Query
[**file_systems_id_delete**](FileSystemsApi.md#file_systems_id_delete) | **DELETE** /file-systems/{id} | Delete
[**file_systems_id_get**](FileSystemsApi.md#file_systems_id_get) | **GET** /file-systems/{id} | Instance Query
[**file_systems_id_patch**](FileSystemsApi.md#file_systems_id_patch) | **PATCH** /file-systems/{id} | Modify
[**file_systems_id_refresh_post**](FileSystemsApi.md#file_systems_id_refresh_post) | **POST** /file-systems/{id}/refresh | Refresh
[**file_systems_id_refresh_quota_post**](FileSystemsApi.md#file_systems_id_refresh_quota_post) | **POST** /file-systems/{id}/refresh_quota | Refresh Quota
[**file_systems_id_restore_post**](FileSystemsApi.md#file_systems_id_restore_post) | **POST** /file-systems/{id}/restore | Restore
[**file_systems_id_snapshot_post**](FileSystemsApi.md#file_systems_id_snapshot_post) | **POST** /file-systems/{id}/snapshot | Snapshot
[**file_systems_post**](FileSystemsApi.md#file_systems_post) | **POST** /file-systems | Create

# **file_system_id_clone_post**
> FileSystemCloneResponse file_system_id_clone_post(body, id)

Clone

Create a clone of a file system.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileSystemsApi()
body = swagger_client.FileSystemClone() # FileSystemClone | 
id = 'id_example' # str | File system id.

try:
    # Clone
    api_response = api_instance.file_system_id_clone_post(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemsApi->file_system_id_clone_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileSystemClone**](FileSystemClone.md)|  | 
 **id** | **str**| File system id. | 

### Return type

[**FileSystemCloneResponse**](FileSystemCloneResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_systems_get**
> list[FileSystemInstance] file_systems_get()

Collection Query

List file systems.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileSystemsApi()

try:
    # Collection Query
    api_response = api_instance.file_systems_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemsApi->file_systems_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileSystemInstance]**](FileSystemInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_systems_id_delete**
> file_systems_id_delete(id)

Delete

Delete a file system.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileSystemsApi()
id = 'id_example' # str | File system id.

try:
    # Delete
    api_instance.file_systems_id_delete(id)
except ApiException as e:
    print("Exception when calling FileSystemsApi->file_systems_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| File system id. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_systems_id_get**
> FileSystemInstance file_systems_id_get(id)

Instance Query

Query a specific file system.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileSystemsApi()
id = 'id_example' # str | File system id.

try:
    # Instance Query
    api_response = api_instance.file_systems_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemsApi->file_systems_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| File system id. | 

### Return type

[**FileSystemInstance**](FileSystemInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_systems_id_patch**
> file_systems_id_patch(body, id)

Modify

Modify a file system.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileSystemsApi()
body = swagger_client.FileSystemModify() # FileSystemModify | 
id = 'id_example' # str | File system id.

try:
    # Modify
    api_instance.file_systems_id_patch(body, id)
except ApiException as e:
    print("Exception when calling FileSystemsApi->file_systems_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileSystemModify**](FileSystemModify.md)|  | 
 **id** | **str**| File system id. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_systems_id_refresh_post**
> file_systems_id_refresh_post(id)

Refresh

Refresh a snapshot of a file system. The content of the snapshot is replaced with the current content of the parent file system.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileSystemsApi()
id = 'id_example' # str | File system snapshot id.

try:
    # Refresh
    api_instance.file_systems_id_refresh_post(id)
except ApiException as e:
    print("Exception when calling FileSystemsApi->file_systems_id_refresh_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| File system snapshot id. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_systems_id_refresh_quota_post**
> file_systems_id_refresh_quota_post(id)

Refresh Quota

Refresh the actual content of tree and user quotas objects.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileSystemsApi()
id = 'id_example' # str | File system id.

try:
    # Refresh Quota
    api_instance.file_systems_id_refresh_quota_post(id)
except ApiException as e:
    print("Exception when calling FileSystemsApi->file_systems_id_refresh_quota_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| File system id. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_systems_id_restore_post**
> CreateResponse file_systems_id_restore_post(body, id)

Restore

Restore from a snapshot of a file system.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileSystemsApi()
body = swagger_client.FileSystemRestore() # FileSystemRestore | 
id = 'id_example' # str | File system id.

try:
    # Restore
    api_response = api_instance.file_systems_id_restore_post(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemsApi->file_systems_id_restore_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileSystemRestore**](FileSystemRestore.md)|  | 
 **id** | **str**| File system id. | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_systems_id_snapshot_post**
> FileSystemsSnapshotResponse file_systems_id_snapshot_post(id, body=body)

Snapshot

Create a snapshot of a file system.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileSystemsApi()
id = 'id_example' # str | File system id.
body = swagger_client.FileSystemSnapshot() # FileSystemSnapshot |  (optional)

try:
    # Snapshot
    api_response = api_instance.file_systems_id_snapshot_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemsApi->file_systems_id_snapshot_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| File system id. | 
 **body** | [**FileSystemSnapshot**](FileSystemSnapshot.md)|  | [optional] 

### Return type

[**FileSystemsSnapshotResponse**](FileSystemsSnapshotResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_systems_post**
> CreateResponse file_systems_post(body)

Create

Create a file system.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileSystemsApi()
body = swagger_client.FileSystemCreate() # FileSystemCreate | 

try:
    # Create
    api_response = api_instance.file_systems_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemsApi->file_systems_post: %s\n" % e)
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

