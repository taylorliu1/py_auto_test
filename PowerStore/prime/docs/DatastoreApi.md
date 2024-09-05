# prime.swagger_client.DatastoreApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datastore_get**](DatastoreApi.md#datastore_get) | **GET** /datastore | Collection Query
[**datastore_id_get**](DatastoreApi.md#datastore_id_get) | **GET** /datastore/{id} | Instance Query


# **datastore_get**
> list[DatastoreInstance] datastore_get()

Collection Query

Query existing datastores that use storage from the storage system. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.DatastoreApi()

try:
    # Collection Query
    api_response = api_instance.datastore_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatastoreApi->datastore_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DatastoreInstance]**](DatastoreInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datastore_id_get**
> DatastoreInstance datastore_id_get(id)

Instance Query

Query a specific datastore instance. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.DatastoreApi()
id = 'id_example' # str | Unique identifier of the datastore to query. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.datastore_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatastoreApi->datastore_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the datastore to query. name:{name} can be used instead of {id}. | 

### Return type

[**DatastoreInstance**](DatastoreInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

