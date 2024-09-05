# prime.swagger_client.DiscoveredInitiatorApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**discovered_initiator_get**](DiscoveredInitiatorApi.md#discovered_initiator_get) | **GET** /discovered_initiator | Collection Query


# **discovered_initiator_get**
> list[DiscoveredInitiatorInstance] discovered_initiator_get()

Collection Query

Query connected initiators that are not associated with a host.  This resource type collection query does not support filtering, sorting or pagination.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.DiscoveredInitiatorApi()

try:
    # Collection Query
    api_response = api_instance.discovered_initiator_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiscoveredInitiatorApi->discovered_initiator_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DiscoveredInitiatorInstance]**](DiscoveredInitiatorInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

