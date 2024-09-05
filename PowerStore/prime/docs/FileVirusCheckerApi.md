# prime.swagger_client.FileVirusCheckerApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_virus_checker_get**](FileVirusCheckerApi.md#file_virus_checker_get) | **GET** /file_virus_checker | Collection Query
[**file_virus_checker_id_delete**](FileVirusCheckerApi.md#file_virus_checker_id_delete) | **DELETE** /file_virus_checker/{id} | Delete
[**file_virus_checker_id_download_config_get**](FileVirusCheckerApi.md#file_virus_checker_id_download_config_get) | **GET** /file_virus_checker/{id}/download_config | Download Config File
[**file_virus_checker_id_get**](FileVirusCheckerApi.md#file_virus_checker_id_get) | **GET** /file_virus_checker/{id} | Instance Query
[**file_virus_checker_id_patch**](FileVirusCheckerApi.md#file_virus_checker_id_patch) | **PATCH** /file_virus_checker/{id} | Modify
[**file_virus_checker_id_upload_config_post**](FileVirusCheckerApi.md#file_virus_checker_id_upload_config_post) | **POST** /file_virus_checker/{id}/upload_config | Upload Config File
[**file_virus_checker_post**](FileVirusCheckerApi.md#file_virus_checker_post) | **POST** /file_virus_checker | Create


# **file_virus_checker_get**
> list[FileVirusCheckerInstance] file_virus_checker_get()

Collection Query

Query all virus checker settings of the NAS Servers.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileVirusCheckerApi()

try:
    # Collection Query
    api_response = api_instance.file_virus_checker_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileVirusCheckerApi->file_virus_checker_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileVirusCheckerInstance]**](FileVirusCheckerInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_virus_checker_id_delete**
> file_virus_checker_id_delete(id)

Delete

Delete virus checker settings of a NAS Server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileVirusCheckerApi()
id = 'id_example' # str | Unique identifier of the virus checker instance.

try:
    # Delete
    api_instance.file_virus_checker_id_delete(id)
except ApiException as e:
    print("Exception when calling FileVirusCheckerApi->file_virus_checker_id_delete: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_virus_checker_id_download_config_get**
> FileVirusCheckerConfigFile file_virus_checker_id_download_config_get(id)

Download Config File

Download a virus checker configuration file containing the template or the actual (if already uploaded) virus checker configuration settings.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileVirusCheckerApi()
id = 'id_example' # str | Unique identifier of the virus checker instance.

try:
    # Download Config File
    api_response = api_instance.file_virus_checker_id_download_config_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileVirusCheckerApi->file_virus_checker_id_download_config_get: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: document/text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_virus_checker_id_get**
> FileVirusCheckerInstance file_virus_checker_id_get(id)

Instance Query

Query a specific virus checker setting of a NAS Server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileVirusCheckerApi()
id = 'id_example' # str | Unique identifier of the virus checker instance.

try:
    # Instance Query
    api_response = api_instance.file_virus_checker_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileVirusCheckerApi->file_virus_checker_id_get: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_virus_checker_id_patch**
> file_virus_checker_id_patch(id, body)

Modify

Modify the virus checker settings of a NAS Server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileVirusCheckerApi()
id = 'id_example' # str | Unique identifier of the virus checker instance.
body = prime.swagger_client.FileVirusCheckerModify() # FileVirusCheckerModify | 

try:
    # Modify
    api_instance.file_virus_checker_id_patch(id, body)
except ApiException as e:
    print("Exception when calling FileVirusCheckerApi->file_virus_checker_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the virus checker instance. | 
 **body** | [**FileVirusCheckerModify**](FileVirusCheckerModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_virus_checker_id_upload_config_post**
> file_virus_checker_id_upload_config_post(id, body=body)

Upload Config File

Upload a virus checker configuration file containing the virus checker configuration settings.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileVirusCheckerApi()
id = 'id_example' # str | Unique identifier of the virus checker instance.
body = '/path/to/file.txt' # file | Upload virus checker configuration file. (optional)

try:
    # Upload Config File
    api_instance.file_virus_checker_id_upload_config_post(id, body=body)
except ApiException as e:
    print("Exception when calling FileVirusCheckerApi->file_virus_checker_id_upload_config_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the virus checker instance. | 
 **body** | **file**| Upload virus checker configuration file. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_virus_checker_post**
> CreateResponse file_virus_checker_post(body)

Create

Add a new virus checker setting to a NAS Server. Only one instance can be created per NAS Server. Workflow to enable the virus checker settings on the NAS Server is as follows: \\n 1. Create a virus checker instance on NAS Server. 2. Download template virus checker configuration file. 3. Edit the configuration file with virus checker configuration details. 4. Upload the configuration file. 5. Enable the virus checker on the NAS Server. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileVirusCheckerApi()
body = prime.swagger_client.FileVirusCheckerCreate() # FileVirusCheckerCreate | 

try:
    # Create
    api_response = api_instance.file_virus_checker_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileVirusCheckerApi->file_virus_checker_post: %s\n" % e)
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

