# prime.swagger_client.SasPortApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sas_port_get**](SasPortApi.md#sas_port_get) | **GET** /sas_port | Collection Query
[**sas_port_id_get**](SasPortApi.md#sas_port_id_get) | **GET** /sas_port/{id} | Instance query


# **sas_port_get**
> list[SasPortInstance] sas_port_get()

Collection Query

Query the SAS port configuration for all cluster nodes.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SasPortApi()

try:
    # Collection Query
    api_response = api_instance.sas_port_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SasPortApi->sas_port_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SasPortInstance]**](SasPortInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sas_port_id_get**
> SasPortInstance sas_port_id_get(id)

Instance query

Query a specific SAS port configuration.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SasPortApi()
id = 'id_example' # str | Unique identifier of the SAS port. name:{name} can be used instead of {id}.

try:
    # Instance query
    api_response = api_instance.sas_port_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SasPortApi->sas_port_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the SAS port. name:{name} can be used instead of {id}. | 

### Return type

[**SasPortInstance**](SasPortInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

