# prime.swagger_client.NvmeDiscoveredCdcApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nvme_discovered_cdc_get**](NvmeDiscoveredCdcApi.md#nvme_discovered_cdc_get) | **GET** /nvme_discovered_cdc | Collection Query


# **nvme_discovered_cdc_get**
> list[NvmeDiscoveredCdcInstance] nvme_discovered_cdc_get()

Collection Query

Query discovered NVMe Centralized Discovery Controllers (CDCs).  Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NvmeDiscoveredCdcApi()

try:
    # Collection Query
    api_response = api_instance.nvme_discovered_cdc_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NvmeDiscoveredCdcApi->nvme_discovered_cdc_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NvmeDiscoveredCdcInstance]**](NvmeDiscoveredCdcInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

