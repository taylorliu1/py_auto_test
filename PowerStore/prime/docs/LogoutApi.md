# prime.swagger_client.LogoutApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logout_post**](LogoutApi.md#logout_post) | **POST** /logout | Logout


# **logout_post**
> CreateResponse logout_post()

Logout

Log out the current user.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.LogoutApi()

try:
    # Logout
    api_response = api_instance.logout_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogoutApi->logout_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

