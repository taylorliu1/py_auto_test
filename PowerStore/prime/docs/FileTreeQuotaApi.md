# prime.swagger_client.FileTreeQuotaApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_tree_quota_get**](FileTreeQuotaApi.md#file_tree_quota_get) | **GET** /file_tree_quota | Collection Query
[**file_tree_quota_id_delete**](FileTreeQuotaApi.md#file_tree_quota_id_delete) | **DELETE** /file_tree_quota/{id} | Delete
[**file_tree_quota_id_get**](FileTreeQuotaApi.md#file_tree_quota_id_get) | **GET** /file_tree_quota/{id} | Instance Query
[**file_tree_quota_id_patch**](FileTreeQuotaApi.md#file_tree_quota_id_patch) | **PATCH** /file_tree_quota/{id} | Modify
[**file_tree_quota_id_refresh_post**](FileTreeQuotaApi.md#file_tree_quota_id_refresh_post) | **POST** /file_tree_quota/{id}/refresh | Refresh
[**file_tree_quota_post**](FileTreeQuotaApi.md#file_tree_quota_post) | **POST** /file_tree_quota | Create


# **file_tree_quota_get**
> list[FileTreeQuotaInstance] file_tree_quota_get()

Collection Query

Query tree quota instances.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileTreeQuotaApi()

try:
    # Collection Query
    api_response = api_instance.file_tree_quota_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileTreeQuotaApi->file_tree_quota_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileTreeQuotaInstance]**](FileTreeQuotaInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_tree_quota_id_delete**
> file_tree_quota_id_delete(id)

Delete

Delete a tree quota instance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileTreeQuotaApi()
id = 'id_example' # str | Unique identifier of the tree quota.

try:
    # Delete
    api_instance.file_tree_quota_id_delete(id)
except ApiException as e:
    print("Exception when calling FileTreeQuotaApi->file_tree_quota_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the tree quota. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_tree_quota_id_get**
> FileTreeQuotaInstance file_tree_quota_id_get(id)

Instance Query

Query a tree quota instance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileTreeQuotaApi()
id = 'id_example' # str | Unique identifier of the tree quota.

try:
    # Instance Query
    api_response = api_instance.file_tree_quota_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileTreeQuotaApi->file_tree_quota_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the tree quota. | 

### Return type

[**FileTreeQuotaInstance**](FileTreeQuotaInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_tree_quota_id_patch**
> file_tree_quota_id_patch(id, body)

Modify

Modify a tree quota instance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileTreeQuotaApi()
id = 'id_example' # str | Unique identifier of the tree quota.
body = prime.swagger_client.FileTreeQuotaModify() # FileTreeQuotaModify | 

try:
    # Modify
    api_instance.file_tree_quota_id_patch(id, body)
except ApiException as e:
    print("Exception when calling FileTreeQuotaApi->file_tree_quota_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the tree quota. | 
 **body** | [**FileTreeQuotaModify**](FileTreeQuotaModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_tree_quota_id_refresh_post**
> file_tree_quota_id_refresh_post(id)

Refresh

Refresh the cache with the actual value of the tree quota.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileTreeQuotaApi()
id = 'id_example' # str | Unique identifier of the tree quota.

try:
    # Refresh
    api_instance.file_tree_quota_id_refresh_post(id)
except ApiException as e:
    print("Exception when calling FileTreeQuotaApi->file_tree_quota_id_refresh_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the tree quota. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_tree_quota_post**
> CreateResponse file_tree_quota_post(body)

Create

Create a tree quota instance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileTreeQuotaApi()
body = prime.swagger_client.FileTreeQuotaCreate() # FileTreeQuotaCreate | 

try:
    # Create
    api_response = api_instance.file_tree_quota_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileTreeQuotaApi->file_tree_quota_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileTreeQuotaCreate**](FileTreeQuotaCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

