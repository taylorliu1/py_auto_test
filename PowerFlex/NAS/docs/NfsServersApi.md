# swagger_client.NfsServersApi

All URIs are relative to *https://10.226.47.34/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nfs_servers_get**](NfsServersApi.md#nfs_servers_get) | **GET** /nfs-servers | Collection Query
[**nfs_servers_id_delete**](NfsServersApi.md#nfs_servers_id_delete) | **DELETE** /nfs-servers/{id} | Delete
[**nfs_servers_id_get**](NfsServersApi.md#nfs_servers_id_get) | **GET** /nfs-servers/{id} | Instance Query
[**nfs_servers_id_join_post**](NfsServersApi.md#nfs_servers_id_join_post) | **POST** /nfs-servers/{id}/join | Join Active Directory (AD) Domain
[**nfs_servers_id_patch**](NfsServersApi.md#nfs_servers_id_patch) | **PATCH** /nfs-servers/{id} | Modify
[**nfs_servers_id_skip_unjoin_and_delete_post**](NfsServersApi.md#nfs_servers_id_skip_unjoin_and_delete_post) | **POST** /nfs-servers/{id}/skip-unjoin-and-delete | Unjoin domain and delete NFS server.
[**nfs_servers_id_unjoin_post**](NfsServersApi.md#nfs_servers_id_unjoin_post) | **POST** /nfs-servers/{id}/unjoin | Unjoin Active Directory (AD) Domain
[**nfs_servers_post**](NfsServersApi.md#nfs_servers_post) | **POST** /nfs-servers | Create

# **nfs_servers_get**
> list[NfsServerInstance] nfs_servers_get()

Collection Query

Query all NFS Servers.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NfsServersApi()

try:
    # Collection Query
    api_response = api_instance.nfs_servers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsServersApi->nfs_servers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NfsServerInstance]**](NfsServerInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nfs_servers_id_delete**
> nfs_servers_id_delete(id)

Delete

Delete an NFS server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NfsServersApi()
id = 'id_example' # str | Unique identifier of the NFS server.

try:
    # Delete
    api_instance.nfs_servers_id_delete(id)
except ApiException as e:
    print("Exception when calling NfsServersApi->nfs_servers_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NFS server. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nfs_servers_id_get**
> NfsServerInstance nfs_servers_id_get(id)

Instance Query

Query settings of an NFS server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NfsServersApi()
id = 'id_example' # str | Unique identifier of the NFS server.

try:
    # Instance Query
    api_response = api_instance.nfs_servers_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsServersApi->nfs_servers_id_get: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nfs_servers_id_join_post**
> nfs_servers_id_join_post(body, id)

Join Active Directory (AD) Domain

Join the secure NFS server to the NAS server's AD domain, which is necessary for Secure NFS.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NfsServersApi()
body = swagger_client.NfsServerJoin() # NfsServerJoin | 
id = 'id_example' # str | Unique identifier of the NFS server.

try:
    # Join Active Directory (AD) Domain
    api_instance.nfs_servers_id_join_post(body, id)
except ApiException as e:
    print("Exception when calling NfsServersApi->nfs_servers_id_join_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NfsServerJoin**](NfsServerJoin.md)|  | 
 **id** | **str**| Unique identifier of the NFS server. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nfs_servers_id_patch**
> nfs_servers_id_patch(body, id)

Modify

Modify NFS server settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NfsServersApi()
body = swagger_client.NfsServerModify() # NfsServerModify | 
id = 'id_example' # str | Unique identifier of the NFS server.

try:
    # Modify
    api_instance.nfs_servers_id_patch(body, id)
except ApiException as e:
    print("Exception when calling NfsServersApi->nfs_servers_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NfsServerModify**](NfsServerModify.md)|  | 
 **id** | **str**| Unique identifier of the NFS server. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nfs_servers_id_skip_unjoin_and_delete_post**
> nfs_servers_id_skip_unjoin_and_delete_post(id)

Unjoin domain and delete NFS server.

Unjoin domain from NFS Server and delete the NFS Server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NfsServersApi()
id = 'id_example' # str | Unique identifier of the NFS server.

try:
    # Unjoin domain and delete NFS server.
    api_instance.nfs_servers_id_skip_unjoin_and_delete_post(id)
except ApiException as e:
    print("Exception when calling NfsServersApi->nfs_servers_id_skip_unjoin_and_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the NFS server. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nfs_servers_id_unjoin_post**
> nfs_servers_id_unjoin_post(body, id)

Unjoin Active Directory (AD) Domain

Unjoin the secure NFS server from the NAS server's Active Directory domain. If you unjoin with secure NFS exports active, exports will be unavailable to the clients.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NfsServersApi()
body = swagger_client.NfsServerUnjoin() # NfsServerUnjoin | 
id = 'id_example' # str | Unique identifier of the NFS server.

try:
    # Unjoin Active Directory (AD) Domain
    api_instance.nfs_servers_id_unjoin_post(body, id)
except ApiException as e:
    print("Exception when calling NfsServersApi->nfs_servers_id_unjoin_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NfsServerUnjoin**](NfsServerUnjoin.md)|  | 
 **id** | **str**| Unique identifier of the NFS server. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nfs_servers_post**
> CreateResponse nfs_servers_post(body)

Create

Create an NFS server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NfsServersApi()
body = swagger_client.NfsServerCreate() # NfsServerCreate | 

try:
    # Create
    api_response = api_instance.nfs_servers_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsServersApi->nfs_servers_post: %s\n" % e)
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

