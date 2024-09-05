# prime.swagger_client.MaintenanceWindowApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**maintenance_window_get**](MaintenanceWindowApi.md#maintenance_window_get) | **GET** /maintenance_window | Collection Query
[**maintenance_window_id_get**](MaintenanceWindowApi.md#maintenance_window_id_get) | **GET** /maintenance_window/{id} | Instance Query
[**maintenance_window_id_patch**](MaintenanceWindowApi.md#maintenance_window_id_patch) | **PATCH** /maintenance_window/{id} | Modify


# **maintenance_window_get**
> list[MaintenanceWindowInstance] maintenance_window_get()

Collection Query

Query the maintenance window configurations.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.MaintenanceWindowApi()

try:
    # Collection Query
    api_response = api_instance.maintenance_window_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceWindowApi->maintenance_window_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MaintenanceWindowInstance]**](MaintenanceWindowInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maintenance_window_id_get**
> MaintenanceWindowInstance maintenance_window_id_get(id)

Instance Query

Query one appliance maintenance window configuration.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.MaintenanceWindowApi()
id = 'id_example' # str | Unique identifier of the maintenance window configuration.

try:
    # Instance Query
    api_response = api_instance.maintenance_window_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenanceWindowApi->maintenance_window_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the maintenance window configuration. | 

### Return type

[**MaintenanceWindowInstance**](MaintenanceWindowInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maintenance_window_id_patch**
> maintenance_window_id_patch(id, body)

Modify

Configure maintenance window.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.MaintenanceWindowApi()
id = 'id_example' # str | Unique identifier of the maintenance window configuration.
body = prime.swagger_client.MaintenanceWindowModify() # MaintenanceWindowModify | 

try:
    # Modify
    api_instance.maintenance_window_id_patch(id, body)
except ApiException as e:
    print("Exception when calling MaintenanceWindowApi->maintenance_window_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the maintenance window configuration. | 
 **body** | [**MaintenanceWindowModify**](MaintenanceWindowModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

