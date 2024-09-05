# swagger_client.NasServersApi

All URIs are relative to *https://10.226.47.34/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**files_nas_servers_id_group_get**](NasServersApi.md#files_nas_servers_id_group_get) | **GET** /files/nas-servers/{id}/group | Download File
[**files_nas_servers_id_group_post**](NasServersApi.md#files_nas_servers_id_group_post) | **POST** /files/nas-servers/{id}/group | Upload File
[**files_nas_servers_id_homedir_get**](NasServersApi.md#files_nas_servers_id_homedir_get) | **GET** /files/nas-servers/{id}/homedir | Download File
[**files_nas_servers_id_homedir_post**](NasServersApi.md#files_nas_servers_id_homedir_post) | **POST** /files/nas-servers/{id}/homedir | Upload File
[**files_nas_servers_id_hosts_get**](NasServersApi.md#files_nas_servers_id_hosts_get) | **GET** /files/nas-servers/{id}/hosts | Download File
[**files_nas_servers_id_hosts_post**](NasServersApi.md#files_nas_servers_id_hosts_post) | **POST** /files/nas-servers/{id}/hosts | Upload File
[**files_nas_servers_id_netgroup_get**](NasServersApi.md#files_nas_servers_id_netgroup_get) | **GET** /files/nas-servers/{id}/netgroup | Download File
[**files_nas_servers_id_netgroup_post**](NasServersApi.md#files_nas_servers_id_netgroup_post) | **POST** /files/nas-servers/{id}/netgroup | Upload File
[**files_nas_servers_id_nsswitch_get**](NasServersApi.md#files_nas_servers_id_nsswitch_get) | **GET** /files/nas-servers/{id}/nsswitch | Download File
[**files_nas_servers_id_nsswitch_post**](NasServersApi.md#files_nas_servers_id_nsswitch_post) | **POST** /files/nas-servers/{id}/nsswitch | Upload File
[**files_nas_servers_id_ntxmap_get**](NasServersApi.md#files_nas_servers_id_ntxmap_get) | **GET** /files/nas-servers/{id}/ntxmap | Download File
[**files_nas_servers_id_ntxmap_post**](NasServersApi.md#files_nas_servers_id_ntxmap_post) | **POST** /files/nas-servers/{id}/ntxmap | Upload File
[**files_nas_servers_id_passwd_get**](NasServersApi.md#files_nas_servers_id_passwd_get) | **GET** /files/nas-servers/{id}/passwd | Download File
[**files_nas_servers_id_passwd_post**](NasServersApi.md#files_nas_servers_id_passwd_post) | **POST** /files/nas-servers/{id}/passwd | Upload File
[**files_nas_servers_id_user_mapping_report_get**](NasServersApi.md#files_nas_servers_id_user_mapping_report_get) | **GET** /files/nas-servers/{id}/user-mapping-report | Download User Mapping Report
[**nas_servers_get**](NasServersApi.md#nas_servers_get) | **GET** /nas-servers | Collection Query
[**nas_servers_id_delete**](NasServersApi.md#nas_servers_id_delete) | **DELETE** /nas-servers/{id} | Delete
[**nas_servers_id_get**](NasServersApi.md#nas_servers_id_get) | **GET** /nas-servers/{id} | Instance Query
[**nas_servers_id_move_post**](NasServersApi.md#nas_servers_id_move_post) | **POST** /nas-servers/{id}/move | Move the Nas server to new node.
[**nas_servers_id_patch**](NasServersApi.md#nas_servers_id_patch) | **PATCH** /nas-servers/{id} | Modify
[**nas_servers_id_ping_post**](NasServersApi.md#nas_servers_id_ping_post) | **POST** /nas-servers/{id}/ping | Ping an IP address
[**nas_servers_id_unjoin_and_delete_post**](NasServersApi.md#nas_servers_id_unjoin_and_delete_post) | **POST** /nas-servers/{id}/unjoin_and_delete | Unjoin SMB domain and delete NAS server.
[**nas_servers_id_update_user_mappings_post**](NasServersApi.md#nas_servers_id_update_user_mappings_post) | **POST** /nas-servers/{id}/update-user-mappings | Update User Mappings
[**nas_servers_post**](NasServersApi.md#nas_servers_post) | **POST** /nas-servers | Create

# **files_nas_servers_id_group_get**
> NasServersGroupFile files_nas_servers_id_group_get(id)

Download File

Download a NAS server group file containing the template or the actual (if already uploaded) group details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasServersApi()
id = 'id_example' # str | Unique identifier of the NAS server.

try:
    # Download File
    api_response = api_instance.files_nas_servers_id_group_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasServersApi->files_nas_servers_id_group_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. | 

### Return type

[**NasServersGroupFile**](NasServersGroupFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: document/text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_nas_servers_id_group_post**
> files_nas_servers_id_group_post(id, body=body)

Upload File

Upload NAS server group file.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasServersApi()
id = 'id_example' # str | Unique identifier of the NAS server.
body = 'body_example' # str |  (optional)

try:
    # Upload File
    api_instance.files_nas_servers_id_group_post(id, body=body)
except ApiException as e:
    print("Exception when calling NasServersApi->files_nas_servers_id_group_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. | 
 **body** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_nas_servers_id_homedir_get**
> NasServersHomedirFile files_nas_servers_id_homedir_get(id)

Download File

Download a NAS server homedir file containing the template or the actual (if already uploaded) homedir configuration settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasServersApi()
id = 'id_example' # str | Unique identifier of the NAS server.

try:
    # Download File
    api_response = api_instance.files_nas_servers_id_homedir_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasServersApi->files_nas_servers_id_homedir_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. | 

### Return type

[**NasServersHomedirFile**](NasServersHomedirFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: document/text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_nas_servers_id_homedir_post**
> files_nas_servers_id_homedir_post(id, body=body)

Upload File

Upload the NAS server homedir file.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasServersApi()
id = 'id_example' # str | Unique identifier of the NAS server.
body = 'body_example' # str |  (optional)

try:
    # Upload File
    api_instance.files_nas_servers_id_homedir_post(id, body=body)
except ApiException as e:
    print("Exception when calling NasServersApi->files_nas_servers_id_homedir_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. | 
 **body** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_nas_servers_id_hosts_get**
> NasServersHostsFile files_nas_servers_id_hosts_get(id)

Download File

Download an NAS server host file containing template/actual(if already uploaded) host details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasServersApi()
id = 'id_example' # str | Unique identifier of the NAS server.

try:
    # Download File
    api_response = api_instance.files_nas_servers_id_hosts_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasServersApi->files_nas_servers_id_hosts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. | 

### Return type

[**NasServersHostsFile**](NasServersHostsFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: document/text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_nas_servers_id_hosts_post**
> files_nas_servers_id_hosts_post(id, body=body)

Upload File

Upload NAS server host file.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasServersApi()
id = 'id_example' # str | Unique identifier of the NAS server.
body = 'body_example' # str |  (optional)

try:
    # Upload File
    api_instance.files_nas_servers_id_hosts_post(id, body=body)
except ApiException as e:
    print("Exception when calling NasServersApi->files_nas_servers_id_hosts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. | 
 **body** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_nas_servers_id_netgroup_get**
> NasServersNetgroupFile files_nas_servers_id_netgroup_get(id)

Download File

Download an NAS server netgroup file containing the template or the actual (if already uploaded) netgroup details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasServersApi()
id = 'id_example' # str | Unique identifier of the NAS server.

try:
    # Download File
    api_response = api_instance.files_nas_servers_id_netgroup_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasServersApi->files_nas_servers_id_netgroup_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. | 

### Return type

[**NasServersNetgroupFile**](NasServersNetgroupFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: document/text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_nas_servers_id_netgroup_post**
> files_nas_servers_id_netgroup_post(id, body=body)

Upload File

Upload the NAS server netgroup file.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasServersApi()
id = 'id_example' # str | Unique identifier of the NAS server.
body = 'body_example' # str |  (optional)

try:
    # Upload File
    api_instance.files_nas_servers_id_netgroup_post(id, body=body)
except ApiException as e:
    print("Exception when calling NasServersApi->files_nas_servers_id_netgroup_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. | 
 **body** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_nas_servers_id_nsswitch_get**
> NasServersNsswitchFile files_nas_servers_id_nsswitch_get(id)

Download File

Download a NAS server nsswitch file containing the template or the actual (if already uploaded) nsswitch configuration settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasServersApi()
id = 'id_example' # str | Unique identifier of the NAS server.

try:
    # Download File
    api_response = api_instance.files_nas_servers_id_nsswitch_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasServersApi->files_nas_servers_id_nsswitch_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. | 

### Return type

[**NasServersNsswitchFile**](NasServersNsswitchFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: document/text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_nas_servers_id_nsswitch_post**
> files_nas_servers_id_nsswitch_post(id, body=body)

Upload File

Upload the NAS server nsswitch file.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasServersApi()
id = 'id_example' # str | Unique identifier of the NAS server.
body = 'body_example' # str |  (optional)

try:
    # Upload File
    api_instance.files_nas_servers_id_nsswitch_post(id, body=body)
except ApiException as e:
    print("Exception when calling NasServersApi->files_nas_servers_id_nsswitch_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. | 
 **body** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_nas_servers_id_ntxmap_get**
> NasServersNtxmapFile files_nas_servers_id_ntxmap_get(id)

Download File

Download an NAS server ntxmap file containing the template or the actual (if already uploaded) ntxmap configuration settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasServersApi()
id = 'id_example' # str | Unique identifier of the NAS server.

try:
    # Download File
    api_response = api_instance.files_nas_servers_id_ntxmap_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasServersApi->files_nas_servers_id_ntxmap_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. | 

### Return type

[**NasServersNtxmapFile**](NasServersNtxmapFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: document/text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_nas_servers_id_ntxmap_post**
> files_nas_servers_id_ntxmap_post(id, body=body)

Upload File

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasServersApi()
id = 'id_example' # str | Unique identifier of the NAS server.
body = 'body_example' # str |  (optional)

try:
    # Upload File
    api_instance.files_nas_servers_id_ntxmap_post(id, body=body)
except ApiException as e:
    print("Exception when calling NasServersApi->files_nas_servers_id_ntxmap_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. | 
 **body** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_nas_servers_id_passwd_get**
> NasServersPasswdFile files_nas_servers_id_passwd_get(id)

Download File

Download a NAS server passwd file containing template or the actual (if already uploaded) passwd details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasServersApi()
id = 'id_example' # str | Unique identifier of the NAS server.

try:
    # Download File
    api_response = api_instance.files_nas_servers_id_passwd_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasServersApi->files_nas_servers_id_passwd_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. | 

### Return type

[**NasServersPasswdFile**](NasServersPasswdFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: document/text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_nas_servers_id_passwd_post**
> files_nas_servers_id_passwd_post(id, body=body)

Upload File

Upload NAS server passwd file.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasServersApi()
id = 'id_example' # str | Unique identifier of the NAS server.
body = 'body_example' # str |  (optional)

try:
    # Upload File
    api_instance.files_nas_servers_id_passwd_post(id, body=body)
except ApiException as e:
    print("Exception when calling NasServersApi->files_nas_servers_id_passwd_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. | 
 **body** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_nas_servers_id_user_mapping_report_get**
> NasServersUserMappingReportFile files_nas_servers_id_user_mapping_report_get(id)

Download User Mapping Report

Download the report generated by the update_user_mappings action. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasServersApi()
id = 'id_example' # str | Unique identifier of the NAS server.

try:
    # Download User Mapping Report
    api_response = api_instance.files_nas_servers_id_user_mapping_report_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasServersApi->files_nas_servers_id_user_mapping_report_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. | 

### Return type

[**NasServersUserMappingReportFile**](NasServersUserMappingReportFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: document/text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_servers_get**
> list[NasServersInstance] nas_servers_get()

Collection Query

Query all NAS servers.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasServersApi()

try:
    # Collection Query
    api_response = api_instance.nas_servers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasServersApi->nas_servers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NasServersInstance]**](NasServersInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_servers_id_delete**
> nas_servers_id_delete(id)

Delete

Delete a NAS server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasServersApi()
id = 'id_example' # str | Unique identifier of the NAS server.

try:
    # Delete
    api_instance.nas_servers_id_delete(id)
except ApiException as e:
    print("Exception when calling NasServersApi->nas_servers_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_servers_id_get**
> NasServersInstance nas_servers_id_get(id)

Instance Query

Query a specific NAS server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasServersApi()
id = 'id_example' # str | Unique identifier of the NAS server.

try:
    # Instance Query
    api_response = api_instance.nas_servers_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasServersApi->nas_servers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. | 

### Return type

[**NasServersInstance**](NasServersInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_servers_id_move_post**
> nas_servers_id_move_post(body, id)

Move the Nas server to new node.

Move NAS server to desride node in SDNAS cluster.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasServersApi()
body = swagger_client.NasServersMove() # NasServersMove | 
id = 'id_example' # str | Unique identifier of the NAS server.

try:
    # Move the Nas server to new node.
    api_instance.nas_servers_id_move_post(body, id)
except ApiException as e:
    print("Exception when calling NasServersApi->nas_servers_id_move_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NasServersMove**](NasServersMove.md)|  | 
 **id** | **str**| Unique identifier of the NAS server. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_servers_id_patch**
> nas_servers_id_patch(body, id)

Modify

Modify the settings of a NAS server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasServersApi()
body = swagger_client.NasServersModify() # NasServersModify | 
id = 'id_example' # str | Unique identifier of the NAS server.

try:
    # Modify
    api_instance.nas_servers_id_patch(body, id)
except ApiException as e:
    print("Exception when calling NasServersApi->nas_servers_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NasServersModify**](NasServersModify.md)|  | 
 **id** | **str**| Unique identifier of the NAS server. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_servers_id_ping_post**
> nas_servers_id_ping_post(body, id)

Ping an IP address

Ping destination from NAS server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasServersApi()
body = swagger_client.NasServersPing() # NasServersPing | 
id = 'id_example' # str | Unique identifier of the NAS server.

try:
    # Ping an IP address
    api_instance.nas_servers_id_ping_post(body, id)
except ApiException as e:
    print("Exception when calling NasServersApi->nas_servers_id_ping_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NasServersPing**](NasServersPing.md)|  | 
 **id** | **str**| Unique identifier of the NAS server. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_servers_id_unjoin_and_delete_post**
> nas_servers_id_unjoin_and_delete_post(body, id)

Unjoin SMB domain and delete NAS server.

Unjoin SMB from NAS Server and delete the NAS Server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasServersApi()
body = swagger_client.NasServersUnjoinAndDelete() # NasServersUnjoinAndDelete | 
id = 'id_example' # str | Unique identifier of the NAS server.

try:
    # Unjoin SMB domain and delete NAS server.
    api_instance.nas_servers_id_unjoin_and_delete_post(body, id)
except ApiException as e:
    print("Exception when calling NasServersApi->nas_servers_id_unjoin_and_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NasServersUnjoinAndDelete**](NasServersUnjoinAndDelete.md)|  | 
 **id** | **str**| Unique identifier of the NAS server. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_servers_id_update_user_mappings_post**
> nas_servers_id_update_user_mappings_post(id)

Update User Mappings

Fix the user mappings for all file systems associated with the NAS server. This process updates file ownership on the NAS server's file systems to reflect changes to users' SIDs. A new UID/GID will be obtained from a Unix Directory Service for the user name of the object owner. A user mapping report is also generated. This operation can take a significant amount of time, depending of the size of the file systems.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasServersApi()
id = 'id_example' # str | Unique identifier of the NAS server.

try:
    # Update User Mappings
    api_instance.nas_servers_id_update_user_mappings_post(id)
except ApiException as e:
    print("Exception when calling NasServersApi->nas_servers_id_update_user_mappings_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_servers_post**
> CreateResponse nas_servers_post(body)

Create

Create a NAS server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NasServersApi()
body = swagger_client.NasServersCreate() # NasServersCreate | 

try:
    # Create
    api_response = api_instance.nas_servers_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasServersApi->nas_servers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NasServersCreate**](NasServersCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

