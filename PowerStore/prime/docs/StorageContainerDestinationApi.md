# prime.swagger_client.StorageContainerDestinationApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storage_container_destination_get**](StorageContainerDestinationApi.md#storage_container_destination_get) | **GET** /storage_container_destination | Collection Query
[**storage_container_destination_id_delete**](StorageContainerDestinationApi.md#storage_container_destination_id_delete) | **DELETE** /storage_container_destination/{id} | Delete
[**storage_container_destination_id_get**](StorageContainerDestinationApi.md#storage_container_destination_id_get) | **GET** /storage_container_destination/{id} | Instance Query
[**storage_container_destination_post**](StorageContainerDestinationApi.md#storage_container_destination_post) | **POST** /storage_container_destination | Create


# **storage_container_destination_get**
> list[StorageContainerDestinationInstance] storage_container_destination_get()

Collection Query

List storage container destinations. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.StorageContainerDestinationApi()

try:
    # Collection Query
    api_response = api_instance.storage_container_destination_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageContainerDestinationApi->storage_container_destination_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[StorageContainerDestinationInstance]**](StorageContainerDestinationInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_container_destination_id_delete**
> storage_container_destination_id_delete(id)

Delete

Delete a storage container destination. This operation doesn't affect replication sessions that have already started. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.StorageContainerDestinationApi()
id = 'id_example' # str | Unique identifier of the storage container destination to be deleted.

try:
    # Delete
    api_instance.storage_container_destination_id_delete(id)
except ApiException as e:
    print("Exception when calling StorageContainerDestinationApi->storage_container_destination_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the storage container destination to be deleted. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_container_destination_id_get**
> StorageContainerDestinationInstance storage_container_destination_id_get(id)

Instance Query

Get a specific storage container destination. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.StorageContainerDestinationApi()
id = 'id_example' # str | Id of the storage container destination.

try:
    # Instance Query
    api_response = api_instance.storage_container_destination_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageContainerDestinationApi->storage_container_destination_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the storage container destination. | 

### Return type

[**StorageContainerDestinationInstance**](StorageContainerDestinationInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_container_destination_post**
> CreateResponse storage_container_destination_post(body)

Create

Create a destination for the storage container. Combination of 'storage_container_id' and 'remote_system_id' must be unique as only one destination per remote system is allowed. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.StorageContainerDestinationApi()
body = prime.swagger_client.StorageContainerDestinationCreate() # StorageContainerDestinationCreate | 

try:
    # Create
    api_response = api_instance.storage_container_destination_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageContainerDestinationApi->storage_container_destination_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StorageContainerDestinationCreate**](StorageContainerDestinationCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

