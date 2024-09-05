# prime.swagger_client.ImportXtremioConsistencyGroupApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_xtremio_consistency_group_get**](ImportXtremioConsistencyGroupApi.md#import_xtremio_consistency_group_get) | **GET** /import_xtremio_consistency_group | Collection Query
[**import_xtremio_consistency_group_id_get**](ImportXtremioConsistencyGroupApi.md#import_xtremio_consistency_group_id_get) | **GET** /import_xtremio_consistency_group/{id} | Instance Query
[**import_xtremio_consistency_group_id_import_snapshot_schedules_post**](ImportXtremioConsistencyGroupApi.md#import_xtremio_consistency_group_id_import_snapshot_schedules_post) | **POST** /import_xtremio_consistency_group/{id}/import_snapshot_schedules | Return snapshot schedules


# **import_xtremio_consistency_group_get**
> list[ImportXtremioConsistencyGroupInstance] import_xtremio_consistency_group_get()

Collection Query

Query XtremIO consistency groups. Was added in version 1.0.2.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportXtremioConsistencyGroupApi()

try:
    # Collection Query
    api_response = api_instance.import_xtremio_consistency_group_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportXtremioConsistencyGroupApi->import_xtremio_consistency_group_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ImportXtremioConsistencyGroupInstance]**](ImportXtremioConsistencyGroupInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_xtremio_consistency_group_id_get**
> ImportXtremioConsistencyGroupInstance import_xtremio_consistency_group_id_get(id)

Instance Query

Query a specific XtremIO consistency group. Was added in version 1.0.2.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportXtremioConsistencyGroupApi()
id = 'id_example' # str | Unique identifier of the XtremIO consistency group. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.import_xtremio_consistency_group_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportXtremioConsistencyGroupApi->import_xtremio_consistency_group_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the XtremIO consistency group. name:{name} can be used instead of {id}. | 

### Return type

[**ImportXtremioConsistencyGroupInstance**](ImportXtremioConsistencyGroupInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_xtremio_consistency_group_id_import_snapshot_schedules_post**
> ImportXtremioConsistencyGroupImportSnapshotSchedulesResponse import_xtremio_consistency_group_id_import_snapshot_schedules_post(id)

Return snapshot schedules

Return the snapshot schedules associated with the specified XtremIO consistency group. Was added in version 1.0.2.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportXtremioConsistencyGroupApi()
id = 'id_example' # str | Unique identifier of the XtremIO consistency group. name:{name} can be used instead of {id}.

try:
    # Return snapshot schedules
    api_response = api_instance.import_xtremio_consistency_group_id_import_snapshot_schedules_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportXtremioConsistencyGroupApi->import_xtremio_consistency_group_id_import_snapshot_schedules_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the XtremIO consistency group. name:{name} can be used instead of {id}. | 

### Return type

[**ImportXtremioConsistencyGroupImportSnapshotSchedulesResponse**](ImportXtremioConsistencyGroupImportSnapshotSchedulesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

