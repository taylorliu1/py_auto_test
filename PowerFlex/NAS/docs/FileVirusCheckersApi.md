# swagger_client.FileVirusCheckersApi

All URIs are relative to *https://10.226.47.34/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_virus_checkers_get**](FileVirusCheckersApi.md#file_virus_checkers_get) | **GET** /file-virus-checkers | Collection Query
[**file_virus_checkers_id_delete**](FileVirusCheckersApi.md#file_virus_checkers_id_delete) | **DELETE** /file-virus-checkers/{id} | Delete
[**file_virus_checkers_id_get**](FileVirusCheckersApi.md#file_virus_checkers_id_get) | **GET** /file-virus-checkers/{id} | Instance Query
[**file_virus_checkers_id_patch**](FileVirusCheckersApi.md#file_virus_checkers_id_patch) | **PATCH** /file-virus-checkers/{id} | Modify
[**file_virus_checkers_post**](FileVirusCheckersApi.md#file_virus_checkers_post) | **POST** /file-virus-checkers | Create
[**files_file_virus_checkers_id_config_get**](FileVirusCheckersApi.md#files_file_virus_checkers_id_config_get) | **GET** /files/file-virus-checkers/{id}/config | Download Config File
[**files_file_virus_checkers_id_config_post**](FileVirusCheckersApi.md#files_file_virus_checkers_id_config_post) | **POST** /files/file-virus-checkers/{id}/config | Upload Config File

# **file_virus_checkers_get**
> list[FileVirusCheckerInstance] file_virus_checkers_get()

Collection Query

Query all virus checker settings of the NAS Servers.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileVirusCheckersApi()

try:
    # Collection Query
    api_response = api_instance.file_virus_checkers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileVirusCheckersApi->file_virus_checkers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileVirusCheckerInstance]**](FileVirusCheckerInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_virus_checkers_id_delete**
> file_virus_checkers_id_delete(id)

Delete

Delete virus checker settings of a NAS Server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileVirusCheckersApi()
id = 'id_example' # str | Unique identifier of the virus checker instance.

try:
    # Delete
    api_instance.file_virus_checkers_id_delete(id)
except ApiException as e:
    print("Exception when calling FileVirusCheckersApi->file_virus_checkers_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the virus checker instance. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_virus_checkers_id_get**
> FileVirusCheckerInstance file_virus_checkers_id_get(id)

Instance Query

Query a specific virus checker setting of a NAS Server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileVirusCheckersApi()
id = 'id_example' # str | Unique identifier of the virus checker instance.

try:
    # Instance Query
    api_response = api_instance.file_virus_checkers_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileVirusCheckersApi->file_virus_checkers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the virus checker instance. | 

### Return type

[**FileVirusCheckerInstance**](FileVirusCheckerInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_virus_checkers_id_patch**
> file_virus_checkers_id_patch(body, id)

Modify

Modify the virus checker settings of a NAS Server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileVirusCheckersApi()
body = swagger_client.FileVirusCheckerModify() # FileVirusCheckerModify | 
id = 'id_example' # str | Unique identifier of the virus checker instance.

try:
    # Modify
    api_instance.file_virus_checkers_id_patch(body, id)
except ApiException as e:
    print("Exception when calling FileVirusCheckersApi->file_virus_checkers_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileVirusCheckerModify**](FileVirusCheckerModify.md)|  | 
 **id** | **str**| Unique identifier of the virus checker instance. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_virus_checkers_post**
> CreateResponse file_virus_checkers_post(body)

Create

Add a new virus checker setting to a NAS Server. Only one instance can be created per NAS Server. Workflow to enable the virus checker settings on the NAS Server is as follows: \\n 1. Create a virus checker instance on NAS Server. 2. Download template virus checker configuration file. 3. Edit the configuration file with virus checker configuration details. 4. Upload the configuration file. 5. Enable the virus checker on the NAS Server. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileVirusCheckersApi()
body = swagger_client.FileVirusCheckerCreate() # FileVirusCheckerCreate | 

try:
    # Create
    api_response = api_instance.file_virus_checkers_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileVirusCheckersApi->file_virus_checkers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileVirusCheckerCreate**](FileVirusCheckerCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_file_virus_checkers_id_config_get**
> FileVirusCheckerConfigFile files_file_virus_checkers_id_config_get(id)

Download Config File

Download a virus checker configuration file containing the template or the actual (if already uploaded) virus checker configuration settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileVirusCheckersApi()
id = 'id_example' # str | Unique identifier of the virus checker instance.

try:
    # Download Config File
    api_response = api_instance.files_file_virus_checkers_id_config_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileVirusCheckersApi->files_file_virus_checkers_id_config_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the virus checker instance. | 

### Return type

[**FileVirusCheckerConfigFile**](FileVirusCheckerConfigFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: document/text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_file_virus_checkers_id_config_post**
> files_file_virus_checkers_id_config_post(id, body=body)

Upload Config File

Upload a virus checker configuration file containing the virus checker configuration settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileVirusCheckersApi()
id = 'id_example' # str | Unique identifier of the virus checker instance.
body = 'body_example' # str |  (optional)

try:
    # Upload Config File
    api_instance.files_file_virus_checkers_id_config_post(id, body=body)
except ApiException as e:
    print("Exception when calling FileVirusCheckersApi->files_file_virus_checkers_id_config_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the virus checker instance. | 
 **body** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

