# prime.swagger_client.ImportVnxConsistencyGroupApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_vnx_consistency_group_get**](ImportVnxConsistencyGroupApi.md#import_vnx_consistency_group_get) | **GET** /import_vnx_consistency_group | Collection Query
[**import_vnx_consistency_group_id_get**](ImportVnxConsistencyGroupApi.md#import_vnx_consistency_group_id_get) | **GET** /import_vnx_consistency_group/{id} | Instance Query


# **import_vnx_consistency_group_get**
> list[ImportVnxConsistencyGroupInstance] import_vnx_consistency_group_get()

Collection Query

Query VNX consistency groups.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportVnxConsistencyGroupApi()

try:
    # Collection Query
    api_response = api_instance.import_vnx_consistency_group_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportVnxConsistencyGroupApi->import_vnx_consistency_group_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ImportVnxConsistencyGroupInstance]**](ImportVnxConsistencyGroupInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_vnx_consistency_group_id_get**
> ImportVnxConsistencyGroupInstance import_vnx_consistency_group_id_get(id)

Instance Query

Query a specific VNX consistency group.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportVnxConsistencyGroupApi()
id = 'id_example' # str | Unique identifier of a VNX consistency group. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.import_vnx_consistency_group_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportVnxConsistencyGroupApi->import_vnx_consistency_group_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of a VNX consistency group. name:{name} can be used instead of {id}. | 

### Return type

[**ImportVnxConsistencyGroupInstance**](ImportVnxConsistencyGroupInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

