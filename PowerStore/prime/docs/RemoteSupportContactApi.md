# prime.swagger_client.RemoteSupportContactApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remote_support_contact_get**](RemoteSupportContactApi.md#remote_support_contact_get) | **GET** /remote_support_contact | Collection query
[**remote_support_contact_id_get**](RemoteSupportContactApi.md#remote_support_contact_id_get) | **GET** /remote_support_contact/{id} | Instance query
[**remote_support_contact_id_patch**](RemoteSupportContactApi.md#remote_support_contact_id_patch) | **PATCH** /remote_support_contact/{id} | Modify


# **remote_support_contact_get**
> list[RemoteSupportContactInstance] remote_support_contact_get()

Collection query

List the current remote support contact information. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.RemoteSupportContactApi()

try:
    # Collection query
    api_response = api_instance.remote_support_contact_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteSupportContactApi->remote_support_contact_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RemoteSupportContactInstance]**](RemoteSupportContactInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_support_contact_id_get**
> RemoteSupportContactInstance remote_support_contact_id_get(id)

Instance query

Query to get the current remote support contact for the cluster. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.RemoteSupportContactApi()
id = 'id_example' # str | The unique id of the remote_support_contact instance. Was added in version 2.0.0.0.

try:
    # Instance query
    api_response = api_instance.remote_support_contact_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteSupportContactApi->remote_support_contact_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique id of the remote_support_contact instance. Was added in version 2.0.0.0. | 

### Return type

[**RemoteSupportContactInstance**](RemoteSupportContactInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_support_contact_id_patch**
> remote_support_contact_id_patch(id, body)

Modify

Modify the remote support contact information. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.RemoteSupportContactApi()
id = 'id_example' # str | The unique id of the remote_support_contact instance. Was added in version 2.0.0.0.
body = prime.swagger_client.RemoteSupportContactModify() # RemoteSupportContactModify | Remote support contact modify parameters.

try:
    # Modify
    api_instance.remote_support_contact_id_patch(id, body)
except ApiException as e:
    print("Exception when calling RemoteSupportContactApi->remote_support_contact_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique id of the remote_support_contact instance. Was added in version 2.0.0.0. | 
 **body** | [**RemoteSupportContactModify**](RemoteSupportContactModify.md)| Remote support contact modify parameters. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

