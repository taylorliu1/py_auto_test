# prime.swagger_client.NasServerApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nas_server_get**](NasServerApi.md#nas_server_get) | **GET** /nas_server | Collection Query
[**nas_server_id_clone_post**](NasServerApi.md#nas_server_id_clone_post) | **POST** /nas_server/{id}/clone | Clone the NAS Server
[**nas_server_id_delete**](NasServerApi.md#nas_server_id_delete) | **DELETE** /nas_server/{id} | Delete
[**nas_server_id_download_group_get**](NasServerApi.md#nas_server_id_download_group_get) | **GET** /nas_server/{id}/download/group | Download File
[**nas_server_id_download_homedir_get**](NasServerApi.md#nas_server_id_download_homedir_get) | **GET** /nas_server/{id}/download/homedir | Download File
[**nas_server_id_download_hosts_get**](NasServerApi.md#nas_server_id_download_hosts_get) | **GET** /nas_server/{id}/download/hosts | Download File
[**nas_server_id_download_netgroup_get**](NasServerApi.md#nas_server_id_download_netgroup_get) | **GET** /nas_server/{id}/download/netgroup | Download File
[**nas_server_id_download_nsswitch_get**](NasServerApi.md#nas_server_id_download_nsswitch_get) | **GET** /nas_server/{id}/download/nsswitch | Download File
[**nas_server_id_download_ntxmap_get**](NasServerApi.md#nas_server_id_download_ntxmap_get) | **GET** /nas_server/{id}/download/ntxmap | Download File
[**nas_server_id_download_passwd_get**](NasServerApi.md#nas_server_id_download_passwd_get) | **GET** /nas_server/{id}/download/passwd | Download File
[**nas_server_id_download_user_mapping_report_get**](NasServerApi.md#nas_server_id_download_user_mapping_report_get) | **GET** /nas_server/{id}/download/user_mapping_report | Download User Mapping Report
[**nas_server_id_get**](NasServerApi.md#nas_server_id_get) | **GET** /nas_server/{id} | Instance Query
[**nas_server_id_patch**](NasServerApi.md#nas_server_id_patch) | **PATCH** /nas_server/{id} | Modify
[**nas_server_id_ping_post**](NasServerApi.md#nas_server_id_ping_post) | **POST** /nas_server/{id}/ping | Ping an IP address
[**nas_server_id_update_user_mappings_post**](NasServerApi.md#nas_server_id_update_user_mappings_post) | **POST** /nas_server/{id}/update_user_mappings | Update User Mappings
[**nas_server_id_upload_group_post**](NasServerApi.md#nas_server_id_upload_group_post) | **POST** /nas_server/{id}/upload/group | Upload File
[**nas_server_id_upload_homedir_post**](NasServerApi.md#nas_server_id_upload_homedir_post) | **POST** /nas_server/{id}/upload/homedir | Upload File
[**nas_server_id_upload_hosts_post**](NasServerApi.md#nas_server_id_upload_hosts_post) | **POST** /nas_server/{id}/upload/hosts | Upload File
[**nas_server_id_upload_netgroup_post**](NasServerApi.md#nas_server_id_upload_netgroup_post) | **POST** /nas_server/{id}/upload/netgroup | Upload File
[**nas_server_id_upload_nsswitch_post**](NasServerApi.md#nas_server_id_upload_nsswitch_post) | **POST** /nas_server/{id}/upload/nsswitch | Upload File
[**nas_server_id_upload_ntxmap_post**](NasServerApi.md#nas_server_id_upload_ntxmap_post) | **POST** /nas_server/{id}/upload/ntxmap | Upload File
[**nas_server_id_upload_passwd_post**](NasServerApi.md#nas_server_id_upload_passwd_post) | **POST** /nas_server/{id}/upload/passwd | Upload File
[**nas_server_post**](NasServerApi.md#nas_server_post) | **POST** /nas_server | Create


# **nas_server_get**
> list[NasServerInstance] nas_server_get()

Collection Query

Query all NAS servers.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NasServerApi()

try:
    # Collection Query
    api_response = api_instance.nas_server_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasServerApi->nas_server_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NasServerInstance]**](NasServerInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_server_id_clone_post**
> CreateResponse nas_server_id_clone_post(id, body)

Clone the NAS Server

Take a clone of NAS Server. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NasServerApi()
id = 'id_example' # str | NAS Server instance id. name:{name} can be used instead of {id}.
body = prime.swagger_client.NasServerClone() # NasServerClone | 

try:
    # Clone the NAS Server
    api_response = api_instance.nas_server_id_clone_post(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasServerApi->nas_server_id_clone_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| NAS Server instance id. name:{name} can be used instead of {id}. | 
 **body** | [**NasServerClone**](NasServerClone.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_server_id_delete**
> nas_server_id_delete(id, body=body)

Delete

Delete a NAS server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NasServerApi()
id = 'id_example' # str | Unique identifier of the NAS server. name:{name} can be used instead of {id}.
body = prime.swagger_client.NasServerDelete() # NasServerDelete |  (optional)

try:
    # Delete
    api_instance.nas_server_id_delete(id, body=body)
except ApiException as e:
    print("Exception when calling NasServerApi->nas_server_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. name:{name} can be used instead of {id}. | 
 **body** | [**NasServerDelete**](NasServerDelete.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_server_id_download_group_get**
> NasServerGroupFile nas_server_id_download_group_get(id)

Download File

Download a NAS server group file containing the template or the actual (if already uploaded) group details.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NasServerApi()
id = 'id_example' # str | Unique identifier of the NAS server. name:{name} can be used instead of {id}.

try:
    # Download File
    api_response = api_instance.nas_server_id_download_group_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasServerApi->nas_server_id_download_group_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. name:{name} can be used instead of {id}. | 

### Return type

[**NasServerGroupFile**](NasServerGroupFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: document/text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_server_id_download_homedir_get**
> NasServerHomedirFile nas_server_id_download_homedir_get(id)

Download File

Download a NAS server homedir file containing the template or the actual (if already uploaded) homedir configuration settings.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NasServerApi()
id = 'id_example' # str | Unique identifier of the NAS server. name:{name} can be used instead of {id}.

try:
    # Download File
    api_response = api_instance.nas_server_id_download_homedir_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasServerApi->nas_server_id_download_homedir_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. name:{name} can be used instead of {id}. | 

### Return type

[**NasServerHomedirFile**](NasServerHomedirFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: document/text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_server_id_download_hosts_get**
> NasServerHostsFile nas_server_id_download_hosts_get(id)

Download File

Download an NAS server host file containing template/actual(if already uploaded) host details.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NasServerApi()
id = 'id_example' # str | Unique identifier of the NAS server. name:{name} can be used instead of {id}.

try:
    # Download File
    api_response = api_instance.nas_server_id_download_hosts_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasServerApi->nas_server_id_download_hosts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. name:{name} can be used instead of {id}. | 

### Return type

[**NasServerHostsFile**](NasServerHostsFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: document/text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_server_id_download_netgroup_get**
> NasServerNetgroupFile nas_server_id_download_netgroup_get(id)

Download File

Download an NAS server netgroup file containing the template or the actual (if already uploaded) netgroup details.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NasServerApi()
id = 'id_example' # str | Unique identifier of the NAS server. name:{name} can be used instead of {id}.

try:
    # Download File
    api_response = api_instance.nas_server_id_download_netgroup_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasServerApi->nas_server_id_download_netgroup_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. name:{name} can be used instead of {id}. | 

### Return type

[**NasServerNetgroupFile**](NasServerNetgroupFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: document/text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_server_id_download_nsswitch_get**
> NasServerNsswitchFile nas_server_id_download_nsswitch_get(id)

Download File

Download a NAS server nsswitch file containing the template or the actual (if already uploaded) nsswitch configuration settings.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NasServerApi()
id = 'id_example' # str | Unique identifier of the NAS server. name:{name} can be used instead of {id}.

try:
    # Download File
    api_response = api_instance.nas_server_id_download_nsswitch_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasServerApi->nas_server_id_download_nsswitch_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. name:{name} can be used instead of {id}. | 

### Return type

[**NasServerNsswitchFile**](NasServerNsswitchFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: document/text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_server_id_download_ntxmap_get**
> NasServerNtxmapFile nas_server_id_download_ntxmap_get(id)

Download File

Download an NAS server ntxmap file containing the template or the actual (if already uploaded) ntxmap configuration settings.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NasServerApi()
id = 'id_example' # str | Unique identifier of the NAS server. name:{name} can be used instead of {id}.

try:
    # Download File
    api_response = api_instance.nas_server_id_download_ntxmap_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasServerApi->nas_server_id_download_ntxmap_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. name:{name} can be used instead of {id}. | 

### Return type

[**NasServerNtxmapFile**](NasServerNtxmapFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: document/text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_server_id_download_passwd_get**
> NasServerPasswdFile nas_server_id_download_passwd_get(id)

Download File

Download a NAS server passwd file containing template or the actual (if already uploaded) passwd details.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NasServerApi()
id = 'id_example' # str | Unique identifier of the NAS server. name:{name} can be used instead of {id}.

try:
    # Download File
    api_response = api_instance.nas_server_id_download_passwd_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasServerApi->nas_server_id_download_passwd_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. name:{name} can be used instead of {id}. | 

### Return type

[**NasServerPasswdFile**](NasServerPasswdFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: document/text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_server_id_download_user_mapping_report_get**
> NasServerUserMappingReportFile nas_server_id_download_user_mapping_report_get(id)

Download User Mapping Report

Download the report generated by the update_user_mappings action. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NasServerApi()
id = 'id_example' # str | Unique identifier of the NAS server. name:{name} can be used instead of {id}.

try:
    # Download User Mapping Report
    api_response = api_instance.nas_server_id_download_user_mapping_report_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasServerApi->nas_server_id_download_user_mapping_report_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. name:{name} can be used instead of {id}. | 

### Return type

[**NasServerUserMappingReportFile**](NasServerUserMappingReportFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: document/text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_server_id_get**
> NasServerInstance nas_server_id_get(id)

Instance Query

Query a specific NAS server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NasServerApi()
id = 'id_example' # str | Unique identifier of the NAS server. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.nas_server_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasServerApi->nas_server_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. name:{name} can be used instead of {id}. | 

### Return type

[**NasServerInstance**](NasServerInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_server_id_patch**
> nas_server_id_patch(id, body)

Modify

Modify the settings of a NAS server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NasServerApi()
id = 'id_example' # str | Unique identifier of the NAS server. name:{name} can be used instead of {id}.
body = prime.swagger_client.NasServerModify() # NasServerModify | 

try:
    # Modify
    api_instance.nas_server_id_patch(id, body)
except ApiException as e:
    print("Exception when calling NasServerApi->nas_server_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. name:{name} can be used instead of {id}. | 
 **body** | [**NasServerModify**](NasServerModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_server_id_ping_post**
> nas_server_id_ping_post(id, body)

Ping an IP address

Ping destination from NAS server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NasServerApi()
id = 'id_example' # str | Unique identifier of the NAS server. name:{name} can be used instead of {id}.
body = prime.swagger_client.NasServerPing() # NasServerPing | 

try:
    # Ping an IP address
    api_instance.nas_server_id_ping_post(id, body)
except ApiException as e:
    print("Exception when calling NasServerApi->nas_server_id_ping_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. name:{name} can be used instead of {id}. | 
 **body** | [**NasServerPing**](NasServerPing.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_server_id_update_user_mappings_post**
> nas_server_id_update_user_mappings_post(id)

Update User Mappings

Fix the user mappings for all file systems associated with the NAS server. This process updates file ownership on the NAS server's file systems to reflect changes to users' SIDs. A new UID/GID will be obtained from a Unix Directory Service for the user name of the object owner. A user mapping report is also generated. This operation can take a significant amount of time, depending of the size of the file systems.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NasServerApi()
id = 'id_example' # str | Unique identifier of the NAS server. name:{name} can be used instead of {id}.

try:
    # Update User Mappings
    api_instance.nas_server_id_update_user_mappings_post(id)
except ApiException as e:
    print("Exception when calling NasServerApi->nas_server_id_update_user_mappings_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_server_id_upload_group_post**
> nas_server_id_upload_group_post(id, body=body)

Upload File

Upload NAS server group file.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NasServerApi()
id = 'id_example' # str | Unique identifier of the NAS server. name:{name} can be used instead of {id}.
body = '/path/to/file.txt' # file | Upload NAS server group file. (optional)

try:
    # Upload File
    api_instance.nas_server_id_upload_group_post(id, body=body)
except ApiException as e:
    print("Exception when calling NasServerApi->nas_server_id_upload_group_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. name:{name} can be used instead of {id}. | 
 **body** | **file**| Upload NAS server group file. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_server_id_upload_homedir_post**
> nas_server_id_upload_homedir_post(id, body=body)

Upload File

Upload the NAS server homedir file.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NasServerApi()
id = 'id_example' # str | Unique identifier of the NAS server. name:{name} can be used instead of {id}.
body = '/path/to/file.txt' # file | Upload the NAS server homedir file. (optional)

try:
    # Upload File
    api_instance.nas_server_id_upload_homedir_post(id, body=body)
except ApiException as e:
    print("Exception when calling NasServerApi->nas_server_id_upload_homedir_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. name:{name} can be used instead of {id}. | 
 **body** | **file**| Upload the NAS server homedir file. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_server_id_upload_hosts_post**
> nas_server_id_upload_hosts_post(id, body=body)

Upload File

Upload NAS server host file.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NasServerApi()
id = 'id_example' # str | Unique identifier of the NAS server. name:{name} can be used instead of {id}.
body = '/path/to/file.txt' # file | Upload NAS server host file. (optional)

try:
    # Upload File
    api_instance.nas_server_id_upload_hosts_post(id, body=body)
except ApiException as e:
    print("Exception when calling NasServerApi->nas_server_id_upload_hosts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. name:{name} can be used instead of {id}. | 
 **body** | **file**| Upload NAS server host file. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_server_id_upload_netgroup_post**
> nas_server_id_upload_netgroup_post(id, body=body)

Upload File

Upload the NAS server netgroup file.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NasServerApi()
id = 'id_example' # str | Unique identifier of the NAS server. name:{name} can be used instead of {id}.
body = '/path/to/file.txt' # file | Upload the NAS server netgroup file. (optional)

try:
    # Upload File
    api_instance.nas_server_id_upload_netgroup_post(id, body=body)
except ApiException as e:
    print("Exception when calling NasServerApi->nas_server_id_upload_netgroup_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. name:{name} can be used instead of {id}. | 
 **body** | **file**| Upload the NAS server netgroup file. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_server_id_upload_nsswitch_post**
> nas_server_id_upload_nsswitch_post(id, body=body)

Upload File

Upload the NAS server nsswitch file.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NasServerApi()
id = 'id_example' # str | Unique identifier of the NAS server. name:{name} can be used instead of {id}.
body = '/path/to/file.txt' # file | Upload the NAS server nsswitch file. (optional)

try:
    # Upload File
    api_instance.nas_server_id_upload_nsswitch_post(id, body=body)
except ApiException as e:
    print("Exception when calling NasServerApi->nas_server_id_upload_nsswitch_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. name:{name} can be used instead of {id}. | 
 **body** | **file**| Upload the NAS server nsswitch file. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_server_id_upload_ntxmap_post**
> nas_server_id_upload_ntxmap_post(id, body=body)

Upload File

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NasServerApi()
id = 'id_example' # str | Unique identifier of the NAS server. name:{name} can be used instead of {id}.
body = '/path/to/file.txt' # file | Upload the NAS server ntxmap file. (optional)

try:
    # Upload File
    api_instance.nas_server_id_upload_ntxmap_post(id, body=body)
except ApiException as e:
    print("Exception when calling NasServerApi->nas_server_id_upload_ntxmap_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. name:{name} can be used instead of {id}. | 
 **body** | **file**| Upload the NAS server ntxmap file. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_server_id_upload_passwd_post**
> nas_server_id_upload_passwd_post(id, body=body)

Upload File

Upload NAS server passwd file.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NasServerApi()
id = 'id_example' # str | Unique identifier of the NAS server. name:{name} can be used instead of {id}.
body = '/path/to/file.txt' # file | Upload NAS server passwd file. (optional)

try:
    # Upload File
    api_instance.nas_server_id_upload_passwd_post(id, body=body)
except ApiException as e:
    print("Exception when calling NasServerApi->nas_server_id_upload_passwd_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NAS server. name:{name} can be used instead of {id}. | 
 **body** | **file**| Upload NAS server passwd file. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nas_server_post**
> CreateResponse nas_server_post(body)

Create

Create a NAS server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NasServerApi()
body = prime.swagger_client.NasServerCreate() # NasServerCreate | 

try:
    # Create
    api_response = api_instance.nas_server_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasServerApi->nas_server_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NasServerCreate**](NasServerCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

