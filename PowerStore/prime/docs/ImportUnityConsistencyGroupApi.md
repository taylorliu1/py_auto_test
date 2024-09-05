# prime.swagger_client.ImportUnityConsistencyGroupApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_unity_consistency_group_get**](ImportUnityConsistencyGroupApi.md#import_unity_consistency_group_get) | **GET** /import_unity_consistency_group | Collection Query
[**import_unity_consistency_group_id_get**](ImportUnityConsistencyGroupApi.md#import_unity_consistency_group_id_get) | **GET** /import_unity_consistency_group/{id} | Instance Query
[**import_unity_consistency_group_id_import_snapshot_schedules_post**](ImportUnityConsistencyGroupApi.md#import_unity_consistency_group_id_import_snapshot_schedules_post) | **POST** /import_unity_consistency_group/{id}/import_snapshot_schedules | Return snapshot schedules


# **import_unity_consistency_group_get**
> list[ImportUnityConsistencyGroupInstance] import_unity_consistency_group_get()

Collection Query

Query Unity consistency groups.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportUnityConsistencyGroupApi()

try:
    # Collection Query
    api_response = api_instance.import_unity_consistency_group_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportUnityConsistencyGroupApi->import_unity_consistency_group_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ImportUnityConsistencyGroupInstance]**](ImportUnityConsistencyGroupInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_unity_consistency_group_id_get**
> ImportUnityConsistencyGroupInstance import_unity_consistency_group_id_get(id)

Instance Query

Query a specific Unity consistency group.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportUnityConsistencyGroupApi()
id = 'id_example' # str | Unique identifier of the Unity consistency group. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.import_unity_consistency_group_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportUnityConsistencyGroupApi->import_unity_consistency_group_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the Unity consistency group. name:{name} can be used instead of {id}. | 

### Return type

[**ImportUnityConsistencyGroupInstance**](ImportUnityConsistencyGroupInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_unity_consistency_group_id_import_snapshot_schedules_post**
> ImportUnityConsistencyGroupImportSnapshotSchedulesResponse import_unity_consistency_group_id_import_snapshot_schedules_post(id)

Return snapshot schedules

Return the snapshot schedules associated with the specified Unity consistency group.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportUnityConsistencyGroupApi()
id = 'id_example' # str | Unique identifier of the Unity consistency group. name:{name} can be used instead of {id}.

try:
    # Return snapshot schedules
    api_response = api_instance.import_unity_consistency_group_id_import_snapshot_schedules_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportUnityConsistencyGroupApi->import_unity_consistency_group_id_import_snapshot_schedules_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the Unity consistency group. name:{name} can be used instead of {id}. | 

### Return type

[**ImportUnityConsistencyGroupImportSnapshotSchedulesResponse**](ImportUnityConsistencyGroupImportSnapshotSchedulesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

