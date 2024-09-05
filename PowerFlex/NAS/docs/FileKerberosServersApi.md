# swagger_client.FileKerberosServersApi

All URIs are relative to *https://10.226.47.34/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_kerberos_servers_get**](FileKerberosServersApi.md#file_kerberos_servers_get) | **GET** /file-kerberos-servers | Collection Query
[**file_kerberos_servers_id_delete**](FileKerberosServersApi.md#file_kerberos_servers_id_delete) | **DELETE** /file-kerberos-servers/{id} | Delete
[**file_kerberos_servers_id_get**](FileKerberosServersApi.md#file_kerberos_servers_id_get) | **GET** /file-kerberos-servers/{id} | Instance Query
[**file_kerberos_servers_id_patch**](FileKerberosServersApi.md#file_kerberos_servers_id_patch) | **PATCH** /file-kerberos-servers/{id} | Modify
[**file_kerberos_servers_post**](FileKerberosServersApi.md#file_kerberos_servers_post) | **POST** /file-kerberos-servers | Create
[**files_file_kerberos_servers_id_keytab_get**](FileKerberosServersApi.md#files_file_kerberos_servers_id_keytab_get) | **GET** /files/file-kerberos-servers/{id}/keytab | Download Keytab File
[**files_file_kerberos_servers_id_keytab_post**](FileKerberosServersApi.md#files_file_kerberos_servers_id_keytab_post) | **POST** /files/file-kerberos-servers/{id}/keytab | Upload Keytab File

# **file_kerberos_servers_get**
> list[FileKerberosInstance] file_kerberos_servers_get()

Collection Query

Query of the Kerberos service settings of NAS Servers.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileKerberosServersApi()

try:
    # Collection Query
    api_response = api_instance.file_kerberos_servers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileKerberosServersApi->file_kerberos_servers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileKerberosInstance]**](FileKerberosInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_kerberos_servers_id_delete**
> file_kerberos_servers_id_delete(id)

Delete

Delete Kerberos configuration of a NAS Server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileKerberosServersApi()
id = 'id_example' # str | Unique identifier of the Kerberos service object.

try:
    # Delete
    api_instance.file_kerberos_servers_id_delete(id)
except ApiException as e:
    print("Exception when calling FileKerberosServersApi->file_kerberos_servers_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the Kerberos service object. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_kerberos_servers_id_get**
> FileKerberosInstance file_kerberos_servers_id_get(id)

Instance Query

Query a specific Kerberos service settings of a NAS Server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileKerberosServersApi()
id = 'id_example' # str | Kerberos service object.

try:
    # Instance Query
    api_response = api_instance.file_kerberos_servers_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileKerberosServersApi->file_kerberos_servers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Kerberos service object. | 

### Return type

[**FileKerberosInstance**](FileKerberosInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_kerberos_servers_id_patch**
> file_kerberos_servers_id_patch(body, id)

Modify

Modify the Kerberos service settings of a NAS Server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileKerberosServersApi()
body = swagger_client.FileKerberosModify() # FileKerberosModify | 
id = 'id_example' # str | Unique identifier of the Kerberos service object.

try:
    # Modify
    api_instance.file_kerberos_servers_id_patch(body, id)
except ApiException as e:
    print("Exception when calling FileKerberosServersApi->file_kerberos_servers_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileKerberosModify**](FileKerberosModify.md)|  | 
 **id** | **str**| Unique identifier of the Kerberos service object. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_kerberos_servers_post**
> CreateResponse file_kerberos_servers_post(body)

Create

Create a Kerberos configuration. The operation will fail if a Kerberos configuration already exists.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileKerberosServersApi()
body = swagger_client.FileKerberosCreate() # FileKerberosCreate | 

try:
    # Create
    api_response = api_instance.file_kerberos_servers_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileKerberosServersApi->file_kerberos_servers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileKerberosCreate**](FileKerberosCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_file_kerberos_servers_id_keytab_get**
> FileKerberosKeytabFile files_file_kerberos_servers_id_keytab_get(id)

Download Keytab File

Download previously uploaded keytab file for secure NFS service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileKerberosServersApi()
id = 'id_example' # str | Unique identifier of the Kerberos service object.

try:
    # Download Keytab File
    api_response = api_instance.files_file_kerberos_servers_id_keytab_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileKerberosServersApi->files_file_kerberos_servers_id_keytab_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the Kerberos service object. | 

### Return type

[**FileKerberosKeytabFile**](FileKerberosKeytabFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/binary

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_file_kerberos_servers_id_keytab_post**
> files_file_kerberos_servers_id_keytab_post(id, body=body)

Upload Keytab File

A keytab file is required for secure NFS service with a Linux or Unix Kerberos Key Distribution Center (KDC). The keytab file can be generated using the KDC server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileKerberosServersApi()
id = 'id_example' # str | Unique identifier of the Kerberos service object.
body = 'body_example' # str |  (optional)

try:
    # Upload Keytab File
    api_instance.files_file_kerberos_servers_id_keytab_post(id, body=body)
except ApiException as e:
    print("Exception when calling FileKerberosServersApi->files_file_kerberos_servers_id_keytab_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the Kerberos service object. | 
 **body** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

