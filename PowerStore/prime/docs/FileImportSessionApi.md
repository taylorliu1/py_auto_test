# prime.swagger_client.FileImportSessionApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_import_session_get**](FileImportSessionApi.md#file_import_session_get) | **GET** /file_import_session | Collection Query
[**file_import_session_id_cancel_post**](FileImportSessionApi.md#file_import_session_id_cancel_post) | **POST** /file_import_session/{id}/cancel | Cancel
[**file_import_session_id_commit_post**](FileImportSessionApi.md#file_import_session_id_commit_post) | **POST** /file_import_session/{id}/commit | Cancel
[**file_import_session_id_cutover_post**](FileImportSessionApi.md#file_import_session_id_cutover_post) | **POST** /file_import_session/{id}/cutover | Cutover
[**file_import_session_id_delete**](FileImportSessionApi.md#file_import_session_id_delete) | **DELETE** /file_import_session/{id} | Delete
[**file_import_session_id_destination_objects_sync_post**](FileImportSessionApi.md#file_import_session_id_destination_objects_sync_post) | **POST** /file_import_session/{id}/destination_objects_sync | Sync
[**file_import_session_id_get**](FileImportSessionApi.md#file_import_session_id_get) | **GET** /file_import_session/{id} | Instance Query
[**file_import_session_id_patch**](FileImportSessionApi.md#file_import_session_id_patch) | **PATCH** /file_import_session/{id} | Modify
[**file_import_session_id_pause_post**](FileImportSessionApi.md#file_import_session_id_pause_post) | **POST** /file_import_session/{id}/pause | Pause
[**file_import_session_id_resume_post**](FileImportSessionApi.md#file_import_session_id_resume_post) | **POST** /file_import_session/{id}/resume | Resume
[**file_import_session_post**](FileImportSessionApi.md#file_import_session_post) | **POST** /file_import_session | Create


# **file_import_session_get**
> list[FileImportSessionInstance] file_import_session_get()

Collection Query

Query of the File Import Session. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileImportSessionApi()

try:
    # Collection Query
    api_response = api_instance.file_import_session_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileImportSessionApi->file_import_session_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileImportSessionInstance]**](FileImportSessionInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_import_session_id_cancel_post**
> file_import_session_id_cancel_post(id, body=body)

Cancel

Cancel an ongoing file import session. The action can be performed at any state of the file import session except in the 'Completed', 'Cancelling' and 'Cancelled' states. Any other ongoing operation on the file import session is terminated immediately. If it happens during/after 'Cutting_Over' state, clients are switched back to the source system (may be disruptive). The source system is cleaned up, the destination NAS server and all imported objects including filesystems are deleted. When cancel is complete the state of the file import session is changed to 'Completed' which is a terminal state. Cancel can be forced if the source system is unresponsive. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileImportSessionApi()
id = 'id_example' # str | Unique identifier of the file import session name:{name} can be used instead of {id}.
body = prime.swagger_client.FileImportSessionCancel() # FileImportSessionCancel |  (optional)

try:
    # Cancel
    api_instance.file_import_session_id_cancel_post(id, body=body)
except ApiException as e:
    print("Exception when calling FileImportSessionApi->file_import_session_id_cancel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file import session name:{name} can be used instead of {id}. | 
 **body** | [**FileImportSessionCancel**](FileImportSessionCancel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_import_session_id_commit_post**
> file_import_session_id_commit_post(id, body=body)

Cancel

Commit a file import session to complete the import. The operation is valid only during 'Ready_For_Commit', when all filesystem data has been synchronized with the source. During commit, the data connection between the source and the destination import file interface is dropped, and the sync of write data to the source system is stopped.     The destination system becomes independent and the source system is cleaned up. When commit is complete the state of the file import session is changed to 'Completed'.     Commit can be forced if the source system becomes unresponsive. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileImportSessionApi()
id = 'id_example' # str | Unique identifier of the file import session. name:{name} can be used instead of {id}.
body = prime.swagger_client.FileImportSessionCommit() # FileImportSessionCommit |  (optional)

try:
    # Cancel
    api_instance.file_import_session_id_commit_post(id, body=body)
except ApiException as e:
    print("Exception when calling FileImportSessionApi->file_import_session_id_commit_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file import session. name:{name} can be used instead of {id}. | 
 **body** | [**FileImportSessionCommit**](FileImportSessionCommit.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_import_session_id_cutover_post**
> file_import_session_id_cutover_post(id, body=body)

Cutover

Cutover a file import session that is during 'Ready_For_Cutover'. Cutover may cause a temporary data unavailability to the NAS clients. During cutover the production file interfaces are disabled on the source system and are enabled on the destination system. In case of SMB import, the switchover is disruptive for the clients and the Active Directory configuration is imported if needed. In case of NFS import, the switchover is transparent as file handles are preserved, NLM locks are reclaimed on the destination. The incremental background data copy operation begins after the cutover completes. The filesystem data is moved to the destination in the background. The destination system serves the clients; data requested by the client is synced immediately; write operations are synced back to the source system before acknowledging, so the source remains authoritative and a rollback is possible at any moment. I/O throughput is degraded at this stage. The service is interrupted if the source data becomes unavailable. When all files are synced, the status of the file import session is changedtransitions to 'Ready_For_Commit'. If cutover operation fails, a rollback is attempted and clients are switched back to the source system (may be disruptive). If it succeeds, the stateoperation becomes 'Ready_For_Cutover' again and the operationcutover can be retried. If it fails, the file import session cleans up the destination resources of the import and enters the 'Failed' state. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileImportSessionApi()
id = 'id_example' # str | Unique identifier of the file import session name:{name} can be used instead of {id}.
body = prime.swagger_client.FileImportSessionCutover() # FileImportSessionCutover |  (optional)

try:
    # Cutover
    api_instance.file_import_session_id_cutover_post(id, body=body)
except ApiException as e:
    print("Exception when calling FileImportSessionApi->file_import_session_id_cutover_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file import session name:{name} can be used instead of {id}. | 
 **body** | [**FileImportSessionCutover**](FileImportSessionCutover.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_import_session_id_delete**
> file_import_session_id_delete(id)

Delete

Delete an File import session. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileImportSessionApi()
id = 'id_example' # str | Unique identifier of the File import session. name:{name} can be used instead of {id}.

try:
    # Delete
    api_instance.file_import_session_id_delete(id)
except ApiException as e:
    print("Exception when calling FileImportSessionApi->file_import_session_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the File import session. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_import_session_id_destination_objects_sync_post**
> file_import_session_id_destination_objects_sync_post(id)

Sync

Synchronize new NAS objects created on SDNAS due to file import session into Trident CP DB. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileImportSessionApi()
id = 'id_example' # str | Unique identifier of the file import session. name:{name} can be used instead of {id}.

try:
    # Sync
    api_instance.file_import_session_id_destination_objects_sync_post(id)
except ApiException as e:
    print("Exception when calling FileImportSessionApi->file_import_session_id_destination_objects_sync_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file import session. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_import_session_id_get**
> FileImportSessionInstance file_import_session_id_get(id)

Instance Query

 Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileImportSessionApi()
id = 'id_example' # str | Unique identifier of the file import session. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.file_import_session_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileImportSessionApi->file_import_session_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file import session. name:{name} can be used instead of {id}. | 

### Return type

[**FileImportSessionInstance**](FileImportSessionInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_import_session_id_patch**
> file_import_session_id_patch(id, body)

Modify

Modify the properties of the file import session. The new SMB administrator credentials are validated if the destination NAS Server and the destination import file interface have already been created. The new credentials become effective immediately. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileImportSessionApi()
id = 'id_example' # str | Unique identifier of the file import session. name:{name} can be used instead of {id}.
body = prime.swagger_client.FileImportSessionModify() # FileImportSessionModify | 

try:
    # Modify
    api_instance.file_import_session_id_patch(id, body)
except ApiException as e:
    print("Exception when calling FileImportSessionApi->file_import_session_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file import session. name:{name} can be used instead of {id}. | 
 **body** | [**FileImportSessionModify**](FileImportSessionModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_import_session_id_pause_post**
> file_import_session_id_pause_post(id)

Pause

Pause an ongoing file import session during 'Initial_Copy' or 'Incremental_Copy' operations. When this occurs, the background data transfer stops, but I/O to the source continues if the file import session during 'Incremental_Copy'. A paused import session can be resumed or cancelled. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileImportSessionApi()
id = 'id_example' # str | Unique identifier of the file import session. name:{name} can be used instead of {id}.

try:
    # Pause
    api_instance.file_import_session_id_pause_post(id)
except ApiException as e:
    print("Exception when calling FileImportSessionApi->file_import_session_id_pause_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file import session. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_import_session_id_resume_post**
> file_import_session_id_resume_post(id)

Resume

Resumes a file import session in 'Paused' state. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileImportSessionApi()
id = 'id_example' # str | Unique identifier of the file import session. name:{name} can be used instead of {id}.

try:
    # Resume
    api_instance.file_import_session_id_resume_post(id)
except ApiException as e:
    print("Exception when calling FileImportSessionApi->file_import_session_id_resume_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file import session. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_import_session_post**
> CreateResponse file_import_session_post(body)

Create

Create a new file import session to import the source file/NAS server discovered via the source file import storage system. The source storage system must be added prior to creating a file import session. The basic configuration (NAS server name, filesystems, production interfaces) of the source file server must not change after the file import session is created. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileImportSessionApi()
body = prime.swagger_client.FileImportSessionCreate() # FileImportSessionCreate | 

try:
    # Create
    api_response = api_instance.file_import_session_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileImportSessionApi->file_import_session_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileImportSessionCreate**](FileImportSessionCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

