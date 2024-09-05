# prime.swagger_client.ServiceConfigApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_config_get**](ServiceConfigApi.md#service_config_get) | **GET** /service_config | Collection Query
[**service_config_id_get**](ServiceConfigApi.md#service_config_id_get) | **GET** /service_config/{id} | Instance Query
[**service_config_id_patch**](ServiceConfigApi.md#service_config_id_patch) | **PATCH** /service_config/{id} | Modify


# **service_config_get**
> list[ServiceConfigInstance] service_config_get()

Collection Query

Query the service configuration instances for the cluster.  This resource type collection query does not support filtering, sorting or pagination.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ServiceConfigApi()

try:
    # Collection Query
    api_response = api_instance.service_config_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceConfigApi->service_config_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ServiceConfigInstance]**](ServiceConfigInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_config_id_get**
> ServiceConfigInstance service_config_id_get(id)

Instance Query

Query the service configuration instances for an appliance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ServiceConfigApi()
id = 'id_example' # str | Unique identifier of the instance.

try:
    # Instance Query
    api_response = api_instance.service_config_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceConfigApi->service_config_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the instance. | 

### Return type

[**ServiceConfigInstance**](ServiceConfigInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_config_id_patch**
> service_config_id_patch(id, body)

Modify

Modify the service configuration for an appliance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ServiceConfigApi()
id = 'id_example' # str | Unique identifier of the instance.
body = prime.swagger_client.ServiceConfigModify() # ServiceConfigModify | 

try:
    # Modify
    api_instance.service_config_id_patch(id, body)
except ApiException as e:
    print("Exception when calling ServiceConfigApi->service_config_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the instance. | 
 **body** | [**ServiceConfigModify**](ServiceConfigModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

