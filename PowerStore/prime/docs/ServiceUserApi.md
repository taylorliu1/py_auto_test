# prime.swagger_client.ServiceUserApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_user_get**](ServiceUserApi.md#service_user_get) | **GET** /service_user | Collection Query
[**service_user_id_get**](ServiceUserApi.md#service_user_id_get) | **GET** /service_user/{id} | Instance Query
[**service_user_id_patch**](ServiceUserApi.md#service_user_id_patch) | **PATCH** /service_user/{id} | Modify


# **service_user_get**
> list[ServiceUserInstance] service_user_get()

Collection Query

Query the service user account instance.  This resource type collection query does not support filtering, sorting or pagination.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ServiceUserApi()

try:
    # Collection Query
    api_response = api_instance.service_user_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceUserApi->service_user_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ServiceUserInstance]**](ServiceUserInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_user_id_get**
> ServiceUserInstance service_user_id_get(id)

Instance Query

Query the service user account using the unique identifier.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ServiceUserApi()
id = 'id_example' # str | Unique identifier of the service user.

try:
    # Instance Query
    api_response = api_instance.service_user_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceUserApi->service_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the service user. | 

### Return type

[**ServiceUserInstance**](ServiceUserInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_user_id_patch**
> service_user_id_patch(id, body)

Modify

Modify the properties of the service user account.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ServiceUserApi()
id = 'id_example' # str | Unique identifier of the service user account.
body = prime.swagger_client.ServiceUserModify() # ServiceUserModify | 

try:
    # Modify
    api_instance.service_user_id_patch(id, body)
except ApiException as e:
    print("Exception when calling ServiceUserApi->service_user_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the service user account. | 
 **body** | [**ServiceUserModify**](ServiceUserModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

