# prime.swagger_client.SmbShareApi

All URIs are relative to *https://10.226.49.175/api/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**smb_share_get**](SmbShareApi.md#smb_share_get) | **GET** /smb_share | Collection Query
[**smb_share_id_delete**](SmbShareApi.md#smb_share_id_delete) | **DELETE** /smb_share/{id} | Delete
[**smb_share_id_get**](SmbShareApi.md#smb_share_id_get) | **GET** /smb_share/{id} | Instance Query
[**smb_share_id_patch**](SmbShareApi.md#smb_share_id_patch) | **PATCH** /smb_share/{id} | Modify
[**smb_share_post**](SmbShareApi.md#smb_share_post) | **POST** /smb_share | Create


# **smb_share_get**
> list[SmbShareInstance] smb_share_get()

Collection Query

List SMB shares.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SmbShareApi()

try:
    # Collection Query
    api_response = api_instance.smb_share_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmbShareApi->smb_share_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SmbShareInstance]**](SmbShareInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smb_share_id_delete**
> smb_share_id_delete(id)

Delete

Delete an SMB Share.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SmbShareApi()
id = 'id_example' # str | SMB Share object id. name:{name} can be used instead of {id}.

try:
    # Delete
    api_instance.smb_share_id_delete(id)
except ApiException as e:
    print("Exception when calling SmbShareApi->smb_share_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| SMB Share object id. name:{name} can be used instead of {id}. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smb_share_id_get**
> SmbShareInstance smb_share_id_get(id)

Instance Query

Get an SMB Share.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SmbShareApi()
id = 'id_example' # str | SMB Share object id. name:{name} can be used instead of {id}.

try:
    # Instance Query
    api_response = api_instance.smb_share_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmbShareApi->smb_share_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| SMB Share object id. name:{name} can be used instead of {id}. | 

### Return type

[**SmbShareInstance**](SmbShareInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smb_share_id_patch**
> smb_share_id_patch(id, body=body)

Modify

Modify SMB share properties.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SmbShareApi()
id = 'id_example' # str | SMB share object id. name:{name} can be used instead of {id}.
body = prime.swagger_client.SmbShareModify() # SmbShareModify |  (optional)

try:
    # Modify
    api_instance.smb_share_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling SmbShareApi->smb_share_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| SMB share object id. name:{name} can be used instead of {id}. | 
 **body** | [**SmbShareModify**](SmbShareModify.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smb_share_post**
> CreateResponse smb_share_post(body)

Create

Create an SMB share.

### Example
```python
from __future__ import print_function
import time
import prime.swagger_client
from prime.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = prime.swagger_client.SmbShareApi()
body = prime.swagger_client.SmbShareCreate() # SmbShareCreate | 

try:
    # Create
    api_response = api_instance.smb_share_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmbShareApi->smb_share_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SmbShareCreate**](SmbShareCreate.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

