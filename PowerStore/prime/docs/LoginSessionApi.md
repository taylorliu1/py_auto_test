# prime.swagger_client.LoginSessionApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_session_get**](LoginSessionApi.md#login_session_get) | **GET** /login_session | Collection Query


# **login_session_get**
> list[LoginSessionInstance] login_session_get()

Collection Query

Obtain the login session for the current user.  This resource type collection query does not support filtering, sorting or pagination.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.LoginSessionApi()

try:
    # Collection Query
    api_response = api_instance.login_session_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginSessionApi->login_session_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LoginSessionInstance]**](LoginSessionInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

