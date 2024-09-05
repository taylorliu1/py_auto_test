# swagger_client.SmbServersApi

All URIs are relative to *https://10.226.47.34/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**smb_servers_get**](SmbServersApi.md#smb_servers_get) | **GET** /smb-servers | Collection Query
[**smb_servers_id_delete**](SmbServersApi.md#smb_servers_id_delete) | **DELETE** /smb-servers/{id} | Delete
[**smb_servers_id_get**](SmbServersApi.md#smb_servers_id_get) | **GET** /smb-servers/{id} | Instance Query
[**smb_servers_id_join_post**](SmbServersApi.md#smb_servers_id_join_post) | **POST** /smb-servers/{id}/join | Domain Join
[**smb_servers_id_patch**](SmbServersApi.md#smb_servers_id_patch) | **PATCH** /smb-servers/{id} | Modify
[**smb_servers_id_skip_unjoin_and_delete_post**](SmbServersApi.md#smb_servers_id_skip_unjoin_and_delete_post) | **POST** /smb-servers/{id}/skip-unjoin-and-delete | Skip Unjoin and Delete
[**smb_servers_id_unjoin_post**](SmbServersApi.md#smb_servers_id_unjoin_post) | **POST** /smb-servers/{id}/unjoin | Domain Unjoin
[**smb_servers_post**](SmbServersApi.md#smb_servers_post) | **POST** /smb-servers | Create

# **smb_servers_get**
> list[SmbServerInstance] smb_servers_get()

Collection Query

Query all SMB servers.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SmbServersApi()

try:
    # Collection Query
    api_response = api_instance.smb_servers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmbServersApi->smb_servers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SmbServerInstance]**](SmbServerInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smb_servers_id_delete**
> smb_servers_id_delete(id)

Delete

Delete a SMB server. The SMB server must not be joined to a domain to be deleted. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SmbServersApi()
id = 'id_example' # str | Unique identifier of the SMB server.

try:
    # Delete
    api_instance.smb_servers_id_delete(id)
except ApiException as e:
    print("Exception when calling SmbServersApi->smb_servers_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the SMB server. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smb_servers_id_get**
> SmbServerInstance smb_servers_id_get(id)

Instance Query

Query settings of a specific SMB server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SmbServersApi()
id = 'id_example' # str | Unique identifier of the SMB server.

try:
    # Instance Query
    api_response = api_instance.smb_servers_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmbServersApi->smb_servers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the SMB server. | 

### Return type

[**SmbServerInstance**](SmbServerInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smb_servers_id_join_post**
> smb_servers_id_join_post(body, id)

Domain Join

Join the SMB server to an Active Directory domain.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SmbServersApi()
body = swagger_client.SmbServerJoin() # SmbServerJoin | 
id = 'id_example' # str | Unique identifier of the SMB server.

try:
    # Domain Join
    api_instance.smb_servers_id_join_post(body, id)
except ApiException as e:
    print("Exception when calling SmbServersApi->smb_servers_id_join_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SmbServerJoin**](SmbServerJoin.md)|  | 
 **id** | **str**| Unique identifier of the SMB server. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smb_servers_id_patch**
> smb_servers_id_patch(body, id)

Modify

Modify an SMB server's settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SmbServersApi()
body = swagger_client.SmbServerModify() # SmbServerModify | 
id = 'id_example' # str | Unique identifier of the SMB server.

try:
    # Modify
    api_instance.smb_servers_id_patch(body, id)
except ApiException as e:
    print("Exception when calling SmbServersApi->smb_servers_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SmbServerModify**](SmbServerModify.md)|  | 
 **id** | **str**| Unique identifier of the SMB server. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smb_servers_id_skip_unjoin_and_delete_post**
> smb_servers_id_skip_unjoin_and_delete_post(id)

Skip Unjoin and Delete

Skip unjoin from AD domain and Delete a SMB server. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SmbServersApi()
id = 'id_example' # str | Unique identifier of the SMB server.

try:
    # Skip Unjoin and Delete
    api_instance.smb_servers_id_skip_unjoin_and_delete_post(id)
except ApiException as e:
    print("Exception when calling SmbServersApi->smb_servers_id_skip_unjoin_and_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the SMB server. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smb_servers_id_unjoin_post**
> smb_servers_id_unjoin_post(body, id)

Domain Unjoin

Unjoin the SMB server from an Active Directory domain.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SmbServersApi()
body = swagger_client.SmbServerUnjoin() # SmbServerUnjoin | 
id = 'id_example' # str | Unique identifier of the SMB server.

try:
    # Domain Unjoin
    api_instance.smb_servers_id_unjoin_post(body, id)
except ApiException as e:
    print("Exception when calling SmbServersApi->smb_servers_id_unjoin_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SmbServerUnjoin**](SmbServerUnjoin.md)|  | 
 **id** | **str**| Unique identifier of the SMB server. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smb_servers_post**
> CreateResponse smb_servers_post(body)

Create

Create an SMB server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SmbServersApi()
body = swagger_client.SmbServerCreate() # SmbServerCreate | 

try:
    # Create
    api_response = api_instance.smb_servers_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmbServersApi->smb_servers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SmbServerCreate**](SmbServerCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

