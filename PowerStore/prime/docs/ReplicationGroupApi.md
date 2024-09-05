# prime.swagger_client.ReplicationGroupApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**replication_group_get**](ReplicationGroupApi.md#replication_group_get) | **GET** /replication_group | Collection Query
[**replication_group_id_delete**](ReplicationGroupApi.md#replication_group_id_delete) | **DELETE** /replication_group/{id} | Delete
[**replication_group_id_get**](ReplicationGroupApi.md#replication_group_id_get) | **GET** /replication_group/{id} | Instance Query
[**replication_group_id_patch**](ReplicationGroupApi.md#replication_group_id_patch) | **PATCH** /replication_group/{id} | Modify


# **replication_group_get**
> list[ReplicationGroupInstance] replication_group_get()

Collection Query

Query existing replication groups. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ReplicationGroupApi()

try:
    # Collection Query
    api_response = api_instance.replication_group_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplicationGroupApi->replication_group_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ReplicationGroupInstance]**](ReplicationGroupInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_group_id_delete**
> replication_group_id_delete(id, body=body)

Delete

Delete a replication group. This method is only for cleanup after unrecoverable disaster of peer site or vCenter. Normally replication group membership and replication status should be manipulated from vSphere side. By default this operation permitted only on primary replication groups without sessions. Replication groups are normally deleted automatically and asynchronously. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ReplicationGroupApi()
id = 'id_example' # str | Unique identifier of the replication group to be deleted. name:{name} can be used instead of {id}.
body = prime.swagger_client.ReplicationGroupDelete() # ReplicationGroupDelete | Parameters of the replication group delete operation. (optional)

try:
    # Delete
    api_instance.replication_group_id_delete(id, body=body)
except ApiException as e:
    print("Exception when calling ReplicationGroupApi->replication_group_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the replication group to be deleted. name:{name} can be used instead of {id}. | 
 **body** | [**ReplicationGroupDelete**](ReplicationGroupDelete.md)| Parameters of the replication group delete operation. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_group_id_get**
> ReplicationGroupInstance replication_group_id_get(id)

Instance Query

Get a specific replication group. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ReplicationGroupApi()
id = 'id_example' # str | Id of the repilcation group. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.replication_group_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReplicationGroupApi->replication_group_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the repilcation group. name:{name} can be used instead of {id}. | 

### Return type

[**ReplicationGroupInstance**](ReplicationGroupInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replication_group_id_patch**
> replication_group_id_patch(id, body)

Modify

Modify the properties of a replication group. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ReplicationGroupApi()
id = 'id_example' # str | Unique identifier of the replication group to modify. name:{name} can be used instead of {id}.
body = prime.swagger_client.ReplicationGroupModify() # ReplicationGroupModify | Parameters of the replication group modify operation.

try:
    # Modify
    api_instance.replication_group_id_patch(id, body)
except ApiException as e:
    print("Exception when calling ReplicationGroupApi->replication_group_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the replication group to modify. name:{name} can be used instead of {id}. | 
 **body** | [**ReplicationGroupModify**](ReplicationGroupModify.md)| Parameters of the replication group modify operation. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

