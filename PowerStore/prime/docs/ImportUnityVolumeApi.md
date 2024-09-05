# prime.swagger_client.ImportUnityVolumeApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_unity_volume_get**](ImportUnityVolumeApi.md#import_unity_volume_get) | **GET** /import_unity_volume | Collection Query
[**import_unity_volume_id_get**](ImportUnityVolumeApi.md#import_unity_volume_id_get) | **GET** /import_unity_volume/{id} | Instance Query
[**import_unity_volume_id_import_snapshot_schedules_post**](ImportUnityVolumeApi.md#import_unity_volume_id_import_snapshot_schedules_post) | **POST** /import_unity_volume/{id}/import_snapshot_schedules | Return snapshot schedules


# **import_unity_volume_get**
> list[ImportUnityVolumeInstance] import_unity_volume_get()

Collection Query

Query Unity volumes.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportUnityVolumeApi()

try:
    # Collection Query
    api_response = api_instance.import_unity_volume_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportUnityVolumeApi->import_unity_volume_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ImportUnityVolumeInstance]**](ImportUnityVolumeInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_unity_volume_id_get**
> ImportUnityVolumeInstance import_unity_volume_id_get(id)

Instance Query

Query a specific Unity volume.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportUnityVolumeApi()
id = 'id_example' # str | Unique identifier of the Unity volume. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.import_unity_volume_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportUnityVolumeApi->import_unity_volume_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the Unity volume. name:{name} can be used instead of {id}. | 

### Return type

[**ImportUnityVolumeInstance**](ImportUnityVolumeInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_unity_volume_id_import_snapshot_schedules_post**
> ImportUnityVolumeImportSnapshotSchedulesResponse import_unity_volume_id_import_snapshot_schedules_post(id)

Return snapshot schedules

Return the snapshot schedules associated with the specified Unity volume.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportUnityVolumeApi()
id = 'id_example' # str | Unique identifier of the Unity volume. name:{name} can be used instead of {id}.

try:
    # Return snapshot schedules
    api_response = api_instance.import_unity_volume_id_import_snapshot_schedules_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportUnityVolumeApi->import_unity_volume_id_import_snapshot_schedules_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the Unity volume. name:{name} can be used instead of {id}. | 

### Return type

[**ImportUnityVolumeImportSnapshotSchedulesResponse**](ImportUnityVolumeImportSnapshotSchedulesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

