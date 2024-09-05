# prime.swagger_client.SoftwareInstalledApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**software_installed_get**](SoftwareInstalledApi.md#software_installed_get) | **GET** /software_installed | Collection Query
[**software_installed_id_get**](SoftwareInstalledApi.md#software_installed_id_get) | **GET** /software_installed/{id} | Instance Query


# **software_installed_get**
> list[SoftwareInstalledInstance] software_installed_get()

Collection Query

Query the software that is installed on each appliance. The output returns a list of JSON objects representing the software that is installed on each appliance and one entry representing the common software installed version that is supported for all appliances in the cluster.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SoftwareInstalledApi()

try:
    # Collection Query
    api_response = api_instance.software_installed_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareInstalledApi->software_installed_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SoftwareInstalledInstance]**](SoftwareInstalledInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_installed_id_get**
> SoftwareInstalledInstance software_installed_id_get(id)

Instance Query

Query a specific item from the list of installed software.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SoftwareInstalledApi()
id = 'id_example' # str | Unique identifier of the installed software to query.

try:
    # Instance Query
    api_response = api_instance.software_installed_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SoftwareInstalledApi->software_installed_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the installed software to query. | 

### Return type

[**SoftwareInstalledInstance**](SoftwareInstalledInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

