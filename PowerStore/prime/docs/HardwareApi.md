# prime.swagger_client.HardwareApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hardware_get**](HardwareApi.md#hardware_get) | **GET** /hardware | Collection Query
[**hardware_id_drive_repurpose_post**](HardwareApi.md#hardware_id_drive_repurpose_post) | **POST** /hardware/{id}/drive_repurpose | Repurpose a drive
[**hardware_id_get**](HardwareApi.md#hardware_id_get) | **GET** /hardware/{id} | Instance Query
[**hardware_id_patch**](HardwareApi.md#hardware_id_patch) | **PATCH** /hardware/{id} | Modify


# **hardware_get**
> list[HardwareInstance] hardware_get()

Collection Query

Query hardware components

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.HardwareApi()

try:
    # Collection Query
    api_response = api_instance.hardware_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HardwareApi->hardware_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[HardwareInstance]**](HardwareInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hardware_id_drive_repurpose_post**
> hardware_id_drive_repurpose_post(id, body)

Repurpose a drive

A drive that has been used in a different appliance will be locked for use only in that appliance. This operation will allow a locked drive to be used in the current appliance. All data on the drive will become unrecoverable. It will fail if the drive is not locked to a different appliance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.HardwareApi()
id = 'id_example' # str | Identifier of the drive to repurpose. name:{name} can be used instead of {id}.
body = prime.swagger_client.HardwareDriveRepurpose() # HardwareDriveRepurpose | Fields required to repurpose the specified drive.

try:
    # Repurpose a drive
    api_instance.hardware_id_drive_repurpose_post(id, body)
except ApiException as e:
    print("Exception when calling HardwareApi->hardware_id_drive_repurpose_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the drive to repurpose. name:{name} can be used instead of {id}. | 
 **body** | [**HardwareDriveRepurpose**](HardwareDriveRepurpose.md)| Fields required to repurpose the specified drive. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hardware_id_get**
> HardwareInstance hardware_id_get(id)

Instance Query

Get a specific hardware component instance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.HardwareApi()
id = 'id_example' # str | Unique id of hardware component to get. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.hardware_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HardwareApi->hardware_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique id of hardware component to get. name:{name} can be used instead of {id}. | 

### Return type

[**HardwareInstance**](HardwareInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hardware_id_patch**
> hardware_id_patch(id, body)

Modify

Modify a hardware instance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.HardwareApi()
id = 'id_example' # str | The hardware component to modify. name:{name} can be used instead of {id}.
body = prime.swagger_client.HardwareModify() # HardwareModify | 

try:
    # Modify
    api_instance.hardware_id_patch(id, body)
except ApiException as e:
    print("Exception when calling HardwareApi->hardware_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The hardware component to modify. name:{name} can be used instead of {id}. | 
 **body** | [**HardwareModify**](HardwareModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

