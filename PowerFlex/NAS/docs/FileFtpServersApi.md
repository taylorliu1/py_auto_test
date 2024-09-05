# swagger_client.FileFtpServersApi

All URIs are relative to *https://10.226.47.34/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_ftp_servers_get**](FileFtpServersApi.md#file_ftp_servers_get) | **GET** /file-ftp-servers | Collection Query
[**file_ftp_servers_id_delete**](FileFtpServersApi.md#file_ftp_servers_id_delete) | **DELETE** /file-ftp-servers/{id} | Delete
[**file_ftp_servers_id_get**](FileFtpServersApi.md#file_ftp_servers_id_get) | **GET** /file-ftp-servers/{id} | Instance Query
[**file_ftp_servers_id_patch**](FileFtpServersApi.md#file_ftp_servers_id_patch) | **PATCH** /file-ftp-servers/{id} | Modify
[**file_ftp_servers_post**](FileFtpServersApi.md#file_ftp_servers_post) | **POST** /file-ftp-servers | Create

# **file_ftp_servers_get**
> list[FileFtpInstance] file_ftp_servers_get()

Collection Query

Query FTP/SFTP instances.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileFtpServersApi()

try:
    # Collection Query
    api_response = api_instance.file_ftp_servers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileFtpServersApi->file_ftp_servers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileFtpInstance]**](FileFtpInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ftp_servers_id_delete**
> file_ftp_servers_id_delete(id)

Delete

Delete an FTP/SFTP Server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileFtpServersApi()
id = 'id_example' # str | Unique identifier of the FTP/SFTP Server object.

try:
    # Delete
    api_instance.file_ftp_servers_id_delete(id)
except ApiException as e:
    print("Exception when calling FileFtpServersApi->file_ftp_servers_id_delete: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ftp_servers_id_get**
> FileFtpInstance file_ftp_servers_id_get(id)

Instance Query

Query a specific FTP/SFTP server for its settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileFtpServersApi()
id = 'id_example' # str | Unique identifier of the FTP/SFTP Server object.

try:
    # Instance Query
    api_response = api_instance.file_ftp_servers_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileFtpServersApi->file_ftp_servers_id_get: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ftp_servers_id_patch**
> file_ftp_servers_id_patch(body, id)

Modify

Modify an FTP/SFTP server settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileFtpServersApi()
body = swagger_client.FileFtpModify() # FileFtpModify | 
id = 'id_example' # str | Unique identifier of the FTP/SFTP Server object.

try:
    # Modify
    api_instance.file_ftp_servers_id_patch(body, id)
except ApiException as e:
    print("Exception when calling FileFtpServersApi->file_ftp_servers_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileFtpModify**](FileFtpModify.md)|  | 
 **id** | **str**| Unique identifier of the FTP/SFTP Server object. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ftp_servers_post**
> CreateResponse file_ftp_servers_post(body)

Create

Create an FTP/SFTP server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileFtpServersApi()
body = swagger_client.FileFtpCreate() # FileFtpCreate | 

try:
    # Create
    api_response = api_instance.file_ftp_servers_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileFtpServersApi->file_ftp_servers_post: %s\n" % e)
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

