# prime.swagger_client.FileLdapApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_ldap_get**](FileLdapApi.md#file_ldap_get) | **GET** /file_ldap | Collection Query
[**file_ldap_id_delete**](FileLdapApi.md#file_ldap_id_delete) | **DELETE** /file_ldap/{id} | Delete
[**file_ldap_id_download_certificate_get**](FileLdapApi.md#file_ldap_id_download_certificate_get) | **GET** /file_ldap/{id}/download_certificate | Download Certificate
[**file_ldap_id_download_config_get**](FileLdapApi.md#file_ldap_id_download_config_get) | **GET** /file_ldap/{id}/download_config | Download Config
[**file_ldap_id_get**](FileLdapApi.md#file_ldap_id_get) | **GET** /file_ldap/{id} | Instance Query
[**file_ldap_id_patch**](FileLdapApi.md#file_ldap_id_patch) | **PATCH** /file_ldap/{id} | Modify
[**file_ldap_id_upload_certificate_post**](FileLdapApi.md#file_ldap_id_upload_certificate_post) | **POST** /file_ldap/{id}/upload_certificate | Upload Certificate
[**file_ldap_id_upload_config_post**](FileLdapApi.md#file_ldap_id_upload_config_post) | **POST** /file_ldap/{id}/upload_config | Upload Config
[**file_ldap_post**](FileLdapApi.md#file_ldap_post) | **POST** /file_ldap | Create


# **file_ldap_get**
> list[FileLdapInstance] file_ldap_get()

Collection Query

List LDAP Service instances.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileLdapApi()

try:
    # Collection Query
    api_response = api_instance.file_ldap_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileLdapApi->file_ldap_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileLdapInstance]**](FileLdapInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ldap_id_delete**
> file_ldap_id_delete(id)

Delete

Delete a NAS Server's LDAP settings.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileLdapApi()
id = 'id_example' # str | LDAP settings object Id.

try:
    # Delete
    api_instance.file_ldap_id_delete(id)
except ApiException as e:
    print("Exception when calling FileLdapApi->file_ldap_id_delete: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ldap_id_download_certificate_get**
> FileLdapCertificateFile file_ldap_id_download_certificate_get(id)

Download Certificate

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileLdapApi()
id = 'id_example' # str | Unique identifier of the LDAP settings object.

try:
    # Download Certificate
    api_response = api_instance.file_ldap_id_download_certificate_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileLdapApi->file_ldap_id_download_certificate_get: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: document/text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ldap_id_download_config_get**
> FileLdapConfigFile file_ldap_id_download_config_get(id)

Download Config

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileLdapApi()
id = 'id_example' # str | Unique identifier of the LDAP settings object.

try:
    # Download Config
    api_response = api_instance.file_ldap_id_download_config_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileLdapApi->file_ldap_id_download_config_get: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: document/text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ldap_id_get**
> FileLdapInstance file_ldap_id_get(id)

Instance Query

Query a specific NAS Server's LDAP settings object.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileLdapApi()
id = 'id_example' # str | Unique identifier of the LDAP settings object.

try:
    # Instance Query
    api_response = api_instance.file_ldap_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileLdapApi->file_ldap_id_get: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ldap_id_patch**
> file_ldap_id_patch(id, body)

Modify

Modify a NAS Server's LDAP settings object.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileLdapApi()
id = 'id_example' # str | Unique identifier of the LDAP settings object id.
body = prime.swagger_client.FileLdapModify() # FileLdapModify | 

try:
    # Modify
    api_instance.file_ldap_id_patch(id, body)
except ApiException as e:
    print("Exception when calling FileLdapApi->file_ldap_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the LDAP settings object id. | 
 **body** | [**FileLdapModify**](FileLdapModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ldap_id_upload_certificate_post**
> file_ldap_id_upload_certificate_post(id, body)

Upload Certificate

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileLdapApi()
id = 'id_example' # str | Unique identifier of the LDAP settings object.
body = '/path/to/file.txt' # file | 

try:
    # Upload Certificate
    api_instance.file_ldap_id_upload_certificate_post(id, body)
except ApiException as e:
    print("Exception when calling FileLdapApi->file_ldap_id_upload_certificate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the LDAP settings object. | 
 **body** | **file**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ldap_id_upload_config_post**
> file_ldap_id_upload_config_post(id, body)

Upload Config

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileLdapApi()
id = 'id_example' # str | Unique identifier of the LDAP settings object.
body = '/path/to/file.txt' # file | 

try:
    # Upload Config
    api_instance.file_ldap_id_upload_config_post(id, body)
except ApiException as e:
    print("Exception when calling FileLdapApi->file_ldap_id_upload_config_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the LDAP settings object. | 
 **body** | **file**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_ldap_post**
> CreateResponse file_ldap_post(body)

Create

Create an LDAP service on a NAS Server. Only one LDAP Service object can be created per NAS Server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileLdapApi()
body = prime.swagger_client.FileLdapCreate() # FileLdapCreate | Name of the LDAP service to create.

try:
    # Create
    api_response = api_instance.file_ldap_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileLdapApi->file_ldap_post: %s\n" % e)
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

