# swagger_client.SmbSharesApi

All URIs are relative to *https://10.226.47.34/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**smb_shares_get**](SmbSharesApi.md#smb_shares_get) | **GET** /smb-shares | Collection Query
[**smb_shares_id_delete**](SmbSharesApi.md#smb_shares_id_delete) | **DELETE** /smb-shares/{id} | Delete
[**smb_shares_id_get**](SmbSharesApi.md#smb_shares_id_get) | **GET** /smb-shares/{id} | Instance Query
[**smb_shares_id_patch**](SmbSharesApi.md#smb_shares_id_patch) | **PATCH** /smb-shares/{id} | Modify
[**smb_shares_post**](SmbSharesApi.md#smb_shares_post) | **POST** /smb-shares | Create

# **smb_shares_get**
> list[SmbShareInstance] smb_shares_get()

Collection Query

List SMB shares.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SmbSharesApi()

try:
    # Collection Query
    api_response = api_instance.smb_shares_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmbSharesApi->smb_shares_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SmbShareInstance]**](SmbShareInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smb_shares_id_delete**
> smb_shares_id_delete(id)

Delete

Delete an SMB Share.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SmbSharesApi()
id = 'id_example' # str | SMB Share object id.

try:
    # Delete
    api_instance.smb_shares_id_delete(id)
except ApiException as e:
    print("Exception when calling SmbSharesApi->smb_shares_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| SMB Share object id. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smb_shares_id_get**
> SmbShareInstance smb_shares_id_get(id)

Instance Query

Get an SMB Share.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SmbSharesApi()
id = 'id_example' # str | SMB Share object id.

try:
    # Instance Query
    api_response = api_instance.smb_shares_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmbSharesApi->smb_shares_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| SMB Share object id. | 

### Return type

[**SmbShareInstance**](SmbShareInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smb_shares_id_patch**
> smb_shares_id_patch(id, body=body)

Modify

Modify SMB share properties.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SmbSharesApi()
id = 'id_example' # str | SMB share object id.
body = swagger_client.SmbShareModify() # SmbShareModify |  (optional)

try:
    # Modify
    api_instance.smb_shares_id_patch(id, body=body)
except ApiException as e:
    print("Exception when calling SmbSharesApi->smb_shares_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| SMB share object id. | 
 **body** | [**SmbShareModify**](SmbShareModify.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **smb_shares_post**
> CreateResponse smb_shares_post(body)

Create

Create an SMB share.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SmbSharesApi()
body = swagger_client.SmbShareCreate() # SmbShareCreate | 

try:
    # Create
    api_response = api_instance.smb_shares_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SmbSharesApi->smb_shares_post: %s\n" % e)
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

