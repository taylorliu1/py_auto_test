# prime.swagger_client.ImportSessionApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_session_get**](ImportSessionApi.md#import_session_get) | **GET** /import_session | Collection Query
[**import_session_id_cancel_post**](ImportSessionApi.md#import_session_id_cancel_post) | **POST** /import_session/{id}/cancel | Cancel
[**import_session_id_cleanup_post**](ImportSessionApi.md#import_session_id_cleanup_post) | **POST** /import_session/{id}/cleanup | Cleanup
[**import_session_id_cutover_post**](ImportSessionApi.md#import_session_id_cutover_post) | **POST** /import_session/{id}/cutover | Cutover
[**import_session_id_delete**](ImportSessionApi.md#import_session_id_delete) | **DELETE** /import_session/{id} | Delete
[**import_session_id_enable_destination_volume_post**](ImportSessionApi.md#import_session_id_enable_destination_volume_post) | **POST** /import_session/{id}/enable_destination_volume | Enable import destination volume
[**import_session_id_get**](ImportSessionApi.md#import_session_id_get) | **GET** /import_session/{id} | Instance Query
[**import_session_id_patch**](ImportSessionApi.md#import_session_id_patch) | **PATCH** /import_session/{id} | Modify
[**import_session_id_pause_post**](ImportSessionApi.md#import_session_id_pause_post) | **POST** /import_session/{id}/pause | Pause
[**import_session_id_resume_post**](ImportSessionApi.md#import_session_id_resume_post) | **POST** /import_session/{id}/resume | Resume
[**import_session_id_start_copy_post**](ImportSessionApi.md#import_session_id_start_copy_post) | **POST** /import_session/{id}/start_copy | Start Copy
[**import_session_post**](ImportSessionApi.md#import_session_post) | **POST** /import_session | Create


# **import_session_get**
> list[ImportSessionInstance] import_session_get()

Collection Query

Query import sessions.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportSessionApi()

try:
    # Collection Query
    api_response = api_instance.import_session_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportSessionApi->import_session_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ImportSessionInstance]**](ImportSessionInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_session_id_cancel_post**
> import_session_id_cancel_post(id, body=body)

Cancel

Cancel an active import session. Cancel is allowed when the import is in a Scheduled, Queued, Copy_In_Progress, or Ready_For_Cutover state. After a successful cancellation, the host is mapped to original source volume, all paths are cleaned up, and the import state is Cancelled. The import can be attempted again in the future. In most cases, the Cancel operation gracefully rolls back the import based on the source and host error responses. Use the force option to stop the import job irrespective of whether the storage system or hosts have issues. When the force option is true, the import process tries to reach out to the source and host to gracefully terminate the import. If either are not reachable or if the request fails, the import is terminated without rolling back.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportSessionApi()
id = 'id_example' # str | Unique identifier of the import session name:{name} can be used instead of {id}.
body = prime.swagger_client.ImportSessionCancel() # ImportSessionCancel |  (optional)

try:
    # Cancel
    api_instance.import_session_id_cancel_post(id, body=body)
except ApiException as e:
    print("Exception when calling ImportSessionApi->import_session_id_cancel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the import session name:{name} can be used instead of {id}. | 
 **body** | [**ImportSessionCancel**](ImportSessionCancel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_session_id_cleanup_post**
> import_session_id_cleanup_post(id)

Cleanup

Clean up an import session that is in Cleanup_Required state and requires user intervention to revert the source volume to its pre-import state as part of the recovery procedure to restore host IO operations.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportSessionApi()
id = 'id_example' # str | Unique identifier of the import session. name:{name} can be used instead of {id}.

try:
    # Cleanup
    api_instance.import_session_id_cleanup_post(id)
except ApiException as e:
    print("Exception when calling ImportSessionApi->import_session_id_cleanup_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the import session. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_session_id_cutover_post**
> import_session_id_cutover_post(id)

Cutover

Commit an import session that is in a Ready_For_Cutover state. When the import session is created with the automatic_cutover attribute set to false, you must use the Cutover operation to complete the import. Until the cutover is complete, PowerStore forwards IO to the source volume to keep it in sync with all host IOs. You can cancel the import during this state if you want to continue using the source volume.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportSessionApi()
id = 'id_example' # str | Unique identifier of an import session name:{name} can be used instead of {id}.

try:
    # Cutover
    api_instance.import_session_id_cutover_post(id)
except ApiException as e:
    print("Exception when calling ImportSessionApi->import_session_id_cutover_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of an import session name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_session_id_delete**
> import_session_id_delete(id)

Delete

Delete an import session that is in a Completed, Failed, or Cancelled state. Delete removes the historical record of the import. To stop active import sessions, use the Cancel operation. You can delete the import session after cancelling it.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportSessionApi()
id = 'id_example' # str | Unique identifier of the import session name:{name} can be used instead of {id}.

try:
    # Delete
    api_instance.import_session_id_delete(id)
except ApiException as e:
    print("Exception when calling ImportSessionApi->import_session_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the import session name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_session_id_enable_destination_volume_post**
> import_session_id_enable_destination_volume_post(id, body=body)

Enable import destination volume

Enable the destination volume of an import session. This action can only be used on an agentless import session that is in the 'Mirror_Enabled' state after the host application using the source volume is brought offline. The host application can be reconfigured to use the destination volume of the import session after enabling the destination volume. To prevent accidental writes to the source volume through the source storage system path due to the incorrect reconfiguration, you can specify the removal of all host mappings of the source volume in the source storage system. Was added in version 1.0.2.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportSessionApi()
id = 'id_example' # str | Unique identifier of the import session. name:{name} can be used instead of {id}.
body = prime.swagger_client.ImportSessionEnableDestinationVolume() # ImportSessionEnableDestinationVolume | Parameters to enable destination volume of an agentless import session. (optional)

try:
    # Enable import destination volume
    api_instance.import_session_id_enable_destination_volume_post(id, body=body)
except ApiException as e:
    print("Exception when calling ImportSessionApi->import_session_id_enable_destination_volume_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the import session. name:{name} can be used instead of {id}. | 
 **body** | [**ImportSessionEnableDestinationVolume**](ImportSessionEnableDestinationVolume.md)| Parameters to enable destination volume of an agentless import session. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_session_id_get**
> ImportSessionInstance import_session_id_get(id)

Instance Query

Query a specific session.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportSessionApi()
id = 'id_example' # str | Unique identifier of the import session name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.import_session_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportSessionApi->import_session_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the import session name:{name} can be used instead of {id}. | 

### Return type

[**ImportSessionInstance**](ImportSessionInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_session_id_patch**
> import_session_id_patch(id, body)

Modify

Modify the scheduled date and time of the specified import session.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportSessionApi()
id = 'id_example' # str | Unique identifier of the import session. name:{name} can be used instead of {id}.
body = prime.swagger_client.ImportSessionModify() # ImportSessionModify | 

try:
    # Modify
    api_instance.import_session_id_patch(id, body)
except ApiException as e:
    print("Exception when calling ImportSessionApi->import_session_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the import session. name:{name} can be used instead of {id}. | 
 **body** | [**ImportSessionModify**](ImportSessionModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_session_id_pause_post**
> import_session_id_pause_post(id)

Pause

Pauses an ongoing import session. When this occurs, the background data copy stops, but IO to the source still occurs. Pause is only supported when the import job is in a in Copy_In_Progress state. You can resume or cancel the paused import.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportSessionApi()
id = 'id_example' # str | Unique identifier of the import session name:{name} can be used instead of {id}.

try:
    # Pause
    api_instance.import_session_id_pause_post(id)
except ApiException as e:
    print("Exception when calling ImportSessionApi->import_session_id_pause_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the import session name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_session_id_resume_post**
> import_session_id_resume_post(id)

Resume

Resumes the paused import session. The background data copy continues from where it was stopped. Resume is only applicable when the import in a Paused state.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportSessionApi()
id = 'id_example' # str | Unique identifier of the import session name:{name} can be used instead of {id}.

try:
    # Resume
    api_instance.import_session_id_resume_post(id)
except ApiException as e:
    print("Exception when calling ImportSessionApi->import_session_id_resume_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the import session name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_session_id_start_copy_post**
> import_session_id_start_copy_post(id)

Start Copy

Start the background data copy operation to import data from the source volume. This action can only be used on an agentless import session that is in the 'Ready_To_Start_Copy' state after the host application is reconfigured and brought online to use the destination volume of the import session. Was added in version 1.0.2.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportSessionApi()
id = 'id_example' # str | Unique identifier of the import session. name:{name} can be used instead of {id}.

try:
    # Start Copy
    api_instance.import_session_id_start_copy_post(id)
except ApiException as e:
    print("Exception when calling ImportSessionApi->import_session_id_start_copy_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the import session. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_session_post**
> CreateResponse import_session_post(body)

Create

Create a new import session. The source storage system and hosts that access the volumes or consistency groups must be added prior to creating an import session. The volumes or consistency groups must be in a migration-ready state.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportSessionApi()
body = prime.swagger_client.ImportSessionCreate() # ImportSessionCreate | 

try:
    # Create
    api_response = api_instance.import_session_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportSessionApi->import_session_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImportSessionCreate**](ImportSessionCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

