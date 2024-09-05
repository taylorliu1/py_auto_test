# prime.swagger_client.ImportXtremioVolumeApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_xtremio_volume_get**](ImportXtremioVolumeApi.md#import_xtremio_volume_get) | **GET** /import_xtremio_volume | Collection Query
[**import_xtremio_volume_id_get**](ImportXtremioVolumeApi.md#import_xtremio_volume_id_get) | **GET** /import_xtremio_volume/{id} | Instance Query
[**import_xtremio_volume_id_import_snapshot_schedules_post**](ImportXtremioVolumeApi.md#import_xtremio_volume_id_import_snapshot_schedules_post) | **POST** /import_xtremio_volume/{id}/import_snapshot_schedules | Return snapshot schedules


# **import_xtremio_volume_get**
> list[ImportXtremioVolumeInstance] import_xtremio_volume_get()

Collection Query

Query XtremIO volumes. Was added in version 1.0.2.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportXtremioVolumeApi()

try:
    # Collection Query
    api_response = api_instance.import_xtremio_volume_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportXtremioVolumeApi->import_xtremio_volume_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ImportXtremioVolumeInstance]**](ImportXtremioVolumeInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_xtremio_volume_id_get**
> ImportXtremioVolumeInstance import_xtremio_volume_id_get(id)

Instance Query

Query a specific XtremIO volume. Was added in version 1.0.2.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportXtremioVolumeApi()
id = 'id_example' # str | Unique identifier of the XtremIO volume. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.import_xtremio_volume_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportXtremioVolumeApi->import_xtremio_volume_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the XtremIO volume. name:{name} can be used instead of {id}. | 

### Return type

[**ImportXtremioVolumeInstance**](ImportXtremioVolumeInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_xtremio_volume_id_import_snapshot_schedules_post**
> ImportXtremioVolumeImportSnapshotSchedulesResponse import_xtremio_volume_id_import_snapshot_schedules_post(id)

Return snapshot schedules

Return the snapshot schedules associated with the specified XtremIO volume. Was added in version 1.0.2.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportXtremioVolumeApi()
id = 'id_example' # str | Unique identifier of the XtremIO volume. name:{name} can be used instead of {id}.

try:
    # Return snapshot schedules
    api_response = api_instance.import_xtremio_volume_id_import_snapshot_schedules_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportXtremioVolumeApi->import_xtremio_volume_id_import_snapshot_schedules_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the XtremIO volume. name:{name} can be used instead of {id}. | 

### Return type

[**ImportXtremioVolumeImportSnapshotSchedulesResponse**](ImportXtremioVolumeImportSnapshotSchedulesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

