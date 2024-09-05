# prime.swagger_client.LocalUserApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**local_user_get**](LocalUserApi.md#local_user_get) | **GET** /local_user | Collection Query
[**local_user_id_delete**](LocalUserApi.md#local_user_id_delete) | **DELETE** /local_user/{id} | Delete
[**local_user_id_get**](LocalUserApi.md#local_user_id_get) | **GET** /local_user/{id} | Instance Query
[**local_user_id_patch**](LocalUserApi.md#local_user_id_patch) | **PATCH** /local_user/{id} | Modify
[**local_user_post**](LocalUserApi.md#local_user_post) | **POST** /local_user | Create


# **local_user_get**
> list[LocalUserInstance] local_user_get()

Collection Query

Query all local user account instances.  This resource type collection query does not support filtering, sorting or pagination.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.LocalUserApi()

try:
    # Collection Query
    api_response = api_instance.local_user_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalUserApi->local_user_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LocalUserInstance]**](LocalUserInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **local_user_id_delete**
> local_user_id_delete(id)

Delete

Delete a local user account instance using the unique identifier. You cannot delete the default \"admin\" account or the account you are currently logged into. Any local user account with Administrator or Security Administrator role can delete any other local user account except the default \"admin\" account.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.LocalUserApi()
id = 'id_example' # str | Unique identifier of the local user account to be deleted.

try:
    # Delete
    api_instance.local_user_id_delete(id)
except ApiException as e:
    print("Exception when calling LocalUserApi->local_user_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the local user account to be deleted. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **local_user_id_get**
> LocalUserInstance local_user_id_get(id)

Instance Query

Query a specific local user account instance using an unique identifier.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.LocalUserApi()
id = 'id_example' # str | Unique identifier of the local user account.

try:
    # Instance Query
    api_response = api_instance.local_user_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalUserApi->local_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the local user account. | 

### Return type

[**LocalUserInstance**](LocalUserInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **local_user_id_patch**
> local_user_id_patch(id, body)

Modify

Modify a property of a local user account using the unique identifier. You cannot modify the default \"admin\" user account.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.LocalUserApi()
id = 'id_example' # str | Unique identifier of the local user account to be modified.
body = prime.swagger_client.LocalUserModify() # LocalUserModify | 

try:
    # Modify
    api_instance.local_user_id_patch(id, body)
except ApiException as e:
    print("Exception when calling LocalUserApi->local_user_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the local user account to be modified. | 
 **body** | [**LocalUserModify**](LocalUserModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **local_user_post**
> CreateResponse local_user_post(body)

Create

Create a new local user account. Any existing local user with either an administrator or a security administrator role can create a new local user account. By default, a new local_user account is NOT locked.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.LocalUserApi()
body = prime.swagger_client.LocalUserCreate() # LocalUserCreate | 

try:
    # Create
    api_response = api_instance.local_user_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalUserApi->local_user_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LocalUserCreate**](LocalUserCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

