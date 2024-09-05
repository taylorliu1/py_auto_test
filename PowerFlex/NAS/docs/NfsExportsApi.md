# swagger_client.NfsExportsApi

All URIs are relative to *https://10.226.47.34/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nfs_exports_get**](NfsExportsApi.md#nfs_exports_get) | **GET** /nfs-exports | Collection Query
[**nfs_exports_id_delete**](NfsExportsApi.md#nfs_exports_id_delete) | **DELETE** /nfs-exports/{id} | Delete
[**nfs_exports_id_get**](NfsExportsApi.md#nfs_exports_id_get) | **GET** /nfs-exports/{id} | Instance Query
[**nfs_exports_id_patch**](NfsExportsApi.md#nfs_exports_id_patch) | **PATCH** /nfs-exports/{id} | Modify
[**nfs_exports_post**](NfsExportsApi.md#nfs_exports_post) | **POST** /nfs-exports | Create

# **nfs_exports_get**
> list[NfsExportInstance] nfs_exports_get()

Collection Query

List NFS Exports.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NfsExportsApi()

try:
    # Collection Query
    api_response = api_instance.nfs_exports_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsExportsApi->nfs_exports_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NfsExportInstance]**](NfsExportInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nfs_exports_id_delete**
> nfs_exports_id_delete(id)

Delete

Delete NFS Export.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NfsExportsApi()
id = 'id_example' # str | NFS Export object id.

try:
    # Delete
    api_instance.nfs_exports_id_delete(id)
except ApiException as e:
    print("Exception when calling NfsExportsApi->nfs_exports_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| NFS Export object id. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nfs_exports_id_get**
> NfsExportInstance nfs_exports_id_get(id)

Instance Query

Get NFS Export properties.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NfsExportsApi()
id = 'id_example' # str | NFS Export object id.

try:
    # Instance Query
    api_response = api_instance.nfs_exports_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsExportsApi->nfs_exports_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| NFS Export object id. | 

### Return type

[**NfsExportInstance**](NfsExportInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nfs_exports_id_patch**
> nfs_exports_id_patch(body, id)

Modify

Modify NFS Export Properties.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NfsExportsApi()
body = swagger_client.NfsExportModify() # NfsExportModify | 
id = 'id_example' # str | NFS Export object id.

try:
    # Modify
    api_instance.nfs_exports_id_patch(body, id)
except ApiException as e:
    print("Exception when calling NfsExportsApi->nfs_exports_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NfsExportModify**](NfsExportModify.md)|  | 
 **id** | **str**| NFS Export object id. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nfs_exports_post**
> CreateResponse nfs_exports_post(body)

Create

Create an NFS Export for a Snapshot.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NfsExportsApi()
body = swagger_client.NfsExportCreate() # NfsExportCreate | 

try:
    # Create
    api_response = api_instance.nfs_exports_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsExportsApi->nfs_exports_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NfsExportCreate**](NfsExportCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

