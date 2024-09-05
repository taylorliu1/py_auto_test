# swagger_client.NasNodesMaintenanceApi

All URIs are relative to *https://10.226.47.34/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nas_nodes_id_enter_maintenance_mode_post**](NasNodesMaintenanceApi.md#nas_nodes_id_enter_maintenance_mode_post) | **POST** /nas-nodes/{id}/enter-maintenance-mode | Enter node maintenance.
[**nas_nodes_id_exit_maintenance_mode_post**](NasNodesMaintenanceApi.md#nas_nodes_id_exit_maintenance_mode_post) | **POST** /nas-nodes/{id}/exit-maintenance-mode | Exit node maintenance.

# **nas_nodes_id_enter_maintenance_mode_post**
> nas_nodes_id_enter_maintenance_mode_post(id)

Enter node maintenance.

Enter NAS node into maintenance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasNodesMaintenanceApi()
id = 'id_example' # str | NAS node Id.

try:
    # Enter node maintenance.
    api_instance.nas_nodes_id_enter_maintenance_mode_post(id)
except ApiException as e:
    print("Exception when calling NasNodesMaintenanceApi->nas_nodes_id_enter_maintenance_mode_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| NAS node Id. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_nodes_id_exit_maintenance_mode_post**
> nas_nodes_id_exit_maintenance_mode_post(id)

Exit node maintenance.

Exit SDNAS node from maintenance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasNodesMaintenanceApi()
id = 'id_example' # str | NAS node Id.

try:
    # Exit node maintenance.
    api_instance.nas_nodes_id_exit_maintenance_mode_post(id)
except ApiException as e:
    print("Exception when calling NasNodesMaintenanceApi->nas_nodes_id_exit_maintenance_mode_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| NAS node Id. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

