# prime.swagger_client.NfsExportApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nfs_export_get**](NfsExportApi.md#nfs_export_get) | **GET** /nfs_export | Collection Query
[**nfs_export_id_delete**](NfsExportApi.md#nfs_export_id_delete) | **DELETE** /nfs_export/{id} | Delete
[**nfs_export_id_get**](NfsExportApi.md#nfs_export_id_get) | **GET** /nfs_export/{id} | Instance Query
[**nfs_export_id_patch**](NfsExportApi.md#nfs_export_id_patch) | **PATCH** /nfs_export/{id} | Modify
[**nfs_export_post**](NfsExportApi.md#nfs_export_post) | **POST** /nfs_export | Create


# **nfs_export_get**
> list[NfsExportInstance] nfs_export_get()

Collection Query

List NFS Exports.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NfsExportApi()

try:
    # Collection Query
    api_response = api_instance.nfs_export_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsExportApi->nfs_export_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NfsExportInstance]**](NfsExportInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nfs_export_id_delete**
> nfs_export_id_delete(id)

Delete

Delete NFS Export.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NfsExportApi()
id = 'id_example' # str | NFS Export object id. name:{name} can be used instead of {id}.

try:
    # Delete
    api_instance.nfs_export_id_delete(id)
except ApiException as e:
    print("Exception when calling NfsExportApi->nfs_export_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| NFS Export object id. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nfs_export_id_get**
> NfsExportInstance nfs_export_id_get(id)

Instance Query

Get NFS Export properties.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NfsExportApi()
id = 'id_example' # str | NFS Export object id. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.nfs_export_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsExportApi->nfs_export_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| NFS Export object id. name:{name} can be used instead of {id}. | 

### Return type

[**NfsExportInstance**](NfsExportInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nfs_export_id_patch**
> nfs_export_id_patch(id, body)

Modify

Modify NFS Export Properties.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NfsExportApi()
id = 'id_example' # str | NFS Export object id. name:{name} can be used instead of {id}.
body = prime.swagger_client.NfsExportModify() # NfsExportModify | 

try:
    # Modify
    api_instance.nfs_export_id_patch(id, body)
except ApiException as e:
    print("Exception when calling NfsExportApi->nfs_export_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| NFS Export object id. name:{name} can be used instead of {id}. | 
 **body** | [**NfsExportModify**](NfsExportModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nfs_export_post**
> CreateResponse nfs_export_post(body)

Create

Create an NFS Export for a Snapshot.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.NfsExportApi()
body = prime.swagger_client.NfsExportCreate() # NfsExportCreate | 

try:
    # Create
    api_response = api_instance.nfs_export_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NfsExportApi->nfs_export_post: %s\n" % e)
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

