# swagger_client.FileLdapServersApi

All URIs are relative to *https://10.226.47.34/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_ldap_servers_get**](FileLdapServersApi.md#file_ldap_servers_get) | **GET** /file-ldap-servers | Collection Query
[**file_ldap_servers_id_delete**](FileLdapServersApi.md#file_ldap_servers_id_delete) | **DELETE** /file-ldap-servers/{id} | Delete
[**file_ldap_servers_id_get**](FileLdapServersApi.md#file_ldap_servers_id_get) | **GET** /file-ldap-servers/{id} | Instance Query
[**file_ldap_servers_id_patch**](FileLdapServersApi.md#file_ldap_servers_id_patch) | **PATCH** /file-ldap-servers/{id} | Modify
[**file_ldap_servers_post**](FileLdapServersApi.md#file_ldap_servers_post) | **POST** /file-ldap-servers | Create
[**files_file_ldap_servers_id_certificate_get**](FileLdapServersApi.md#files_file_ldap_servers_id_certificate_get) | **GET** /files/file-ldap-servers/{id}/certificate | Download Certificate
[**files_file_ldap_servers_id_certificate_post**](FileLdapServersApi.md#files_file_ldap_servers_id_certificate_post) | **POST** /files/file-ldap-servers/{id}/certificate | Upload Certificate
[**files_file_ldap_servers_id_config_get**](FileLdapServersApi.md#files_file_ldap_servers_id_config_get) | **GET** /files/file-ldap-servers/{id}/config | Download Config
[**files_file_ldap_servers_id_config_post**](FileLdapServersApi.md#files_file_ldap_servers_id_config_post) | **POST** /files/file-ldap-servers/{id}/config | Upload Config

# **file_ldap_servers_get**
> list[FileLdapInstance] file_ldap_servers_get()

Collection Query

List LDAP Service instances.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileLdapServersApi()

try:
    # Collection Query
    api_response = api_instance.file_ldap_servers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileLdapServersApi->file_ldap_servers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileLdapInstance]**](FileLdapInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ldap_servers_id_delete**
> file_ldap_servers_id_delete(id)

Delete

Delete a NAS Server's LDAP settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileLdapServersApi()
id = 'id_example' # str | LDAP settings object Id.

try:
    # Delete
    api_instance.file_ldap_servers_id_delete(id)
except ApiException as e:
    print("Exception when calling FileLdapServersApi->file_ldap_servers_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| LDAP settings object Id. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ldap_servers_id_get**
> FileLdapInstance file_ldap_servers_id_get(id)

Instance Query

Query a specific NAS Server's LDAP settings object.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileLdapServersApi()
id = 'id_example' # str | Unique identifier of the LDAP settings object.

try:
    # Instance Query
    api_response = api_instance.file_ldap_servers_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileLdapServersApi->file_ldap_servers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the LDAP settings object. | 

### Return type

[**FileLdapInstance**](FileLdapInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ldap_servers_id_patch**
> file_ldap_servers_id_patch(body, id)

Modify

Modify a NAS Server's LDAP settings object.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileLdapServersApi()
body = swagger_client.FileLdapModify() # FileLdapModify | 
id = 'id_example' # str | Unique identifier of the LDAP settings object id.

try:
    # Modify
    api_instance.file_ldap_servers_id_patch(body, id)
except ApiException as e:
    print("Exception when calling FileLdapServersApi->file_ldap_servers_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileLdapModify**](FileLdapModify.md)|  | 
 **id** | **str**| Unique identifier of the LDAP settings object id. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ldap_servers_post**
> CreateResponse file_ldap_servers_post(body)

Create

Create an LDAP service on a NAS Server. Only one LDAP Service object can be created per NAS Server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileLdapServersApi()
body = swagger_client.FileLdapCreate() # FileLdapCreate | Name of the LDAP service to create.

try:
    # Create
    api_response = api_instance.file_ldap_servers_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileLdapServersApi->file_ldap_servers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileLdapCreate**](FileLdapCreate.md)| Name of the LDAP service to create. | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_file_ldap_servers_id_certificate_get**
> FileLdapCertificateFile files_file_ldap_servers_id_certificate_get(id)

Download Certificate

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileLdapServersApi()
id = 'id_example' # str | Unique identifier of the LDAP settings object.

try:
    # Download Certificate
    api_response = api_instance.files_file_ldap_servers_id_certificate_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileLdapServersApi->files_file_ldap_servers_id_certificate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the LDAP settings object. | 

### Return type

[**FileLdapCertificateFile**](FileLdapCertificateFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: document/text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_file_ldap_servers_id_certificate_post**
> files_file_ldap_servers_id_certificate_post(body, id)

Upload Certificate

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileLdapServersApi()
body = 'body_example' # str | 
id = 'id_example' # str | Unique identifier of the LDAP settings object.

try:
    # Upload Certificate
    api_instance.files_file_ldap_servers_id_certificate_post(body, id)
except ApiException as e:
    print("Exception when calling FileLdapServersApi->files_file_ldap_servers_id_certificate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 
 **id** | **str**| Unique identifier of the LDAP settings object. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_file_ldap_servers_id_config_get**
> FileLdapConfigFile files_file_ldap_servers_id_config_get(id)

Download Config

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileLdapServersApi()
id = 'id_example' # str | Unique identifier of the LDAP settings object.

try:
    # Download Config
    api_response = api_instance.files_file_ldap_servers_id_config_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileLdapServersApi->files_file_ldap_servers_id_config_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the LDAP settings object. | 

### Return type

[**FileLdapConfigFile**](FileLdapConfigFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: document/text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_file_ldap_servers_id_config_post**
> files_file_ldap_servers_id_config_post(body, id)

Upload Config

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileLdapServersApi()
body = 'body_example' # str | 
id = 'id_example' # str | Unique identifier of the LDAP settings object.

try:
    # Upload Config
    api_instance.files_file_ldap_servers_id_config_post(body, id)
except ApiException as e:
    print("Exception when calling FileLdapServersApi->files_file_ldap_servers_id_config_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 
 **id** | **str**| Unique identifier of the LDAP settings object. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

