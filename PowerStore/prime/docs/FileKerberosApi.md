# prime.swagger_client.FileKerberosApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_kerberos_get**](FileKerberosApi.md#file_kerberos_get) | **GET** /file_kerberos | Collection Query
[**file_kerberos_id_delete**](FileKerberosApi.md#file_kerberos_id_delete) | **DELETE** /file_kerberos/{id} | Delete
[**file_kerberos_id_download_keytab_get**](FileKerberosApi.md#file_kerberos_id_download_keytab_get) | **GET** /file_kerberos/{id}/download_keytab | Download Keytab File
[**file_kerberos_id_get**](FileKerberosApi.md#file_kerberos_id_get) | **GET** /file_kerberos/{id} | Instance Query
[**file_kerberos_id_patch**](FileKerberosApi.md#file_kerberos_id_patch) | **PATCH** /file_kerberos/{id} | Modify
[**file_kerberos_id_upload_keytab_post**](FileKerberosApi.md#file_kerberos_id_upload_keytab_post) | **POST** /file_kerberos/{id}/upload_keytab | Upload Keytab File
[**file_kerberos_post**](FileKerberosApi.md#file_kerberos_post) | **POST** /file_kerberos | Create


# **file_kerberos_get**
> list[FileKerberosInstance] file_kerberos_get()

Collection Query

Query of the Kerberos service settings of NAS Servers.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileKerberosApi()

try:
    # Collection Query
    api_response = api_instance.file_kerberos_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileKerberosApi->file_kerberos_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileKerberosInstance]**](FileKerberosInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_kerberos_id_delete**
> file_kerberos_id_delete(id)

Delete

Delete Kerberos configuration of a NAS Server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileKerberosApi()
id = 'id_example' # str | Unique identifier of the Kerberos service object.

try:
    # Delete
    api_instance.file_kerberos_id_delete(id)
except ApiException as e:
    print("Exception when calling FileKerberosApi->file_kerberos_id_delete: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_kerberos_id_download_keytab_get**
> FileKerberosKeytabFile file_kerberos_id_download_keytab_get(id)

Download Keytab File

Download previously uploaded keytab file for secure NFS service.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileKerberosApi()
id = 'id_example' # str | Unique identifier of the Kerberos service object.

try:
    # Download Keytab File
    api_response = api_instance.file_kerberos_id_download_keytab_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileKerberosApi->file_kerberos_id_download_keytab_get: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/binary

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_kerberos_id_get**
> FileKerberosInstance file_kerberos_id_get(id)

Instance Query

Query a specific Kerberos service settings of a NAS Server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileKerberosApi()
id = 'id_example' # str | Kerberos service object.

try:
    # Instance Query
    api_response = api_instance.file_kerberos_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileKerberosApi->file_kerberos_id_get: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_kerberos_id_patch**
> file_kerberos_id_patch(id, body)

Modify

Modify the Kerberos service settings of a NAS Server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileKerberosApi()
id = 'id_example' # str | Unique identifier of the Kerberos service object.
body = prime.swagger_client.FileKerberosModify() # FileKerberosModify | 

try:
    # Modify
    api_instance.file_kerberos_id_patch(id, body)
except ApiException as e:
    print("Exception when calling FileKerberosApi->file_kerberos_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the Kerberos service object. | 
 **body** | [**FileKerberosModify**](FileKerberosModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_kerberos_id_upload_keytab_post**
> file_kerberos_id_upload_keytab_post(id, body=body)

Upload Keytab File

A keytab file is required for secure NFS service with a Linux or Unix Kerberos Key Distribution Center (KDC). The keytab file can be generated using the KDC server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileKerberosApi()
id = 'id_example' # str | Unique identifier of the Kerberos service object.
body = '/path/to/file.txt' # file |  (optional)

try:
    # Upload Keytab File
    api_instance.file_kerberos_id_upload_keytab_post(id, body=body)
except ApiException as e:
    print("Exception when calling FileKerberosApi->file_kerberos_id_upload_keytab_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the Kerberos service object. | 
 **body** | **file**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_kerberos_post**
> CreateResponse file_kerberos_post(body)

Create

Create a Kerberos configuration. The operation will fail if a Kerberos configuration already exists.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileKerberosApi()
body = prime.swagger_client.FileKerberosCreate() # FileKerberosCreate | 

try:
    # Create
    api_response = api_instance.file_kerberos_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileKerberosApi->file_kerberos_post: %s\n" % e)
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

