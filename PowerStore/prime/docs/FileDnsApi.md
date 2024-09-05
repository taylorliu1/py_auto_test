# prime.swagger_client.FileDnsApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_dns_get**](FileDnsApi.md#file_dns_get) | **GET** /file_dns | Collection Query
[**file_dns_id_delete**](FileDnsApi.md#file_dns_id_delete) | **DELETE** /file_dns/{id} | Delete
[**file_dns_id_get**](FileDnsApi.md#file_dns_id_get) | **GET** /file_dns/{id} | Instance Query
[**file_dns_id_patch**](FileDnsApi.md#file_dns_id_patch) | **PATCH** /file_dns/{id} | Modify
[**file_dns_post**](FileDnsApi.md#file_dns_post) | **POST** /file_dns | Create


# **file_dns_get**
> list[FileDnsInstance] file_dns_get()

Collection Query

Query of the DNS settings of NAS Servers.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileDnsApi()

try:
    # Collection Query
    api_response = api_instance.file_dns_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileDnsApi->file_dns_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileDnsInstance]**](FileDnsInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_dns_id_delete**
> file_dns_id_delete(id)

Delete

Delete DNS settings of a NAS Server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileDnsApi()
id = 'id_example' # str | Unique identifier of the DNS object.

try:
    # Delete
    api_instance.file_dns_id_delete(id)
except ApiException as e:
    print("Exception when calling FileDnsApi->file_dns_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the DNS object. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_dns_id_get**
> FileDnsInstance file_dns_id_get(id)

Instance Query

Query a specific DNS settings object of a NAS Server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileDnsApi()
id = 'id_example' # str | Unique identifier of the DNS object.

try:
    # Instance Query
    api_response = api_instance.file_dns_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileDnsApi->file_dns_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the DNS object. | 

### Return type

[**FileDnsInstance**](FileDnsInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_dns_id_patch**
> file_dns_id_patch(id, body)

Modify

Modify the DNS settings of a NAS Server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileDnsApi()
id = 'id_example' # str | Unique identifier of the DNS object.
body = prime.swagger_client.FileDnsModify() # FileDnsModify | 

try:
    # Modify
    api_instance.file_dns_id_patch(id, body)
except ApiException as e:
    print("Exception when calling FileDnsApi->file_dns_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the DNS object. | 
 **body** | [**FileDnsModify**](FileDnsModify.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_dns_post**
> CreateResponse file_dns_post(body)

Create

Create a new DNS Server configuration for a NAS Server. Only one object can be created per NAS Server.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.FileDnsApi()
body = prime.swagger_client.FileDnsCreate() # FileDnsCreate | 

try:
    # Create
    api_response = api_instance.file_dns_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileDnsApi->file_dns_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileDnsCreate**](FileDnsCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

