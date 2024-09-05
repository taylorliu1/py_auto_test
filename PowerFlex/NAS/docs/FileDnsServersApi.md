# swagger_client.FileDnsServersApi

All URIs are relative to *https://10.226.47.34/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_dns_servers_get**](FileDnsServersApi.md#file_dns_servers_get) | **GET** /file-dns-servers | Collection Query
[**file_dns_servers_id_delete**](FileDnsServersApi.md#file_dns_servers_id_delete) | **DELETE** /file-dns-servers/{id} | Delete
[**file_dns_servers_id_get**](FileDnsServersApi.md#file_dns_servers_id_get) | **GET** /file-dns-servers/{id} | Instance Query
[**file_dns_servers_id_patch**](FileDnsServersApi.md#file_dns_servers_id_patch) | **PATCH** /file-dns-servers/{id} | Modify
[**file_dns_servers_post**](FileDnsServersApi.md#file_dns_servers_post) | **POST** /file-dns-servers | Create

# **file_dns_servers_get**
> list[FileDnsInstance] file_dns_servers_get()

Collection Query

Query of the DNS settings of NAS Servers.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileDnsServersApi()

try:
    # Collection Query
    api_response = api_instance.file_dns_servers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileDnsServersApi->file_dns_servers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FileDnsInstance]**](FileDnsInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_dns_servers_id_delete**
> file_dns_servers_id_delete(id)

Delete

Delete DNS settings of a NAS Server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileDnsServersApi()
id = 'id_example' # str | Unique identifier of the DNS object.

try:
    # Delete
    api_instance.file_dns_servers_id_delete(id)
except ApiException as e:
    print("Exception when calling FileDnsServersApi->file_dns_servers_id_delete: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_dns_servers_id_get**
> FileDnsInstance file_dns_servers_id_get(id)

Instance Query

Query a specific DNS settings object of a NAS Server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileDnsServersApi()
id = 'id_example' # str | Unique identifier of the DNS object.

try:
    # Instance Query
    api_response = api_instance.file_dns_servers_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileDnsServersApi->file_dns_servers_id_get: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_dns_servers_id_patch**
> file_dns_servers_id_patch(body, id)

Modify

Modify the DNS settings of a NAS Server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileDnsServersApi()
body = swagger_client.FileDnsModify() # FileDnsModify | 
id = 'id_example' # str | Unique identifier of the DNS object.

try:
    # Modify
    api_instance.file_dns_servers_id_patch(body, id)
except ApiException as e:
    print("Exception when calling FileDnsServersApi->file_dns_servers_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileDnsModify**](FileDnsModify.md)|  | 
 **id** | **str**| Unique identifier of the DNS object. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_dns_servers_post**
> CreateResponse file_dns_servers_post(body)

Create

Create a new DNS Server configuration for a NAS Server. Only one object can be created per NAS Server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileDnsServersApi()
body = swagger_client.FileDnsCreate() # FileDnsCreate | 

try:
    # Create
    api_response = api_instance.file_dns_servers_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileDnsServersApi->file_dns_servers_post: %s\n" % e)
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

