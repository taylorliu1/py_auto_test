# prime.swagger_client.DnsApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dns_get**](DnsApi.md#dns_get) | **GET** /dns | Collection Query
[**dns_id_get**](DnsApi.md#dns_id_get) | **GET** /dns/{id} | Instance Query
[**dns_id_patch**](DnsApi.md#dns_id_patch) | **PATCH** /dns/{id} | Modify


# **dns_get**
> list[DnsInstance] dns_get()

Collection Query

Query DNS settings for a cluster.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.DnsApi()

try:
    # Collection Query
    api_response = api_instance.dns_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsApi->dns_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DnsInstance]**](DnsInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dns_id_get**
> DnsInstance dns_id_get(id)

Instance Query

Query a specific DNS setting.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.DnsApi()
id = 'id_example' # str | Unique identifier of the DNS setting.

try:
    # Instance Query
    api_response = api_instance.dns_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsApi->dns_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the DNS setting. | 

### Return type

[**DnsInstance**](DnsInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dns_id_patch**
> dns_id_patch(id, body)

Modify

Modify a DNS setting.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.DnsApi()
id = 'id_example' # str | Unique identifier of the DNS setting.
body = prime.swagger_client.DnsModify() # DnsModify | 

try:
    # Modify
    api_instance.dns_id_patch(id, body)
except ApiException as e:
    print("Exception when calling DnsApi->dns_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the DNS setting. | 
 **body** | [**DnsModify**](DnsModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

