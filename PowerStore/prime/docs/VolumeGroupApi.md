# prime.swagger_client.VolumeGroupApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**volume_group_get**](VolumeGroupApi.md#volume_group_get) | **GET** /volume_group | Collection Query
[**volume_group_id_add_members_post**](VolumeGroupApi.md#volume_group_id_add_members_post) | **POST** /volume_group/{id}/add_members | Add Members
[**volume_group_id_clone_post**](VolumeGroupApi.md#volume_group_id_clone_post) | **POST** /volume_group/{id}/clone | Clone
[**volume_group_id_delete**](VolumeGroupApi.md#volume_group_id_delete) | **DELETE** /volume_group/{id} | Delete
[**volume_group_id_get**](VolumeGroupApi.md#volume_group_id_get) | **GET** /volume_group/{id} | Instance Query
[**volume_group_id_patch**](VolumeGroupApi.md#volume_group_id_patch) | **PATCH** /volume_group/{id} | Modify
[**volume_group_id_refresh_post**](VolumeGroupApi.md#volume_group_id_refresh_post) | **POST** /volume_group/{id}/refresh | Refresh
[**volume_group_id_remove_members_post**](VolumeGroupApi.md#volume_group_id_remove_members_post) | **POST** /volume_group/{id}/remove_members | Remove Members
[**volume_group_id_restore_post**](VolumeGroupApi.md#volume_group_id_restore_post) | **POST** /volume_group/{id}/restore | Restore
[**volume_group_id_snapshot_post**](VolumeGroupApi.md#volume_group_id_snapshot_post) | **POST** /volume_group/{id}/snapshot | Snapshot
[**volume_group_post**](VolumeGroupApi.md#volume_group_post) | **POST** /volume_group | Create


# **volume_group_get**
> list[VolumeGroupInstance] volume_group_get()

Collection Query

Query volume groups, including snapshot sets and clones of volume groups. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VolumeGroupApi()

try:
    # Collection Query
    api_response = api_instance.volume_group_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeGroupApi->volume_group_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VolumeGroupInstance]**](VolumeGroupInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_group_id_add_members_post**
> volume_group_id_add_members_post(id, body)

Add Members

Add member volumes to an existing primary or clone volume group. This cannot be used to add members to a snapshot set. Members cannot be added to a volume group that is acting as the destination in a replication session. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VolumeGroupApi()
id = 'id_example' # str | Unique identifier of the volume group. name:{name} can be used instead of {id}.
body = prime.swagger_client.VolumeGroupAddMembers() # VolumeGroupAddMembers | 

try:
    # Add Members
    api_instance.volume_group_id_add_members_post(id, body)
except ApiException as e:
    print("Exception when calling VolumeGroupApi->volume_group_id_add_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the volume group. name:{name} can be used instead of {id}. | 
 **body** | [**VolumeGroupAddMembers**](VolumeGroupAddMembers.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_group_id_clone_post**
> VolumeGroupCloneResponse volume_group_id_clone_post(id, body)

Clone

Clone a volume group. The clone volume group will be created on the same appliance as the source volume group. A clone of a volume group will result in a new volume group of __Clone__ type. The clone will belong to the same family as the source volume group. When the source of a clone operation is a either primary or clone volume group,  * __source_id__ will be set to the identifier of the source volume group.  * __source_time__ will be set to the time at which the clone will be created.  When the source of a clone operation is a snapshot set,  * __source_id__ will be set to the source_id of the source snapshot set.  * __source_time__ will be set to the source_time of the source snapshot set.  The clone volume group will inherit the value of the __is_write_order_consistent__ property from the source volume group. A clone of a snapshot set is modeled as a clone of the snapshot set's source, created at the same time instant as when the source snapshot set was created. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VolumeGroupApi()
id = 'id_example' # str | Unique identifier of the volume group. name:{name} can be used instead of {id}.
body = prime.swagger_client.VolumeGroupClone() # VolumeGroupClone | 

try:
    # Clone
    api_response = api_instance.volume_group_id_clone_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeGroupApi->volume_group_id_clone_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the volume group. name:{name} can be used instead of {id}. | 
 **body** | [**VolumeGroupClone**](VolumeGroupClone.md)|  | 

### Return type

[**VolumeGroupCloneResponse**](VolumeGroupCloneResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_group_id_delete**
> volume_group_id_delete(id, body=body)

Delete

Delete a volume group, snapshot set, or clone. Before you try deleting a volume group, snapshot set, or clone, ensure that you first detach it from all hosts. Note the following: * When a volume group or clone is deleted, all related snapshot sets will also be deleted. * When a snapshot set is deleted, all of its constituent snapshots will also be deleted. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VolumeGroupApi()
id = 'id_example' # str | Unique identifier of the volume group. name:{name} can be used instead of {id}.
body = prime.swagger_client.VolumeGroupDelete() # VolumeGroupDelete |  (optional)

try:
    # Delete
    api_instance.volume_group_id_delete(id, body=body)
except ApiException as e:
    print("Exception when calling VolumeGroupApi->volume_group_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the volume group. name:{name} can be used instead of {id}. | 
 **body** | [**VolumeGroupDelete**](VolumeGroupDelete.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_group_id_get**
> VolumeGroupInstance volume_group_id_get(id)

Instance Query

Query a specific volume group, snapshot set, or clone.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VolumeGroupApi()
id = 'id_example' # str | Unique identifier of the volume group. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.volume_group_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeGroupApi->volume_group_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the volume group. name:{name} can be used instead of {id}. | 

### Return type

[**VolumeGroupInstance**](VolumeGroupInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_group_id_patch**
> volume_group_id_patch(id, body)

Modify

Modify a volume group, snapshot set, or clone.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VolumeGroupApi()
id = 'id_example' # str | Unique identifier of the volume group. name:{name} can be used instead of {id}.
body = prime.swagger_client.VolumeGroupModify() # VolumeGroupModify | 

try:
    # Modify
    api_instance.volume_group_id_patch(id, body)
except ApiException as e:
    print("Exception when calling VolumeGroupApi->volume_group_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the volume group. name:{name} can be used instead of {id}. | 
 **body** | [**VolumeGroupModify**](VolumeGroupModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_group_id_refresh_post**
> VolumeGroupRefreshResponse volume_group_id_refresh_post(id, body)

Refresh

 Refresh the contents of a volume group (the target volume group) from another volume group in the same family. A backup snapshot set of the target volume group will be created before refresh is attempted. This behavior can be overridden by setting the __create_backup_snap__ property to false. The profile for the backup snapshot set will be auto-generated, unless a custom profile is specified. The auto-generated profile only initializes the name to an auto-generated, unique value. Other optional parameters are not specified. The table below outlines supported modes of operation and resulting updates to __source_id__ and __source_time__ attributes of __protection_data__. |Target volume group|Source volume group|New source_id|New source_time| |-|-|-|-| |Primary (P1) |Clone (C1)|id of clone (C1)|Current time| |Primary (P1) |snapshot set (C1S1) of clone (C1)|id of source snapshot set (C1S1)|source_time of source snapshot set (C1S1)| |Clone (C1) |Primary (P1)|id of primary (P1)|Current time| |Clone (C1) |snapshot set (S1) of primary (P1)|id of source snapshot set (S1)|source_time of source snapshot set (S1)| |Clone (C1) |Clone (C2)|id of source clone(C2)|Current time| |Clone (C1) |snapshot set (C2S1) of clone (C2)|id of source snapshot set (C2S1)|source_time of source snapshot set (C2S1)| Refresh operation is only supported if there are no membership changes between the source and target volume groups of the refresh operation. You can refresh a volume group even when the sizes of the volumes in the target volume group have changed. This represents a case where the source volumes have been modified over time and you want to refresh the target to the new state of the source volume group. A volume group that is acting as the destination in a replication session cannot be refreshed. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VolumeGroupApi()
id = 'id_example' # str | Unique identifier of the volume group. name:{name} can be used instead of {id}.
body = prime.swagger_client.VolumeGroupRefresh() # VolumeGroupRefresh | 

try:
    # Refresh
    api_response = api_instance.volume_group_id_refresh_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeGroupApi->volume_group_id_refresh_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the volume group. name:{name} can be used instead of {id}. | 
 **body** | [**VolumeGroupRefresh**](VolumeGroupRefresh.md)|  | 

### Return type

[**VolumeGroupRefreshResponse**](VolumeGroupRefreshResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_group_id_remove_members_post**
> volume_group_id_remove_members_post(id, body)

Remove Members

Remove members from an existing primary or clone volume group. This cannot be used to remove members from a snapshot set. Members cannot be removed from a volume group that is a acting as the destination in a replication session. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VolumeGroupApi()
id = 'id_example' # str | Unique identifier of the volume group. name:{name} can be used instead of {id}.
body = prime.swagger_client.VolumeGroupRemoveMembers() # VolumeGroupRemoveMembers | 

try:
    # Remove Members
    api_instance.volume_group_id_remove_members_post(id, body)
except ApiException as e:
    print("Exception when calling VolumeGroupApi->volume_group_id_remove_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the volume group. name:{name} can be used instead of {id}. | 
 **body** | [**VolumeGroupRemoveMembers**](VolumeGroupRemoveMembers.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_group_id_restore_post**
> VolumeGroupRestoreResponse volume_group_id_restore_post(id, body)

Restore

Restore a volume group from a snapshot set. A primary or a clone volume group can only be restored from one of its immediate snapshot sets. A backup snapshot set of the target volume group will be created before restore is attempted. This behavior can be overridden by setting the __create_backup_snap__ property to false.  The profile for the backup snapshot set will be auto-generated unless a custom profile is specified. The auto-generated profile only initializes the name to an auto-generated, unique value. Other optional parameters are not specified. Restore operation is only supported if there are no membership changes between the target volume group and source snapshot set. You can restore a volume group even when the sizes of the volumes in the target volume group have changed. This represents a case where the target volumes have been modified over time, but you want to revert them back to their old state captured in the source snapshot set. When a volume group is restored,  * __source_time__ is set to the __source_time__ of the snapshot set it is being restored from.  A volume group that is acting as the destination in a replication session cannot be restored. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VolumeGroupApi()
id = 'id_example' # str | Unique identifier of the volume group. name:{name} can be used instead of {id}.
body = prime.swagger_client.VolumeGroupRestore() # VolumeGroupRestore | 

try:
    # Restore
    api_response = api_instance.volume_group_id_restore_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeGroupApi->volume_group_id_restore_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the volume group. name:{name} can be used instead of {id}. | 
 **body** | [**VolumeGroupRestore**](VolumeGroupRestore.md)|  | 

### Return type

[**VolumeGroupRestoreResponse**](VolumeGroupRestoreResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_group_id_snapshot_post**
> VolumeGroupSnapshotResponse volume_group_id_snapshot_post(id, body)

Snapshot

Create a new snapshot set for a volume group. When a snapshot of a volume group is created, the resultant snapshot volume group is referred to as a \"snapshot set\" and it represents a point-in-time copy of the members in the volume group. The snapshot set will be created on the same appliance as the source volume group. A snapshot of a volume group will result in a new volume group of __Snapshot__ type. The snapshot set will belong to the same family as the source volume group. When the source of a snapshot operation is a primary or clone volume group,  * __source_id__ of the snapshot set will be set to the identifier of the source volume group.  * __source_time__ of the snapshot set will be set to the time at which the snapshot set will be created.  The __is_write_order_consistent__ property of the source volume group determines whether the snapshot set will be write-order consistent. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VolumeGroupApi()
id = 'id_example' # str | Unique identifier of the volume group. name:{name} can be used instead of {id}.
body = prime.swagger_client.VolumeGroupSnapshot() # VolumeGroupSnapshot | 

try:
    # Snapshot
    api_response = api_instance.volume_group_id_snapshot_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeGroupApi->volume_group_id_snapshot_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the volume group. name:{name} can be used instead of {id}. | 
 **body** | [**VolumeGroupSnapshot**](VolumeGroupSnapshot.md)|  | 

### Return type

[**VolumeGroupSnapshotResponse**](VolumeGroupSnapshotResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_group_post**
> CreateResponse volume_group_post(body)

Create

Create a new volume group. The resulting volume group will have a type of Primary. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.VolumeGroupApi()
body = prime.swagger_client.VolumeGroupCreate() # VolumeGroupCreate | 

try:
    # Create
    api_response = api_instance.volume_group_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeGroupApi->volume_group_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VolumeGroupCreate**](VolumeGroupCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

