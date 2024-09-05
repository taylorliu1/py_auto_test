# prime.swagger_client.AuditEventApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_logs**](AuditEventApi.md#get_audit_logs) | **GET** /audit_event | Collection Query


# **get_audit_logs**
> list[AuditEventInstance] get_audit_logs()

Collection Query

Query audit log entries.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.AuditEventApi()

try:
    # Collection Query
    api_response = api_instance.get_audit_logs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditEventApi->get_audit_logs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AuditEventInstance]**](AuditEventInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

