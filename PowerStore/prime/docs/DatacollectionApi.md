# prime.swagger_client.DatacollectionApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datacollection_get**](DatacollectionApi.md#datacollection_get) | **GET** /datacollection | Collection Query
[**datacollection_id_delete**](DatacollectionApi.md#datacollection_id_delete) | **DELETE** /datacollection/{id} | Delete
[**datacollection_id_get**](DatacollectionApi.md#datacollection_id_get) | **GET** /datacollection/{id} | Instance Query
[**datacollection_id_upload_post**](DatacollectionApi.md#datacollection_id_upload_post) | **POST** /datacollection/{id}/upload | Upload
[**datacollection_post**](DatacollectionApi.md#datacollection_post) | **POST** /datacollection | Create


# **datacollection_get**
> list[DatacollectionInstance] datacollection_get()

Collection Query

List data collections. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.DatacollectionApi()

try:
    # Collection Query
    api_response = api_instance.datacollection_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatacollectionApi->datacollection_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DatacollectionInstance]**](DatacollectionInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datacollection_id_delete**
> datacollection_id_delete(id)

Delete

Delete the specified data collection. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.DatacollectionApi()
id = 'id_example' # str | Unique identifier for an instance. Was added in version 3.0.0.0.

try:
    # Delete
    api_instance.datacollection_id_delete(id)
except ApiException as e:
    print("Exception when calling DatacollectionApi->datacollection_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for an instance. Was added in version 3.0.0.0. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datacollection_id_get**
> DatacollectionInstance datacollection_id_get(id)

Instance Query

Query data collection instance. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.DatacollectionApi()
id = 'id_example' # str | Unique identifier for an instance. Was added in version 3.0.0.0.

try:
    # Instance Query
    api_response = api_instance.datacollection_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatacollectionApi->datacollection_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for an instance. Was added in version 3.0.0.0. | 

### Return type

[**DatacollectionInstance**](DatacollectionInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datacollection_id_upload_post**
> datacollection_id_upload_post(id, body=body)

Upload

Upload a data collection to your service provider. This operation is only available if SupportAssist is enabled. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.DatacollectionApi()
id = 'id_example' # str | Unique identifier for an instance. Was added in version 3.0.0.0.
body = prime.swagger_client.DatacollectionUpload() # DatacollectionUpload |  (optional)

try:
    # Upload
    api_instance.datacollection_id_upload_post(id, body=body)
except ApiException as e:
    print("Exception when calling DatacollectionApi->datacollection_id_upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for an instance. Was added in version 3.0.0.0. | 
 **body** | [**DatacollectionUpload**](DatacollectionUpload.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datacollection_post**
> CreateResponse datacollection_post(body=body)

Create

Create a new datacollection by collecting and bundling support materials. Only one datacollection create may be running at a time. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.DatacollectionApi()
body = prime.swagger_client.DatacollectionCreate() # DatacollectionCreate |  (optional)

try:
    # Create
    api_response = api_instance.datacollection_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatacollectionApi->datacollection_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DatacollectionCreate**](DatacollectionCreate.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

