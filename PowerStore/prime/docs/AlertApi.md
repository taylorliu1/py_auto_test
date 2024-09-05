# prime.swagger_client.AlertApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alert_get**](AlertApi.md#alert_get) | **GET** /alert | Collection Query
[**alert_id_get**](AlertApi.md#alert_id_get) | **GET** /alert/{id} | Instance Query
[**alert_id_patch**](AlertApi.md#alert_id_patch) | **PATCH** /alert/{id} | Modify


# **alert_get**
> list[AlertInstance] alert_get()

Collection Query

Query all alerts.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.AlertApi()

try:
    # Collection Query
    api_response = api_instance.alert_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->alert_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AlertInstance]**](AlertInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_id_get**
> AlertInstance alert_id_get(id)

Instance Query

Query a specific alert.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.AlertApi()
id = 'id_example' # str | Unique identifier of the alert.

try:
    # Instance Query
    api_response = api_instance.alert_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->alert_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the alert. | 

### Return type

[**AlertInstance**](AlertInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alert_id_patch**
> alert_id_patch(id, alert_modify)

Modify

Modify an alert. acknowledged_severity parameter, if included, will cause the request to fail when the alert's severity is higher than the acknowledged_severity parameter value. acknowledged_severity  is ignored when is_acknowledged is set to false.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.AlertApi()
id = 'id_example' # str | Unique identifier of the specific alert.
alert_modify = prime.swagger_client.AlertModify() # AlertModify | 

try:
    # Modify
    api_instance.alert_id_patch(id, alert_modify)
except ApiException as e:
    print("Exception when calling AlertApi->alert_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the specific alert. | 
 **alert_modify** | [**AlertModify**](AlertModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

