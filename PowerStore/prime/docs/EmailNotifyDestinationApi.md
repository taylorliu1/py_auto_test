# prime.swagger_client.EmailNotifyDestinationApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**email_notify_destination_get**](EmailNotifyDestinationApi.md#email_notify_destination_get) | **GET** /email_notify_destination | Collection Query
[**email_notify_destination_id_delete**](EmailNotifyDestinationApi.md#email_notify_destination_id_delete) | **DELETE** /email_notify_destination/{id} | Delete
[**email_notify_destination_id_get**](EmailNotifyDestinationApi.md#email_notify_destination_id_get) | **GET** /email_notify_destination/{id} | Instance Query
[**email_notify_destination_id_patch**](EmailNotifyDestinationApi.md#email_notify_destination_id_patch) | **PATCH** /email_notify_destination/{id} | Modify
[**email_notify_destination_id_test_post**](EmailNotifyDestinationApi.md#email_notify_destination_id_test_post) | **POST** /email_notify_destination/{id}/test | Test
[**email_notify_destination_post**](EmailNotifyDestinationApi.md#email_notify_destination_post) | **POST** /email_notify_destination | Create


# **email_notify_destination_get**
> list[EmailNotifyDestinationInstance] email_notify_destination_get()

Collection Query

Query all email notification destinations.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.EmailNotifyDestinationApi()

try:
    # Collection Query
    api_response = api_instance.email_notify_destination_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailNotifyDestinationApi->email_notify_destination_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EmailNotifyDestinationInstance]**](EmailNotifyDestinationInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_notify_destination_id_delete**
> email_notify_destination_id_delete(id)

Delete

Delete an email notification destination.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.EmailNotifyDestinationApi()
id = 'id_example' # str | Unique identifier of the email notification destination.

try:
    # Delete
    api_instance.email_notify_destination_id_delete(id)
except ApiException as e:
    print("Exception when calling EmailNotifyDestinationApi->email_notify_destination_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the email notification destination. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_notify_destination_id_get**
> EmailNotifyDestinationInstance email_notify_destination_id_get(id)

Instance Query

Query a specific email notification destination.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.EmailNotifyDestinationApi()
id = 'id_example' # str | Unique identifier of the email notification destination.

try:
    # Instance Query
    api_response = api_instance.email_notify_destination_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailNotifyDestinationApi->email_notify_destination_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the email notification destination. | 

### Return type

[**EmailNotifyDestinationInstance**](EmailNotifyDestinationInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_notify_destination_id_patch**
> email_notify_destination_id_patch(id, body)

Modify

Modify an email notification destination.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.EmailNotifyDestinationApi()
id = 'id_example' # str | Unique identifier of the email notification destination.
body = prime.swagger_client.EmailNotifyDestinationModify() # EmailNotifyDestinationModify | Email address to receive notifications.

try:
    # Modify
    api_instance.email_notify_destination_id_patch(id, body)
except ApiException as e:
    print("Exception when calling EmailNotifyDestinationApi->email_notify_destination_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the email notification destination. | 
 **body** | [**EmailNotifyDestinationModify**](EmailNotifyDestinationModify.md)| Email address to receive notifications. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_notify_destination_id_test_post**
> email_notify_destination_id_test_post(id)

Test

Send a test email to an email address.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.EmailNotifyDestinationApi()
id = 'id_example' # str | Unique identifier of the email notification destination.

try:
    # Test
    api_instance.email_notify_destination_id_test_post(id)
except ApiException as e:
    print("Exception when calling EmailNotifyDestinationApi->email_notify_destination_id_test_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the email notification destination. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_notify_destination_post**
> CreateResponse email_notify_destination_post(body)

Create

Add an email address to receive notifications.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.EmailNotifyDestinationApi()
body = prime.swagger_client.EmailNotifyDestinationCreate() # EmailNotifyDestinationCreate | Email address to receive notifications.

try:
    # Create
    api_response = api_instance.email_notify_destination_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailNotifyDestinationApi->email_notify_destination_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmailNotifyDestinationCreate**](EmailNotifyDestinationCreate.md)| Email address to receive notifications. | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

