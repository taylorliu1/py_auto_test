# prime.swagger_client.SmbServerApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**smb_server_get**](SmbServerApi.md#smb_server_get) | **GET** /smb_server | Collection Query
[**smb_server_id_delete**](SmbServerApi.md#smb_server_id_delete) | **DELETE** /smb_server/{id} | Delete
[**smb_server_id_get**](SmbServerApi.md#smb_server_id_get) | **GET** /smb_server/{id} | Instance Query
[**smb_server_id_join_post**](SmbServerApi.md#smb_server_id_join_post) | **POST** /smb_server/{id}/join | Domain Join
[**smb_server_id_patch**](SmbServerApi.md#smb_server_id_patch) | **PATCH** /smb_server/{id} | Modify
[**smb_server_id_unjoin_post**](SmbServerApi.md#smb_server_id_unjoin_post) | **POST** /smb_server/{id}/unjoin | Domain Unjoin
[**smb_server_post**](SmbServerApi.md#smb_server_post) | **POST** /smb_server | Create


# **smb_server_get**
> list[SmbServerInstance] smb_server_get()

Collection Query

Query all SMB servers.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SmbServerApi()

try:
    # Collection Query
    api_response = api_instance.smb_server_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmbServerApi->smb_server_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SmbServerInstance]**](SmbServerInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smb_server_id_delete**
> smb_server_id_delete(id, body=body)

Delete

Delete a SMB server. The SMB server must not be joined to a domain to be deleted. 

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SmbServerApi()
id = 'id_example' # str | Unique identifier of the SMB server.
body = prime.swagger_client.SmbServerDelete() # SmbServerDelete |  (optional)

try:
    # Delete
    api_instance.smb_server_id_delete(id, body=body)
except ApiException as e:
    print("Exception when calling SmbServerApi->smb_server_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the SMB server. | 
 **body** | [**SmbServerDelete**](SmbServerDelete.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smb_server_id_get**
> SmbServerInstance smb_server_id_get(id)

Instance Query

Query settings of a specific SMB server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SmbServerApi()
id = 'id_example' # str | Unique identifier of the SMB server.

try:
    # Instance Query
    api_response = api_instance.smb_server_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmbServerApi->smb_server_id_get: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smb_server_id_join_post**
> smb_server_id_join_post(id, body)

Domain Join

Join the SMB server to an Active Directory domain.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SmbServerApi()
id = 'id_example' # str | Unique identifier of the SMB server.
body = prime.swagger_client.SmbServerJoin() # SmbServerJoin | 

try:
    # Domain Join
    api_instance.smb_server_id_join_post(id, body)
except ApiException as e:
    print("Exception when calling SmbServerApi->smb_server_id_join_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the SMB server. | 
 **body** | [**SmbServerJoin**](SmbServerJoin.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smb_server_id_patch**
> smb_server_id_patch(id, body)

Modify

Modify an SMB server's settings.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SmbServerApi()
id = 'id_example' # str | Unique identifier of the SMB server.
body = prime.swagger_client.SmbServerModify() # SmbServerModify | 

try:
    # Modify
    api_instance.smb_server_id_patch(id, body)
except ApiException as e:
    print("Exception when calling SmbServerApi->smb_server_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the SMB server. | 
 **body** | [**SmbServerModify**](SmbServerModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smb_server_id_unjoin_post**
> smb_server_id_unjoin_post(id, body)

Domain Unjoin

Unjoin the SMB server from an Active Directory domain.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SmbServerApi()
id = 'id_example' # str | Unique identifier of the SMB server.
body = prime.swagger_client.SmbServerUnjoin() # SmbServerUnjoin | 

try:
    # Domain Unjoin
    api_instance.smb_server_id_unjoin_post(id, body)
except ApiException as e:
    print("Exception when calling SmbServerApi->smb_server_id_unjoin_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the SMB server. | 
 **body** | [**SmbServerUnjoin**](SmbServerUnjoin.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smb_server_post**
> CreateResponse smb_server_post(body)

Create

Create an SMB server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SmbServerApi()
body = prime.swagger_client.SmbServerCreate() # SmbServerCreate | 

try:
    # Create
    api_response = api_instance.smb_server_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmbServerApi->smb_server_post: %s\n" % e)
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

