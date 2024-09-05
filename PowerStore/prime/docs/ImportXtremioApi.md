# prime.swagger_client.ImportXtremioApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_xtremio_get**](ImportXtremioApi.md#import_xtremio_get) | **GET** /import_xtremio | Collection Query
[**import_xtremio_id_discover_post**](ImportXtremioApi.md#import_xtremio_id_discover_post) | **POST** /import_xtremio/{id}/discover | Discover the importable volumes and consistency groups
[**import_xtremio_id_get**](ImportXtremioApi.md#import_xtremio_id_get) | **GET** /import_xtremio/{id} | Instance Query


# **import_xtremio_get**
> list[ImportXtremioInstance] import_xtremio_get()

Collection Query

Query XtremIO storage systems X1 and X2. Was added in version 1.0.2.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportXtremioApi()

try:
    # Collection Query
    api_response = api_instance.import_xtremio_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportXtremioApi->import_xtremio_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ImportXtremioInstance]**](ImportXtremioInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_xtremio_id_discover_post**
> import_xtremio_id_discover_post(id)

Discover the importable volumes and consistency groups

Discover the importable volumes and consistency groups in the XtremIO storage system. Was added in version 1.0.2. Was deprecated in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportXtremioApi()
id = 'id_example' # str | Unique identifier of the XtremIO storage system. name:{name} can be used instead of {id}.

try:
    # Discover the importable volumes and consistency groups
    api_instance.import_xtremio_id_discover_post(id)
except ApiException as e:
    print("Exception when calling ImportXtremioApi->import_xtremio_id_discover_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the XtremIO storage system. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_xtremio_id_get**
> ImportXtremioInstance import_xtremio_id_get(id)

Instance Query

Query a specific XtremIO storage system. Was added in version 1.0.2.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.ImportXtremioApi()
id = 'id_example' # str | Unique identifier of the XtremIO storage system. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.import_xtremio_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportXtremioApi->import_xtremio_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the XtremIO storage system. name:{name} can be used instead of {id}. | 

### Return type

[**ImportXtremioInstance**](ImportXtremioInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

