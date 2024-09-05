# prime.swagger_client.VolumeApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**volume_get**](VolumeApi.md#volume_get) | **GET** /volume | Collection Query
[**volume_id_attach_post**](VolumeApi.md#volume_id_attach_post) | **POST** /volume/{id}/attach | Attach
[**volume_id_clone_post**](VolumeApi.md#volume_id_clone_post) | **POST** /volume/{id}/clone | Clone
[**volume_id_configure_metro_post**](VolumeApi.md#volume_id_configure_metro_post) | **POST** /volume/{id}/configure_metro | Configure Metro
[**volume_id_delete**](VolumeApi.md#volume_id_delete) | **DELETE** /volume/{id} | Delete
[**volume_id_detach_post**](VolumeApi.md#volume_id_detach_post) | **POST** /volume/{id}/detach | Detach
[**volume_id_end_metro_post**](VolumeApi.md#volume_id_end_metro_post) | **POST** /volume/{id}/end_metro | End Metro Configuration
[**volume_id_get**](VolumeApi.md#volume_id_get) | **GET** /volume/{id} | Instance Query
[**volume_id_patch**](VolumeApi.md#volume_id_patch) | **PATCH** /volume/{id} | Modify
[**volume_id_refresh_post**](VolumeApi.md#volume_id_refresh_post) | **POST** /volume/{id}/refresh | Refresh
[**volume_id_restore_post**](VolumeApi.md#volume_id_restore_post) | **POST** /volume/{id}/restore | Restore
[**volume_id_snapshot_post**](VolumeApi.md#volume_id_snapshot_post) | **POST** /volume/{id}/snapshot | Snapshot
[**volume_post**](VolumeApi.md#volume_post) | **POST** /volume | Create


# **volume_get**
> list[VolumeInstance] volume_get()

Collection Query

Query volumes that are provisioned on the appliance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VolumeApi()

try:
    # Collection Query
    api_response = api_instance.volume_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeApi->volume_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VolumeInstance]**](VolumeInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_id_attach_post**
> volume_id_attach_post(id, body)

Attach

Attach a volume to a host or host group.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VolumeApi()
id = 'id_example' # str | Unique identifier of volume to attach. name:{name} can be used instead of {id}.
body = prime.swagger_client.VolumeAttach() # VolumeAttach | 

try:
    # Attach
    api_instance.volume_id_attach_post(id, body)
except ApiException as e:
    print("Exception when calling VolumeApi->volume_id_attach_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of volume to attach. name:{name} can be used instead of {id}. | 
 **body** | [**VolumeAttach**](VolumeAttach.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_id_clone_post**
> VolumeCloneResponse volume_id_clone_post(id, body=body)

Clone

Create a clone of a volume or snapshot.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VolumeApi()
id = 'id_example' # str | Unique identifier of the volume or snapshot to clone. name:{name} can be used instead of {id}.
body = prime.swagger_client.VolumeClone() # VolumeClone |  (optional)

try:
    # Clone
    api_response = api_instance.volume_id_clone_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeApi->volume_id_clone_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the volume or snapshot to clone. name:{name} can be used instead of {id}. | 
 **body** | [**VolumeClone**](VolumeClone.md)|  | [optional] 

### Return type

[**VolumeCloneResponse**](VolumeCloneResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_id_configure_metro_post**
> VolumeConfigureMetroResponse volume_id_configure_metro_post(id, body)

Configure Metro

Configure a metro volume so it exists in two PowerStore clusters. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VolumeApi()
id = 'id_example' # str | Unique identifier of volume to configure. name:{name} can be used instead of {id}.
body = prime.swagger_client.VolumeConfigureMetro() # VolumeConfigureMetro | 

try:
    # Configure Metro
    api_response = api_instance.volume_id_configure_metro_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeApi->volume_id_configure_metro_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of volume to configure. name:{name} can be used instead of {id}. | 
 **body** | [**VolumeConfigureMetro**](VolumeConfigureMetro.md)|  | 

### Return type

[**VolumeConfigureMetroResponse**](VolumeConfigureMetroResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_id_delete**
> volume_id_delete(id)

Delete

Delete a volume.  For a metro volume, first end the metro configuration and then delete the local volume. * A volume which is attached to a host or host group or is a member of a volume group cannot be deleted. * A volume which has protection policies attached to it cannot be deleted. * A volume which has snapshots that are part of a snapset cannot be deleted. * Clones of a deleted production volume or a clone are not deleted. * Snapshots of the volume are deleted along with the volume being deleted.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VolumeApi()
id = 'id_example' # str | Unique identifier of the volume to delete. name:{name} can be used instead of {id}.

try:
    # Delete
    api_instance.volume_id_delete(id)
except ApiException as e:
    print("Exception when calling VolumeApi->volume_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the volume to delete. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_id_detach_post**
> volume_id_detach_post(id, body)

Detach

Detach a volume from a host or host group.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VolumeApi()
id = 'id_example' # str | Unique identifier of volume to detach. name:{name} can be used instead of {id}.
body = prime.swagger_client.VolumeDetach() # VolumeDetach | 

try:
    # Detach
    api_instance.volume_id_detach_post(id, body)
except ApiException as e:
    print("Exception when calling VolumeApi->volume_id_detach_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of volume to detach. name:{name} can be used instead of {id}. | 
 **body** | [**VolumeDetach**](VolumeDetach.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_id_end_metro_post**
> volume_id_end_metro_post(id, body=body)

End Metro Configuration

End a metro configuration from a volume and keep both copies. The local copy will retain its SCSI Identity while the remote volume will get a new SCSI Identity. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VolumeApi()
id = 'id_example' # str | Unique identifier of volume for which to end the metro configuration. name:{name} can be used instead of {id}.
body = prime.swagger_client.VolumeEndMetro() # VolumeEndMetro |  (optional)

try:
    # End Metro Configuration
    api_instance.volume_id_end_metro_post(id, body=body)
except ApiException as e:
    print("Exception when calling VolumeApi->volume_id_end_metro_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of volume for which to end the metro configuration. name:{name} can be used instead of {id}. | 
 **body** | [**VolumeEndMetro**](VolumeEndMetro.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_id_get**
> VolumeInstance volume_id_get(id)

Instance Query

Query a specific volume instance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VolumeApi()
id = 'id_example' # str | Unique identifier of the volume to query. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.volume_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeApi->volume_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the volume to query. name:{name} can be used instead of {id}. | 

### Return type

[**VolumeInstance**](VolumeInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_id_patch**
> volume_id_patch(id, body)

Modify

Modify the parameters of a volume. For metro volumes, name and performance_policy can only be modified from the preferred side when the metro replication session is paused. Volume size of metro volumes can only be modified if the metro replication session is fractured or paused.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VolumeApi()
id = 'id_example' # str | Unique identifier of the volume to modify. name:{name} can be used instead of {id}.
body = prime.swagger_client.VolumeModify() # VolumeModify | 

try:
    # Modify
    api_instance.volume_id_patch(id, body)
except ApiException as e:
    print("Exception when calling VolumeApi->volume_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the volume to modify. name:{name} can be used instead of {id}. | 
 **body** | [**VolumeModify**](VolumeModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_id_refresh_post**
> VolumeRefreshResponse volume_id_refresh_post(id, body)

Refresh

Refresh the contents of the target volume from another volume in the same family. This operation can be run on a metro volume only if the metro replication session is fractured or paused. By default, a backup snapshot of the target volume is created before the target volume is refreshed. To skip creating a backup snapshot, set the __create_backup_snap__ property to false in the refresh request. A profile for the backup snapshot is automatically generated if a custom profile is not specified. An automatically generated profile only contains a system generated unique name for the backup snapshot. When a volume is refreshed, its __source_time__ is set to the __source_time__ of the volume from which it was refreshed.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VolumeApi()
id = 'id_example' # str | Unique identifier of the volume to refresh. name:{name} can be used instead of {id}.
body = prime.swagger_client.VolumeRefresh() # VolumeRefresh | 

try:
    # Refresh
    api_response = api_instance.volume_id_refresh_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeApi->volume_id_refresh_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the volume to refresh. name:{name} can be used instead of {id}. | 
 **body** | [**VolumeRefresh**](VolumeRefresh.md)|  | 

### Return type

[**VolumeRefreshResponse**](VolumeRefreshResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_id_restore_post**
> VolumeRestoreResponse volume_id_restore_post(id, body)

Restore

Restore a primary volume or clone from a snapshot. A primary or clone volume can only be restored from one of its immediate snapshots. This operation can be run on a metro volume only if the metro replication session is fractured or paused. By default, a backup snapshot of the target volume is created before the target volume is restored. To skip creating a backup snapshot, set the __create_backup_snap__ property to false in the restore request. A profile for the backup snapshot is automatically generated if a custom profile is not specified. An automatically generated profile only contains a system generated unique name for the backup snapshot. When a volume is restored, its __source_time__ is set to the __source_time__ of the volume from which it was restored.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VolumeApi()
id = 'id_example' # str | Unique identifier of the volume to restore. name:{name} can be used instead of {id}.
body = prime.swagger_client.VolumeRestore() # VolumeRestore | 

try:
    # Restore
    api_response = api_instance.volume_id_restore_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeApi->volume_id_restore_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the volume to restore. name:{name} can be used instead of {id}. | 
 **body** | [**VolumeRestore**](VolumeRestore.md)|  | 

### Return type

[**VolumeRestoreResponse**](VolumeRestoreResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_id_snapshot_post**
> VolumeSnapshotResponse volume_id_snapshot_post(id, body=body)

Snapshot

Create a snapshot of a volume or a clone. A snapshot is a point-in-time copy of a volume or clone.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VolumeApi()
id = 'id_example' # str | Unique identifier of the volume or clone that is the source of the snapshot. name:{name} can be used instead of {id}.
body = prime.swagger_client.VolumeSnapshot() # VolumeSnapshot |  (optional)

try:
    # Snapshot
    api_response = api_instance.volume_id_snapshot_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeApi->volume_id_snapshot_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the volume or clone that is the source of the snapshot. name:{name} can be used instead of {id}. | 
 **body** | [**VolumeSnapshot**](VolumeSnapshot.md)|  | [optional] 

### Return type

[**VolumeSnapshotResponse**](VolumeSnapshotResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_post**
> CreateResponse volume_post(body)

Create

Create a volume on the appliance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VolumeApi()
body = prime.swagger_client.VolumeCreate() # VolumeCreate | 

try:
    # Create
    api_response = api_instance.volume_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeApi->volume_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VolumeCreate**](VolumeCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

