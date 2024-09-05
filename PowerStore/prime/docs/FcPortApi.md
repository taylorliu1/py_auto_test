# prime.swagger_client.FcPortApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fc_port_get**](FcPortApi.md#fc_port_get) | **GET** /fc_port | Collection Query
[**fc_port_id_get**](FcPortApi.md#fc_port_id_get) | **GET** /fc_port/{id} | Instance Query
[**fc_port_id_patch**](FcPortApi.md#fc_port_id_patch) | **PATCH** /fc_port/{id} | Modify


# **fc_port_get**
> list[FcPortInstance] fc_port_get()

Collection Query

Query the FC front-end port configurations for all cluster nodes.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FcPortApi()

try:
    # Collection Query
    api_response = api_instance.fc_port_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FcPortApi->fc_port_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FcPortInstance]**](FcPortInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fc_port_id_get**
> FcPortInstance fc_port_id_get(id)

Instance Query

Query a specific FC front-end port configuration.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FcPortApi()
id = 'id_example' # str | Unique identifier of the FC front-end port. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.fc_port_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FcPortApi->fc_port_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the FC front-end port. name:{name} can be used instead of {id}. | 

### Return type

[**FcPortInstance**](FcPortInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fc_port_id_patch**
> fc_port_id_patch(id, body)

Modify

Modify an FC front-end port's speed. Setting the port's requested speed might not cause the port speed to change immediately. In cases where the Small Form-Factor Pluggable (SFP) is not inserted or the port is down, the requested speed is set, but the current_speed attribute shows the old value until the SFP is able to change speed. By default, the partner port speed on the other node in the appliance is set to the same requested speed. If the requested speed is not supported by the partner port, it is left unchanged.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FcPortApi()
id = 'id_example' # str | Unique identifier of the FC front-end port. name:{name} can be used instead of {id}.
body = prime.swagger_client.FcPortModify() # FcPortModify | 

try:
    # Modify
    api_instance.fc_port_id_patch(id, body)
except ApiException as e:
    print("Exception when calling FcPortApi->fc_port_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the FC front-end port. name:{name} can be used instead of {id}. | 
 **body** | [**FcPortModify**](FcPortModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

