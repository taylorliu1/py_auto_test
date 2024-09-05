# prime.swagger_client.ImportNetappVolumeApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_netapp_volume_get**](ImportNetappVolumeApi.md#import_netapp_volume_get) | **GET** /import_netapp_volume | Collection Query
[**import_netapp_volume_id_get**](ImportNetappVolumeApi.md#import_netapp_volume_id_get) | **GET** /import_netapp_volume/{id} | Instance Query
[**import_netapp_volume_id_import_snapshot_schedules_post**](ImportNetappVolumeApi.md#import_netapp_volume_id_import_snapshot_schedules_post) | **POST** /import_netapp_volume/{id}/import_snapshot_schedules | Return snapshot schedules


# **import_netapp_volume_get**
> list[ImportNetappVolumeInstance] import_netapp_volume_get()

Collection Query

Query importable NetApp volumes. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportNetappVolumeApi()

try:
    # Collection Query
    api_response = api_instance.import_netapp_volume_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportNetappVolumeApi->import_netapp_volume_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ImportNetappVolumeInstance]**](ImportNetappVolumeInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_netapp_volume_id_get**
> ImportNetappVolumeInstance import_netapp_volume_id_get(id)

Instance Query

Query a specific importable NetApp volume. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportNetappVolumeApi()
id = 'id_example' # str | Unique identifier of the NetApp volume. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.import_netapp_volume_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportNetappVolumeApi->import_netapp_volume_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NetApp volume. name:{name} can be used instead of {id}. | 

### Return type

[**ImportNetappVolumeInstance**](ImportNetappVolumeInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_netapp_volume_id_import_snapshot_schedules_post**
> ImportNetappVolumeImportSnapshotSchedulesResponse import_netapp_volume_id_import_snapshot_schedules_post(id)

Return snapshot schedules

Return the snapshot schedules associated with the specified NetApp volume. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportNetappVolumeApi()
id = 'id_example' # str | Unique identifier of the NetApp volume. name:{name} can be used instead of {id}.

try:
    # Return snapshot schedules
    api_response = api_instance.import_netapp_volume_id_import_snapshot_schedules_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportNetappVolumeApi->import_netapp_volume_id_import_snapshot_schedules_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NetApp volume. name:{name} can be used instead of {id}. | 

### Return type

[**ImportNetappVolumeImportSnapshotSchedulesResponse**](ImportNetappVolumeImportSnapshotSchedulesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

