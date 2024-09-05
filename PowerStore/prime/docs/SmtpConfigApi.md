# prime.swagger_client.SmtpConfigApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**smtp_config_get**](SmtpConfigApi.md#smtp_config_get) | **GET** /smtp_config | Collection Query
[**smtp_config_id_get**](SmtpConfigApi.md#smtp_config_id_get) | **GET** /smtp_config/{id} | Instance Query
[**smtp_config_id_patch**](SmtpConfigApi.md#smtp_config_id_patch) | **PATCH** /smtp_config/{id} | Modify
[**smtp_config_id_test_post**](SmtpConfigApi.md#smtp_config_id_test_post) | **POST** /smtp_config/{id}/test | Test


# **smtp_config_get**
> list[SmtpConfigInstance] smtp_config_get()

Collection Query

Query the SMTP configuration. There is always exactly one smtp_config instance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SmtpConfigApi()

try:
    # Collection Query
    api_response = api_instance.smtp_config_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmtpConfigApi->smtp_config_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SmtpConfigInstance]**](SmtpConfigInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smtp_config_id_get**
> SmtpConfigInstance smtp_config_id_get(id)

Instance Query

Query the specific SMTP configuration.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SmtpConfigApi()
id = 'id_example' # str | Unique identifier of the SMTP configuration. This value is always '0'.

try:
    # Instance Query
    api_response = api_instance.smtp_config_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmtpConfigApi->smtp_config_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the SMTP configuration. This value is always &#39;0&#39;. | 

### Return type

[**SmtpConfigInstance**](SmtpConfigInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smtp_config_id_patch**
> smtp_config_id_patch(id, body)

Modify

Configure the outgoing SMTP information.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SmtpConfigApi()
id = 'id_example' # str | Unique identifier of the SMTP configuration. This value is always '0'.
body = prime.swagger_client.SmtpConfigModify() # SmtpConfigModify | 

try:
    # Modify
    api_instance.smtp_config_id_patch(id, body)
except ApiException as e:
    print("Exception when calling SmtpConfigApi->smtp_config_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the SMTP configuration. This value is always &#39;0&#39;. | 
 **body** | [**SmtpConfigModify**](SmtpConfigModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smtp_config_id_test_post**
> smtp_config_id_test_post(id, body)

Test

Test the SMTP configuration.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SmtpConfigApi()
id = 'id_example' # str | Unique identifier of the SMTP configuration. This value is always '0'.
body = prime.swagger_client.SmtpConfigTest() # SmtpConfigTest | Test operation request body.

try:
    # Test
    api_instance.smtp_config_id_test_post(id, body)
except ApiException as e:
    print("Exception when calling SmtpConfigApi->smtp_config_id_test_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the SMTP configuration. This value is always &#39;0&#39;. | 
 **body** | [**SmtpConfigTest**](SmtpConfigTest.md)| Test operation request body. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

