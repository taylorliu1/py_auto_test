# prime.swagger_client.LoginBannerApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_banner_get**](LoginBannerApi.md#login_banner_get) | **GET** /login_banner | Collection Query
[**login_banner_id_get**](LoginBannerApi.md#login_banner_id_get) | **GET** /login_banner/{id} | Instance Query
[**login_banner_id_patch**](LoginBannerApi.md#login_banner_id_patch) | **PATCH** /login_banner/{id} | Modify


# **login_banner_get**
> list[LoginBannerInstance] login_banner_get()

Collection Query

Query login banner. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.LoginBannerApi()

try:
    # Collection Query
    api_response = api_instance.login_banner_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginBannerApi->login_banner_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LoginBannerInstance]**](LoginBannerInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_banner_id_get**
> LoginBannerInstance login_banner_id_get(id)

Instance Query

Query a specific login banner. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.LoginBannerApi()
id = 'id_example' # str | Unique identifier of the instance. Was added in version 2.0.0.0.

try:
    # Instance Query
    api_response = api_instance.login_banner_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginBannerApi->login_banner_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the instance. Was added in version 2.0.0.0. | 

### Return type

[**LoginBannerInstance**](LoginBannerInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_banner_id_patch**
> login_banner_id_patch(id, body)

Modify

Modify the login banner. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.LoginBannerApi()
id = 'id_example' # str | Unique identifier of the instance. Was added in version 2.0.0.0.
body = prime.swagger_client.LoginBannerModify() # LoginBannerModify | 

try:
    # Modify
    api_instance.login_banner_id_patch(id, body)
except ApiException as e:
    print("Exception when calling LoginBannerApi->login_banner_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the instance. Was added in version 2.0.0.0. | 
 **body** | [**LoginBannerModify**](LoginBannerModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

