# prime.swagger_client.FileDhsmConfigApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_dhsm_config_get**](FileDhsmConfigApi.md#file_dhsm_config_get) | **GET** /file_dhsm_config | Collection Query
[**file_dhsm_config_id_delete**](FileDhsmConfigApi.md#file_dhsm_config_id_delete) | **DELETE** /file_dhsm_config/{id} | Delete
[**file_dhsm_config_id_get**](FileDhsmConfigApi.md#file_dhsm_config_id_get) | **GET** /file_dhsm_config/{id} | Instance Query
[**file_dhsm_config_id_patch**](FileDhsmConfigApi.md#file_dhsm_config_id_patch) | **PATCH** /file_dhsm_config/{id} | Modify
[**file_dhsm_config_post**](FileDhsmConfigApi.md#file_dhsm_config_post) | **POST** /file_dhsm_config | Create


# **file_dhsm_config_get**
> list[FileDhsmConfigInstance] file_dhsm_config_get()

Collection Query

List configured DHSM server instances. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileDhsmConfigApi()

try:
    # Collection Query
    api_response = api_instance.file_dhsm_config_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileDhsmConfigApi->file_dhsm_config_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileDhsmConfigInstance]**](FileDhsmConfigInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_dhsm_config_id_delete**
> file_dhsm_config_id_delete(id)

Delete

Delete an DHSM server configuration instance of a NAS Server. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileDhsmConfigApi()
id = 'id_example' # str | Unique identifier of the DHSM server object.

try:
    # Delete
    api_instance.file_dhsm_config_id_delete(id)
except ApiException as e:
    print("Exception when calling FileDhsmConfigApi->file_dhsm_config_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the DHSM server object. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_dhsm_config_id_get**
> FileDhsmConfigInstance file_dhsm_config_id_get(id)

Instance Query

Query an DHSM server configuration instance. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileDhsmConfigApi()
id = 'id_example' # str | Unique identifier of the DHSM server object.

try:
    # Instance Query
    api_response = api_instance.file_dhsm_config_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileDhsmConfigApi->file_dhsm_config_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the DHSM server object. | 

### Return type

[**FileDhsmConfigInstance**](FileDhsmConfigInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_dhsm_config_id_patch**
> file_dhsm_config_id_patch(id, body)

Modify

Modify an DHSM server configuration instance. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileDhsmConfigApi()
id = 'id_example' # str | Unique identifier of the DHSM server object.
body = prime.swagger_client.FileDhsmConfigModify() # FileDhsmConfigModify | 

try:
    # Modify
    api_instance.file_dhsm_config_id_patch(id, body)
except ApiException as e:
    print("Exception when calling FileDhsmConfigApi->file_dhsm_config_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the DHSM server object. | 
 **body** | [**FileDhsmConfigModify**](FileDhsmConfigModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_dhsm_config_post**
> CreateResponse file_dhsm_config_post(body)

Create

Add an DHSM server configuration to a NAS server. Only one DHSM server object can be configured per NAS server. Was added in version 3.0.0.0.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileDhsmConfigApi()
body = prime.swagger_client.FileDhsmConfigCreate() # FileDhsmConfigCreate | 

try:
    # Create
    api_response = api_instance.file_dhsm_config_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileDhsmConfigApi->file_dhsm_config_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileDhsmConfigCreate**](FileDhsmConfigCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

