# prime.swagger_client.SecurityConfigApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**security_config_get**](SecurityConfigApi.md#security_config_get) | **GET** /security_config | Collection Query
[**security_config_id_get**](SecurityConfigApi.md#security_config_id_get) | **GET** /security_config/{id} | Instance Query
[**security_config_id_patch**](SecurityConfigApi.md#security_config_id_patch) | **PATCH** /security_config/{id} | Modify


# **security_config_get**
> list[SecurityConfigInstance] security_config_get()

Collection Query

Query system security configurations.  This resource type collection query does not support filtering, sorting or pagination.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SecurityConfigApi()

try:
    # Collection Query
    api_response = api_instance.security_config_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityConfigApi->security_config_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SecurityConfigInstance]**](SecurityConfigInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **security_config_id_get**
> SecurityConfigInstance security_config_id_get(id)

Instance Query

Query a specific system security configuration.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SecurityConfigApi()
id = 'id_example' # str | Unique identifier of the instance.

try:
    # Instance Query
    api_response = api_instance.security_config_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityConfigApi->security_config_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the instance. | 

### Return type

[**SecurityConfigInstance**](SecurityConfigInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **security_config_id_patch**
> security_config_id_patch(id, body)

Modify

Modify the security configuration for the cluster. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SecurityConfigApi()
id = 'id_example' # str | Unique identifier of the instance.
body = prime.swagger_client.SecurityConfigModify() # SecurityConfigModify | 

try:
    # Modify
    api_instance.security_config_id_patch(id, body)
except ApiException as e:
    print("Exception when calling SecurityConfigApi->security_config_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the instance. | 
 **body** | [**SecurityConfigModify**](SecurityConfigModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

