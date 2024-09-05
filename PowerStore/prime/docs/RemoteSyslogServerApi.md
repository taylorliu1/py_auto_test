# prime.swagger_client.RemoteSyslogServerApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remote_syslog_server_get**](RemoteSyslogServerApi.md#remote_syslog_server_get) | **GET** /remote_syslog_server | Collection Query
[**remote_syslog_server_id_delete**](RemoteSyslogServerApi.md#remote_syslog_server_id_delete) | **DELETE** /remote_syslog_server/{id} | Delete
[**remote_syslog_server_id_get**](RemoteSyslogServerApi.md#remote_syslog_server_id_get) | **GET** /remote_syslog_server/{id} | Instance Query
[**remote_syslog_server_id_patch**](RemoteSyslogServerApi.md#remote_syslog_server_id_patch) | **PATCH** /remote_syslog_server/{id} | Modify
[**remote_syslog_server_id_test_post**](RemoteSyslogServerApi.md#remote_syslog_server_id_test_post) | **POST** /remote_syslog_server/{id}/test | Validate configuration settings
[**remote_syslog_server_post**](RemoteSyslogServerApi.md#remote_syslog_server_post) | **POST** /remote_syslog_server | Create


# **remote_syslog_server_get**
> list[RemoteSyslogServerInstance] remote_syslog_server_get()

Collection Query

Query the remote_syslog_server configurations. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.RemoteSyslogServerApi()

try:
    # Collection Query
    api_response = api_instance.remote_syslog_server_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteSyslogServerApi->remote_syslog_server_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RemoteSyslogServerInstance]**](RemoteSyslogServerInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_syslog_server_id_delete**
> remote_syslog_server_id_delete(id)

Delete

Delete a remote_syslog_server object. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.RemoteSyslogServerApi()
id = 'id_example' # str | Unique identifier of the remote syslog server object.

try:
    # Delete
    api_instance.remote_syslog_server_id_delete(id)
except ApiException as e:
    print("Exception when calling RemoteSyslogServerApi->remote_syslog_server_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the remote syslog server object. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_syslog_server_id_get**
> RemoteSyslogServerInstance remote_syslog_server_id_get(id)

Instance Query

Query a specific remote_syslog_server configuration. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.RemoteSyslogServerApi()
id = 'id_example' # str | Unique identifier of the remote_syslog_server configuration. Was added in version 2.0.0.0.

try:
    # Instance Query
    api_response = api_instance.remote_syslog_server_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteSyslogServerApi->remote_syslog_server_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the remote_syslog_server configuration. Was added in version 2.0.0.0. | 

### Return type

[**RemoteSyslogServerInstance**](RemoteSyslogServerInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_syslog_server_id_patch**
> remote_syslog_server_id_patch(id, body)

Modify

Modify a remote_syslog_server configuration. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.RemoteSyslogServerApi()
id = 'id_example' # str | Unique identifier of the remote_syslog_server configuration. Was added in version 2.0.0.0.
body = prime.swagger_client.RemoteSyslogServerModify() # RemoteSyslogServerModify | 

try:
    # Modify
    api_instance.remote_syslog_server_id_patch(id, body)
except ApiException as e:
    print("Exception when calling RemoteSyslogServerApi->remote_syslog_server_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the remote_syslog_server configuration. Was added in version 2.0.0.0. | 
 **body** | [**RemoteSyslogServerModify**](RemoteSyslogServerModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_syslog_server_id_test_post**
> remote_syslog_server_id_test_post(id, body=body)

Validate configuration settings

Test the specific remote_syslog_server configuration. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.RemoteSyslogServerApi()
id = 'id_example' # str | Unique identifier of the remote syslog server object.
body = prime.swagger_client.RemoteSyslogServerTest() # RemoteSyslogServerTest | Custom text message to be sent as part of the test message. (optional)

try:
    # Validate configuration settings
    api_instance.remote_syslog_server_id_test_post(id, body=body)
except ApiException as e:
    print("Exception when calling RemoteSyslogServerApi->remote_syslog_server_id_test_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the remote syslog server object. | 
 **body** | [**RemoteSyslogServerTest**](RemoteSyslogServerTest.md)| Custom text message to be sent as part of the test message. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remote_syslog_server_post**
> CreateResponse remote_syslog_server_post(body)

Create

Create a remote_syslog_server object. Was added in version 2.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.RemoteSyslogServerApi()
body = prime.swagger_client.RemoteSyslogServerCreate() # RemoteSyslogServerCreate | Remote syslog server to receive logging information.

try:
    # Create
    api_response = api_instance.remote_syslog_server_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RemoteSyslogServerApi->remote_syslog_server_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemoteSyslogServerCreate**](RemoteSyslogServerCreate.md)| Remote syslog server to receive logging information. | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

