# prime.swagger_client.NtpApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ntp_get**](NtpApi.md#ntp_get) | **GET** /ntp | Collection Query
[**ntp_id_get**](NtpApi.md#ntp_id_get) | **GET** /ntp/{id} | Instance Query
[**ntp_id_patch**](NtpApi.md#ntp_id_patch) | **PATCH** /ntp/{id} | Modify


# **ntp_get**
> list[NtpInstance] ntp_get()

Collection Query

Query NTP settings for a cluster.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NtpApi()

try:
    # Collection Query
    api_response = api_instance.ntp_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NtpApi->ntp_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NtpInstance]**](NtpInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ntp_id_get**
> NtpInstance ntp_id_get(id)

Instance Query

Query a specific NTP setting.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NtpApi()
id = 'id_example' # str | Unique identifier of the NTP setting.

try:
    # Instance Query
    api_response = api_instance.ntp_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NtpApi->ntp_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NTP setting. | 

### Return type

[**NtpInstance**](NtpInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ntp_id_patch**
> ntp_id_patch(id, body)

Modify

Modify NTP settings.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NtpApi()
id = 'id_example' # str | Unique identifier of the NTP setting.
body = prime.swagger_client.NtpModify() # NtpModify | 

try:
    # Modify
    api_instance.ntp_id_patch(id, body)
except ApiException as e:
    print("Exception when calling NtpApi->ntp_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NTP setting. | 
 **body** | [**NtpModify**](NtpModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

