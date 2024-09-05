# prime.swagger_client.FileFtpApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_ftp_get**](FileFtpApi.md#file_ftp_get) | **GET** /file_ftp | Collection Query
[**file_ftp_id_delete**](FileFtpApi.md#file_ftp_id_delete) | **DELETE** /file_ftp/{id} | Delete
[**file_ftp_id_get**](FileFtpApi.md#file_ftp_id_get) | **GET** /file_ftp/{id} | Instance Query
[**file_ftp_id_patch**](FileFtpApi.md#file_ftp_id_patch) | **PATCH** /file_ftp/{id} | Modify
[**file_ftp_post**](FileFtpApi.md#file_ftp_post) | **POST** /file_ftp | Create


# **file_ftp_get**
> list[FileFtpInstance] file_ftp_get()

Collection Query

Query FTP/SFTP instances.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileFtpApi()

try:
    # Collection Query
    api_response = api_instance.file_ftp_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileFtpApi->file_ftp_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileFtpInstance]**](FileFtpInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ftp_id_delete**
> file_ftp_id_delete(id)

Delete

Delete an FTP/SFTP Server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileFtpApi()
id = 'id_example' # str | Unique identifier of the FTP/SFTP Server object.

try:
    # Delete
    api_instance.file_ftp_id_delete(id)
except ApiException as e:
    print("Exception when calling FileFtpApi->file_ftp_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the FTP/SFTP Server object. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ftp_id_get**
> FileFtpInstance file_ftp_id_get(id)

Instance Query

Query a specific FTP/SFTP server for its settings.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileFtpApi()
id = 'id_example' # str | Unique identifier of the FTP/SFTP Server object.

try:
    # Instance Query
    api_response = api_instance.file_ftp_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileFtpApi->file_ftp_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the FTP/SFTP Server object. | 

### Return type

[**FileFtpInstance**](FileFtpInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ftp_id_patch**
> file_ftp_id_patch(id, body)

Modify

Modify an FTP/SFTP server settings.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileFtpApi()
id = 'id_example' # str | Unique identifier of the FTP/SFTP Server object.
body = prime.swagger_client.FileFtpModify() # FileFtpModify | 

try:
    # Modify
    api_instance.file_ftp_id_patch(id, body)
except ApiException as e:
    print("Exception when calling FileFtpApi->file_ftp_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the FTP/SFTP Server object. | 
 **body** | [**FileFtpModify**](FileFtpModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ftp_post**
> CreateResponse file_ftp_post(body)

Create

Create an FTP/SFTP server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileFtpApi()
body = prime.swagger_client.FileFtpCreate() # FileFtpCreate | 

try:
    # Create
    api_response = api_instance.file_ftp_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileFtpApi->file_ftp_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileFtpCreate**](FileFtpCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

