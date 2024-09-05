# prime.swagger_client.NfsServerApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nfs_server_get**](NfsServerApi.md#nfs_server_get) | **GET** /nfs_server | Collection Query
[**nfs_server_id_delete**](NfsServerApi.md#nfs_server_id_delete) | **DELETE** /nfs_server/{id} | Delete
[**nfs_server_id_get**](NfsServerApi.md#nfs_server_id_get) | **GET** /nfs_server/{id} | Instance Query
[**nfs_server_id_join_post**](NfsServerApi.md#nfs_server_id_join_post) | **POST** /nfs_server/{id}/join | Join Active Directory (AD) Domain.
[**nfs_server_id_patch**](NfsServerApi.md#nfs_server_id_patch) | **PATCH** /nfs_server/{id} | Modify
[**nfs_server_id_unjoin_post**](NfsServerApi.md#nfs_server_id_unjoin_post) | **POST** /nfs_server/{id}/unjoin | Unjoin Active Directory (AD) Domain.
[**nfs_server_post**](NfsServerApi.md#nfs_server_post) | **POST** /nfs_server | Create


# **nfs_server_get**
> list[NfsServerInstance] nfs_server_get()

Collection Query

Query NFS Servers.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NfsServerApi()

try:
    # Collection Query
    api_response = api_instance.nfs_server_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsServerApi->nfs_server_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NfsServerInstance]**](NfsServerInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nfs_server_id_delete**
> nfs_server_id_delete(id, body=body)

Delete

Delete an NFS server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NfsServerApi()
id = 'id_example' # str | Unique identifier of the NFS server.
body = prime.swagger_client.NfsServerDelete() # NfsServerDelete |  (optional)

try:
    # Delete
    api_instance.nfs_server_id_delete(id, body=body)
except ApiException as e:
    print("Exception when calling NfsServerApi->nfs_server_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NFS server. | 
 **body** | [**NfsServerDelete**](NfsServerDelete.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nfs_server_id_get**
> NfsServerInstance nfs_server_id_get(id)

Instance Query

Query a specific NFS server setings instance.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NfsServerApi()
id = 'id_example' # str | Unique identifier of the NFS server.

try:
    # Instance Query
    api_response = api_instance.nfs_server_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsServerApi->nfs_server_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NFS server. | 

### Return type

[**NfsServerInstance**](NfsServerInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nfs_server_id_join_post**
> nfs_server_id_join_post(id, body)

Join Active Directory (AD) Domain.

Join the secure NFS server to the NAS server's AD domain, which is necessary for Secure NFS.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NfsServerApi()
id = 'id_example' # str | Unique identifier of the NFS server.
body = prime.swagger_client.NfsServerJoin() # NfsServerJoin | 

try:
    # Join Active Directory (AD) Domain.
    api_instance.nfs_server_id_join_post(id, body)
except ApiException as e:
    print("Exception when calling NfsServerApi->nfs_server_id_join_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NFS server. | 
 **body** | [**NfsServerJoin**](NfsServerJoin.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nfs_server_id_patch**
> nfs_server_id_patch(id, body)

Modify

Modify NFS server settings.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NfsServerApi()
id = 'id_example' # str | Unique identifier of the NFS server.
body = prime.swagger_client.NfsServerModify() # NfsServerModify | 

try:
    # Modify
    api_instance.nfs_server_id_patch(id, body)
except ApiException as e:
    print("Exception when calling NfsServerApi->nfs_server_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NFS server. | 
 **body** | [**NfsServerModify**](NfsServerModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nfs_server_id_unjoin_post**
> nfs_server_id_unjoin_post(id, body)

Unjoin Active Directory (AD) Domain.

Unjoin the secure NFS server from the NAS server's Active Directory domain. If you unjoin with secure NFS exports active, exports will be unavailable to the clients.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NfsServerApi()
id = 'id_example' # str | Unique identifier of the NFS server.
body = prime.swagger_client.NfsServerUnjoin() # NfsServerUnjoin | 

try:
    # Unjoin Active Directory (AD) Domain.
    api_instance.nfs_server_id_unjoin_post(id, body)
except ApiException as e:
    print("Exception when calling NfsServerApi->nfs_server_id_unjoin_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NFS server. | 
 **body** | [**NfsServerUnjoin**](NfsServerUnjoin.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nfs_server_post**
> CreateResponse nfs_server_post(body)

Create

Create an NFS server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NfsServerApi()
body = prime.swagger_client.NfsServerCreate() # NfsServerCreate | 

try:
    # Create
    api_response = api_instance.nfs_server_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsServerApi->nfs_server_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NfsServerCreate**](NfsServerCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

