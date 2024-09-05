# prime.swagger_client.ImportStorageCenterVolumeApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_storage_center_volume_get**](ImportStorageCenterVolumeApi.md#import_storage_center_volume_get) | **GET** /import_storage_center_volume | Collection Query
[**import_storage_center_volume_id_get**](ImportStorageCenterVolumeApi.md#import_storage_center_volume_id_get) | **GET** /import_storage_center_volume/{id} | Instance Query
[**import_storage_center_volume_id_import_snapshot_profiles_post**](ImportStorageCenterVolumeApi.md#import_storage_center_volume_id_import_snapshot_profiles_post) | **POST** /import_storage_center_volume/{id}/import_snapshot_profiles | Return snapshot profiles


# **import_storage_center_volume_get**
> list[ImportStorageCenterVolumeInstance] import_storage_center_volume_get()

Collection Query

Query SC volumes.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportStorageCenterVolumeApi()

try:
    # Collection Query
    api_response = api_instance.import_storage_center_volume_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportStorageCenterVolumeApi->import_storage_center_volume_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ImportStorageCenterVolumeInstance]**](ImportStorageCenterVolumeInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_storage_center_volume_id_get**
> ImportStorageCenterVolumeInstance import_storage_center_volume_id_get(id)

Instance Query

Query a specific SC volume.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportStorageCenterVolumeApi()
id = 'id_example' # str | Unique identifier of the SC volume. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.import_storage_center_volume_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportStorageCenterVolumeApi->import_storage_center_volume_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the SC volume. name:{name} can be used instead of {id}. | 

### Return type

[**ImportStorageCenterVolumeInstance**](ImportStorageCenterVolumeInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_storage_center_volume_id_import_snapshot_profiles_post**
> ImportStorageCenterVolumeImportSnapshotProfilesResponse import_storage_center_volume_id_import_snapshot_profiles_post(id)

Return snapshot profiles

Return the snapshot profiles of an SC volume.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportStorageCenterVolumeApi()
id = 'id_example' # str | Unique identifier of the SC volume. name:{name} can be used instead of {id}.

try:
    # Return snapshot profiles
    api_response = api_instance.import_storage_center_volume_id_import_snapshot_profiles_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportStorageCenterVolumeApi->import_storage_center_volume_id_import_snapshot_profiles_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the SC volume. name:{name} can be used instead of {id}. | 

### Return type

[**ImportStorageCenterVolumeImportSnapshotProfilesResponse**](ImportStorageCenterVolumeImportSnapshotProfilesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

