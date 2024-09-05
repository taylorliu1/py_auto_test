# prime.swagger_client.EventApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event_instance_get**](EventApi.md#event_instance_get) | **GET** /event/{id} | Event summary
[**event_instances_get**](EventApi.md#event_instances_get) | **GET** /event | Get events


# **event_instance_get**
> EventInstance event_instance_get(id)

Event summary

Get event by Event Id.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.EventApi()
id = 'id_example' # str | Event Id

try:
    # Event summary
    api_response = api_instance.event_instance_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->event_instance_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Event Id | 

### Return type

[**EventInstance**](EventInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_instances_get**
> list[EventInstance] event_instances_get()

Get events

Returns all events in the database.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.EventApi()

try:
    # Get events
    api_response = api_instance.event_instances_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->event_instances_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EventInstance]**](EventInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

