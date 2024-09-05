# prime.swagger_client.KmipConfigApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**kmip_config_get**](KmipConfigApi.md#kmip_config_get) | **GET** /kmip_config | Collection Query
[**kmip_config_id_get**](KmipConfigApi.md#kmip_config_id_get) | **GET** /kmip_config/{id} | Instance Query
[**kmip_config_id_patch**](KmipConfigApi.md#kmip_config_id_patch) | **PATCH** /kmip_config/{id} | Modify
[**kmip_config_id_verify_post**](KmipConfigApi.md#kmip_config_id_verify_post) | **POST** /kmip_config/{id}/verify | Verify


# **kmip_config_get**
> list[KmipConfigInstance] kmip_config_get()

Collection Query

Get the KMIP configuration for the cluster. Was added in version 3.0.0.0.  This resource type collection query does not support filtering, sorting or pagination.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.KmipConfigApi()

try:
    # Collection Query
    api_response = api_instance.kmip_config_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KmipConfigApi->kmip_config_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[KmipConfigInstance]**](KmipConfigInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kmip_config_id_get**
> KmipConfigInstance kmip_config_id_get(id)

Instance Query

Get a specific KMIP server configuration. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.KmipConfigApi()
id = 'id_example' # str |  Was added in version 3.0.0.0.

try:
    # Instance Query
    api_response = api_instance.kmip_config_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KmipConfigApi->kmip_config_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  Was added in version 3.0.0.0. | 

### Return type

[**KmipConfigInstance**](KmipConfigInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kmip_config_id_patch**
> kmip_config_id_patch(id, body)

Modify

Modify the KMIP server configuration for the cluster. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.KmipConfigApi()
id = 'id_example' # str |  Was added in version 3.0.0.0.
body = prime.swagger_client.KmipConfigModify() # KmipConfigModify |  Was added in version 3.0.0.0.

try:
    # Modify
    api_instance.kmip_config_id_patch(id, body)
except ApiException as e:
    print("Exception when calling KmipConfigApi->kmip_config_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  Was added in version 3.0.0.0. | 
 **body** | [**KmipConfigModify**](KmipConfigModify.md)|  Was added in version 3.0.0.0. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kmip_config_id_verify_post**
> kmip_config_id_verify_post(id)

Verify

Verify the connection to the KMIP server and update the status of individual servers. This operation simply updates the status property of each member KMIP server and returns success or failure based on the status. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.KmipConfigApi()
id = 'id_example' # str |  Was added in version 3.0.0.0.

try:
    # Verify
    api_instance.kmip_config_id_verify_post(id)
except ApiException as e:
    print("Exception when calling KmipConfigApi->kmip_config_id_verify_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  Was added in version 3.0.0.0. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

