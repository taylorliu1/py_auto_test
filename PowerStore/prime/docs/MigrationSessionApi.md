# prime.swagger_client.MigrationSessionApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**migration_session_get**](MigrationSessionApi.md#migration_session_get) | **GET** /migration_session | Collection Query
[**migration_session_id_cutover_post**](MigrationSessionApi.md#migration_session_id_cutover_post) | **POST** /migration_session/{id}/cutover | Cutover
[**migration_session_id_delete**](MigrationSessionApi.md#migration_session_id_delete) | **DELETE** /migration_session/{id} | Delete
[**migration_session_id_get**](MigrationSessionApi.md#migration_session_id_get) | **GET** /migration_session/{id} | Instance Query
[**migration_session_id_pause_post**](MigrationSessionApi.md#migration_session_id_pause_post) | **POST** /migration_session/{id}/pause | Pause
[**migration_session_id_resume_post**](MigrationSessionApi.md#migration_session_id_resume_post) | **POST** /migration_session/{id}/resume | Resume
[**migration_session_id_sync_post**](MigrationSessionApi.md#migration_session_id_sync_post) | **POST** /migration_session/{id}/sync | Sync
[**migration_session_post**](MigrationSessionApi.md#migration_session_post) | **POST** /migration_session | Create


# **migration_session_get**
> list[MigrationSessionInstance] migration_session_get()

Collection Query

Query migration sessions.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.MigrationSessionApi()

try:
    # Collection Query
    api_response = api_instance.migration_session_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MigrationSessionApi->migration_session_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MigrationSessionInstance]**](MigrationSessionInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migration_session_id_cutover_post**
> migration_session_id_cutover_post(id)

Cutover

Final phase of the migration, when ownership of the volume, vVol, or volume group is transferred to the new appliance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.MigrationSessionApi()
id = 'id_example' # str | Unique identifier of the migration session. name:{name} can be used instead of {id}.

try:
    # Cutover
    api_instance.migration_session_id_cutover_post(id)
except ApiException as e:
    print("Exception when calling MigrationSessionApi->migration_session_id_cutover_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the migration session. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migration_session_id_delete**
> migration_session_id_delete(id, body=body)

Delete

Delete a migration session. With the force option, a migration session can be deleted regardless of its state. All background activity is canceled before deleting the session.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.MigrationSessionApi()
id = 'id_example' # str | Unique identifier of the migration session. name:{name} can be used instead of {id}.
body = prime.swagger_client.MigrationSessionDelete() # MigrationSessionDelete | Parameters for a deletion. (optional)

try:
    # Delete
    api_instance.migration_session_id_delete(id, body=body)
except ApiException as e:
    print("Exception when calling MigrationSessionApi->migration_session_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the migration session. name:{name} can be used instead of {id}. | 
 **body** | [**MigrationSessionDelete**](MigrationSessionDelete.md)| Parameters for a deletion. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migration_session_id_get**
> MigrationSessionInstance migration_session_id_get(id)

Instance Query

Query a specific migration session.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.MigrationSessionApi()
id = 'id_example' # str | Unique identifier of the migration session. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.migration_session_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MigrationSessionApi->migration_session_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the migration session. name:{name} can be used instead of {id}. | 

### Return type

[**MigrationSessionInstance**](MigrationSessionInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migration_session_id_pause_post**
> migration_session_id_pause_post(id)

Pause

Pause a migration session. Only migration sessions in the synchronizing state can be paused.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.MigrationSessionApi()
id = 'id_example' # str | Unique identifier of the migration session. name:{name} can be used instead of {id}.

try:
    # Pause
    api_instance.migration_session_id_pause_post(id)
except ApiException as e:
    print("Exception when calling MigrationSessionApi->migration_session_id_pause_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the migration session. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migration_session_id_resume_post**
> migration_session_id_resume_post(id)

Resume

Resume a paused migration session. You cannot resume a migration session in the failed state.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.MigrationSessionApi()
id = 'id_example' # str | Unique identifier of the migration session. name:{name} can be used instead of {id}.

try:
    # Resume
    api_instance.migration_session_id_resume_post(id)
except ApiException as e:
    print("Exception when calling MigrationSessionApi->migration_session_id_resume_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the migration session. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migration_session_id_sync_post**
> migration_session_id_sync_post(id, body)

Sync

Synchronize a migration session. During this phase, the majority of the background copy is completed and there are no interruptions to any services. Sync can be run multiple times to reduce the amount of data that must be copied during the cutover.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.MigrationSessionApi()
id = 'id_example' # str | Unique identifier of the migration session. name:{name} can be used instead of {id}.
body = prime.swagger_client.MigrationSessionSync() # MigrationSessionSync | Parameters for synchronizing a migration session.

try:
    # Sync
    api_instance.migration_session_id_sync_post(id, body)
except ApiException as e:
    print("Exception when calling MigrationSessionApi->migration_session_id_sync_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the migration session. name:{name} can be used instead of {id}. | 
 **body** | [**MigrationSessionSync**](MigrationSessionSync.md)| Parameters for synchronizing a migration session. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migration_session_post**
> MigrationSessionCreateResponse migration_session_post(body)

Create

Create a new migration session. For virtual volumes (vVols), the background copy is completed during this phase and the ownership of the vVol is transferred to the new appliance. For volumes and application groups, a migration session is created in this phase and no background copy is performed until either the sync or cutover operation is invoked. There are no interruptions to any services during this phase.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.MigrationSessionApi()
body = prime.swagger_client.MigrationSessionCreate() # MigrationSessionCreate | Parameters to create a migration session.

try:
    # Create
    api_response = api_instance.migration_session_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MigrationSessionApi->migration_session_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MigrationSessionCreate**](MigrationSessionCreate.md)| Parameters to create a migration session. | 

### Return type

[**MigrationSessionCreateResponse**](MigrationSessionCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

