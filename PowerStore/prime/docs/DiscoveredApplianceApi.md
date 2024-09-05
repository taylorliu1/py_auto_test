# prime.swagger_client.DiscoveredApplianceApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**discovered_appliance_get**](DiscoveredApplianceApi.md#discovered_appliance_get) | **GET** /discovered_appliance | Collection Query
[**discovered_appliance_id_update_software_post**](DiscoveredApplianceApi.md#discovered_appliance_id_update_software_post) | **POST** /discovered_appliance/{id}/update_software | Update Software


# **discovered_appliance_get**
> list[DiscoveredApplianceInstance] discovered_appliance_get()

Collection Query

List information about unmanaged appliances on the local subnet.  This resource type collection query does not support filtering, sorting or pagination. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.DiscoveredApplianceApi()

try:
    # Collection Query
    api_response = api_instance.discovered_appliance_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveredApplianceApi->discovered_appliance_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DiscoveredApplianceInstance]**](DiscoveredApplianceInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discovered_appliance_id_update_software_post**
> discovered_appliance_id_update_software_post(id, body)

Update Software

Upload software package on unconfigured appliance and initiate factory reset to bring that appliance to the same version as cluster. This is a long running operation. If you want to run it in the background, append \"?async=true\" to the request URL. Use the job id that is returned to monitor the operation. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.DiscoveredApplianceApi()
id = 'id_example' # str | Unique identifier of a discovered appliance. Use 0 for the local appliance.
body = prime.swagger_client.DiscoveredApplianceUpdateSoftware() # DiscoveredApplianceUpdateSoftware | 

try:
    # Update Software
    api_instance.discovered_appliance_id_update_software_post(id, body)
except ApiException as e:
    print("Exception when calling DiscoveredApplianceApi->discovered_appliance_id_update_software_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of a discovered appliance. Use 0 for the local appliance. | 
 **body** | [**DiscoveredApplianceUpdateSoftware**](DiscoveredApplianceUpdateSoftware.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

