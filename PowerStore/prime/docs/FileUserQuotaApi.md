# prime.swagger_client.FileUserQuotaApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_user_quota_get**](FileUserQuotaApi.md#file_user_quota_get) | **GET** /file_user_quota | Collection Query
[**file_user_quota_id_get**](FileUserQuotaApi.md#file_user_quota_id_get) | **GET** /file_user_quota/{id} | Instance Query
[**file_user_quota_id_patch**](FileUserQuotaApi.md#file_user_quota_id_patch) | **PATCH** /file_user_quota/{id} | Modify
[**file_user_quota_id_refresh_post**](FileUserQuotaApi.md#file_user_quota_id_refresh_post) | **POST** /file_user_quota/{id}/refresh | Refresh
[**file_user_quota_post**](FileUserQuotaApi.md#file_user_quota_post) | **POST** /file_user_quota | Create


# **file_user_quota_get**
> list[FileUserQuotaInstance] file_user_quota_get()

Collection Query

List user quota instances.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileUserQuotaApi()

try:
    # Collection Query
    api_response = api_instance.file_user_quota_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileUserQuotaApi->file_user_quota_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileUserQuotaInstance]**](FileUserQuotaInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_user_quota_id_get**
> FileUserQuotaInstance file_user_quota_id_get(id)

Instance Query

Query a user quota instance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileUserQuotaApi()
id = 'id_example' # str | Unique identifier of the file user quota.

try:
    # Instance Query
    api_response = api_instance.file_user_quota_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileUserQuotaApi->file_user_quota_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file user quota. | 

### Return type

[**FileUserQuotaInstance**](FileUserQuotaInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_user_quota_id_patch**
> file_user_quota_id_patch(id, body)

Modify

Modify a user quota instance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileUserQuotaApi()
id = 'id_example' # str | Unique identifier of the file user quota.
body = prime.swagger_client.FileUserQuotaModify() # FileUserQuotaModify | 

try:
    # Modify
    api_instance.file_user_quota_id_patch(id, body)
except ApiException as e:
    print("Exception when calling FileUserQuotaApi->file_user_quota_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file user quota. | 
 **body** | [**FileUserQuotaModify**](FileUserQuotaModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_user_quota_id_refresh_post**
> file_user_quota_id_refresh_post(id)

Refresh

Refresh the cache with the actual value of the user quota.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileUserQuotaApi()
id = 'id_example' # str | Unique identifier of the file user quota.

try:
    # Refresh
    api_instance.file_user_quota_id_refresh_post(id)
except ApiException as e:
    print("Exception when calling FileUserQuotaApi->file_user_quota_id_refresh_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the file user quota. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_user_quota_post**
> CreateResponse file_user_quota_post(body)

Create

Create a user quota instance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileUserQuotaApi()
body = prime.swagger_client.FileUserQuotaCreate() # FileUserQuotaCreate | 

try:
    # Create
    api_response = api_instance.file_user_quota_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileUserQuotaApi->file_user_quota_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileUserQuotaCreate**](FileUserQuotaCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

