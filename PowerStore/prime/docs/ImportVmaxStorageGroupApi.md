# prime.swagger_client.ImportVmaxStorageGroupApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_vmax_storage_group_get**](ImportVmaxStorageGroupApi.md#import_vmax_storage_group_get) | **GET** /import_vmax_storage_group | Collection Query
[**import_vmax_storage_group_id_get**](ImportVmaxStorageGroupApi.md#import_vmax_storage_group_id_get) | **GET** /import_vmax_storage_group/{id} | Instance Query
[**import_vmax_storage_group_id_import_snapshot_policy_post**](ImportVmaxStorageGroupApi.md#import_vmax_storage_group_id_import_snapshot_policy_post) | **POST** /import_vmax_storage_group/{id}/import_snapshot_policy | Return snapshot policy


# **import_vmax_storage_group_get**
> list[ImportVmaxStorageGroupInstance] import_vmax_storage_group_get()

Collection Query

Query VMAX storage groups. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportVmaxStorageGroupApi()

try:
    # Collection Query
    api_response = api_instance.import_vmax_storage_group_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportVmaxStorageGroupApi->import_vmax_storage_group_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ImportVmaxStorageGroupInstance]**](ImportVmaxStorageGroupInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_vmax_storage_group_id_get**
> ImportVmaxStorageGroupInstance import_vmax_storage_group_id_get(id)

Instance Query

Query a specific VMAX storage group. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportVmaxStorageGroupApi()
id = 'id_example' # str | Unique identifier of a VMAX storage group. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.import_vmax_storage_group_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportVmaxStorageGroupApi->import_vmax_storage_group_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of a VMAX storage group. name:{name} can be used instead of {id}. | 

### Return type

[**ImportVmaxStorageGroupInstance**](ImportVmaxStorageGroupInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_vmax_storage_group_id_import_snapshot_policy_post**
> ImportVmaxStorageGroupImportSnapshotPolicyResponse import_vmax_storage_group_id_import_snapshot_policy_post(id)

Return snapshot policy

Return the snapshot policy associated with the specified VMAX storage group. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportVmaxStorageGroupApi()
id = 'id_example' # str | Unique identifier of the VMAX storage group. name:{name} can be used instead of {id}.

try:
    # Return snapshot policy
    api_response = api_instance.import_vmax_storage_group_id_import_snapshot_policy_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportVmaxStorageGroupApi->import_vmax_storage_group_id_import_snapshot_policy_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the VMAX storage group. name:{name} can be used instead of {id}. | 

### Return type

[**ImportVmaxStorageGroupImportSnapshotPolicyResponse**](ImportVmaxStorageGroupImportSnapshotPolicyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

